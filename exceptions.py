# Use "tr- catch"  to process the exceptions.
# Check Exception Hierarchy.  Create a numeric variable. Divide it by zero.
# Handle exception and print in console exception message;

try:
   numeric_var = 1 / 0
except Exception:
   print("Error: Unable to divide by zero")
else:
   print(num_var)
