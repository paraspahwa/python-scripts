# Accept command line arguments using argparse

import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Add command line arguments
parser.add_argument('num1', type=int, help='First number')
parser.add_argument('num2', type=int, help='Second number')
parser.add_argument('--operation', choices=['add', 'subtract'], default='add', help='Operation to perform')

# Parse the command line arguments
args = parser.parse_args()

# Perform the specified operation
if args.operation == 'add':
    result = args.num1 + args.num2
else:
    result = args.num1 - args.num2

print(f"Result: {result}")
