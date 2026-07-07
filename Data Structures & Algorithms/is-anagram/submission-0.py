class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        characters = list(s) # split up the string into a list of its characters
        characters2 = list(t)

        characters.sort()
        characters2.sort()

        if (len(s) != len(t)):
            return False
           
        for i in range(len(s)):
            if (characters[i] != characters2[i]):
                return False
        
        return True

