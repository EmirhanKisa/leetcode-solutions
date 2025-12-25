# Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Zorluk: Medium

# Time Complexity: O(N * K * log K) (N: kelime sayısı, K: en uzun kelime uzunluğu. Sıralama işlemi K*logK sürer)
# Space Complexity: O(N * K) (Tüm kelimeleri gruplanmış halde sözlükte tuttuğumuz için)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sozluk = {}

        for s in strs:

            anahtar = "".join(sorted(s))

            if anahtar in sozluk:
                sozluk[anahtar].append(s)

            else:
                sozluk[anahtar] = [s]

        return list(sozluk.values())


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: strs = {strs1}")
    print(f"Output: {solution.groupAnagrams(strs1)}")

    print("-" * 20)

    # Test Senaryosu 2
    strs2 = [""]
    print(f"Input: strs = {strs2}")
    print(f"Output: {solution.groupAnagrams(strs2)}")

    print("-" * 20)

    # Test Senaryosu 3
    strs3 = ["a"]
    print(f"Input: strs = {strs3}")
    print(f"Output: {solution.groupAnagrams(strs3)}")