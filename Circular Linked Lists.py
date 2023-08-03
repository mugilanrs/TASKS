class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:  # if there is no node at all u make the single node as cirlr LL
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # if there is a list
            self.tail.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:  # same as insertion at start but mark it as tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_start(self):
        if self.head is None:
            print("Circular linked list is empty. Nothing to delete.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Circular linked list is empty. Nothing to delete.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current

    def print_list(self):
        if self.head is None:
            print("Circular linked list is empty.")
        else:
            current = self.head
            print("Circular Linked List:", end=" ")
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print(" (back to the start)")

if __name__ == "__main__":
    circular_list = CircularLinkedList()

    while True:
        print("\nCircular Linked List Operations:")
        print("1. Insert at Start")
        print("2. Insert at End")
        print("3. Delete at Start")
        print("4. Delete at End")
        print("5. Print List")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the start: "))
            circular_list.insert_at_start(data)
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            circular_list.insert_at_end(data)
        elif choice == 3:
            circular_list.delete_at_start()
        elif choice == 4:
            circular_list.delete_at_end()
        elif choice == 5:
            circular_list.print_list()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")