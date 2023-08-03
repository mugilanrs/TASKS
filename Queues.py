class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):  # use this function to check whether the queue is empty
        return self.front is None  # by creating a function u can repeat this line of code many times

    def enqueue(self, data):  # u always start adding at the last
        new_node = Node(data)
        if self.rear is None:  # so if last is empty newNode is front and rear
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # the next pointr or rear is made pointin to the newNode
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        popped_data = self.front.data  # u r going to return the deleted data so save it 1st then proceed
        self.front = self.front.next  # now shift the front pointr to the next node
        return popped_data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current:
                print(current.data, end=" | ")
                current = current.next
            print("\n")


# this is a function for interface u giv the choice and queue as i/p
def perform_operation(choice, queue):
    if choice == 1:
        data = int(input("Enter the value to enqueue: "))
        queue.enqueue(data)
        print(f"Enqueued: {data}")
    elif choice == 2:
        data = queue.dequeue()
        if data is not None:
            print(f"Dequeued: {data}")
        else:
            print("Queue is empty. Nothing to dequeue.")
    elif choice == 3:
        queue.display()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\nQueue operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))
        print("---------------------------")

        if choice == 4:
            print("Exiting the program.")
            break

        perform_operation(choice, queue)
