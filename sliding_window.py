# sliding window technique

# sub arrays that add up to 9

num_list = list(range(1,10))
def up_to_nine(array):
    pass

print(num_list)

# easy: given array of ints, find maxisum sum subarray of size

eg_input = [-1,2,3,1,-3,2]

# for this example, size of sub array is 2
def max_sum_sub(array):
    max = 0
    for i in range(len(array)-1):
        test = array[i] + array[i+1]
        if test > max:
            max = test
    return max
            

print(max_sum_sub(eg_input))
