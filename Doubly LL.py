class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            # if empty make the node as head and tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # if empty make the node as head and tail (for notes)
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_last(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # move the tail pointer to the previous node
            self.tail.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        current = self.get_node(index)

        if current == self.head:
            self.head = self.head.next  # if the reached node is the head of the list move the head to the 2nd node
            if self.head:
                self.head.prev = None
        elif current == self.tail:  # if the reached node is
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def insert_at_index(self, index, data):
        if index <= 0:
            self.prepend(data)
        elif index >= self.length():
            self.append(data)
        else:
            new_node = Node(data)
            current = self.get_node(index-1)  # get to a node thats before the index
            new_node.prev = current
            new_node.next = current.next
            current.next = new_node


    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def set_node(self, index, data):
        node = self.get_node(index)
        if node:
            node.data = data

    def print_nodes(self):
        current = self.head
        while current:

            print(current.data, end=" --> ")

            current = current.next
        print("None")

    def reverse(self):
        current = self.head
        while current:  # keep swapping each node's next and prev until u reach null
            current.prev, current.next = current.next, current.prev
            # we started at head and to move in right after swapping v have to go through prev links
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert_values(self, values):
        for data in values:
            self.append(data)

def interactive_linked_list():
    linked_list = DoublyLinkedList()
    show_menu = True

    while True:
        if show_menu:
            print("\nOptions:")
            print("1. Append")
            print("2. Prepend")
            print("3. Remove Last")
            print("4. Remove at Index")
            print("5. Insert at Index")
            print("6. Get Node at Index")
            print("7. Set Node at Index")
            print("8. Print Nodes")
            print("9. Reverse")
            print("10. Length of List")
            print("11. Insert Multiple Values")
            print("0. Exit")

        choice = int(input("Enter your choice: "))
        show_menu = True  # Resetting the flag to show the menu next time if needed

        if choice == 1:
            data = input("Enter the value to append: ")
            linked_list.append(data)
        elif choice == 2:
            data = input("Enter the value to prepend: ")
            linked_list.prepend(data)
        elif choice == 3:
            linked_list.remove_last()
        elif choice == 4:
            index = int(input("Enter the index to remove: "))
            linked_list.remove_at_index(index)
        elif choice == 5:
            index = int(input("Enter the index to insert: "))
            data = input("Enter the value to insert: ")
            linked_list.insert_at_index(index, data)
        elif choice == 6:
            index = int(input("Enter the index to get node: "))
            node = linked_list.get_node(index)
            if node:
                print("Node at index {}: {}".format(index, node.data))
            else:
                print("Invalid index.")
        elif choice == 7:
            index = int(input("Enter the index to set node: "))
            data = input("Enter the new value: ")
            linked_list.set_node(index, data)
        elif choice == 8:

            linked_list.print_nodes()

        elif choice == 9:
            linked_list.reverse()
        elif choice == 10:
            print("Length of the list: ", linked_list.length())
        elif choice == 11:
            values = input("Enter comma-separated values to insert: ").split(',')
            linked_list.insert_values(values)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")

        continue_choice = input("Do you want to continue? (yes/no): ")
        print("------------------------------------------------------")
        if continue_choice.lower() == "n":
            break
        elif continue_choice.lower() == "y":
            show_menu = False
        else:
            print("Invalid input. Assuming 'yes' and continuing.")
            show_menu = False

if __name__ == "__main__":
    interactive_linked_list()
