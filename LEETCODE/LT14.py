# def longestCommonPrefix(strs):
#     res = ""
    
#     for i in range(0, len(strs[0])):
#         count = 0
#         for s in strs:
#             if(len(s) == i):
#                 return res
#             elif(s[i] == strs[0][i]):
#                 count= count+1
#         if(count == len(strs)):
#             res = res + strs[0][i]
#     return res    


def longestCommonPrefix(strs) -> str:
        res = ""
        for i in range(0, len(strs[0])):
            count = 0
            for j in range(0, len(strs)):
                if(len(strs[j]) == i):
                    return res
                elif(strs[j][i] == strs[0][i]):
                    count= count+1
            if(count == len(strs)):
                res = res + strs[0][i]
            else:
                break
        return res     

print(longestCommonPrefix(['flower','flow','flight']))

s= "   fly me   to   the moon  "
empty = " "
def lengthOfLastWord(s: str) -> int:
    return [x for x in s.split(" ") if len(x)>0][-1]
    init = -1
    end = -1
    br = False
    for i in range(0,len(s)):
        if(s[i] == empty and init>-1 and end>-1):
            br = True
        if(s[i]!=empty and init==-1):
            init = i
            end = i
        elif(s[i]!=empty and init!=-1 and not br):
            end = end +1
        elif(s[i]!=empty and init>=-1 and end>-1 and br):
            init = i 
            end = i
            br = False
    
    return len(s[init:end+1])
print(lengthOfLastWord(s))
