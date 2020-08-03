'''
Find the number of smaller elements to the right
Array is [3, 4, 9, 6, 1] >> returns [1, 1, 2, 1, 0]

'''



nums = [3, 4, 9, 6, 1]

smaller_elements = []
for index, num in enumerate(nums):
    smaller_counter = 0
    subset = nums[index:]
    for new_num in subset:
        if new_num < num:
            smaller_counter += 1

    
    smaller_elements.append(smaller_counter)

print(smaller_elements)
