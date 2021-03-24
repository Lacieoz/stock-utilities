import simple_options as so

# array with the mandatory keys which every dictionary, describing a leg, have to contain
keys_leg = ['t',   # type
            'd',   # direction
            's',   # strike
            'pp',  # price paid
            'ep',  # end stock price
            'cs',  # contract size
            'ps']  # position size


def calculate_multi_leg_payoff(legs):
    """
    calculates the cumulative payoff of all the legs submitted as input

    :param legs: array of dictionaries with mandatory keys, contained in the array keys_leg
    :return: "InputError" - if input doesn't have the needed keys
             total - value of multi-leg strategy
    """

    # check dictionaries contains keys needed
    for leg in legs:
        missing_key = check_leg_input(leg)
        if missing_key != '':
            print("Missing from a leg the following key : " + missing_key)
            return "InputError"

    total = 0

    for leg in legs:
        type = leg['t']
        direction = leg['d']
        strike = leg['s']
        price_paid = leg['pp']
        end_stock_price = leg['ep']
        contract_size = leg['cs']
        position_size = leg['ps']

        payoff_leg = so.calculate_option_payoff(type, direction, strike, price_paid, end_stock_price, contract_size, position_size)
        total += payoff_leg

    return total


def check_leg_input(leg):
    """
    checks if every key contained in keys_leg is missing from the input

    :param leg: dictionary
    :return: '' - if every mandatory key is contained in the input
             name of the key - if a key is missing
    """
    keys = list(leg)
    for key_leg in keys_leg:
        if key_leg not in keys:
            return key_leg
    return ''










