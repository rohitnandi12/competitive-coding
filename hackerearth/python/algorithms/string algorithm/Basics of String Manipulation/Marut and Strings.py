
# Write your code here
# try catch for exceptions when T is not Integer
try:
    T = int(input())
    if(T<1 or T>10): # constraint 1
        print("Invalid Test")
    else:
        while(T):
            T -= 1
            S = input()
            if(len(S) <1 or len(S)>100): # contraint for string length
                print('Invalid Input')
                continue
            count_L = 0
            count_U = 0
            for c in S:  # count the lower and Upper case english characters
                if('a'<=c and c<='z'):
                    count_L += 1
                elif('A'<=c and c<='Z'):
                    count_U += 1
            if(count_L == 0 and count_U == 0): # If no English characters
                print("Invalid Input")
            else:
                print(min(count_L,count_U)) # smaller count = less conversion
except:
    print('Invalid Test')