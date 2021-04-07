import simple_options as simple_options
import black_scholes as black_scholes
import multi_leg_strategies as mls
import greeks as greeks

# TESTS SIMPLE_OPTIONS.PY
print("\nTESTS SIMPLE_OPTIONS.PY")
print(simple_options.calculate_long_call_payoff(45, 2.3, 49, 1, 100))
print(simple_options.calculate_long_option_payoff("CALL", 45, 2.3, 49, 1, 100))

print(simple_options.calculate_long_put_payoff(49, 2.3, 44, 1, 100))
print(simple_options.calculate_long_option_payoff("PUT", 49, 2.3, 44, 1, 100))

# TESTS BLACK_SCHOLES.PY
print("\nTESTS BLACK_SCHOLES.PY")
s = 122.53
k = 118.75
t = 24/365
r = 0.017
sigma = 0.30
print(black_scholes.calculate_call_value(s, k, t, r, sigma))
print(black_scholes.calculate_put_value(s, k, t, r, sigma))
print(black_scholes.calculate_option_value(s, k, t, r, sigma))

# TESTS MULTI_LEG_STRATEGIES.PY
print("\nTESTS MULTI_LEG_STRATEGIES.PY")
dicts = [{'t': 'call', 'd': 'long', 's': 99, 'pp': 2, 'ep': 102, 'cs': 1, 'ps': 1},
         {'t': 'put', 'd': 'long', 's': 105, 'pp': 2, 'ep': 102, 'cs': 1, 'ps': 1}]

print(mls.calculate_multi_leg_payoff(dicts))

# TESTS GREEKS.PY
print("\nTESTS GREEKS.PY")
print("delta")
print(greeks.calculate_delta('call', s, k, t, r, sigma, 0))
print("vega")
print(greeks.calculate_vega(s, k, t, r, sigma, 0))
print("theta")
print(greeks.calculate_theta('call', s, k, t, r, sigma, 0))
print("rho")
print(greeks.calculate_rho('call', s, k, t, r, sigma, 0))
print("phi")
print(greeks.calculate_phi('call', s, k, t, r, sigma, 0))
print("gamma")
print(greeks.calculate_gamma(s, k, t, r, sigma, 0))
print("d deltad time")
print(greeks.calculate_d_deltad_time('call', s, k, t, r, sigma, 0))
print("d deltad vol")
print(greeks.calculate_d_deltad_vol(s, k, t, r, sigma, 0))
print("d vega d vol")
print(greeks.calculate_d_vegad_vol(s, k, t, r, sigma, 0))