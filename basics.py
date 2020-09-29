# https://github.com/voliinyk-nix/vo_atqc

# Don't assign any values and compare variables. . ·
# Assign the same values and compare variables. //Assign in same order [0.5,0.7,1.0,0.1] values to float and double variables and compare them.
# Divide numeric values by zero.
# Divide values by 3 and assign result to variable.
# Divide values by 3.0 and assign result and make round operatio.Explain all results

# Basic variable types. Casting  Create 5 variables with type int,long,float,double,String;
# Assign different values to these variables and compare them.
var_integer, var_complex, var_float, var_double, var_string = 13, 13j, 13.0, 13.13, "thirteen"
if var_integer == var_complex:
    print("Integer is equal to complex")
else:
    print("Integer is not equal to complex")

#print(var_integer, var_complex, var_float, var_double, var_string)


