from check_inputs import check_inputs


def calculate_long_call_payoff(strike, price_paid, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else

    err, clean_inputs = check_inputs([strike, price_paid, end_stock_price, contract_size, position_size])
    if err == "":
        strike, price_paid, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    price_diff = max(end_stock_price - strike, 0)
    payoff = price_diff - price_paid

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_long_put_payoff(strike, price_paid, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, price_paid, end_stock_price, contract_size, position_size])
    if err == "":
        strike, price_paid, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    price_diff = max(strike - end_stock_price, 0)
    payoff = price_diff - price_paid

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_long_option_payoff(type, strike, price_paid, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, price_paid, end_stock_price, contract_size, position_size])
    if err == "":
        strike, price_paid, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    # calculate price difference based on option type (call or put)
    if type.lower() == "put" or type.lower() == "p":
        price_diff = max(strike - end_stock_price, 0)

    elif type.lower() == "call" or type.lower() == "c":
        price_diff = max(end_stock_price - strike, 0)

    else:
        print("Type inserted not recognized")
        return "InputError"

    payoff = price_diff - price_paid

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_short_call_payoff(strike, premium_received, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, premium_received, end_stock_price, contract_size, position_size])
    if err == "":
        strike, premium_received, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    price_diff = max(end_stock_price - strike, 0)
    payoff = premium_received - price_diff

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_short_put_payoff(strike, premium_received, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, premium_received, end_stock_price, contract_size, position_size])
    if err == "":
        strike, premium_received, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    price_diff = max(strike - end_stock_price, 0)
    payoff = premium_received - price_diff

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_short_option_payoff(type, strike, premium_received, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, premium_received, end_stock_price, contract_size, position_size])
    if err == "":
        strike, premium_received, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    # calculate price difference based on type of option (call or put)
    if type.lower() == "put" or type.lower() == "p":
        price_diff = max(strike - end_stock_price, 0)

    elif type.lower() == "call" or type.lower() == "c":
        price_diff = max(end_stock_price - strike, 0)

    else:
        print("Type inserted not recognized")
        return "InputError"

    payoff = premium_received - price_diff

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded


def calculate_option_payoff(type, direction, strike, premium_or_paid, end_stock_price, contract_size, position_size):
    # casting in case variables are string or something else
    err, clean_inputs = check_inputs([strike, premium_or_paid, end_stock_price, contract_size, position_size])
    if err == "":
        strike, premium_or_paid, end_stock_price, contract_size, position_size = clean_inputs
    else:
        return err

    # calculate price difference based on option type (call or put)
    if type.lower() == "put" or type.lower() == "p":
        price_diff = max(strike - end_stock_price, 0)

    elif type.lower() == "call" or type.lower() == "c":
        price_diff = max(end_stock_price - strike, 0)

    else:
        print("Type inserted not recognized")
        return "InputError"

    # calculate payoff based on option direction (long or short)
    if direction.lower() == "long" or direction.lower() == "l":
        payoff = price_diff - premium_or_paid

    elif direction.lower() == "short" or direction.lower() == "s":
        payoff = premium_or_paid - price_diff

    else:
        print("Direction inserted not recognized")
        return "InputError"

    total_payoff = payoff * contract_size * position_size

    # result rounded to 2 decimal numbers
    total_payoff_rounded = round(total_payoff, 3)

    return total_payoff_rounded
