# 設計メモ
# ※
# ```
# ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]を要素とするリストlを宣言
# ループ終了後、「重複する文字列 : 」と　　　をprintで出力


# 再チャレンジ
l = [1, 2, 3, 3]
l_copy =[i for i in l]
for i in l:
    if i in l_copy:
        l_copy.remove(i)
print(len(l_copy))
if len(l_copy) > 0:
    print("重複している値があります。")
else:
    print("重複する値がありません。") 


l = [1, 2, 3, 3]

seen = []
duplicate = False

for i in l:
    if i in seen:
        duplicate = True
        break
    seen.append(i)

if duplicate:
    print("重複している値があります。")
else:
    print("重複する値がありません。")