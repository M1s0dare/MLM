import random
from collections import Counter
import statistics
import time

# 定数の設定
ENTRY_FEE = 420000  # 入会金
DIRECT_CASHBACK = 40000  # 直接勧誘のキャッシュバック
INDIRECT_CASHBACK = 13333  # 間接勧誘のキャッシュバック
CONVERGENCE_INCOME = 60000  # 1人勧誘の理論収束値
CAFE_COST = 500  # カフェ代
TRANSPORT_COST = 600  # 交通費（3回ごと）
TIME_PER_MEETING = 1.5  # 1回の勧誘にかかる時間（時間）
NUM_SIMULATIONS = 1000  # シミュレーション実行回数

# 結果を保存するリスト
all_recruitment_counts = []  # 勧誘成功数
all_meeting_counts = []  # 勧誘試行数
all_total_expenses = []  # 総支出
all_hourly_wages = []  # 時給
all_success_rates = []  # 成功率

print(f"マルチ商法シミュレーション（{NUM_SIMULATIONS}回実行）")
print("計算中...\n")

start_time = time.time()

# シミュレーションを複数回実行
for sim_num in range(NUM_SIMULATIONS):
    # 初期設定
    total_expense = ENTRY_FEE  # 累計支出（入会金から開始）
    total_income = 0  # 累計収入
    recruitment_count = 0  # 勧誘成功回数
    meeting_count = 0  # 勧誘試行回数
    
    # 収入が支出を上回るまでシミュレーション続行
    while total_income < total_expense:
        dice1 = random.randint(1, 6)  # 1つ目のサイコロ - 勧誘回数を決定
        
        # この人に対する勧誘回数と費用
        person_meeting_count = dice1
        person_expense = 0
        
        # この人への勧誘を実行
        for i in range(person_meeting_count):
            # 勧誘回数カウント
            meeting_count += 1
            
            # 勧誘費用の追加
            meeting_expense = CAFE_COST
            if meeting_count % 3 == 0:  # 3回ごとに交通費
                meeting_expense += TRANSPORT_COST
            
            person_expense += meeting_expense
        
        # 勧誘費用の合計を追加
        total_expense += person_expense
        
        # 勧誘成功の判定
        dice2 = random.randint(1, 6)  # 2つ目のサイコロ
        if dice2 == 1:  # 勧誘成功
            recruitment_count += 1
            # 1人勧誘成功で得られる理論収入
            total_income += CONVERGENCE_INCOME
    
    # 時間と効率の計算
    total_hours = meeting_count * TIME_PER_MEETING
    hourly_wage = (total_income - total_expense) / total_hours if total_hours > 0 else 0
    success_rate = recruitment_count / meeting_count if meeting_count > 0 else 0
    
    # 結果を記録
    all_recruitment_counts.append(recruitment_count)
    all_meeting_counts.append(meeting_count)
    all_total_expenses.append(total_expense)
    all_hourly_wages.append(hourly_wage)
    all_success_rates.append(success_rate)

end_time = time.time()
computation_time = end_time - start_time

# 統計データの計算
avg_recruitment = statistics.mean(all_recruitment_counts)
avg_meetings = statistics.mean(all_meeting_counts)
avg_expenses = statistics.mean(all_total_expenses)
avg_hourly_wage = statistics.mean(all_hourly_wages)
avg_success_rate = statistics.mean(all_success_rates)

med_recruitment = statistics.median(all_recruitment_counts)
med_meetings = statistics.median(all_meeting_counts)
med_expenses = statistics.median(all_total_expenses)
med_hourly_wage = statistics.median(all_hourly_wages)

min_recruitment = min(all_recruitment_counts)
max_recruitment = max(all_recruitment_counts)
min_meetings = min(all_meeting_counts)
max_meetings = max(all_meeting_counts)

# 結果の表示
print("===== シミュレーション結果統計 =====")
print(f"実行回数: {NUM_SIMULATIONS}回 (計算時間: {computation_time:.2f}秒)")
print("\n【収支が黒字化するために必要な勧誘成功数】")
print(f"平均: {avg_recruitment:.2f}人")
print(f"中央値: {med_recruitment}人")
print(f"最小: {min_recruitment}人 / 最大: {max_recruitment}人")

print("\n【勧誘を試みた回数】")
print(f"平均: {avg_meetings:.2f}回")
print(f"中央値: {med_meetings}回")
print(f"最小: {min_meetings}回 / 最大: {max_meetings}回")

print("\n【費用と時間】")
print(f"平均支出: {avg_expenses:,.0f}円 (入会金 {ENTRY_FEE:,}円 + 勧誘費用)")
print(f"平均勧誘時間: {avg_meetings * TIME_PER_MEETING:.1f}時間")
print(f"平均時給: {avg_hourly_wage:,.0f}円/時間")
print(f"中央値時給: {med_hourly_wage:,.0f}円/時間")
print(f"平均勧誘成功率: {avg_success_rate:.2%}")

recruitment_distribution = Counter(all_recruitment_counts)
print("\n【勧誘成功数の分布】")
for count, occurrences in sorted(recruitment_distribution.items()):
    print(f"{count}人: {occurrences}回 ({occurrences/NUM_SIMULATIONS:.1%})")
