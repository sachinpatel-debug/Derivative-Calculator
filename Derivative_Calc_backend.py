class Polynomial:
    # This is the class polynomial. This class is used to find the derivative of any polynomial using the power rule
    def __init__(self, ex):
        self.expression = ex
    def coefficient(input_ex):
        carat_index = input_ex.expression.find('^')
        new_val = input_ex.expression.lstrip()
        if len(new_val[0:carat_index]) == 1:
            coefficient = 1
   
        else:
            coefficient = float(new_val[0:carat_index-1])
        return coefficient
    # This class has getter and setter methods to make sure the polynomial has the correct form
    @property
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        carat_index = input_ex.expression.find('^')
        if input_ex.coefficient() != 1:
            if not isinstance(float(input_ex.expression[0:carat_index]), float):
                raise ValueError("Error. Rule 7. Please provide a legitimate polynomial function in the form: x^c")
        # The setter method checks if the input expression has the form x^c by splitting the expression at the x
        # and seeing if a carat comes after the x and a number comes before the x


        elif (input_ex.split('x')[1][0]) != '^' or not isinstance(float(input_ex.split('x')[1][1::]), float):
            raise ValueError("Error. Rule 7. Please provide a legitimate polynomial function in the form: x^c")
        else:
            self.expression = input_ex
    # This derivate function finds the derivative of a polynomial using power rule
    def derivate(self):
        self.expression = self.expression.replace('(', '')
        self.expression = self.expression.replace(')','')


        if self.expression[-1] == 'x':
            self.expression = self.expression + '^1'
        # The number that comes after the carat is the power, so it is found and multiplied by the coefficient and concatenated with x^ (power -1)
        derivative = str(float(self.expression.split('x')[1][1::])*(self.coefficient())) + 'x^' + str(float(self.expression.split('x')[1][1::]) - 1)
        if derivative[-3::] == "0.0":
            derivative = '1'
       
        if float(self.expression.split('x')[1][1::]) == 0:
            derivative = "0"
   
        return derivative
class Constant:
    # This is the class for the function type constant
    def __init__(self, ex):
        self.expression = ex
    # the getter and setter method checks if the input expression checking if every character in the constant is part of a number
    # these characters include numbers, the minus sign, and the . sign
    @property    
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        for char in input_ex:
            if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']:
                raise ValueError('This is not a constant')
            else:
                continue
        self.expression = input_ex
    # The derivate function for this class is simple, every constant has the same derivative: 0
    def derivate(self):
        derivative = '0'
        return derivative


class Trig:
    # This is the class for trigonometic functions


    trig_functions = ['cos(x)', 'sin(x)', 'tan(x)', 'sec(x)', 'csc(x)', 'cot(x)']
    def __init__(self, ex):
        self.expression = ex
    # The getter and setter method checks if the input expression is a trig function by establishing the fact that all trig functions
    # come from the list shown in trig_functions, so the setter method checks if the input_expression is in the established trig function list
    @property
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        if input_ex not in Trig.trig_functions:
            raise ValueError("Error. Please provide a legitimate trig function")
        else:
            self.expression = input_ex
    # The derivate function finds the derivative of the trig function based on what the trig function is
    def derivate(self):
        if self.expression =='cos(x)':
            derivative = '-sin(x)'
        if self.expression =='sin(x)':
            derivative = 'cos(x)'
        if self.expression =='tan(x)':
            derivative = 'sec(x)*sec(x)'
        if self.expression == 'sec(x)':
            derivative = 'tan(x)*sec(x)'
        if self.expression == 'csc(x)':
            derivative = '-cot(x)*csc(x)'
        if self.expression == 'cot(x)':
            derivative = '-csc(x)*csc(x)'
        return derivative
       
         
class InverseTrig:
        # This is the class for the function type inverse trig


    inv_trig_functions = ['arccos(x)', 'arcsin(x)', 'arctan(x)', 'arcsec(x)', 'arccsc(x)', 'arccot(x)']
    def __init__(self, ex):
        self.expression = ex
    # The getter and setter method checks if the input expression is a inverse trig function by establishing the fact that all inverse trig functions
    # come from the list shown in inv_trig_functions, so the setter method checks if the input_expression is in the established inverse trig function list
    @property
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        if input_ex not in InverseTrig.inv_trig_functions:
            raise ValueError("Error. Please provide a legitimate trig function")
        else:
            self.expression = input_ex
