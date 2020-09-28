import time
from collections import Counter


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check for empty node to the left
        # if no node create one
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # repeat process for node to left, if not present, create node
                self.left.insert(value)
        # check if new node value is greater than or equal to new node value against self.value
        # after check value, repeat process for right side
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if self.value is target
        if self.value == target:
            # If yes return True,
            return True
        # If No:
        # go right
        elif self.value <= target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # Or go left
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right till you can not anymore
        # Return value at far right
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Lowest number is number to left
        # base case?
        if not self:
            return
        # recursive case?
        if self.left:
            self.in_order_print()
        print(self.value)
        if self.right:
            self.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)

        while len(queue) > 0:
            node = queue.dequeue()
            print(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            node = stack.pop()
            # call 'print()'
            print(node.value)
            # push its left and right children onto stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
sorted_list = BSTNode("names entered here")
for i in names_1:
    sorted_list.insert(i)
for i_2 in names_2:
    if sorted_list.contains(i_2):
        duplicates.append(i_2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
print("--------------------------Stretch----------------------------")
s_time = time.time()
stretch = []
a = Counter(names_1)
b = Counter(names_2)
c = a + b
for i in c:
    if c[i] > 1:
        print(i)

stretch.append(c[i])
e_time = time.time()
print(f"{len(stretch)} duplicates:\n\n{', '.join(stretch)}\n\n")
print(f"runtime: {e_time - s_time} seconds")
