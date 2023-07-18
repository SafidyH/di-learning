def count_letters(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count

my_string = "Hello, World!"
uppercase_count, lowercase_count = count_letters(my_string)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
