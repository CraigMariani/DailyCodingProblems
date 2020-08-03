'''
Given an array of integers, return a new array such that each element at index i of the new array is 
the product of all numbers in the origingal array except the one at i.

'''

nums = [1, 2, 3, 4, 5]
result = []


# Solution 1: 
# Has a nested for loop that compares each number in the second for loop with the single number in the first one
# When ever the number from the first for loop matches with the second, the number will be skipped
# this does not work well with duplicates, maybe use and index instead?

for i, num1 in enumerate(nums):
    # print('Index: {}'.format(i), end=' ')
    # print('Number: {}'.format(num))
    
    product = 1

    for num2 in nums:

        if num2 != num1:
            product *= num2
    
    result.append(product)

print('Solution 1')
print(result)

result = []

# solution 1 with index
for i, num1 in enumerate(nums):

    product = 1

    for j, num2 in enumerate(nums):

        if i != j:
            product *= num2
    
    result.append(product)

print('Solution1 with index')
print(result)

result = []


# Try recreating this with the books solution at 7/23
