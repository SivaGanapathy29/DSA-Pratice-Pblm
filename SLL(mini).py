class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def start_d(self):
        if not self.head:
            print("SLL is Empty")
        self.head = self.head.next
    def end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def end_d(self):
        if not self.head:
            print("SLL is Empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def begin(self,data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp:
            print("position out of bound")
            return
        new_node.next = temp.next
        temp.next = new_node
    def begin_d(self,position):
        if not self.head:
            print("SLL is Empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if not temp or not temp.next:
            print("Position out of the bound")
            return
        temp.next = temp.next.next
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

if __name__ == "__main__":
    s = SLL()
    while True:
        print("\n Menu")
        print("1. Insert at Beginning")
        print("2. Insert at Position")
        print("3. Insert at End")
        print("4. Delete at Begining")
        print("5. Delete at End")
        print("6. Delete at position")
        print("7. Display")
        print("8. Exit")
        choice = int(input("Enter you Choice"))
        if choice == 1:
            data = int(input("insert start :"))
            s.start(data)
        elif choice == 2:
            data = int(input("insert at data:"))
            position = int(input("insert at position:"))
            s.begin(data,position)
        elif choice == 3:
            data = int(input("insert end :"))
            s.end(data)
        elif choice == 4:
            s.start_d()
        elif choice == 5:
            s.end_d()
        elif choice == 6:
            data = int(input("delete at position:"))
            s.begin_d(data)
        elif choice == 7:
            s.display()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice plz try again")