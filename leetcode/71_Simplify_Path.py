from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: List[str] = []
        for subpath in path.split('/'):
            if subpath in ['', '.']:
                continue
            if subpath == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(subpath)
        return '/' + '/'.join(stack)
