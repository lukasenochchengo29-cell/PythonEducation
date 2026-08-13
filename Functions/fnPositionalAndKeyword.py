def my_function(first, second, /, *, third, fourth):
  return first + second + third + fourth

result = my_function(5, 10, third = 15, fourth = 20)
print(result)
