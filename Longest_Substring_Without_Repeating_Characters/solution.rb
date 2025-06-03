def length_of_longest_substring(s)
  max_length = 0
  substr = []
  s.each_char do |c|
    if substr.include?(c)
      deleted_char = substr.shift until deleted_char == c
    end

    substr << c
    max_length = [max_length, substr.size].max
  end

  max_length
end

# Example usage:
puts length_of_longest_substring("abcabcbb") # Output: 3
puts length_of_longest_substring("bbbbb")    # Output: 1
puts length_of_longest_substring("pwwkew")   # Output: 3
puts length_of_longest_substring("")          # Output: 0
puts length_of_longest_substring("a")         # Output: 1
puts length_of_longest_substring("dvdf")      # Output: 3
puts length_of_longest_substring("anviaj")    # Output: 5
puts length_of_longest_substring("tmmzuxt")   # Output: 5