def concatArray(nums):
    n = len(nums)
    ans = nums + nums
    return ans

# Get input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
# Split the user input into a list of integers
nums = [int(x) for x in user_input.split()]

result = concatArray(nums)
print("Concatenated Array:", result)