# The derivate function finds the derivative of the inverse trig function based on what the inverse trig function is
    def derivate(self):
        derivative = False
        if self.expression =='arccos(x)':
            derivative = '-1/(sqrt(1-(x^2)))'
        if self.expression =='arcsin(x)':
            derivative = '1/(sqrt(1-(x^2)))'
        if self.expression =='arctan(x)':
            derivative = '(1/(1+(x^2)))'
        if self.expression =='arcsec(x)':
            derivative = '1/(abs(x)*(sqrt(1-(x^2))))'
        if self.expression =='arccsc(x)':
            derivative = '-1/(abs(x)*(sqrt(1-(x^2))))'
        if self.expression =='arccot(x)':
            derivative = '(-1/(1+(x^2)))'        
        return derivative
   
       
class Ln:
    # This is the class for the function type natural log
    def __init__(self, ex):
        self.expression = ex
    # the input expression must be of the form ln(x), so this is what the setter method checks
    @property
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        if input_ex.lstrip(' ') != 'ln(x)':
            raise ValueError('Error, please enter a valid ln(x) function.')
    # The derivative of natural log is 1/x or x^-1, so that is what the derivate function returns
    def derivate(self):
        derivative = 'x^-1'
        return derivative


class Exp:
    # This is the class for the function type e^x
    def __init__(self, ex):
        self.expression = ex
    # this setter method works in a similar way to the polynomial checking, but this time, the method checks if the character after the
    # carat is x and the character(s) before the split at x are numbers


    @property
    def expression(self):
        return self.expression
    expression.setter
    def expression(self, input_ex):
        carat_index = input_ex.find('^')
        if (not isinstance(float(input_ex[0:carat_index]) , float) and input_ex.count('e', 0, carat_index) != 1) or (carat_index ==-1) or ('x' not in input_ex[carat_index + 1 ::]):
            raise ValueError("Error. Please provide a legitimate exponential function")
        else:
            self.expression = input_ex
    # The derivative of an exponential function is a^x * ln(a), so if the function is e^x, the derivative is e^x
    # So the derivate function has a special method for e^x where it only returns e^x
    # if a is any other number, it returns a^x * ln(a)
    def derivate(self):
        carat_index = self.expression.find('^')
        if self.expression == 'e^x' or self.expression == 'e^(x)':
            derivative = 'e^(x)'
        else:
            derivative = self.expression + '*ln(' + self.expression[0:carat_index] + ')'
        return derivative
       
# split expression accounts for nested functions by assinging all parts of the expression with a certain depth
# this will account for the chain rule later on  
def split_expression(input_ex):
    if input_ex.count('(') != input_ex.count(')'):
        raise ValueError('Error, you have a parentheses mismatch.')
    else:
        if input_ex.count('(') >= 0:
            functions_list = []
            left_paren_list = []
           
            depth = 0
       
        input_ex = '(' + input_ex + ')'
        for k in range(len(input_ex)):
            if input_ex[k] == '(':
                depth += 1
                left_paren_list.append(k)
               
            if input_ex[k] == ')':
                lp_top = left_paren_list.pop()
                functions_list.append([input_ex[lp_top + 1 : k], depth])
               
                depth -= 1
       
        return functions_list


# This function assigns an expression to a class so that the expression can be derivated with the classe
def assign_function_type(expression):
    expression = expression.strip()
    trig_functions = ['cos(x)', 'sin(x)', 'tan(x)', 'sec(x)', 'csc(x)', 'cot(x)']
    inv_trig_functions = ['arccos(x)', 'arcsin(x)', 'arctan(x)', 'arcsec(x)', 'arccsc(x)', 'arccot(x)']
    if '^x' in expression or "^(x)" in expression:
        func = Exp(expression)
    elif "ln(x)" in expression:
        func = Ln(expression)
    elif ("x^" in expression) or (expression == "x") or ("(x)^" in expression) or (expression == "(x)"):
        func = Polynomial(expression)
    elif expression in trig_functions:
        func = Trig(expression)
    elif expression in inv_trig_functions:
        func = InverseTrig(expression)
    else:
        expression = expression.replace('(', '').replace(')','')
        for char in expression:
                if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']:
                    raise TypeError(f'ERROR: {expression} is not a valid function type, please read the directions.')
                else:
                    continue
        func = Constant(expression)
    return func


