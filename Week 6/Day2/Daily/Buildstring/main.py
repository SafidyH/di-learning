import random

text = input("Enter a string (10 characters): ")

if len(text) < 10:
    print("String not long enough.")
elif len(text) > 10:
    print("String too long.")
else:
    print("Perfect string!")

    print("First character:", text[0])
    print("Last character:", text[-1])

    for i in range(len(text)):
        print(text[:i+1])

    shuffled_text = list(text)
    random.shuffle(shuffled_text)
    shuffled_text = ''.join(shuffled_text)
    print("Shuffled string:", shuffled_text)
