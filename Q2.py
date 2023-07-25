class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list_in_groups(head, k):
    current = head
    next_node = None
    prev = None
    count = 0

    
    while current is not None and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    if next_node is not None:
        head.next = reverse_linked_list_in_groups(next_node, k)

    return prev


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
   
    elements = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3 

  
    head = Node(elements[0])
    current = head
    for data in elements[1:]:
        current.next = Node(data)
        current = current.next

    print("Original Linked List:")
    display_linked_list(head)

    head = reverse_linked_list_in_groups(head, k)

    print("\nLinked List after reversing in groups of", k, ":")
    display_linked_list(head)
