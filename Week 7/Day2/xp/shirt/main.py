def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'")

# Call the function with different arguments
make_shirt("large", "I love Python")
make_shirt("medium", "I love Python")
make_shirt("small", "Hello, world!")

# Call the function using keyword arguments
make_shirt(size="large", message="I love Python")
make_shirt(message="Hello, world!", size="small")
