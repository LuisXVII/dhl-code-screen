# Need to find the first element in the array that is occurring or repeating k times the array.

# Input: [5,2,2,12,12,1] k=2
# Output: 2

def main(nums, k):
    numberCount = {}
    # Count the entire array in case there is a number that is repeating more than k times
    for num in nums:
        if num in numberCount:
            numberCount[num] += 1
        else:
            numberCount[num] = 1

    for num in numberCount:
        if numberCount[num] == k:
            print(num)
            return

    print("No number found")


if __name__ == "__main__":
    nums = [5,2,2,2,12,12,1]
    k = 2
    # output = 12
    main(nums, k)
