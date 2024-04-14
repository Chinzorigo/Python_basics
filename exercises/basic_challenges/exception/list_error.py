str_of_num = '2, 5, 10'  # input()
list_of_num = str_of_num.split(', ')
print(list_of_num)  # ['2', '5', '10']
print(type(list_of_num))  # <class 'list'>

# numbers_list = []

# for num_str in list_of_num:
#     numbers_list.append(int(num_str))

numbers_list = list(map(int, list_of_num))

print(numbers_list)  # ['2', '5', '10']
print(type(numbers_list))  # <class 'list'>

result = 1

for i in range(len(numbers_list)):
    print(i)
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
