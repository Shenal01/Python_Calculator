import math
history = []

while True:
    print('Select operation.')
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    print("8.History  : ?")
    
    operation = input('Enter choice(+,-,*,/,^,%,#,$,?): ')
    print(operation)

    if operation == '#':
            print("Done. Terminating")
            exit()
        
    elif operation == '$':
        print("Reseting... ")
        continue

    elif operation == '?':
            if history:
                for last_calculation in history:
                    print(last_calculation)
                continue
            else:
                print('No past calculations to show')
                continue

    num1 = None
    num2 = None
    result = 0.0
    last_calculation = ""

    try:
        num1 = str(input('Enter first number: '))
        print(str(num1))
        num2 = str(input('Enter second number: '))
        print(str(num2))
        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2

        elif operation == '-':
            result = num1 - num2

        elif operation == '*':
            result = num1 * num2
        
        elif operation == '/':    
            if float(num1) is not None and float(num2) is not None:
                        if num2 != 0:
                            result = num1 / num2

                        else:
                            print("float division by zero")
                            last_calculation =  "{0} {1} {2} = {3}".format(num1, operation, num2, None) 
                            print(last_calculation )
                            history.append(last_calculation)
                            num2 = str(num2)
                            continue
        
        elif operation == '^':
            result = math.pow(num1, num2)
            #formated_result = "{:.3f}".format(result)
            #print(f'{num1} {operation} {num2} = {formated_result}')

        elif operation == '%':
            result = num1 % num2

        else:
            print('Invalid operation')
            exit()

        last_calculation =  "{0} {1} {2} = {3}".format(num1, operation, num2, result) 
        print(last_calculation )
        history.append(last_calculation)

    

    except ValueError as e:
                #data1 = type(num1)
                data2 = type(num2)

                if num1 == '#' or num2 == '#':
                    if num1 == '#':
                         print(f"{num1}")
                    elif num2 == '#':
                         print(f"{num2}")
                    print("Done. Terminating")
                    exit()

                elif num1 == '$' or num2 == '$':
                    if num1 == '$':
                         print(f"{num1}")
                    elif num2 == '$':
                         print(f"{num2}")
                    print("Reseting... ")
                    continue

                elif data2 == str:
                    num2 = str(num2)
                    print(f"{num2}")
                    continue
                else:
                    num1 = str(num1)
                    print(f"{num1}")
                    continue
