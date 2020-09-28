import time

# IMPLEMENTATION OF BINARY SEARCH TREE FROM DATA-STRUCTURES ASSIGNMENT
# insertions and searches are speed O(log(n)) on average compared to arrays at O(n)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur = self
        while True:
            if value >= cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = BSTNode(value)
                    break
            else: # value < cur.value
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = BSTNode(value)
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur = self
        while True:
            if target > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    return False
            elif target < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    return False
            else: # equals
                return True

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree_1 =  None
for name in names_1:
    if tree_1:
        tree_1.insert(name)
    else:
        tree_1 = BSTNode(name)

for name in names_2:
    if tree_1.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
