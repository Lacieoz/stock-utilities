from math import log, e
from scipy.stats import norm
from check_inputs import check_inputs

# type  : type of contract (call or put
# S     : spot price
# K     : strike price
# r     : interest rate
# q     : dividend continuous rate
# sigma : volatility of underlying asset
# T     : time to maturity (expressed as #days/365)

############################################
############ 1st order greeks ##############
############################################


def calculate_delta(type, S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    dfq = e ** (-q * T)

    if type.lower() == "put" or type.lower() == "p":
        return round(dfq * (norm.cdf(d1) - 1), 4)

    elif type.lower() == "call" or type.lower() == "c":
        return round(dfq * norm.cdf(d1), 4)

    else:
        print("Type inserted not recognized")
        return "InputError"


# Vega for 1% change in vol
def calculate_vega(S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT

    return round(0.01 * S * e ** (-q * T) * norm.pdf(d1) * T ** 0.5, 4)


# Theta for 1 day change
def calculate_theta(type, S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    df = e ** -(r * T)
    dfq = e ** (-q * T)

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    d2 = d1 - sigmaT

    if type.lower() == "put" or type.lower() == "p":
        type = -1
    elif type.lower() == "call" or type.lower() == "c":
        type = 1
    else:
        print("Type inserted not recognized")
        return "InputError"

    tmptheta = (1.0 / 365.0) * (-0.5 * S * dfq * norm.pdf(d1) * sigma / (T ** 0.5)
                + type * (q * S * dfq * norm.cdf(type * d1) - r * K * df * norm.cdf(type * d2)))

    return round(tmptheta, 4)


def calculate_rho(type, S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    d2 = d1 - sigmaT

    if type.lower() == "put" or type.lower() == "p":
        type = -1
    elif type.lower() == "call" or type.lower() == "c":
        type = 1
    else:
        print("Type inserted not recognized")
        return "InputError"

    df = e ** -(r * T)
    return round(type * K * T * df * 0.01 * norm.cdf(type * d2), 4)


def calculate_phi(type, S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT

    if type.lower() == "put" or type.lower() == "p":
        type = -1
    elif type.lower() == "call" or type.lower() == "c":
        type = 1
    else:
        print("Type inserted not recognized")
        return "InputError"

    return round(0.01 * -type * T * S * e ** (-q * T) * norm.cdf(type * d1), 4)


############################################
############ 2nd order greeks ##############
############################################

def calculate_gamma(S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT

    sigmaT = sigma * T ** 0.5
    return round(e ** (-q * T) * norm.pdf(d1) / (S * sigmaT), 4)


# Charm for 1 day change
def calculate_d_deltad_time(type, S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    d2 = d1 - sigmaT
    dfq = e ** (-q * T)

    if type.lower() == "put" or type.lower() == "p":
        return round((1.0 / 365.0) * -dfq * (norm.pdf(d1) * ((r - q) / (sigmaT) - d2 / (2 * T))
                                       + q * norm.cdf(-d1)), 4)

    elif type.lower() == "call" or type.lower() == "c":
        return round((1.0 / 365.0) * -dfq * (norm.pdf(d1) * ((r - q) / (sigmaT) - d2 / (2 * T))
                                       + (-q) * norm.cdf(d1)), 4)

    else:
        print("Type inserted not recognized")
        return "InputError"


# Vanna for 1% change in vol
def calculate_d_deltad_vol(S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    d2 = d1 - sigmaT

    return round(0.01 * -e ** (-q * T) * d2 / sigma * norm.pdf(d1), 4)


# Vomma
def calculate_d_vegad_vol(S, K, T, r, sigma, q):

    err, clean_inputs = check_inputs([S, K, r, q, sigma, T])
    if err == "":
        S, K, r, q, sigma, T = clean_inputs
    else:
        return err

    sigmaT = sigma * T ** 0.5
    d1 = (log(S / K) + (r - q + 0.5 * (sigma ** 2)) * T) / sigmaT
    d2 = d1 - sigmaT

    return round(0.01 * -e ** (-q * T) * d2 / sigma * norm.pdf(d1), 4)


""" CREDIT TO http://www.smileofthales.com/computation/options-greeks-python/ """
