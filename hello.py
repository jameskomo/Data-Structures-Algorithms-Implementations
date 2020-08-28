# ENUMERATE FUNCTION PYTHON-Keep counter of items

# my_list = ['apple', 'banana', 'grapes', 'pear']
# for (index, item )in enumerate(my_list, 1):
#     print(index, item)
# counter_list = list(enumerate(my_list, 1))
# print(counter_list)
# lst2=counter_list.append('Bys')

# # Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]

# *******************************************************************************************************************************

# # LIST COMPREHENSIONS AND GENERATORS-list=[], generators=()
# my_list=[3,9,7,6,6,8,9,2,5,4,3,8,4,2,5,6]
# squared_comprehension=[n*n for n in my_list if n % 2==0]
# squared_generator=(n*n for n in my_list if n % 2==0)
# print(squared_comprehension)
# print(squared_generator)
# print(next(squared_generator))
# next(squared_generator)

# *******************************************************************************************************************************
# *ARGS AND ** KWARGS IN PYTHON

# 1. KWARGS
# def candidate(**info):
#     for key, value in info.items():
#         print("{} is {}". format(key, value))

# *******************************************************************************************************************************

# 2. ARGS
# def summation(*num):
#     sum = 0
    
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# summation(3,5)
# summation(4,5,6,7)
# summation(1,2,3,5,6)

# *******************************************************************************************************************************
# DEBUGGING USING PDB/ FINDING MAX NUMBER.
# def find_max(list):
#     max_num=-float('inf')
#     for num in list:
#         breakpoint() Python3.7 and above
#         import pdb; pdb.set_trace()
#         if num>max_num:
#             max_num=num
#     return max_num

# print(find_max([10, 9, 45, 73,22,12,16]))

# F-STRINGS-->FORMATTED STRINGS
# def candidate(**info):
#     for key, value in info.items():
#         print(f"{key} is {value}")

# candidate(Name="James Komo", Age=20)
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')