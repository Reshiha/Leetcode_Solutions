class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr1 = []
        arr2 = []
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            arr1.append(temp)
        max_candies = max(candies)
        for candy in arr1:
            if candy >= max_candies:
                arr2.append(True)
            else:
                arr2.append(False)
        return arr2
         