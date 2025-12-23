# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Zorluk: Easy

# Time Complexity: O(n)
# Space Complexity: O(1) (Alfabe 26 harf olduğu için sabit alan kullanır)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        else:
            sozluk = {}  # key : harf / value : sayı
            cevap = True

            for i in s:
                if i in sozluk:
                    sozluk[i] = sozluk[i] + 1
                else:
                    sozluk[i] = 1

            for j in t:
                if j not in sozluk:
                    cevap = False
                    break

                else:
                    sozluk[j] = sozluk[j] - 1

                if sozluk[j] < 0:
                    cevap = False
                    break

            return cevap


if __name__ == "__main__":
    solution = Solution()

    # Test Senaryosu 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = {s1}, t = {t1}")
    print(f"Output: {solution.isAnagram(s1, t1)}")

    print("-" * 20)

    # Test Senaryosu 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = {s2}, t = {t2}")
    print(f"Output: {solution.isAnagram(s2, t2)}")