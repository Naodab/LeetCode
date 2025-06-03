class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

def list_to_number(node)
  number = 0
  multiplier = 1

  while node
    number += node.val * multiplier
    multiplier *= 10
    node = node.next
  end
  
  number
end

def add_two_numbers(l1, l2)
    num1 = list_to_number(l1)
    num2 = list_to_number(l2)

    sum = num1 + num2
    dummy_head = ListNode.new(0)
    current = dummy_head
    sum_digits = sum.to_s.chars.reverse.map(&:to_i)

    sum_digits.each do |digit|
      current.next = ListNode.new(digit)
      current = current.next
    end
    dummy_head.next
end

# Example usage:
l1 = ListNode.new(2, ListNode.new(4, ListNode.new(3)))
l2 = ListNode.new(5, ListNode.new(6, ListNode.new(4)))
result = add_two_numbers(l1, l2)
while result
  puts result.val
  result = result.next
end
# Output should be: 7 -> 0 -> 8 (which represents the number 807)