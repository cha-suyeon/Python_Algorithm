# 1
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        arr.remove(min(arr))
        arr.insert(0,-1)
        return arr
        
print(solution([4,3,2,1]))
print(solution([10]))

# 2
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))

# 3
def rm_small(mylist):
    mylist.pop(mylist.index(min(mylist)))
    return mylist

my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))