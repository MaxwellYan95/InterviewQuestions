class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        sortedCoins = sorted(coins, reverse=True);
        return self.traverse(sortedCoins, amount);

    def traverse(self, coins: list[int], amount: int) -> int:
        found = False;
        minimum = -1;
        if amount < 0:
            return -1;
        if amount == 0:
            return 0;
        for c in coins:
            if c > amount:
                continue;
            coinAmount = int(amount/c);
            newAmount = int(amount - (c*coinAmount));
            next = self.traverse(coins, newAmount);
            if found == False and next != -1:
                minimum = next + coinAmount;
                found = True;
            else:
                if next != -1:
                    minimum = min(minimum, next + coinAmount);
        return minimum;

sol = Solution();
print(sol.coinChange([1,2,5], 11));
print(sol.coinChange([1,2,5], 11));
print();