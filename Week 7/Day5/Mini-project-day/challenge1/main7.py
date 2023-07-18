def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Test the function
lst = ['a', 'a', 't', 'o']
element = 'a'
result = list_count(lst, element)
print(result)
