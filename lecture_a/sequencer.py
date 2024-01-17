
import argparse

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate prime sequence
def prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Function to generate square sequence
def square(n):
    return [i**2 for i in range(1, n+1)]

# Function to generate triangular sequence
def triangular(n):
    return [int(i*(i+1)/2) for i in range(1, n+1)]

# Function to generate factorial sequence
def factorial(n):
    if n == 0: return [1]  
    fact_seq = []
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        fact_seq.append(factorial)
    return fact_seq

# Main function to parse arguments and return the sequence
def main(args=None):
    parser = argparse.ArgumentParser(description='Generate mathematical sequences.')
    parser.add_argument('--length', type=int, help='Length of the sequence', required=True)
    parser.add_argument('--sequence', type=str, help='Type of sequence', required=True,
                        choices=['fibonacci', 'prime', 'square', 'triangular', 'factorial'])
    
    if args is None:
        args = parser.parse_args()
    else:
        if isinstance(args, list):
            args = parser.parse_args(args)
        elif not isinstance(args, argparse.Namespace):
            raise TypeError("Argument 'args' must be a list or Namespace")

    if args.sequence == 'fibonacci':
        return fibonacci(args.length)
    elif args.sequence == 'prime':
        return prime(args.length)
    elif args.sequence == 'square':
        return square(args.length)
    elif args.sequence == 'triangular':
        return triangular(args.length)
    elif args.sequence == 'factorial':
        return factorial(args.length)
    
if __name__ == "__main__":
    print(main())
