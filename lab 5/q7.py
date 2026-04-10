queue = []

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter item: ")
        queue.append(item)
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            removed_item = queue[0]
            queue = queue[1:]
            print(removed_item)
    elif choice == 3:
        print(queue)
    elif choice == 4:
        break