# https://www.hackerrank.com/challenges/is-binary-search-tree/problem
# 
# cool solution with c++
# https://www.hackerrank.com/challenges/is-binary-search-tree/forum/comments/1295649

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return check_subtree(root, 0, 10000)

def check_subtree(node, min, max):
    
    if node.data <= min or node.data >= max:
        return False
    
    if node.left and not check_subtree(node.left, min, node.data):
        return False
        
    if node.right and not check_subtree(node.right, node.data, max):
        return False
    
    return True
