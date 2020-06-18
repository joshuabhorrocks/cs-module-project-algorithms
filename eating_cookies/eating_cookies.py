'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    CL = [0 for i in range(0, n + 1)] 
    CL[0] = CL[1] = 1
    CL[2] = 2
    CL[3] = 3
  
    for i in range(3, n + 1): 
        CL[i] = CL[i - 1] + CL[i - 2] + CL[i - 3] 
    return CL[n] 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

# 1+1+1+1+1
# 1+1+1+2
# 1+1+2+1
# 1+2+1+1
# 2+1+1+1
# 2+2+1
# 2+1+2
# 1+2+2
# 3+1+1
# 1+3+1
# 1+1+3
# 2+3
# 3+2

# 13 ways
