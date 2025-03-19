class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        sortedCoins = sorted(coins, reverse=True);
        return self.traverse(sortedCoins, amount);

    def traverse(self, coins: list[int], amount: int) -> int:
        minimum = -1;
        if amount < 0:
            return -1;
        if amount == 0:
            return 0;
        for c in coins:
            if c > amount:
                continue;
            next = self.traverse(coins, amount-c);
            if next != -1:
                if minimum == -1:
                    minimum = next + 1;
                elif minimum > next + 1:
                    minimum = next + 1;
                else:
                    break;
        return minimum;

sol = Solution();
print(sol.coinChange([1,2,5], 11));
print(sol.coinChange([1,2,5], 11));
print();