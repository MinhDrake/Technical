from typing import List
class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        start, end = -k , -k 
        score = 0
        ans = 0
        while end < k:
            score += cards[end]

            if end - start + 1 >= k:
                ans = max(ans, score)
                score -= cards[start]
                start += 1
            end += 1
        return ans

sol = Solution()
print(sol.maxScore([1,2,3,4,5,6,1], 3))