my_fav_numbers = {3, 7, 9, 12}  # Create a set with favorite numbers
my_fav_numbers.add(5)  # Add two new numbers to the set
my_fav_numbers.add(8)
my_fav_numbers.remove(12)  # Remove the last number

friend_fav_numbers = {2, 4, 6, 8}  # Create a set with friend's favorite numbers

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)  # Concatenate sets

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)
