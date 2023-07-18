import random

class MyList:
    def __init__(self, letters):
        self.my_list = letters

    def reverse_list(self):
        return list(reversed(self.my_list))

    def sort_list(self):
        return sorted(self.my_list)

    def generate_random_list(self):
        return [random.randint(1, 100) for _ in self.my_list]

# Example usage
letters = ['a', 'b', 'c', 'd', 'e']
my_list = MyList(letters)
reversed_list = my_list.reverse_list()
sorted_list = my_list.sort_list()
random_list = my_list.generate_random_list()

print(f"Original List: {letters}")
print(f"Reversed List: {reversed_list}")
print(f"Sorted List: {sorted_list}")
print(f"Random List: {random_list}")
