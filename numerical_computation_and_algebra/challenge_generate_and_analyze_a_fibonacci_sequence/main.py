def generate_fibonacci(n):
  sequence= []
  a,b = 0,1
  for _ in range(n):
    sequence.append(a)
    a, b=b , a+b
  return (sequence)
fib_sequence = generate_fibonacci(10)   
sequence_sum = sum(fib_sequence)
sequence_average = sequence_sum/len(fib_sequence)

fib_sequence = generate_fibonacci(10)
sequence_sum = sum(fib_sequence)
sequence_average = sequence_sum / len(fib_sequence)

print("Fibonacci sequence (first 10 terms):", fib_sequence)
print("Sum:", sequence_sum)
print("Average:", sequence_average)