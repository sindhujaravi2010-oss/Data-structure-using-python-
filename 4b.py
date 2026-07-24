class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty!")
            return

        temp = self.front
        print("Deleted element:", temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is Empty!")
            return

        temp = self.front
        print("Queue elements are:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

q = Queue()

while True:
    print("\n----- QUEUE USING LINKED LIST -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
