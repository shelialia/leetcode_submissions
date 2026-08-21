from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a Counter to store value -> count
        #   - Helps us to fill up the Bucket

        # Use a Bucket of size len(nums) + 1 to store count -> values with this count
        #   - Helps us to hit final goal of "return the k most frequent elements"

        nums_counter = Counter(nums)
        # Use len(nums) + 1 because a number can appear as many as len(nums) times
        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in nums_counter.items():
            bucket[count].append(num)
        
        res = []

        for count in range(len(nums), -1, -1):
            for num in bucket[count]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
                
