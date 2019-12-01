class Solution:
    def isSubsequence(self, s, t):
        #use a queue to hold the substrings order
        que = list(s)
        #check for empty substring
        if que == []:
            return True
        #iterate through the string and dequeue the queue everytime a character matches
        for character in t:
            if character == que[0]:
                que.pop(0)
            else:
                continue
            #an empty queue means the substring appears in the string in the correct order
            if que == []:
                return True
        return False