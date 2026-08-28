class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for i in range(len(strs)):
            size = len(strs[i])
            string += str(size) + '#' + strs[i]
        return string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            curr =''
            while s[i] != '#':
                curr += s[i]
                i += 1
            if curr:
                size = int(curr)
                i += 1
                res.append(s[i: i+size])
                i += size
                curr = ''
        return res