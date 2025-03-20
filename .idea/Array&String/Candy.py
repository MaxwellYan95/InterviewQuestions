class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [];
        for index in range(len(ratings)):
            left = -1;
            right = -1;
            if index-1 > -1:
                left = ratings[index-1];
            if index+1 < len(ratings):
                right = ratings[index+1];
            number = 1;
            curRating = ratings[index];
            haveValues = (right != -1 and left != -1);
            if curRating > left and right == -1:
                number = candies[index-1] + 1;
            elif curRating > right and left == -1:
                number = number + 1;
            elif curRating >= right and curRating > left and haveValues:
                number = candies[index-1] + 1;
            elif curRating > right and curRating >= left and haveValues:
                number = candies[index+1] + 1;
            candies.append(number);
        return sum(candies);

sol = Solution();
print(sol.candy([1,2,2]));
print();