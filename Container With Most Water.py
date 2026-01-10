# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Zorluk: Medium

# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        winner = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:

            genislik = p2 - p1
            yukseklik = min(height[p1], height[p2])

            alan = genislik * yukseklik

            if winner < alan:
                winner = alan

            if height[p1] < height[p2]:
                p1 = p1 + 1
            else:
                p2 = p2 - 1

        return winner


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1 (Klasik Örnek)
    nums1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = {nums1}")
    print(f"Output: {solution.maxArea(nums1)}")

    print("-" * 20)

    # Test Senaryosu 2 (İkili Dizi)
    nums2 = [1, 1]
    print(f"Input: height = {nums2}")
    print(f"Output: {solution.maxArea(nums2)}")

    print("-" * 20)

    # Test Senaryosu 3 (Artan/Azalan Karışık)
    nums3 = [4, 3, 2, 1, 4]
    print(f"Input: height = {nums3}")
    print(f"Output: {solution.maxArea(nums3)}")