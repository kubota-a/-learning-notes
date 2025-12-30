l = [1, 5, 3, 2, 4]
l_int = [int(i) for i in l]
max_num = l_int[0]
for num in l_int:
    if num > max_num:
        max_num = num
print(f'リスト内の最大値 : {max_num}')
