import uuid

from collections import deque
from anytree import Node, RenderTree

print("-"*33+" ARBRE GENERALISE "+"-"*33)

root = Node('A')

level_1_child_3 = Node('D', parent = root)
level_1_child_2 = Node('C', parent = root)
level_1_child_1 = Node('B', parent = root)

level_2_child_3 = Node('G', parent = level_1_child_1)
level_2_child_2 = Node('F', parent = level_1_child_1)
level_2_child_1 = Node('E', parent = level_1_child_1)

level_3_child_3 = Node('J', parent = level_1_child_2)
level_3_child_2 = Node('I', parent = level_1_child_2)
level_3_child_1 = Node('H', parent = level_1_child_2)

level_4_child_3 = Node('M', parent = level_1_child_3)
level_4_child_2 = Node('L', parent = level_1_child_3)
level_4_child_1 = Node('K', parent = level_1_child_3)

for pre, fill, node in RenderTree(root):
    print("%s%s" %(pre, node.name))

print("-"*33+" ARBRE BINARISER "+"-"*33)

#En haut c'est a droite en bas c'est a gauche

root = Node('A')

level_1_child_2 = Node('-', parent = root)
level_1_child_1 = Node('B', parent = root)

level_2_child_2 = Node('C', parent = level_1_child_1)
level_2_child_1 = Node('E', parent = level_1_child_1)

level_3_child_1 = Node('F', parent = level_2_child_1)
level_3_child_2 = Node('-', parent = level_2_child_1)

level_4_child_1 = Node('G', parent = level_3_child_1)
level_4_child_2 = Node('-', parent = level_3_child_1)

level_5_child_2 = Node('D', parent = level_2_child_2)
level_5_child_1 = Node('H', parent = level_2_child_2)

level_6_child_1 = Node('I', parent = level_5_child_1)
level_6_child_2 = Node('-', parent = level_5_child_1)

level_7_child_1 = Node('J', parent = level_6_child_1)
level_7_child_2 = Node('-', parent = level_6_child_1)

level_8_child_2 = Node('-', parent = level_5_child_2)
level_8_child_1 = Node('K', parent = level_5_child_2)

level_9_child_1 = Node('L', parent = level_8_child_1)
level_9_child_2 = Node('-', parent = level_8_child_1)

level_10_child_1 = Node('M', parent = level_9_child_1)
level_10_child_2 = Node('-', parent = level_9_child_1)

for pre, fill, node in RenderTree(root):
    print("%s%s" %(pre, node.name))

print("-"*33+" ARBRE EN LISTE CHAINEE "+"-"*33)