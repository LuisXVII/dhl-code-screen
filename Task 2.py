# Intersection of two arrays:
# Given two arrays, write a function to compute their intersection

# Input:
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output: [2]

# Input:
# nums1 = [4,9,5]
# Nums2 = [9,4,9,8,4]
# Output: [9,4]


def main(nums1, nums2):
    # make a set with the first array
    visitedNums = set(nums1)

    # make a set with the intersection to store the result
    intersection = set()

    # iterate through the second array
    for num in nums2:
        # check if the number is in the visited set
        if num in visitedNums:
            # if it is, add it to the intersection set
            intersection.add(num)

    print(intersection)


if __name__ == "__main__":

    numsA = [1,2,2,1]
    numsB = [2,2]

    numsC = [4,9,5]
    numsD = [9,4,9,8,4]

    main(numsA, numsB)
    main(numsC, numsD)
