def is_palindrome(lst):
  i = 0
  j = len(lst) - 1
  while i < j:
      if lst[i] != lst[j]:
          return False
      i += 1
      j -= 1
  return True

# Read 10 numbers from the user
numbers = []
print("Enter the 10 numbers:")
for _ in range(10):
  number = int(input())
  numbers.append(number)

# Print the list of numbers
print("The numbers you entered are:", numbers)

# Check if the list is a palindrome
if is_palindrome(numbers):
  print("is a palindrome")
else:
  print("is not a palindrome")