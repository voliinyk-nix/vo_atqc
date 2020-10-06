print("_____________ Basic variable types. Casting  Create 5 variables with type int,long,float,double,String_________")
var_integer = int
print(var_integer)    #<class 'int'>

var_complex = complex
print(var_complex)    #<class 'complex'>

var_float = float
print(var_float)      #<class 'float'>

var_string = str
print(var_string)     #<class 'str'>

print("___________________________Assign different values to these variables and compare them__________________________")

var_integer, var_complex, var_float, var_string = 13, 13j, 13.13, "thirteen"

# var_integer_from_complex = int(var_complex)
# print(var_integer_from_complex)  # TypeError: can't convert complex to int

var_complex_from_integer = complex(var_integer)
print(var_complex_from_integer)

var_integer_from_float = int(var_float)
print(var_integer_from_float)

var_float_from_integer  = float(var_integer)
print(var_float_from_integer)

# var_integer_from_string = int(var_string)      # ValueError: invalid literal for int() with base 10: 'thirteen'
# print(var_integer_from_string)

var_string_from_integer = str(var_integer)
print(type(var_string_from_integer))        # <class 'str'>

var_string_from_complex = str(var_complex)
print(var_string_from_complex)

print("________________________Don't assign any values and compare variables_____________________________")

var_integer, var_complex, var_float, var_string = int, complex, float, str

# var_integer_from_complex = int(var_complex)     # TypeError: int() argument must be a string, a bytes-like object or a number, not 'type'
# print(var_integer_from_complex)

# var_complex_from_integer = complex(var_integer)   # TypeError: complex() first argument must be a string or a number, not 'type'
# print(var_complex_from_integer)

# var_integer_from_float = int(var_float)     # TypeError: int() argument must be a string, a bytes-like object or a number, not 'type'
# print(var_integer_from_float)

print("________________# ??? Assign the same values and compare variable__________________")

("__________Assign in same order [0.5,0.7,1.0,0.1] values to float and double variables and compare them.__________________________________________________")

var_1, var_2, var_3, var_4 = float(0.5), float(0.7), float(1.0), float(0.1)

print(min(var_1, var_2, var_3, var_4))
print(max(var_1, var_2, var_3, var_4))

print("_______________Divide numeric values by zero_____________________________")
# var_divided_0 = 1 / 0:  # ZeroDivisionError: division by zero
# print(var_divided_0)

print("_________ Divide values by 3 and assign result to variable___________________")
var_divided_3 = var_1 / 3
print(var_divided_3)

print("_________Divide values by 3.0 and assign result and make round operatioN.Explain all results_______________")

var_divided_3_0 = var_1 / 3.0
print(var_divided_3_0)
print(round(var_divided_3_0))