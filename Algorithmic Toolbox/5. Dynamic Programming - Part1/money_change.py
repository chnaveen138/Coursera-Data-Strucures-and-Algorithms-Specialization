# Source code in python3
def moneyChange(money, coins):
    minNumCoins = dict();
    minNumCoins[0] = 0;
    for m in range(1, money + 1):
        minNumCoins[m] = 999999999999999;
        for j in coins:
            if m >= j:
                numCoins = minNumCoins[m - j] + 1;
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins;
    return minNumCoins[money];
money = int(input());
coinDenominations = [1, 3, 4];
changeForMoney = moneyChange(money, coinDenominations);
print(changeForMoney);