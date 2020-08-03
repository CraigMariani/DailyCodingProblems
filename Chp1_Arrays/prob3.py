'''
Given an array of numbers, find the maximum sum of any contigous(sharing an edge or boundary)
subarray of the array

For example:
If array is

[34, -50, 42, 14, -5, 86], Then the max sum is -> 42 + 14 + (-5) + 86 = 137
[-5,-1, -8, -9], Then the max sum is -> 0 since we take none of these

Do it in O(n) time
'''


def find_contigous(nums):
    max_sum = 0
    new_sum = 0
    result = []

    for i in range(len(nums) - 1):
        num = nums[i]
        next_num = nums[i + 1]
        new_sum = num + next_num + new_sum

        if new_sum > max_sum:
            result.append(num)
            result.append(next_num)
            max_sum = new_sum

    if not result:
        result.append(0)

    result = list(set(result))
    result = result[::-1]
    return result


if __name__ == '__main__':
    nums = [34, -50, 42, 14, -5, 86]
    # nums = [-5, -1, -8 ,-9]
    result = find_contigous(nums)
    print(result)