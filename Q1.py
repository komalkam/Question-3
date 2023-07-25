class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_nodes_with_zero_sum(self):
        dummy_head = Node(0)
        dummy_head.next = self.head

        current = dummy_head
        sum_so_far = 0
        sum_to_node = {}

        while current:
            sum_so_far += current.data
            if sum_so_far in sum_to_node:
          
                temp = sum_to_node[sum_so_far].next
                while temp != current.next:
                    temp = temp.next
                sum_to_node[sum_so_far].next = temp
            else:
                sum_to_node[sum_so_far] = current
            current = current.next

        self.head = dummy_head.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()
   
    elements = [1, 2, -3, 3, 1, -2, -1, -1]
    for element in elements:
        linked_list.append(element)

    print("Original Linked List:")
    linked_list.display()

    linked_list.delete_nodes_with_zero_sum()

    print("\nLinked List after deleting nodes with zero sum:")
    linked_list.display()
