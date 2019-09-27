class Solution:
    def lengthOfLastWord(self, s):
        s = s.split(" ")
        for item in s[::-1]:
            if item is "":
                continue
            else:
                break
        return len(item)

Obj = Solution()
print(Obj.lengthOfLastWord("Ah ha ha aaa "))