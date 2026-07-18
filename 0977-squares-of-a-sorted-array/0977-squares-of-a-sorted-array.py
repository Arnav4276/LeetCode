class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in nums:
            nums2.append(i*i)
        nums3=sorted(nums2)
        return nums3