def function_with_uncommon_error(x):
    if x == 0:
        return 1/x # ZeroDivisionError
    elif x < 0:
        return x**0.5 # ValueError, because negative number raised to power 0.5 gives complex number.  This might not always be explicitly caught.
    else:
        return x + 5

# Example usage that will only produce a ValueError (for simplicity):
result = function_with_uncommon_error(-4)