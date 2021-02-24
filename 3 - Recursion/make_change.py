"""
Two methods of calculating the amount of coins needed to make change
for a specific amount.
"""


def make_change_recursive(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [coin for coin in coin_value_list if coin <= change]:
            num_coins = 1 + make_change_recursive(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins
    return min_coins


print(make_change_recursive([1, 2, 5, 10, 25, 50, 100, 200], 412, [0] * 500))


#####################################################


def make_change_loop(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [coin for coin in coin_value_list if coin <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


def main():
    amount = 63
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print(
        f"Making change for {amount} requires the following "
        f"{make_change_loop(coin_list, amount, coin_count, coins_used)} "
        f"coins: ", end="")

    print_coins(coins_used, amount)
    print("The used list is as follows:")
    print(coins_used)


main()

















