# Two numbers add up to a target
# Sorted array is given
# For problems that have unsorted arrays, just sort the array to continue the steps below

class Solution:
    def twoPointers(self, array, target):
        i = 0
        j = len(array) - 1

        while(i < j):
            if(array[i] + array[j] < target):
                i += 1

            elif(array[i] + array[j] > target):
                j -= 1

            else:
                print(f"Solution: {array[i]} + {array[j]} = {target}")
                i += 1

solution = Solution()
solution.twoPointers([2,3,4,5,6,7], 11)
