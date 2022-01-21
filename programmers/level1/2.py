# 행렬의 덧셈

import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = arr1 + arr2
    answer = answer.tolist()
    return answer