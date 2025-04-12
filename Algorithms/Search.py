import sys
import os

# Add the "Code" folder to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DS.Queue.Queue import Queue
from DS.BST.BST import BinarySearchTree, Node

def bfs(tree):
    """
    Performs a breadth-first search (BFS) traversal of the binary search tree.

    Args:
        tree: The binary search tree to traverse.

    Returns:
        list: A list of values in the order they were visited during the BFS traversal.
    """
    if not tree.root:
        return []

    queue = Queue()
    queue.enqueue(tree.root)
    result = []

    while queue.length > 0:
        current_node = queue.dequeue()
        result.append(current_node.data)

        if current_node.left:
            queue.enqueue(current_node.left)
        if current_node.right:
            queue.enqueue(current_node.right)

    return result
    
def bfs_R(queue,list):
    """
    Recursive helper function for breadth-first search (BFS) traversal.

    Args:
        queue: The queue containing nodes to visit.
        list: The list to store the visited node values.
    """
    if queue.length == 0:
        return list

    current_node = queue.dequeue()
    list.append(current_node.data)

    if current_node.left:
        queue.enqueue(current_node.left)
    if current_node.right:
        queue.enqueue(current_node.right)

    bfs_R(queue, list)

def dfs_InOrder(tree):
    """
    Performs an in-order depth-first search (DFS) traversal of the binary search tree.

    Args:
        tree: The binary search tree to traverse.

    Returns:
        list: A list of values in the order they were visited during the DFS traversal.
    """
    if not tree.root:
        return []

    stack = []
    current_node = tree.root
    result = []

    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        result.append(current_node.data)
        current_node = current_node.right

    return result

def dfs_PreOrder(tree):
    """
    Performs a pre-order depth-first search (DFS) traversal of the binary search tree.

    Args:
        tree: The binary search tree to traverse.

    Returns:
        list: A list of values in the order they were visited during the DFS traversal.
    """
    if not tree.root:
        return []

    stack = [tree.root]
    result = []

    while stack:
        current_node = stack.pop()
        result.append(current_node.data)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return result

def dfs_PostOrder(tree):
    """
    Performs a post-order depth-first search (DFS) traversal of the binary search tree.

    Args:
        tree: The binary search tree to traverse.

    Returns:
        list: A list of values in the order they were visited during the DFS traversal.
    """
    if not tree.root:
        return []

    stack = [tree.root]
    result = []

    while stack:
        current_node = stack.pop()
        result.append(current_node.data)

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)

    return result[::-1]

tree = BinarySearchTree()
tree.insert(10)
tree.insert(15)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(12)
tree.insert(1)

print(bfs(tree))