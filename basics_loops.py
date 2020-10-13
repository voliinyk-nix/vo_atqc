# use cycles "for",  "while",  "foreach"Cycle operators
# Create for, while, do while cycles that iterate 10 times and print iteration number to console.

for x in range(10):
    print(x)

x = 0
while x < 10:
    print(x)
    x = x + 1

# Create an infinite loop.
inf_loop = 0
while inf_loop < 1:
    print("One more row from infinite loop")
    break


# Create recursion with exit condition.
def print_row():
    print("Print the row")

print_row()
print("Exit")


# Create recursion without exit condition.
def no_exit():
    print("No exit condition")
    no_exit()

no_exit()
