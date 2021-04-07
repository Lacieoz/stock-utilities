def check_inputs(inputs):

    for input in inputs:
        try:
            input = float(input)
        except ValueError:
            print("Some input isn't a number")
            return "InputError", []
    return "", inputs
