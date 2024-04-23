
nums = ["10", "20", "30"]


# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# print(nums)

nums2 = list(map(int, nums))
print(nums2)

abcd = ["a", "b", "c", "d"]
abcd2 = list(map(str.upper, abcd))
print(abcd2)

nums3 = ["a", "b", "c", "d"]
nums4 = list(map(str.isalnum, nums3))
print(nums4)

nums5 = ["a", "b", "c", "d"]
nums6 = list(map(str.isascii, nums5))
print(nums6)

nums7 = ["a", "B", "C", "d"]
nums8 = list(map(str.swapcase, nums7))
print(nums8)

