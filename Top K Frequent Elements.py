# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Zorluk: Medium

# Time Complexity: O(n log n) (Sıralama fonksiyonu kullanıldığı için)
# Space Complexity: O(n)

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sozluk = {}  # key : sayı / value : kaç kere geçtiği

        for i in nums:
            if i in sozluk:
                sozluk[i] = sozluk[i] + 1
            else:
                sozluk[i] = 1

        # Elemanları sıralama
        sirali_liste = sorted(sozluk.items(), key=lambda x: x[1], reverse=True)

        sonuc = []
        for i in range(k):
            sonuc.append(sirali_liste[i][0])

        return sonuc


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.topKFrequent(nums1, k1)}")

    print("-" * 20)

    # Test Senaryosu 2
    nums2 = [1]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.topKFrequent(nums2, k2)}")

    print("-" * 20)

    # Test Senaryosu 3
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.topKFrequent(nums3, k3)}")