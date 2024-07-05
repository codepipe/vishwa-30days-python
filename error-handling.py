Error handling in Python is done using the try, except, else, and finally blocks. 
This allows you to manage exceptions (errors) gracefully and provide a mechanism to handle them without breaking the program.


try:
    # Code that might cause an exception
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    # This block will execute if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero.")
except ValueError:
    # This block will execute if a ValueError occurs
    print("Error: Invalid input. Please enter an integer.")
else:
    # This block will execute if no exceptions are raised
    print(f"The result is {result}")
finally:
    # This block will always execute
    print("Execution complete.")

# Example usage:
# Enter a numerator: 10
# Enter a denominator: 0
# Output:
# Error: You cannot divide by zero.
# Execution complete.


Explanation:
try block: Contains code that might raise an exception.
except block: Handles specific exceptions. In this example, ZeroDivisionError and ValueError are handled.
else block: Executes if no exceptions are raised in the try block.
finally block: Always executes, regardless of whether an exception was raised or not. This is typically used for cleanup actions.
You can have multiple except blocks to handle different types of exceptions. If you don't know the specific exceptions, you can use a generic except block to catch all exceptions, but it's generally better to handle specific exceptions when possible for clarity and better debugging.