# This function appends an element to the end of the list returned by the split expression function
# the element that this function appends is the nested function to the end of the list
# this means that if an element has a nested function inside of it, it will append what the nested function is to the end of the list
def overall_func_creator(func_list):
    for k in func_list:
        for i in func_list:
            if k[1]-1==i[1]:
                i.append(k[0])
                break


# This function replaces the nested function with a 'G'
# The G denotes the fact that their is a nested function inside the outer function
# The G also makes the overall function easier to read and process later on
def replace_all_exes(func_list):
    for i in range(len(func_list) -1, -1, -1):
        for k in range(2, len(func_list[i])):
            func_list[i][0] = func_list[i][0].replace("("+ func_list[i][k] + ")", '(G)', 1)


# since the list changes with the previous function, the overall function is now gone as the nested functions have been replaced with Gs
# This function replaces the Gs with their constituent functions
# This is done to know what the outer functions actually are so that the derivatives of the inner functions can be found and multiplied per the rules of the chain rule
def replace_all_g(g_list):
    exp = g_list[0]
    for i in range(2, len(g_list)):
        exp = exp.replace("G", g_list[i], 1)
    return exp
       
# Function that finds and stores the derivative of each nested fuction at the end of it's list index:
def find_derivative_list(func_list):
   
    for i in range(len(func_list)):   # Start by iterating over every nested function, starting from most nested to the outermost
        base_ex = func_list[i][0]               # Set the first entry in the list of functions as the base expression to be differentiated
        split_at_plus = base_ex.split("+")      # split it at any plus signs to be evaluated independently
        count_g = 0             # initialize a counter for the number of G's indicating the location of nested functions
        derivative_list = []    # and a list to store the derivatives of each term separated by a plus sign
       
        for exp in split_at_plus:  # Now iterate over all expressions split by a plus sign
            exp = exp.lstrip() # strip the expression of whitespace and check for product rule
           
            if '*' in exp:     # if product rule    
                split_at_mult = exp.split("*")   # store products in a list
                acc = [split_at_mult[0]]    # initialize an accumulator variable
                const_list = []             # and a list to store constants


                for q in range(len(split_at_mult) - 1):  # iterate over the number of products excluding the last two
                    base_func_list = ['','','','']       # initialize a list of length four to store the current two products being evaluated and their derivatives
                    if q == 0:  # condition for the first iteration as it needs to intialize the accumulator's derivative
                        # Parse both of the first two products for constants and base functions, appending the constant list and storing the function in its corresponding index:
                        for prod in range(0,2):
                            count = 0
                            for char in split_at_mult[prod]:
                                if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']:
                                    count += 1
                                else:
                                    break
                            const_list.append(split_at_mult[prod][0:count])
                            base_func_list[prod] = split_at_mult[prod][count:]
                       
                        count_given_exp = 0   # initialize counter variable for the index of the current base function being processed


                        for given_exp in base_func_list[0:2]:  # iterate over the two base functions
                            if 'G' in given_exp:                    # if the base function contains a nested function indicated by 'G"
                                count_g += 1                             # increase the count of instances of G for future cases
                                index_of_G_func = 1 + count_g            # To find the location of the contents of the nested expression, add the count of 'G's to 1
                                given_exp = given_exp.replace('G', 'x')  # Replace G with x to pass through the base function assignment for derivation
                                g = func_list[i][index_of_G_func]        # store the value pf the nested expression in a variable called 'g'
       
                                for fx in func_list:   # iterate over the function list to locate where the nested function is
                                    temp_val = replace_all_g(fx)  # temp_val is a temporary variable to ensure the function displays all of its nested contents
                                    if func_list[i][1]+1==fx[1] and g == temp_val:
                                        deriv_of_g = fx[-1]  # extract the derivative of the nested function
                                        break
                                # store the derivative of the function according to the chain rule:
                                cur_derivative = "(" + deriv_of_g + ')' + "(" + assign_function_type(given_exp).derivate().replace('x', g) + ")"  
                                given_exp = given_exp.replace("x", g, 1)  # make sure the expression contains all nested contents for future display
                               
                                base_func_list[count_given_exp] = given_exp   # store expression in its corresponding location to reference later
                               
                            else: # if there are no nested expressions (no 'G' found)
                                cur_derivative = assign_function_type(given_exp).derivate()  # the derivative can easily be found because it is a base function
                           
                            base_func_list[count_given_exp+2] = cur_derivative    # store derivative in its corresponding location to reference later
                           
                            count_given_exp += 1   # track the current expression handled for indexing reasons
                           
                        # Store the derivative according to the product rule and combine the two functions for future calculatio if more than two products:
                        product_rule_deriv = "((" + base_func_list[0] + ")" + '*' + base_func_list[-1] + ' + ' + "(" + base_func_list[1] + ")" + '*' + base_func_list[2] + ")"
                        product_rule_exp = "(" + base_func_list[0] + "*" + base_func_list[1] + ")"
                     
                    # if the current iteration is not the first one, repeat previous steps but using the accumulator for the first product and q+1th item in split_at_mult as the second
                    else:
                        # only need to calculate the derivative of second product since first product's is stored in acc_deriv
                        count = 0
                        for char in split_at_mult[q+1]:
                            if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']:
                                count+=1
                            else:
                                break
                       
                        const_list.append(split_at_mult[q+1][0:count])
                       
                        base_func_list[1] = split_at_mult[q+1][count:]
                       
                        if 'G' in base_func_list[1]:
                                count_g += 1
                                index_of_G_func = 1+count_g
                                base_func_list[1] = base_func_list[1].replace('G', 'x')
                                g = func_list[i][index_of_G_func]
       
                                for fx in func_list:
                                   
                                    tempVal = replace_all_g(fx)
                                    if func_list[i][1]+1==fx[1] and g == tempVal:
                                        deriv_of_g = fx[-1]
                                        break
                                cur_derivative = "(" + deriv_of_g + ')' + "(" + assign_function_type(base_func_list[1]).derivate().replace('x', g) + ")"
                                base_func_list[1] = base_func_list[1].replace('x', g, 1)
                        else:
                            cur_derivative =  assign_function_type(base_func_list[1]).derivate()


                        # usage of the accumulator and its derivative with the product rule:
                        product_rule_deriv = '(' + acc + ")*(" + cur_derivative + ") + (" + acc_deriv + ")*(" + base_func_list[1] + ')'
                        product_rule_exp = "(" + acc + "*" + base_func_list[1] + ")"
                   
                    # storage of accumulator values:
                    acc = product_rule_exp
                    acc_deriv = product_rule_deriv


                # Because the product rule indicates multplication of two functions, all constants can be multiplied into one final constant to be included at the end:    
                the_last_constant = 1
                for iterator in const_list: # use all values that have been appended to the constant list thus far
                    if iterator =='':
                        the_last_constant *= 1
                    else:
                        the_last_constant *= float(iterator)


                cur_derivative = str(the_last_constant) + '(' + acc_deriv + ')'   # set current derivative for final joining appendage to function list
           
            # if there is no "*" sign found, use the same logic for finding derivative of individual products and simply store that derivative for final appendage
            else:
                count = 0
                for char in exp:
                    if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-']:
                        count+=1
                    else:
                        break
                const = exp[0:count]
                base_func = exp[count:]
                if 'G' in base_func:
                    count_g += 1
                    index_of_G_func = 1+count_g
                    base_func = base_func.replace('G', 'x')
                    g = func_list[i][index_of_G_func]
           
                    for fx in func_list:
                       
                        tempVal = replace_all_g(fx)
                        if func_list[i][1]+1==fx[1] and g == tempVal:
                            deriv_of_g = fx[-1]
                            break
                   
                    cur_derivative = const + "(" + deriv_of_g + ')' + "(" + assign_function_type(base_func).derivate().replace('x', g) + ")"
                else:
                   
                    assigned_func = assign_function_type(base_func)
                    cur_derivative = const + "(" + assigned_func.derivate() + ")"
           
            # After the evaluation of every expression split at a "+" sign, store its derivative in a list:
            derivative_list.append(cur_derivative)
        # once all expressions have been iterated, join the list of derivatives with a "+" between each expression
        next_derivative = ' + '.join(derivative_list)
       
        # finally append the derivative to the end of the current evaluated function in the list
        func_list[i].append(next_derivative)
       


