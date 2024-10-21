import timeit 

# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [{} for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1
    return coin_count[amount]

# Приклад для суми 113
print(find_coins_greedy(113))
print(find_min_coins(113))

# Оцінка часу виконання
greedy_time = timeit.timeit("find_coins_greedy(113)", globals=globals(), number=1000)
dp_time = timeit.timeit("find_min_coins(113)", globals=globals(), number=1000)

print(f"Greedy Time: {greedy_time}")
print(f"DP Time: {dp_time}")