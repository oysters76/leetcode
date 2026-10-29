class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set() 
        for n in nums:
            if n in seen:
                return True 
            else:
                seen.add(n) 
        return False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


# Notes:
# - Both are O(n) time, O(n) space
# - Approach 1 can exit early the moment it finds a duplicate (faster in best case)
# - Approach 2 always processes the entire list first (simpler but no early exit)
# - Approach 1 uses the same "check then store" pattern from Two Sum

'''

Same lesson reinforced: check as you go beats processing everything first.

But there’s a new layer here — you wrote both approaches, so the takeaway is: know when a shortcut exists, 
but understand why the longer version matters.

The one-liner (set(nums) != len(nums)) is clever, but it always scans the full list. The loop version 
can bail out on the first duplicate. In an interview or with huge data, that early exit matters.

So the meta learning: “shorter code” and “better solution” aren’t always the same thing.

'''