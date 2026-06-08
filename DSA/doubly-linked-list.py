from typing import Literal


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node

    def display(self, options: Literal["forward", "back"]):
        if options == "back":
            current = self.tail
            while current:
                print(current.data)
                current = current.prev
        if options == "forward":
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def delete(self, key):
        if self.head == None and self.tail == None:
            print("List is empty.")
            return
        elif self.head.data == key and self.tail.data == key:
            self.tail = None
            self.head = None
        elif self.head.data == key and self.tail.data != key:
            self.head.next.prev = None
            self.head = self.head.next
        elif self.tail.data == key and self.head.data != key:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            current = self.head
            while current:
                if current.data == key:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    break
                else:
                    current = current.next


# Got these testing code from AI

dll = DoublyLinkedList()

print("--- 1. Testing Empty List Delete ---")
dll.delete(10)  # Should print "List is empty." Safely!

print("\n--- 2. Appending Items (10, 20, 30) ---")
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward display:")
dll.display("forward")  # Should be: 10 <-> 20 <-> 30

print("Backward display:")
dll.display("back")  # Should be: 30 <-> 20 <-> 10

print("\n--- 3. Deleting Middle Node (20) ---")
dll.delete(20)
dll.display("forward")  # Should be: 10 <-> 30

print("\n--- 4. Deleting Head Node (10) ---")
dll.delete(10)
dll.display("forward")  # Should be: 30

print("\n--- 5. Deleting Single/Last Node (30) ---")
dll.delete(30)
dll.display("forward")  # Should print nothing (list is now empty)

print("\n--- 6. Confirming List is Safely Empty Again ---")
dll.delete(99)  # Should print "List is empty."
