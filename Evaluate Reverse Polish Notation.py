# Problem: Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Zorluk: Medium

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 + s2)
            elif token == "-":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 - s2)
            elif token == "*":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1 * s2)
            elif token == "/":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(s1 / s2))
            else:

                stack.append(int(token))

        return stack[0]

if __name__ == "__main__":
    solution = Solution()

    tokens1 = ["2", "1", "+", "3", "*"]
    print(f"Input: {tokens1}")
    print(f"Output: {solution.evalRPN(tokens1)}")

    print("-" * 20)

    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"Input: {tokens2}")
    print(f"Output: {solution.evalRPN(tokens2)}")

    print("-" * 20)

    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"Input: {tokens3}")
    print(f"Output: {solution.evalRPN(tokens3)}")