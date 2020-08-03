'''
Given an array of integers that are out of order, determine the bounds of the smallest window 
that must be sorted in order for the entire array to be sorted. 

For example, given [3, 7, 5, 6, 9], you should return (1, 3)

This result works because 1 and 3 are the indicies of numbers that we are switching 

'''
nums = [3, 7, 5, 6, 9]
window = []
for i in range(len(nums) - 1):
    
    next_val = nums[i + 1]
    val = nums[i]

    if val > next_val:
        # print('val index: {} of val: {}'.format(i, val))
        # print('next_val index: {} of next_Val {}'.format(i+1, next_val))
        
        window.append(i)
        window.append(i+1)

        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp
        
window_result = []

window_result.append(window[0])
window_result.append(window[len(window) - 1])

print(window_result)
print(nums)
    