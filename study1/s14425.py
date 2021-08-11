import sys

n, m = map(int, sys.stdin.readline().split())
words = []
ans = []

for i in range(n):
    w = sys.stdin.readline()
    words.append(w)

for i in range(m):
    w = sys.stdin.readline()
    if w in words:
        ans.append(1)
    else:
        ans.append(0)

print(sum(ans))


############# 출처 : https://geonlee.tistory.com/72 #############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert_value(self.root, data)
#         return self.root is not None

#     def _insert_value(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data <= node.data:
#                 node.left = self._insert_value(node.left, data)
#             else:
#                 node.right = self._insert_value(node.right, data)
#         return node

#     def find(self, key):
#         return self._find_value(self.root, key)

#     def _find_value(self, root, key):
#         if root is None or root.data == key:
#             return root is not None
#         elif key < root.data:
#             return self._find_value(root.left, key)
#         else:
#             return self._find_value(root.right, key)

# def main():
#     n, m = map(int, sys.stdin.readline().split())
#     ans = []

#     tree = BinarySearchTree()

#     for i in range(n):
#         word = sys.stdin.readline()
#         tree.insert(word)
    
#     for i in range(m):
#         word = sys.stdin.readline()
#         ans.append(tree.find(word))
    
#     print(sum(ans))

# main()





############# 엘리스 코치님께서 주신 코드 #############
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert(self.root, data)
#         return

#     def _insert(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data <= node.data:
#                 self._insert(node.left, data)
#             else:
#                 self._insert(node.right, data)
#         return node

#     def find(self, data):
#         return self._find(self.root, data)

#     def _find(self, node, data):
#         if node == None:
#             return 0
#         elif node.data is data:
#             return 1
#         else:
#             if data <= node.data:
#                 return self._find(node.left, data)
#             else:
#                 return self._find(node.right, data)