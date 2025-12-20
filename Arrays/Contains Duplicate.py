# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Zorluk: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        gorduklerim = set()

        for sayi in nums:
            if sayi in gorduklerim:
                return True

            gorduklerim.add(sayi)

        return False

if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1
    nums1 = [1,2,3,1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.containsDuplicate(nums1)}")

    print("-" * 20)

    # Test Senaryosu 2
    nums2 = [1,2,3,4]
    print(f"Input: {nums2}")
    print(f"Output: {solution.containsDuplicate(nums2)}")
