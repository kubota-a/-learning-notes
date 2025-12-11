# 12/11
# Q1：0〜10 の数字を順番に出力しよう
for i in range(11):
    print(i)

print("-" * 15)    # ----------------
# Q2：2〜10 の偶数だけを出力しよう▲
for i in range(0, 11, 2):
    print(i)
print("-" * 15)    # ----------------
for i in range(11):
    if i % 2 == 0:
        print(i)

print("-" * 15)    # ----------------
# Q3：文字列 "Python" の各文字を1文字ずつ出力しよう▲
word = "Python"
for s in word:
    print(s)
print("-" * 15)    # ----------------
word = "Python"
for i in range(len(word)):
    print(word[i])

print("-" * 15)    # ----------------
# Q4：文字列 "Hello" の長さを出力しよう
s = "Hello"
print(len(s))

print("-" * 15)    # ----------------
# Q5：文字列 "fjeophslgotnnoremcl" の最後から3文字を出力しよう▲
s = "fjeophslgotnnoremcl"
print(s[-3:])