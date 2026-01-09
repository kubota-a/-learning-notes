# 設計メモ
# ※
# ```
# ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]を要素とするリストlを宣言
# ループ終了後、「重複する文字列 : 」と　　　をprintで出力

telephone_numbers = ['080-1203-4455', '090-9372-9682', '090-3080-4982', '080-3917-5918']
new_telephone_numbers = [n for n in telephone_numbers if n.startswith("080")]
print(f'080で始まる電話番号 : {new_telephone_numbers}')