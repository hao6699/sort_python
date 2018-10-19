def FindGreatestSumOfSubArray(self, array):
        # write code here
        totalsum = array[0]
        max_sum = array[0]
        for i in range(1,len(array)):
            totalsum = max(totalsum+array[i],array[i])
            max_sum = max(totalsum,max_sum)
        return max_sum
