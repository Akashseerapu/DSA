class Solution:
    def longestRepeating(self, s: str, qc: str, qi: list[int]) -> list[int]:
        n = len(s)
        
        # Segment tree parallel arrays
        mx = [0] * (4 * n)
        pl = [0] * (4 * n)
        sl = [0] * (4 * n)
        pc = [''] * (4 * n)
        sc = [''] * (4 * n)
        
        def up(i, l, r):
            m = (l + r) >> 1
            L, R = i << 1, (i << 1) | 1
            sz_L = m - l + 1
            sz_R = r - m
            
            pc[i] = pc[L]
            sc[i] = sc[R]
            
            pl[i] = pl[L]
            if pl[L] == sz_L and pc[L] == pc[R]:
                pl[i] += pl[R]
                
            sl[i] = sl[R]
            if sl[R] == sz_R and sc[R] == sc[L]:
                sl[i] += sl[L]
                
            mx[i] = max(mx[L], mx[R])
            if sc[L] == pc[R]:
                mx[i] = max(mx[i], sl[L] + pl[R])
        
        def build(i, l, r):
            if l == r:
                mx[i] = pl[i] = sl[i] = 1
                pc[i] = sc[i] = s[l]
                return
            m = (l + r) >> 1
            L, R = i << 1, (i << 1) | 1
            build(L, l, m)
            build(R, m + 1, r)
            up(i, l, r)
            
        def modify(i, l, r, idx, c):
            if l == r:
                pc[i] = sc[i] = c
                return
            m = (l + r) >> 1
            L, R = i << 1, (i << 1) | 1
            if idx <= m:
                modify(L, l, m, idx, c)
            else:
                modify(R, m + 1, r, idx, c)
            up(i, l, r)

        build(1, 0, n - 1)
        
        ans = []
        for c, idx in zip(qc, qi):
            modify(1, 0, n - 1, idx, c)
            ans.append(mx[1])
            
        return ans