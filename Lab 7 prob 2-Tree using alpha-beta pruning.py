# Solve the below tree by using alpha-beta pruning method.


class GameNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def custom_minimax_with_pruning(node, depth, alpha, beta, is_max_player):
    if not node.children:
        return node.val

    if is_max_player:
        best_val = float('-inf')
        for child_node in node.children:
            val = custom_minimax_with_pruning(child_node, depth - 1, alpha, beta, False)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break  # Beta cut-off
        return best_val
    else:
        best_val = float('inf')
        for child_node in node.children:
            val = custom_minimax_with_pruning(child_node, depth - 1, alpha, beta, True)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_val


node_alpha = GameNode(val=5)
node_beta = GameNode(val=6)
node_gamma = GameNode(val=7)
node_delta = GameNode(val=4)
node_epsilon = GameNode(val=5)
node_zeta = GameNode(val=3)
node_eta = GameNode(val=6)
node_theta = GameNode(val=6)
node_iota = GameNode(val=9)
node_kappa = GameNode(val=7)
node_lambda = GameNode(val=5)
node_mu = GameNode(val=9)
node_nu = GameNode(val=8)
node_xi = GameNode(val=6)

node_aa = GameNode(children=[node_alpha, node_beta])
node_ab = GameNode(children=[node_gamma, node_delta, node_epsilon])
node_ac = GameNode(children=[node_zeta])
node_ad = GameNode(children=[node_eta])
node_ae = GameNode(children=[node_theta, node_iota])
node_af = GameNode(children=[node_kappa])
node_ag = GameNode(children=[node_lambda])
node_ah = GameNode(children=[node_mu, node_nu])
node_ai = GameNode(children=[node_xi])

node_ba = GameNode(children=[node_aa, node_ab])
node_bb = GameNode(children=[node_ac])
node_bc = GameNode(children=[node_ad, node_ae])
node_bd = GameNode(children=[node_af])
node_be = GameNode(children=[node_ag])
node_bf = GameNode(children=[node_ah, node_ai])

node_ca = GameNode(children=[node_ba, node_bb])
node_cb = GameNode(children=[node_bc, node_bd])
node_cc = GameNode(children=[node_be, node_bf])

root_node = GameNode(children=[node_ca, node_cb, node_cc])

best_score = custom_minimax_with_pruning(root_node, 5, float('-inf'), float('inf'), True)
print(f"The best score with alpha-beta pruning is: {best_score}")
