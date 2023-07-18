def box_printer(*words):
    max_length = max(len(word) for word in words)
    border = '*' * (max_length + 4)
    print(border)
    for word in words:
        print('* {:<{}} *'.format(word, max_length))
    print(border)

# Test the function
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
