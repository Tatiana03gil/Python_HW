#Task 22

"""first_length = int(input("Введите кол-во элементов 1-го набора чисел: "))
second_length = int(input("Введите кол-во элементов 2-го набора чисел: "))

print("Заполните 1 набор чисел: ")
list_1 = list()
for i in range(first_length):
    list_1.append(int(input()))
print("Заполните 2 набор чисел: ")
list_2 = list()
for i in range(second_length):
    list_2.append(int(input()))

set_1 = set(list_1)
set_2 = set(list_2)

result = list(set_1.intersection(set_2))

for i in range (len(result)):
    ind_min = i
    for j in range (i, len(result)):
        if result[j] < result[ind_min]:
            ind_min = j
    temp = result[i]
    result[i] = result[ind_min]
    result[ind_min] = temp
print(*result)"""

#task 24

num_of_scrubs = int(input("Введите кол-во кустов: "))
berries = list()
print("Введите количество ягод на кустах: ")
for i in range(num_of_scrubs):
    berries.append(int(input()))

sum_max = berries[0] + berries[1] + berries[-1]
for i in range (1,len(berries)-1):
    sum_temp = berries[i] + berries[i+1] + berries[i-1]
    if sum_max < sum_temp:
        sum_max = sum_temp  
print (f"Максимальное число ягод за заход - {sum_max}")
