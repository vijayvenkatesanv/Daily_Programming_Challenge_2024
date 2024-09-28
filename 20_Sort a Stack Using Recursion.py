class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def sorted_insert(stack, element):
    if stack.is_empty() or stack.peek() <= element:
        stack.push(element)
        return
    temp = stack.pop()
    sorted_insert(stack, element)
    stack.push(temp)

def sort_stack(stack):
    if stack.is_empty():
        return
    top_element = stack.pop()
    sort_stack(stack)
    sorted_insert(stack, top_element)

if __name__ == "__main__":
    test_cases = [
        ([3, 1, 4, 2], [1, 2, 3, 4]),
        ([7, 1, 5], [1, 5, 7]),
        ([5], [5]),
        ([-3, 14, 8, 2], [-3, 2, 8, 14]),
        ([], []),
        ([3, 3, 3], [3, 3, 3])
    ]

    for idx, (input_stack, expected) in enumerate(test_cases):
        stack = Stack()
        for num in input_stack:
            stack.push(num)
        sort_stack(stack)
        result = stack.items
        print(f"Test Case {idx + 1}: Input: {input_stack}, Sorted: {result}, Expected: {expected}")

    user_input = input("Enter numbers separated by space (e.g., '3 1 4 2'): ")
    user_stack = Stack()
    for num in map(int, user_input.split()):
        user_stack.push(num)
    
    sort_stack(user_stack)
    print("Sorted Stack:", user_stack)
