

def maxarray(arr,k):
    max_ = []
    cnt = 0
    init = 0 
       
    for el in range(len(arr)):
        cnt +=1
        if (cnt-init)==k:
            max_.append(max(arr[init:cnt]))
            init+=1
    return max_

print(maxarray([10,5,2,7,8,7],3))

        