"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def max_area(height: list[int]) -> int:
    l, r = 0, len(height)-1
    area = 0
    
    while l < r:
        c_area = (r - l)
        
        if height[r] > height[l]:
            c_area *= height[l]
            l += 1
        else:
            c_area *= height[r]
            r -= 1
        area = max(area, c_area)
    return area

# 49
value = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(value))

# 1
value = [1, 1]
print(max_area(value))

# 2
value = [1, 2, 1]
print(max_area(value))

# 4
value = [1, 2, 4, 3]
print(max_area(value))

# 17
value = [2, 3, 4, 5, 18, 17, 6]
print(max_area(value))