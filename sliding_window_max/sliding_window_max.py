'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max = 0
    rMax = []
    for i in range(len(nums) - k + 1): 
        max = nums[i] 
        for j in range(1, k): 
            if nums[i + j] > max: 
                max = nums[i + j] 
        rMax.append(max)
    return rMax

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
