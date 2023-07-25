class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_linked_lists_at_alternate_positions(head1, head2):
    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return head1


def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

   
    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)

    print("First Linked List:")
    display_linked_list(head1)

    print("\nSecond Linked List:")
    display_linked_list(head2)

    head1 = merge_linked_lists_at_alternate_positions(head1, head2)

    print("\nMerged Linked List:")
    display_linked_list(head1)
