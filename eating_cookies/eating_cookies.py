'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    CL = [0 for i in range(0, n + 1)] 
    CL[0] = CL[1] = CL[2] = 1
    CL[3] = 2
  
    for i in range(3, n + 1): 
        CL[i] = CL[i - 1] + CL[i - 2] + CL[i - 3] 
    return CL[n] 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
