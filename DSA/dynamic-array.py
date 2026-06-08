import ctypes


class DynamicArray:
    def __init__(self) -> None:
        self.count = 0
        self.capacity = 1
        self.storage = (self.capacity * ctypes.py_object)()

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if 0 <= index <= (self.count - 1):
            return self.storage[index]
        else:
            raise IndexError

    def append(self, item):

        if self.count == 0:
            self.storage[self.capacity - 1] = item
            self.count += 1

        elif self.count == self.capacity:
            self._resize(self.capacity + 1)
            self.storage[self.capacity - 1] = item
            self.count += 1

        else:
            self.storage[self.capacity - 1] = item
            self.count += 1

    def _resize(self, new_capacity):
        self.temp_storage = (new_capacity * ctypes.py_object)()
        for _ in range(self.capacity):
            self.temp_storage[_] = self.storage[_]
        self.capacity = new_capacity
        self.storage = self.temp_storage


# The Test Suite from me

dynamic_array = DynamicArray()

dynamic_array.append("aziz")
dynamic_array.append("aziz")

print(dynamic_array[1])
print(len(dynamic_array))

# The Test Suite from AI

# 1. Instantiate your custom array
arr = DynamicArray()

print("--- Testing Initialization ---")
print(f"Initial Length: {len(arr)}")  # Expected: 0
print(f"Initial Capacity: {arr.capacity}")  # Expected: 1

print("\n--- Testing First Append ---")
arr.append("Python")
print(f"Length: {len(arr)}")  # Expected: 1
print(f"Capacity: {arr.capacity}")  # Expected: 1
print(f"Element at index 0: {arr[0]}")  # Expected: 'Python'

print("\n--- Testing Triggering a Resize (Doubling) ---")
arr.append("C++")  # This should trigger the resize because count was equal to capacity
print(f"Length: {len(arr)}")  # Expected: 2
print(f"New Capacity: {arr.capacity}")  # Expected: 2
print(f"Element at index 1: {arr[1]}")  # Expected: 'C++'

print("\n--- Testing Mass Appends ---")
arr.append("Java")
arr.append("Rust")
print(f"Length: {len(arr)}")  # Expected: 4
print(f"Capacity after Rust: {arr.capacity}")  # Expected: 4

print("\n--- Testing Guardrails (Error Handling) ---")
try:
    print(arr[5])  # Index 5 doesn't exist!
except IndexError:
    print("Success: IndexError successfully raised for out-of-bounds index!")
