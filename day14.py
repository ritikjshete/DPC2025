def countSubstringsWithKDistinct(s: str, k: int) -> int:
    def atMostK(s, k):
        count = {}
        left = 0
        res = 0
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            
         
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            
            res += (right - left + 1)
        return res
    
    if k == 0: return 0
    return atMostK(s, k) - atMostK(s, k - 1)
