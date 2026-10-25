class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        total=sum(nums)

        for i in range(len(nums)):

            current=nums[i]
            required=target-current

            if required in hashmap:

                return [hashmap[required],i]

            hashmap[current]=i
           
        