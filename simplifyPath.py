class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == '..' and len(stack) > 0:
                stack.pop()
            if p == '' or p == '.' or p =='..':
                continue
            else:
                stack.append(p)
        return '/' + '/'.join(stack)