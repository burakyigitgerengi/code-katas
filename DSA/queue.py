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


# Test Cases code taken from AI

# 1. Create a fresh queue
q = Queue()
print(f"Is it empty? {q.is_empty()}")  # Expected: True

# 2. Add some people to the line
print("\n--- Lining up ---")
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")

print(f"Queue size: {len(q)}")  # Expected: 3
print(f"Is it empty now? {q.is_empty()}")  # Expected: False

# 3. Serve them (FIFO order)
print("\n--- Serving ---")
print(f"Served: {q.dequeue()}")  # Expected: Alice
print(f"Served: {q.dequeue()}")  # Expected: Bob

# 4. Check the final state
print("\n--- Final Check ---")
print(f"Remaining size: {len(q)}")  # Expected: 1
print(f"Last person left: {q.dequeue()}")  # Expected: Charlie
