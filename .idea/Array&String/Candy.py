class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [];
        for index in range(len(ratings)):
            candies[index] = 1;
        for index in range(len(ratings)):
            left = -1;
            if index-1 > -1:
                left = ratings[index-1];
            number = 1;
            curRating = ratings[index];
            haveValues = (left != -1);
            if left > curRating and haveValues:
                candies[index-1] = candies[index-1] + 1;
            if curRating > left and haveValues:
                number = candies[index-1] + 1;
            candies.append(number);
        return sum(candies);

sol = Solution();
print(sol.candy([1, 0, 2]));
print(sol.candy([1, 3, 2, 2, 1]));
print();