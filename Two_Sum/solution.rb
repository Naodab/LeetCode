def two_sum(nums, target)
  num_indices = {}
  
  nums.each_with_index do |num, index|
    complement = target - num
    if num_indices.key?(complement)
      return [num_indices[complement], index]
    end
    num_indices[num] = index
  end
  
  []
end

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
puts result.inspect  # Output: [0, 1]