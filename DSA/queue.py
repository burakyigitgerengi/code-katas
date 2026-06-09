class Queue:
    def __init__(self) -> None:
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.pop(0)

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return not self.elements

    def sort(self, reverse_choice: bool = False):
        self.elements.sort(reverse=reverse_choice)

    def search(self, term):
        index = 0
        for _ in self.elements:
            if _ == term:
                print(f"{term} found at index: {index}")

            else:
                index += 1

    def __str__(self) -> str:

        queue_print = "Queue: "

        index = 0

        for _ in self.elements:

            if index == len(q) - 1:
                queue_print += str(_)

            else:
                queue_print += str(_) + " <- "
            index += 1

        return queue_print


# Test Cases code taken from AI

# 1. Create a fresh queue
# q = Queue()
# print(f"Is it empty? {q.is_empty()}")  # Expected: True
#
## 2. Add some people to the line
# print("\n--- Lining up ---")
# q.enqueue("Alice")
# q.enqueue("Bob")
# q.enqueue("Charlie")
#
# print(f"Queue size: {len(q)}")  # Expected: 3
# print(f"Is it empty now? {q.is_empty()}")  # Expected: False
#
## 3. Serve them (FIFO order)
# print("\n--- Serving ---")
# print(f"Served: {q.dequeue()}")  # Expected: Alice
# print(f"Served: {q.dequeue()}")  # Expected: Bob
#
## 4. Check the final state
# print("\n--- Final Check ---")
# print(f"Remaining size: {len(q)}")  # Expected: 1
# print(f"Last person left: {q.dequeue()}")  # Expected: Charlie

# Test Cases code written by me

# Create a queue, and add 3 people:

q = Queue()

q.enqueue("Celal")
q.enqueue("Aziz")
q.enqueue("Samet")

# Print the queue:

print(q)

# Sort & print:

q.sort()
print(q)

# Add Celal again & search Celal:

q.enqueue("Celal")
print(q)
q.search("Celal")

# Dequeue & print

q.dequeue()
print(q)
