from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            while freq_map[nums[right]] > k:
                freq_map[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1) 
        return max_length