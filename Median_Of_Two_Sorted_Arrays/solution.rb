# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    len1 = nums1.length
    len2 = nums2.length

    x = 0
    y = 0
    merged = []

    until x == len1 || y == len2
        if nums1[x] < nums2[y]
            merged << nums1[x]
            x += 1
        else
            merged << nums2[y]
            y += 1
        end
    end

    merged.concat(nums1[x..-1]) if x < len1
    merged.concat(nums2[y..-1]) if y < len2

    mid = merged.length / 2
    if merged.length.odd?
        return merged[mid]
    else
        return (merged[mid - 1] + merged[mid]) / 2.0
    end
end

# Example usage:
puts find_median_sorted_arrays([1, 3], [2])          # Output: 2.0
puts find_median_sorted_arrays([1, 2], [3, 4])       # Output: 2.5
puts find_median_sorted_arrays([0, 0], [0, 0])       # Output: 0.0