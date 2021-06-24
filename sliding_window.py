# sliding window technique

# easy: given array of ints, find maxisum sum subarray of size

eg_input = [-1,2,3,1,-3,2]

def max_sum_sub(array, subarraysize):
    
    max = 0
    for i in range(len(array) - (subarraysize -1)):
        
        test = sum(array[i: i+subarraysize])
        if test > max:
            max = test
    return max


print(max_sum_sub(eg_input, 2), 'easy')


        
