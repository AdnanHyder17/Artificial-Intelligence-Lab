# Suppose there are three boxes, each containing two coins. Box 1 has two gold
# coins, Box 2 has two silver coins, and Box 3 has one gold coin and one silver coin. You
# randomly pick a box and take out one coin. It turns out to be a gold coin. What is the probability
# that the other coin in the box is also gold if:

# (a) You picked Box 1?
# (b) You picked Box 2?
# (c) You picked Box 3?

# Use ‘pomegranate’ and create conditional probability table for each box.

from pomegranate import *

# Define the boxes and their coin types
box1 = {'Gold': 2, 'Silver': 0}
box2 = {'Gold': 0, 'Silver': 2}
box3 = {'Gold': 1, 'Silver': 1}

# Define the probability of picking each box
prob_box1 = 1/3
prob_box2 = 1/3
prob_box3 = 1/3

# Define the probabilities of picking a gold coin given the box
prob_gold_given_box1 = box1['Gold'] / sum(box1.values())
prob_gold_given_box2 = box2['Gold'] / sum(box2.values())
prob_gold_given_box3 = box3['Gold'] / sum(box3.values())

# Create Bayesian Network
# Define the nodes and their distributions
box_node = DiscreteDistribution({'Box1': prob_box1, 'Box2': prob_box2, 'Box3': prob_box3})
gold_node = ConditionalProbabilityTable(
    [[ 'Box1', 'Gold', prob_gold_given_box1 ],
     [ 'Box1', 'Silver', 1 - prob_gold_given_box1 ],
     [ 'Box2', 'Gold', prob_gold_given_box2 ],
     [ 'Box2', 'Silver', 1 - prob_gold_given_box2 ],
     [ 'Box3', 'Gold', prob_gold_given_box3 ],
     [ 'Box3', 'Silver', 1 - prob_gold_given_box3 ]],
    [box_node]
)

# Create the Bayesian Network model
box = Node(box_node, name="box")
gold = Node(gold_node, name="gold")

network = BayesianNetwork("Coin Picking")
network.add_nodes(box, gold)
network.add_edge(box, gold)
network.bake()

# Given that a gold coin was picked, we need to find the probability that the other coin in the box is gold
# P(Box_i | Gold) for each Box_i

def probability_other_coin_is_gold(box_name):
    # Define the query
    query = network.predict_proba({'gold': 'Gold'})
    if box_name == 'Box1':
        return query[0].parameters[0]['Box1']
    elif box_name == 'Box2':
        return query[0].parameters[0]['Box2']
    elif box_name == 'Box3':
        return query[0].parameters[0]['Box3']
    else:
        raise ValueError("Invalid box name")

# Calculate probabilities
prob_box1_given_gold = probability_other_coin_is_gold('Box1')
prob_box2_given_gold = probability_other_coin_is_gold('Box2')
prob_box3_given_gold = probability_other_coin_is_gold('Box3')

print(f"Probability that the other coin is gold given that Box 1 was picked: {prob_box1_given_gold:.2f}")
print(f"Probability that the other coin is gold given that Box 2 was picked: {prob_box2_given_gold:.2f}")
print(f"Probability that the other coin is gold given that Box 3 was picked: {prob_box3_given_gold:.2f}")
