# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Zorluk: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sozluk = {}  # { Sayı : İndex }

        for i, sayi in enumerate(nums):
            fark = target - sayi

            if fark in sozluk:
                return [sozluk[fark], i]

            sozluk[sayi] = i

        return []


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: {nums1}, Target: {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")

    print("-" * 20)

    # Test Senaryosu 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: {nums2}, Target: {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")
