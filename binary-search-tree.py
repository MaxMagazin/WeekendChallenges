# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    print("root.data:", root.data)

    if root.left != None:
        if root.left.data > root.data:
            return False
        else:
            print("left.data:", root.left.data, "on root.data", root.data)
            check_binary_search_tree_(root.left)

    if root.right != None:
        if root.right.data < root.data:
            return False
        else:
            print("right.data:", root.right.data, "on root.data", root.data)
            check_binary_search_tree_(root.right)

    return True
    



'''''''''
    if (root.left and root.data < root.left.data) or (root.right and root.data > root.right.data):
        return False
    else:
        if root.left:
            check_binary_search_tree_(root.left)
            
        if root.right:
            check_binary_search_tree_(root.right)
            
    return True        
        
    print(root.info, end = " ")
    
        