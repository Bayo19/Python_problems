# Medium - dynamically sized sliding window - given an array of positive integers, find the subarrays of integers that add up to a given number

def get_sub_arrays(input, desired):
    
    solutions = []
    le_sum = 0
    sum_start_index = 0

    for current_item in range(len(input)):
        le_sum += input[current_item]

        while le_sum > desired:
            le_sum -= input[sum_start_index]
            sum_start_index += 1
        
        if le_sum == desired:
            solutions.append(input[sum_start_index: current_item + 1])
            
    return solutions


# -------------- TEST CASES -----------------

# test case 1            
exampleInput1 = [1, 7, 9, 4, 3, 2, 2]
desiredSum1 = 7
print(get_sub_arrays(exampleInput1, desiredSum1))

# test case 2 

exampleInput2 = [23, 1, 6, 9, 15, 8]
desiredSum2 = 24
print(get_sub_arrays(exampleInput2, desiredSum2))

# test case 3
# sliding window technique cannot handle negative numbers in this case so solution will not be full

# Kadan's algorithm is optimal for this question when it includes all integers, positive, negative and 0

# Sliding window is not recommended

exampleInput3 = [-1, -4, 0, 5, 3, 2 , 1]
desiredSum3 = 5

print(get_sub_arrays(exampleInput3, desiredSum3))