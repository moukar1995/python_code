num = 100

total = sum(range(1, num + 1))
print(total)  # 👉️ 5050

# 👇️ [1, 2, 3, ... 98, 99, 100]
print(list(range(1, num + 1)))

# ------------------------------------------------

# 👇️ alternatively, you can use a formula

total_2 = num * (num + 1) // 2

print(total_2)  # 👉️ 5050
