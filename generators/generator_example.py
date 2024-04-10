# my_list = [1, 2, 3, 4, 5]

def my_list():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for num in my_list():
    print(num)

# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))