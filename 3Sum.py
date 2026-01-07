# Problem: 3Sum
# Link: https://leetcode.com/problems/3sum/
# Zorluk: Medium

# Time Complexity: O(N^2) (İç içe geçen tarama işlemi nedeniyle)
# Space Complexity: O(N) (Cevapları tutmak için 'set' kullandığımız ve sonuç listesi oluşturduğumuz için)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cevap = set()

        p1 = 0
        p2 = 1
        p3 = len(nums) - 1

        while p1 < len(nums) - 2:

            if p2 >= p3:
                p1 = p1 + 1
                p2 = p1 + 1
                p3 = len(nums) - 1
                continue

            if p1 >= len(nums) - 2:
                break

            c = nums[p1] + nums[p2] + nums[p3]

            if c == 0:
                cevap.add((nums[p1], nums[p2], nums[p3]))
                p2 = p2 + 1
                p3 = p3 - 1

            elif c < 0:
                p2 = p2 + 1

            else:
                p3 = p3 - 1

        return [list(x) for x in cevap]


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1 (Klasik Örnek)
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.threeSum(nums1)}")

    print("-" * 20)

    # Test Senaryosu 2 (Boş Dönmesi Gereken)
    nums2 = [0, 1, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.threeSum(nums2)}")

    print("-" * 20)

    # Test Senaryosu 3 (Sıfırlar)
    nums3 = [0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.threeSum(nums3)}")