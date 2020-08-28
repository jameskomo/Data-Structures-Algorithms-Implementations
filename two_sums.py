from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    '''
    Return indices of two numbers in list that add up to a specific target
    '''
    dict={}
    for i, num in enumerate(nums):
        second_number=target-num
        if second_number in dict:
            return (dict[second_number],i)
        else:
            dict[num]=i

print(twoSum(nums=[3, 6,2,9], target=8))


