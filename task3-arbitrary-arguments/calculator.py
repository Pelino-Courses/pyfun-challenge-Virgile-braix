def perform_operation(args, operation):
    """
    Helper function to perform the selected operation on given numbers.

    """

    result = args[0]
    for num in args[1:]:
        if operation == 'add':
            result += num
        elif operation == 'sub':
            result -= num
        elif operation == 'mult':
            result *= num
        elif operation == 'div':
            if num == 0:
                raise ZeroDivisionError ("cannot divide by zero. ")
            result /= num
    return result
           

def calculate(*args, **kwargs):
    """

    A simple calculator which will perform one operation (add, subtract, multiply, divide) on any number of inputs using keyword flags.

    """

    if not args:
        raise ValueError("At least one number must be provided.")

    operations =  ['add', 'sub', 'mult', 'div']
    
    # we are going to use for loop to filter active operations
    active_ops = []
    for op in operations :
        if kwargs.get (op, False):
            active_ops.append(op)

    if len(active_ops )!= 1 :
        raise ValueError("Please choose exactly one operation. ")

    operation = active_ops[0]
    return perform_operation(args, operation)
        

# User input for the calculator
if __name__ == "__main__":
    print("=== Command-Line Calculator ===")

    try:
        count = int(input("How many numbers do you want to enter to calculate ?"))
        if count < 1:
            raise ValueError("You must enter at least one number. ")

        args = []
        for i in range(count):
            num = float(input(f" Enter number {i + 1}: "))
            args.append(num)

        op_input = input("Choose between those operaions(add, sub, mult, div): ").strip().lower() 
        if op_input not in ['add', 'sub', 'mult', 'div']:
            raise ValueError("Invalid Operation .")
        
        kwargs = {op_input: True}

        result = calculate(*args, **kwargs)
         
        print("Result: ", result)

    except Exception as e:
        print("Error: ", e)

