def goodPairs(nums):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                count+=1
    return count
num1=input()
# num = list(map(int, input().strip().split()))[:num1]
nums=[int(x) for x in num1.split()]
result=goodPairs(nums)
print(result)


# n = int(input("Enter number of elements : "))
 
# # # Below line read inputs from user using map() function
# a = list(map(int,
#     input("\nEnter the numbers : ").strip().split()))[:n]




# Initialize an empty list to store the numbers
# nums = []

# Ask the user to enter numbers one by one
# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     num = int(input(f"Enter element {i + 1}: "))
#     nums.append(num)

# Now, 'nums' contains the list of integers entered by the user
# print("nums =", nums)
# result=goodPairs(nums)
# print(result)