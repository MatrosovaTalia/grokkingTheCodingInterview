def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = dict()
        for c1 in s:
            if c1 in letters:  
                letters[c1] += 1
            else:
                letters[c1] = 1
                
        for c2 in t:
            if c2 not in letters:
                return False
            else:
                letters[c2] -= 1
                if letters[c2] == 0:
                    letters.pop(c2)
            
        if not bool(letters):
            return True
        else:
            return False

print(isAnagram("anagram", "nagaram"))
print(isAnagram("anagram", ""))