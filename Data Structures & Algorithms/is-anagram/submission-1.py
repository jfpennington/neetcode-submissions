class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        characters = list(s) # split up the string into a list of its characters
        characters2 = list(t)

        characters.sort()
        characters2.sort()

        return (characters == characters2)

