class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        

        freq={}

        for ch in nums:

            freq[ch]=freq.get(ch,0)+1

        for num,count in freq.items():

            if count > len(nums)//2:

                return num
        