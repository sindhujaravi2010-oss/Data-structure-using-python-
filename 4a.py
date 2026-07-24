SIZE = 5
queue = []
front = -1
rear = -1

def enqueue():
    global front, rear
    if rear == SIZE - 1:
        print("Queue is FULL!")
    else:
        value = int(input("Enter the value: "))
        if front == -1:
            front = 0
        rear += 1
        queue.append(value)
        print(value, "inserted into the queue.")

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue is EMPTY!")
    else:
        print("Deleted element:", queue[front])
        front += 1
        if front > rear:
            front = rear = -1
            queue.clear()

def display():
    if front == -1 or front > rear:
        print("Queue is EMPTY!")
    else:
        print("Queue elements are:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice!")
