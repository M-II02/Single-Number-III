class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hs = set()
        for i in nums:
            if i in hs:
                hs.remove(i)
            else:
                hs.add(i)
        return list(hs)

        
