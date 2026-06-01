class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wl = int(s[i:j])
            ws = j + 1
            wf = ws + wl
            res.append(s[ws:wf])
            i = wf
        return res
