# Write Python Program for each task, create sample space and calculate the probability and show the output.
# A manufacturing firm employs three analytical plans for the design and development of a
# particular product. For cost reasons, all three are used at varying times. In fact, plans 1, 2,
# and 3 are used for 30%, 20%, and 50% of the products, respectively. The defect rate is
# different for the three procedures as follows: P(D|P1)=0.01, P(D|P2)=0.03, P(D|P3)=0.02,
# where P(D|Pj ) is the probability of a defective product, given plan j. If a random product was
# observed and found to be defective, which plan was most likely used and thus responsible?


# Define the probabilities
P_P1 = 0.30  # Probability of using Plan 1
P_P2 = 0.20  # Probability of using Plan 2
P_P3 = 0.50  # Probability of using Plan 3

P_D_given_P1 = 0.01  # Probability of defect given Plan 1
P_D_given_P2 = 0.03  # Probability of defect given Plan 2
P_D_given_P3 = 0.02  # Probability of defect given Plan 3

# Calculate the total probability of defect (P(Defective))
P_D = (P_P1 * P_D_given_P1) + (P_P2 * P_D_given_P2) + (P_P3 * P_D_given_P3)

# Calculate the posterior probabilities using Bayes' Theorem
P_P1_given_D = (P_D_given_P1 * P_P1) / P_D
P_P2_given_D = (P_D_given_P2 * P_P2) / P_D
P_P3_given_D = (P_D_given_P3 * P_P3) / P_D

# Print the results with interpretation
print(f"P(Plan1 | Defective) = {P_P1_given_D:.4f}")
print(f"P(Plan2 | Defective) = {P_P2_given_D:.4f}")
print(f"P(Plan3 | Defective) = {P_P3_given_D:.4f}")

print("\nInterpretation:")
print(f"- The probability that Plan 1 was used given that the product is defective is {P_P1_given_D:.4f}.")
print(f"  This is relatively low because Plan 1 has the smallest defect rate and also is used less frequently compared to other plans.")
print(f"- The probability that Plan 2 was used given that the product is defective is {P_P2_given_D:.4f}.")
print(f"  Plan 2 is somewhat more likely than Plan 1 because it has a higher defect rate and is used more often.")
print(f"- The probability that Plan 3 was used given that the product is defective is {P_P3_given_D:.4f}.")
print(f"  Plan 3 has the highest probability of being the plan used because it has the highest usage rate and a lower defect rate, making it the most likely source of the defect.")
