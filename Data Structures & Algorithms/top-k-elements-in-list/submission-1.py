class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        freq=Counter(nums)

        buckets=[]

        for i in range(len(nums)+1):

            buckets.append([])

        for num,count in freq.items():

            buckets[count].append(num)

        result=[]

        for i in range(len(buckets)-1,0,-1):

            for num in buckets[i]:

                result.append(num)

                if len(result)==k:

                    return result




        