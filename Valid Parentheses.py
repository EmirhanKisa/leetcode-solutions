# Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Zorluk: Easy

# Time Complexity: O(n) - Listenin üzerinden bir kez geçilir.
# Space Complexity: O(n) - En kötü durumda tüm parantezler stack'e eklenir.

class Solution:
    def isValid(self, s: str) -> bool:
        sozluk = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in sozluk:
                if stack and stack[-1] == sozluk[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    s1 = "()"
    print(f"Input: s = '{s1}'")
    print(f"Output: {solution.isValid(s1)}")

    print("-" * 20)

    s2 = "()[]{}"
    print(f"Input: s = '{s2}'")
    print(f"Output: {solution.isValid(s2)}")

    print("-" * 20)

    s3 = "(]"
    print(f"Input: s = '{s3}'")
    print(f"Output: {solution.isValid(s3)}")

    print("-" * 20)

    s4 = "([)]"
    print(f"Input: s = '{s4}'")
    print(f"Output: {solution.isValid(s4)}")