class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n , left , right = len(citations) , 0 , len(citations)
        while left < right:
            mid = left + (right - left) // 2
            numGreater = n - mid
            if numGreater <= citations[mid]:
                right = mid
            else:
                left = mid + 1
        return n - left
