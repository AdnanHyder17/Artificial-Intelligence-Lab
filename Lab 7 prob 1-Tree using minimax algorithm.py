# Implement the following tree using minimax algorithm.


class GameNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def minimax(node, depth, is_max_player):

    if not node.children:
        return node.val

    if is_max_player:
        best_val = float('-inf')
        for child in node.children:
            val = minimax(child, depth - 1, False)
            best_val = max(best_val, val)
        node.val = best_val
        return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            val = minimax(child, depth - 1, True)
            best_val = min(best_val, val)
        node.val = best_val
        return best_val


# Tree
node_h = GameNode(val=-1)
node_i = GameNode(val=4)
node_j = GameNode(val=2)
node_k = GameNode(val=-6)
node_l = GameNode(val=-3)
node_m = GameNode(val=-5)
node_n = GameNode(val=0)
node_o = GameNode(val=7)

node_d = GameNode(children=[node_h, node_i])
node_e = GameNode(children=[node_j, node_k])
node_f = GameNode(children=[node_l, node_m])
node_g = GameNode(children=[node_n, node_o])

node_b = GameNode(children=[node_d, node_d])
node_c = GameNode(children=[node_f, node_g])

root = GameNode(children=[node_b, node_c])
# Run the minimax algorithm
best_move_value = minimax(root, 4, True)
print(f"The best move value is: {best_move_value}")
