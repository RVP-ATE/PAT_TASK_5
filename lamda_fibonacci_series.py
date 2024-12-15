# Generate Fibonacci sequence using lambda and a loop
# Lambda function to calculate the next Fibonacci number
fibonacci = lambda a, b: a + b

# Function to generate Fibonacci series up to a given limit (50 in this case)
def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, fibonacci(a, b)
    return fib_sequence

# Generate Fibonacci series from 1 to 50
fibonacci_series = generate_fibonacci(50)

# Print the Fibonacci series
print(fibonacci_series)