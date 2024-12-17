import cmath
def function_with_uncommon_error_solution(x):
    if x == 0:
        return float('inf') # Or raise a more descriptive exception: raise ValueError("Cannot divide by zero.")
    elif x < 0:
        return cmath.sqrt(x) # Use cmath for complex number support
    else:
        return x + 5

# Example usage:
result = function_with_uncommon_error_solution(-4)
print(result) # Output: 2j
result = function_with_uncommon_error_solution(0)
print(result) # Output: inf
result = function_with_uncommon_error_solution(5)
print(result) # Output: 10