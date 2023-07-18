def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

# Test
name1 = get_full_name(first_name="john", middle_name="hooker", last_name="lee")
print(name1)

name2 = get_full_name(first_name="bruce", last_name="lee")
print(name2)
