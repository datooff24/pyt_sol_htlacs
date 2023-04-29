class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


#def print_tree_inorder(tree):
 #   if tree is None: return
  #  print_tree_inorder(tree.left)
   # print(tree.cargo, end=" ")
    #print_tree_inorder(tree.right)


def print_tree_inorder(tree):
    if tree is None: return
    if tree.left is None and tree.right is None:
        print("(", end=" ")
    if tree.left is not None:
        print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")


    if tree.right is not None:
        print_tree_inorder(tree.right)
        print(")", end = "")



tree = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))
print_tree_inorder(tree)
