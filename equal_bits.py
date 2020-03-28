"""
Your input will be an integer. Your output should be the next higher number with the same number of 1 bits in the binary representation.

Input Format: Integer

Constraints: Numbers will be positive

Output Format: Integer

Sample Input: 12
Sample Output: 17
Explanation: Both have  1 bits, and no other number between them does.
"""

def reverse_binary_list():
    """
    Calculate the first 1,000 binary numbers. 
    Store in list in descending order.

    return:
        list: Array of integers of firs 1,000 binary
    """
    # Start with 1 and 2 in list (can't generate)
    binary_list = [1 , 2]
    
    # Start from binary number 2 (when pattern starts)
    i = 1
    # Get the first 1,000 numbers
    while i < 1000:
        next = binary_list[i] * 2
        binary_list.append(next)
        i += 1

    # Reverse the list so in desc order, to compare with correctly
    binary_list.reverse()
    return binary_list

def num_of_ones(n, binary_list):
    """
    Calculate the number of ones used to represent number in binary.

    param:
        n(int)                  Integer to convert to binary
        binary_list(int arr)    List of first 1,000 binary numbers in desc

    return:
        int: Number of ones used in binary representation of n
    """
    # Start with no 1's
    num_ones = 0    
    while n > 0:    
        for num in binary_list:
            # Start with the largest binary number
            # 1 occurs when num is equal to n or n can be subtracted positively         
            if (num - n) <= 0:
                # Add 1 to tally and subtract binary num
                num_ones += 1
                n = n - num
                # Continue with new n
    return num_ones

def bits(n):
    """
    Get the next integer with the same number of ones used in binary 
    representation as the input.

    param:
        n(int): starting integer

    return:
        int: next integer with same number of ones
    """

    # Create a list of the first 1,000 binary numbers
    binary_list = reverse_binary_list()

    # Start by calculating number of 1's for n
    n_ones = num_of_ones(n, binary_list)

    # Calculate number of 1's for next value
    next_ones = 0
    while n_ones != next_ones:
        n = n + 1
        next_ones = num_of_ones(n, binary_list)

    return(n)

# Sample output 12 -> Should output 17
output = bits(12)
print(output)            