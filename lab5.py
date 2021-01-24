# 2
def function(fruits):
    return fruits[5]


fruits = ['Orange', 'Banana', 'Berries', 'Apples', 'Lemon', 'Grape']
print(function(fruits))


# 3
def dictionary(cloth_dict, num2):
    return [num2]


cloth_dict = myDict = {'Gray': 'Casual', 'white': 'Church', 'Blue': 'Work'}
print(dictionary(cloth_dict, num2='white'))

# 4
x = [4, 5, 6]
y = [6, 7, 8]


def set_of_values(x, y):
    values = [x + y]
    return values


result = set_of_values(x, y)
print(result)
