"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

def find_median_sorted_arrays(nums1, nums2) -> float:
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
        
    first_num = nums1[n//2 - (1 if n%2 == 0 else 0)] 
    second_num = nums1[n//2]
        
    return (first_num + second_num)/2
    

# 2.00000
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))

# 2.50000
nums1 = [1,]
nums2 = [2, 3, 4]
print(find_median_sorted_arrays(nums1, nums2))

# 4.5
nums1 = [1, 2, 3]
nums2 = [4, 5, 6, 7, 8]
print(find_median_sorted_arrays(nums1, nums2))

# 2.5
nums1 = [4,]
nums2 = [1, 2, 3]
print(find_median_sorted_arrays(nums1, nums2))

# 3.5
nums1 = [1,]
nums2 = [2, 3, 4, 5, 6]
print(find_median_sorted_arrays(nums1, nums2))