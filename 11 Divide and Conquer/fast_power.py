def fast_power(x, n):   # x^n
    if n == 0:
        return 1.0
    
    elif n < 0:
        return 1 / fast_power(x, -n)
    
    elif n % 2 == 1:
        return fast_power(x * x, n // 2) * x  # 5^7 = 5^3 * 5^3 * 5 = (5*5)^3 * 5
    
    else:
        return fast_power(x * x, n // 2)