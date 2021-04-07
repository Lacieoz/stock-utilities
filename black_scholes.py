import numpy as np
import scipy.stats as si
from check_inputs import check_inputs

# S: spot price
# K: strike price
# T: time to maturity
# r: interest rate
# sigma: volatility of underlying asset


def calculate_call_value(S, K, T, r, sigma):

    err, clean_inputs = check_inputs([S, K, r, sigma, T])
    if err == "":
        S, K, r, sigma, T = clean_inputs
    else:
        return err

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))

    return round(call, 3)


def calculate_put_value(S, K, T, r, sigma):

    err, clean_inputs = check_inputs([S, K, r, sigma, T])
    if err == "":
        S, K, r, sigma, T = clean_inputs
    else:
        return err

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))

    return round(put, 3)


def calculate_option_value(S, K, T, r, sigma, option='call'):

    err, clean_inputs = check_inputs([S, K, r, sigma, T])
    if err == "":
        S, K, r, sigma, T = clean_inputs
    else:
        return err

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option.lower() == "put" or option.lower() == "p":
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))

    elif option.lower() == "call" or option.lower() == "c":
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))

    return round(result, 3)


""" CREDIT TO https://aaronschlegel.me/black-scholes-formula-python.html """
