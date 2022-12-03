a = [8 , 3, 5, 2 , 4 , 9, 7, 11]
dp = {}

for i in range(len(a) - 1, -1 , -1):
    print(f"i : {i}")
    choices = [1,]
    for j in range(i + 1, len(a)):
        print(f"j : {j}")
        if a[i] < a[j]:
            choices.append(dp[j] + 1)
            print(f"dp in if: {dp}")
            dp[i] = max(choices)
    dp[i] = max(choices)
            
        
    print(f"dp : {dp}")


print(dp)
