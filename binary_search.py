def binary_search(list, item):
     # low and high keep track of which part of the list you'll search in.
    low=0
    high=len(list)-1
    while low<=high:
        # ... check the middle element
        mid=(low+high)//2
        guess=list[mid]
         # Found the item.
        if guess == item:
          return mid
        # The guess was too high.
        if guess > item:
          high = mid - 1
        # The guess was too low.
        else:
          low = mid + 1

    # Item doesn't exist
    return None

my_list=[1,3,5,7,9]


# print(binary_search(my_list,3))
print(binary_search(my_list, 3))#=>1

# # 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list,-1))# => None



# *********Binary Search Explained********
# //Binary search is a fast algorithm for searching in a sorted array of keys S. To search
# for key q, we compare q to the middle key S[n/2]. If q appears before S[n/2], it
# must reside in the top half of S; if not, it must reside in the bottom half of S. By
# repeating this process recursively on the correct half, we locate the key in a total
# of log n comparisons//
# ************TESTING***********
# S=[1,3,7,9,10]
# low=0
# new low=3
# high=len(list)=5-1=4
# mid=4+0//2=2
# newmid=4+3//3=3
# guess=list[mid]=list[2]=7
# guess2=list[newmid] =list[3]==9
# if 7==9...return 2
# elif 7>9...high=mid-1  =2-1  =1
# else 7<9....low=mid+1  =2+1  =3


# ******************End*******************