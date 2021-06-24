# Medium - dynamically sized sliding window - given an array of positive integers, find the subarrays of integers that add up to a given number

def get_sub_arrays(input, desired):
    
    solutions = []
    le_sum = 0
    sum_start_index = 0

    for item in range(len(input)):
        le_sum += input[item]

        while le_sum > desired:
            le_sum -= input[sum_start_index]
            sum_start_index += 1
        
        if le_sum == desired:
            solutions.append(input[sum_start_index: item + 1])
            
    return solutions
            
exampleInput1 = [1, 7, 9, 4, 3, 2, 2]
desiredSum1 = 7
print(get_sub_arrays(exampleInput1, desiredSum1))