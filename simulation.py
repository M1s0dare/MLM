import random
from collections import Counter

# 2つ目のサイコロが1を7回出すまで繰り返す
count = 0 # 2つ目のサイコロが1を出した回数
output_count = 0 # 10回ごとに改行をいれるためのカウンター

# 出力結果を座標データとしてカウント
data = []

while count < 7:
    dice1 = random.randint(1, 6) # 1つ目のサイコロ
    dice2 = random.randint(1, 6) # 2つ目のサイコロ

    # サイコロの目を表示
    print(f"( {dice1}, {dice2})", end=" ")

    # 10回ごとに改行
    output_count += 1
    if output_count % 10 == 0:
        print() # 改行

    if dice2 == 1:
        count += 1 # 2つ目のサイコロが1を出した回数をカウント
    
    # 結果を座標データとして保存
    data.append((dice1, dice2))

print("\nサイコロ2が1を7回出ました")

# x座標の出現回数をカウント
x_counts = Counter(x for x, _ in data)

# 結果を表示
for x, count in sorted(x_counts.items()):
    print(f"x={x} : {count}回")

# 元を取るまでにカフェに行く回数(1*x1+2*x2+3*x3+4*x4+5*x5+6*x6)
go_cafe = 0
for x, count in x_counts.items():
    go_cafe += x * count

print(f"カフェに行く回数: {go_cafe}回")