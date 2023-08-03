class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def get_top(self):
        return None if self.is_empty() else self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next


def perform_operation(choice, stack):
    if choice == 1:
        data = int(input("Enter the value to push: "))
        stack.push(data)
        print(f"Pushed: {data}")

    elif choice == 2:
        data = stack.pop()
        if data is not None:
            print(f"Popped: {data}")
        else:
            print("Stack is empty. Nothing to pop.")
    elif choice == 3:
        data = stack.get_top()
        if data is not None:
            print(f"The TOP is: {data}")
        else:
            print("Stack is empty. Nothing to get_top.")
    elif choice == 4:
        stack.display()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n------------------------------------------------")
        print("\nStack operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Get_TOP")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice (1/2/3/4/5): "))
        print("----------------------------------------------------")

        if choice == 5:
            print("Exiting the program.")
            break

        perform_operation(choice, stack)
