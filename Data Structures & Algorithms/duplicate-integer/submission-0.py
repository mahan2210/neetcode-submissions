class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dub = set()
        for num in nums:
            if num in no_dub:
                return True
            no_dub.add(num)
        return False