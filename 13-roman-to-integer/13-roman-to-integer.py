class Solution:
    def romanToInt(self, s: str) -> int:
        Sum = []
        s = list(s)
        s.append([''])
        for i in range(0, len(s)-1):
            #print(Sum)
            if s[i] == 'I' and s[i+1]=='V' or  s[i] == 'I'and s[i+1]=='X':
                Sum.append(-1)
            elif s[i]=="I":
                 Sum.append(1)
            if s[i] == 'X' and s[i+1]=='L' or s[i] == 'X' and s[i+1]=='C':
                Sum.append(-10)
            elif s[i] == 'X':
                 Sum.append(10)            
            if s[i] == 'C' and s[i+1]=='D' or s[i] == 'C' and s[i+1]=='M':
                Sum.append(-100)
            elif s[i] == 'C':
                 Sum.append(100)
            if s[i] == 'V':
                Sum.append(5)
            if s[i] == 'L':
                Sum.append(50)            
            if s[i] == 'D':
                Sum.append(500)            
            if s[i] == 'M':
                Sum.append(1000)
        return sum(Sum)