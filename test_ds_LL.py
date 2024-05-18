
# Date : 08:38 pm 18-05-24
##############################################################################
# Based on GFG : https://www.geeksforgeeks.org/singly-linked-list-tutorial/  #
##############################################################################


# Single NODE without next Element.
                         ########
                        # A NODE #
                         ########


# Multi NODE with Head and Tail.
                 ########  #######  ########
                # NODE 1 # NODE 2 # NODE 3 #
                 ########  #######  ########


# To create a single unit of Node we will use class, initialise next address as None.
class Node:
    def __init__(self,data):
        self.data = data
        self.next_element = None

# to read Node elements


def read_nodes(head):
    while head is not None:

        # get the data from node
        print(head.data)

        # point to the address of next node
        head = head.next_element

# let's consider 3 nodes


first = Node(1)
second = Node(2)
third = Node(3)

# Now lets chained them.

first.next_element=second
second.next_element=third

# Now let's read them
read_nodes(first)