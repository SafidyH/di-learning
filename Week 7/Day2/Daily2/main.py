import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

# Initialize counter for the number of pairs found
pair_counter = 0

# Iterate over each number in the list
for i in range(len(list_of_numbers)):
    current_number = list_of_numbers[i]
    
    # Iterate over the remaining numbers
    for j in range(i + 1, len(list_of_numbers)):
        other_number = list_of_numbers[j]
        
        # Check if the pair sums to the target number
        if current_number + other_number == target_number:
            pair_counter += 1

# Print the total number of pairs found
print("Number of pairs that sum to the target number:", pair_counter)
