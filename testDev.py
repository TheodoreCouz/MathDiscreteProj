import code
import numpy as np

# #Should print [2 4 4]
# print(code.pageRankPower(np.array([
#     [0.0, 2.0, 0.0],
#     [0.0, 0.0, 2.0],
#     [1.0, 1.0, 0.0]
# ]), 1.0, 1.0))
#
# #Should print [2 4 4]
# print(code.pageRankLinear(np.array([
#     [0.0, 2.0, 0.0],
#     [0.0, 0.0, 2.0],
#     [1.0, 1.0, 0.0]
# ]), 1.0, 1.0))

#What happens with dangling nodes?

# print(code.pageRankLinear(np.array([
#     [0.0, 0.0, 0.0],
#     [1.0, 0.0, 0.0],
#     [1.0, 2.0, 0.0]
# ]), 0.9, 1.0))
#
print(code.pageRankPower(np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 2.0, 0.0]
]), 0.9, np.array([0.8, 0.1, 0.1])))

print(code.pageRankPower(np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 2.0, 0.0]
]), 0.9, np.array([0.1, 0.8, 0.1])))

print(code.pageRankPower(np.array([
    [0.0, 1.0],
    [1.0, 0.0],
]), 0.9, np.array([0.9, 0.1])))






