class Solution(object):
    def reverseVowels(self, s):

        #in case of empty string
        if not s:
            return ""
        else:
            s = list(s)

        vowels = set('aeiouAEIOU')

        p1 = 0
        p2 = len(s)-1
 

        while p1 < p2:

            if p1 < p2 and s[p1] not in vowels:
                p1 += 1
        

            if p1 < p2 and s[p2] not in vowels:
                p2 -= 1
        
            if p1 < p2 and s[p1] in vowels and s[p2] in vowels: 
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1

        return ''.join(s)


            
            
        