num_list = []

num = int(input())

for i in range(num):
    new_num = int(input())
    num_list.append(new_num)

num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])