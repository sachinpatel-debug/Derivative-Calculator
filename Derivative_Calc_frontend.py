from Derivative_Calc_backend import find_final_derivative_answer as derivative
import os




trig_functions = ['cos(x)', 'sin(x)', 'tan(x)', 'sec(x)', 'csc(x)', 'cot(x)']
inverse_trig_functions = ['arccos(x)', 'arcsin(x)', 'arctan(x)', 'arcsec(x)', 'arccsc(x)', 'arccot(x)']


# print statements containing direction
print()
print("Hello. Welcome to Keaton and Sachin's Derivative Calculator\u2122. There are rules and regulations you must follow")
print(f'before we can provide you with your desired derivative:') # type: ignore
print(f'{'-'*145}')


print(f'Rule 1: You must use the variable x (case sensitive), you cannot use any other variables.')
print(f'{'-'*145}')


print(f"Rule 2: If you want to nest one function inside the other you must put the inner function in parentheses in place of the outer function's x.\n{' ' * 8}This would be in the form 'f(g(x))'. For example: to nest e^x within cos(x) simply write cos(e^x).")
print(f'{'-'*145}')


print(f'Rule 3: Do not use the asterisk symbol (*) to multiply a function by a constant. For example 5*cos(x) is illegal. You must write it\n{' ' * 8}in the form "cf(x)" where c is the constant to be multiplied and f(x) is the function, if you wanted to execute the previous example,\n{' ' * 8}you would write 5cos(x).')
print(f'{'-'*145}')


print(f'Rule 4: To multiply two functions together, you must use the asterisk between the two functions. \n{' '*8}This means your function multiplication must be of the form f(x)*g(x) or f(x)*g(x)*h(x).\n{' '*8}For example, you would write x*e^x to obtain the derivative of the function.')
print(f'{'-'*145}')


print(f'Rule 5: To find the derivative of a function subtracted from another, you must write it in the form f(x) + (-g(x)). Example: x + (-x).\n{' '*8}One can use "+" for regular addition.')
print(f'{'-'*145}')


print(f'Rule 6: To divide a function in your expression, you must put the expression in parentheses,\n{' '*8}raise it to the power of -1, and multiply it with the rest of your expression.\n{' '*8}This means f(x)/g(x) should be written as f(x)*(g(x))^-1. Example: sin(x) / cos(x) should be written as sin(x)*(cos(x))^-1.')
print(f'{'-'*145}')


print(f'Rule 7: Each function that you have in your expression must be an approved function. \n{' '*8}The list of approved functions for use in our calculator can be found below:\n')
print(f'{' '*8}\u2022 Polynomials must of the form ax^b or ax (if x is raise to the 1) where a and b are real numbers.')
print()
print(f'{' '*8}\u2022 There are six trig functions that you can use. They are:{trig_functions}.')
print()
print(f'{' '*8}\u2022 To write an inverse trig function, use the following:{inverse_trig_functions}.')
print()
print(f'{' '*8}\u2022 For log functions, only the natural log, ln, is supported.')
print()
print(f'{' '*8}\u2022 For exponential functions, only e^x is supported. Of course you can always nest something within x in this function.')
print(f'{'-'*145}')
print('Thems the rules. Happy deriving!')


# code logic to have the user input their expression to be derivated
# this logic will clear the rules when the user is ready to input their expression
# this logic will then ask the user if they would like to derive another expression
# if they don't want to keep going, the program ends, if they do want to keep going, they are prompted to input another expression
end = 0
input_string = input("When you're ready to move on to the derivation, input anything.  ")
while end != 1:
    os.system("cls")
    input_function = input("What is the expression you'd like to derive?  ")
    print()
    print(f'The derivative of your function is {derivative(input_function)} ')
    print()
    input_answer = input("Would you like to keep deriving? Type 'c' if yes or input anything else if you're done.  ")
    print()
    if input_answer == "c":
        pass
    else:
        print("Thanks for using our Derivative Calculator\u2122 goodbye!")
        end = 1


   



