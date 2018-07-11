# my_list = [1, 2, 3]
# my_list = ['asdf', 1, 'two', 3, ['a', 'b', 'c']]
# print(len(my_list))
# print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e']

print('my_list: ', my_list[0])
print('my_list: ', my_list[-1])
print('my_list: ', my_list[1:])
print('my_list: ', my_list[:3])
print('my_list: ', my_list[1:3])

# Lists are mutable!
my_list[0] = 'New Item'
print('my_list', my_list)

# append
my_list.append('New Item to End')
print('my_list: ', my_list)

ext_list = ['more', 'stuff', 'to', 'add']

# extend
my_list.extend(ext_list)
print('my_list extended: ', my_list)

# poppimg
my_list.pop()
print('my_list popped: ', my_list)

my_list.pop(3)
print('my_list popped specific: ', my_list)

# reverse
my_list.reverse()
print('my_list reversed: ', my_list)

# sort
my_list = [5, 3, 69, 21, 55]
my_list.sort()
print('my_list sorted: ', my_list)

# nested lists
my_list = [1,2,['x','y','z']]
print('my_list find nested y: ', my_list[2][1])

# list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('matrix first of first: ', matrix[0][0])
first_col = [row[0] for row in matrix]
print('first_col: ', first_col)
