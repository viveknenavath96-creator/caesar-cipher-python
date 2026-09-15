import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
symbols_dict={
    "+":add,
    "-":subtract,
    "*":multiplication,
    "/":division
}
def calculator():

   
    number1 = float(input("enter the first number:"))
    for symbols in symbols_dict:
      print(symbols)
    continue_flag = True
    while continue_flag:

       op_symbol= input("pick an operation:")
       number2 = float(input("enter the next number:"))
       calculator_func=symbols_dict[op_symbol]
       output = calculator_func(number1,number2)
       print(f" {number1} {op_symbol} {number2} = {output}")

       should_continue = input(f"enter 'y' to continue with the {output}, or 'n' new calculation or 'x' to exit").lower()
       if should_continue =='y':
          number1 = output
       elif should_continue == 'n':
          continue_flag = False
          os.system('cls')
          calculator()
       else:
           continue_flag=False
           print("bye")
calculator()           



