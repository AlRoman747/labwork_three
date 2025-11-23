List = [2,0,2,1,1,0]
def bouble_sort(nums: List):
    sorted_flag = True
    while sorted_flag:
        sorted_flag = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted_flag = True
        if sorted_flag == False:
            break
    return nums



print(bouble_sort(List))