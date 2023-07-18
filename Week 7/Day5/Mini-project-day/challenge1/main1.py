def insert_item(lst, index, item):
    lst.insert(index, item)

my_list = [1, 2, 3, 4, 5]
insert_index = 2
new_item = "Hello"

insert_item(my_list, insert_index, new_item)
print(my_list)
