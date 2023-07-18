def count_spaces(string):
    count = 0
    for char in string:
        if char == ' ':
            count += 1
    return count

my_string = "Hello, world! How are you?"
spaces_count = count_spaces(my_string)
print("Number of spaces:", spaces_count)