# function extracts the derivative expression from the last entry in the function list:
def final_deriv(func_list):
    final_deriv = func_list[-1][-1]
    return final_deriv


# This predicate determines of there is not a plus sign withing only the outermost parentheses (plus sign cannot be nested within more "()")
def plus_not_on_level(substring):
    op_list = ['+']
    parenth_unresolved = 0
    for char in substring:
        if char == "(":
            parenth_unresolved += 1
        if char == ")":
            parenth_unresolved -= 1
        if char in op_list:
            if parenth_unresolved == 1:
                return False
    return True


# This function cleans up any redundant expressions or parentheses:
def clean_up_answer(final_derivative):
   
    left_parenth = [] #  intialize an empty list to store the left parentheses indices
    for _ in range(final_derivative.count('(')): # iterate over the number of times a left parenthesis occurs in the final derivative
        for k in range(len(final_derivative)): # iterate over the final derivative string
            if final_derivative[k] == "(": # if a left parentheses is encountered, store its index in the list
                left_parenth.append(k)  
            elif final_derivative[k] == ")": # if a right parenthesis is encountered, check for redundancy
                right_parenth_index = k
                left_parenth_index = left_parenth.pop()
                # a set of parentheses is redundant and therefore should be removed if there is not plus sign nested directly within and
                # if the expression replaced with the second and second to last indices removed equals the
                # expression with the outer most parentheses removed.
                if final_derivative[left_parenth_index:right_parenth_index+1].replace(final_derivative[left_parenth_index + 1:right_parenth_index], final_derivative[left_parenth_index + 2:right_parenth_index - 1]) == final_derivative[left_parenth_index + 1:right_parenth_index]:
                    if plus_not_on_level(final_derivative[left_parenth_index:right_parenth_index+1]):
                        final_derivative = final_derivative.replace(final_derivative[left_parenth_index:right_parenth_index + 1], final_derivative[left_parenth_index + 1:right_parenth_index], 1)
                        break


    # Replacements below get rid of any arithmetic redundancies:
    final_derivative = final_derivative.replace('(1)(', '(')
    final_derivative = final_derivative.replace('((1))(', '(')
    final_derivative = final_derivative.replace('1(', '(')
    final_derivative = final_derivative.replace(')(1)', ')')
    final_derivative = final_derivative.replace(')((1))', '(')
    final_derivative = final_derivative.replace(')1', ')')
    final_derivative = final_derivative.replace('*1', '')
    final_derivative = final_derivative.replace('*(1)', '')
    final_derivative = final_derivative.replace('^1.0)', ')')


    return final_derivative


# Code to open a file where each line is a test expression and write the results in a new file
# If you want to test your own file, you'd likely need to alter the 'path' variable and change
# the name of the file to your desired text  
# path = "C:/Users/kjoze/.vscode/"
# with open(path + "DerivCalcTestCases.txt", mode ='r') as test_file,\
#      open(path + "TestDisplay.txt", mode = 'w') as output_file:
#     for line in test_file:
#         line = line.strip()
#         func_list = split_expression(line)
#         overall_func_creator(func_list)
#         replace_all_exes(func_list)
#         find_derivative_list(func_list)
#         derivative = final_deriv(func_list)
#         derivative = clean_up_answer(derivative)
#         space_amount = 35 - len(line)
#         print(f'Original Function: {line.strip()} {' '*space_amount} Derivative Of Function: {derivative}', file = output_file)


# This is the final funciton that gives you the derivative of your expression
# It combines all the functions that are needed to produce the final derivative answer in the form of a string
def find_final_derivative_answer(exp):
    func_list = split_expression(exp)
    overall_func_creator(func_list)
    replace_all_exes(func_list)
    find_derivative_list(func_list)
    derivative = final_deriv(func_list)
    derivative = clean_up_answer(derivative)
    return derivative


