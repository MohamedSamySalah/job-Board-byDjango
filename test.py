
def solution(s):
    l = []
    string = '' 
    if len(s) %2 == 0:
        for letter in s:
            string+= letter #a
            if len(string) == 2:
                l.append(string)
                string = ''
        return l
    else:
        for letter in range(0,len(s)): 
            string+= s[letter]
            if len(string) == 2:
                l.append(string)
                string = ''
            if letter == len(s) - 1:
                l.append(s[letter]+'_')
        return l

print(solution('abc'))

# s = ''
# print(len(s))