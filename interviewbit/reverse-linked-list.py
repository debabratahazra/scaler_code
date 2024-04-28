class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        list = []
        current = self.head
        while current:
            list.append(current.data)  # Print the data of the current node
            current = current.next 
        return list

    def reverse_and_store(self):
        prev = None
        current = self.head
        reversed_list = []
        while current is not None:
            reversed_list.insert(0, current.data)  # Insert the data at the beginning of the list
            next = current.next
            current.next = prev
            prev = current
            current = next
        return reversed_list

# Create a linked list
llist = LinkedList()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)

# Print the original linked list
print("Original linked list:", llist.print_list())
# Traverse and print the original linked list

# Reverse the linked list and store in another list
reversed_elements = llist.reverse_and_store()

# Print the reversed elements
print("Reversed elements:", reversed_elements)
