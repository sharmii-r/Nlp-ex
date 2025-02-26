#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

# Get input from the user
c_v_with = float(input("Enter the C(v, with): "))
c_v = float(input("Enter the C(v): "))
c_n_with = float(input("Enter the C(n, with): "))
c_n = float(input("Enter the C(n): "))

# Check for zero inputs to avoid division by zero or invalid log calculations
if c_v == 0 or c_n == 0 or c_n_with == 0:
    print("\nError: Input values cannot be zero. Please provide valid inputs.")
else:
    # Calculate probabilities
    p_with_1_V = c_v_with / c_v
    p_with_1_N = c_n_with / c_n
    p_with_0_N = 1 - p_with_1_N

    # Check if the argument of log2 is valid (must be positive)
    log_argument = (p_with_1_V * p_with_0_N) / p_with_1_N
    if log_argument <= 0:
        print("\nError: Invalid calculation. The argument for log2 must be positive.")
    else:
        # Calculate lambda(v, n, p)
        lambda_value = math.log2(log_argument)

        # Display the results
        print("\nCalculated Probabilities:")
        print(f"P(VA with = 1 | v) = {p_with_1_V:.8f}")
        print(f"P(NA with = 1 | n) = {p_with_1_N:.8f}")
        print(f"P(NA with = 0 | n) = {p_with_0_N:.8f}")

        print("\nCalculated Lambda:")
        print(f"lambda(v, n, p) = {lambda_value:.8f}")

        # Determine if PP attaches with V or N
        if lambda_value > 0:
            print("\nResult: PP attaches with V")
        else:
            print("\nResult: PP attaches with N")


# In[ ]:





# In[ ]:




