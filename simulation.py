import random
from collections import Counter

# 定数の設定
ENTRY_FEE = 420000  # 入会金
DIRECT_CASHBACK = 40000  # 直接勧誘のキャッシュバック
INDIRECT_CASHBACK = 13333  # 間接勧誘のキャッシュバック
CONVERGENCE_INCOME = 60000  # 1人勧誘の理論収束値
CAFE_COST = 500  # カフェ代
TRANSPORT_COST = 600  # 交通費（3回ごと）
TIME_PER_MEETING = 1.5  # 1回の勧誘にかかる時間（時間）

# 初期設定
total_expense = ENTRY_FEE  # 累計支出（入会金から開始）
total_income = 0  # 累計収入
recruitment_count = 0  # 勧誘成功回数
meeting_count = 0  # 勧誘試行回数
output_count = 0  # 表示用カウンター

# 出力結果を座標データとしてカウント
data = []

print(f"マルチ商法シミュレーション開始（入会金: {ENTRY_FEE:,}円）")

# 収入が支出を上回るまでシミュレーション続行
while total_income < total_expense:
    dice1 = random.randint(1, 6)  # 1つ目のサイコロ
    dice2 = random.randint(1, 6)  # 2つ目のサイコロ
    
    # サイコロの目を表示
    print(f"({dice1}, {dice2})", end=" ")
    
    # 10回ごとに改行
    output_count += 1
    if output_count % 10 == 0:
        print()
    
    # 勧誘回数カウント
    meeting_count += 1
    
    # 勧誘費用の追加
    meeting_expense = CAFE_COST
    if meeting_count % 3 == 0:  # 3回ごとに交通費
        meeting_expense += TRANSPORT_COST
    
    total_expense += meeting_expense
    
    # 結果を座標データとして保存
    data.append((dice1, dice2))
    
    # 勧誘成功の場合
    if dice2 == 1:
        recruitment_count += 1
        # 1人勧誘成功で得られる理論収入
        total_income += CONVERGENCE_INCOME
        print(f"\n★ 勧誘成功 {recruitment_count}人目！現在の収支: 収入{total_income:,}円 - 支出{total_expense:,}円 = {total_income - total_expense:,}円")

# x座標の出現回数をカウント
x_counts = Counter(x for x, _ in data)

print("\n===== シミュレーション結果 =====")
print(f"入会金を回収するために必要だった勧誘成功数: {recruitment_count}人")
print(f"勧誘を試みた回数: {meeting_count}回")

# 結果を表示
for x, count in sorted(x_counts.items()):
    print(f"サイコロ1の目 {x}: {count}回")

# カフェに行った回数
print(f"\nカフェに行った回数: {meeting_count}回")

# 勧誘費用の計算
cafe_cost = meeting_count * CAFE_COST
transport_trips = meeting_count // 3
transport_cost = transport_trips * TRANSPORT_COST
recruitment_cost = cafe_cost + transport_cost

print(f"飲み物代: {cafe_cost:,}円（{CAFE_COST}円 × {meeting_count}回）")
print(f"交通費: {transport_cost:,}円（{TRANSPORT_COST}円 × {transport_trips}回）")
print(f"勧誘費用合計: {recruitment_cost:,}円")

# 総費用と収入
print(f"\n入会金: {ENTRY_FEE:,}円")
print(f"総支出: {total_expense:,}円（入会金 + 勧誘費用）")
print(f"総収入: {total_income:,}円（{CONVERGENCE_INCOME}円 × {recruitment_count}人）")
print(f"収支: {total_income - total_expense:,}円")

# 時間計算
total_hours = meeting_count * TIME_PER_MEETING
print(f"\n勧誘にかかった時間: {total_hours:.1f}時間")

# 時給換算
hourly_wage = (total_income - total_expense) / total_hours if total_hours > 0 else 0
print(f"時給換算: {hourly_wage:,.1f}円/時間")

# 成功確率の計算
success_rate = recruitment_count / meeting_count if meeting_count > 0 else 0
print(f"勧誘成功率: {success_rate:.2%} ({recruitment_count}/{meeting_count})")
