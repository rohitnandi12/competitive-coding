# Write your code here
T = int(input())
# Manually compute which character falls under which range.
# I this question all type of characters are to be condensed in the range of prime between 'A' to 'Z' and 'a' to 'z'
UCs = [67]*5 + [71]*3 + [73]*4 + [79]*5 + [83]*5 + [89]*7
LCs = [97]*6 + [101]*3 + [103]*3 + [107]*3 + [109]*3 + [113]*11
while(T):
    T -= 1
    
    N = int(input())
    S = list(input())
    
    for i in range(N):
        c = S[i]
        if(c<'A'):
            S[i] = chr(67)
        elif('A'<=c and c<=chr(93)):
            S[i] = chr(UCs[ord(c)-65])
        elif(chr(94)<=c and c<='z'):
            S[i] = chr(LCs[ord(c)-94])
        elif('z'<c):
            S[i] = chr(113)
            
    print("".join(S))