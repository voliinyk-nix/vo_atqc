# use conditions "if" and  "case"

# Create 4 boolean variables(true,true,false,false) and compare them between themselves - result print in console.

boolean_true_1 = True
boolean_true_2 = True
boolean_false_1 = False
boolean_false_2 = False

print(boolean_true_1 == boolean_true_2)
print(boolean_true_1 == boolean_false_1)
print(boolean_true_1 == boolean_false_2)

print(boolean_false_1 == boolean_false_2)
print(boolean_false_1 == boolean_true_1)
print(boolean_false_1 == boolean_true_2)

# Create 4 different numeric variables and compare them with the usage of <, <=, !=, ==, ===, >=, >. Explain result

number_1, number_2, number_3, number_4 = 1, 10, 100, 1000

if (number_1 < number_2):
    print("1 is less than 10")

if (number_2 <= number_3):
    print("10 is less than 100")

if (number_3 != number_4):
    print("100 is not equal to 1000")

if (number_1 == number_2):
    print("1 is less than 10")
else:
    print("1 !=10")

# if (number_1 === number_2):   SyntaxError: invalid syntax
  #  (print("10 === 1")


comparison_result = number_1 <= number_2 < number_3 <= number_4
print(comparison_result)

if (number_1 > number_2):
    print("1 > 10")
else:
    print("1 < 10")

if (number_2 >= number_3):
    print("10 > 100")
else:
    print("10 < 100")


# Create 2 different strings. Compare them with usage  if ??? trinar operator and print "Not equal", "Equal" and explain
var_string_1 = "one simple string"
var_string_2 = "Another one simple string!"

if (var_string_1 == var_string_2):
    print("Equal")
else:
    print("Not equal")

# Explain difference betweeb &,|,&&,|| and provide example.