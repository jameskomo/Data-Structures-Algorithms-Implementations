from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    Return indices of two numbers in list that add up to a specific target
    '''
    numbers_visited=set()
    for first_number in nums:
        second_number = target - first_number
        if second_number in numbers_visited:
            return True
        numbers_visited.add(first_number)

print(twoSum(nums=[3, 6,2,9], target=11))