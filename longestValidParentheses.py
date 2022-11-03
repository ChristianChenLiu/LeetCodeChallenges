class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        parentheses_stack = [-1]
        
        for i, parentheses in enumerate(s):
            if parentheses == '(':
                parentheses_stack.append(i)
            else:
                start_idx = parentheses_stack.pop()
                if len(parentheses_stack) <= 0:
                    parentheses_stack.append(i)
                else: 
                    max_length = max(max_length, i - parentheses_stack[-1])
        
        return max_length