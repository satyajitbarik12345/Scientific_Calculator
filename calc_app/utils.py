import math
from cmath import phase, polar
from .models import CalculationHistory

def log_operation(op_type, result):
    CalculationHistory.objects.create(operation=op_type, result=result)
    if CalculationHistory.objects.count() > 50:
        CalculationHistory.objects.order_by('timestamp').first().delete()

# Trigonometric Functions
def sin(value):
    result = math.sin(value)
    log_operation(f'sin({value})', result)
    return result

def cos(value):
    result = math.cos(value)
    log_operation(f'cos({value})', result)
    return result

def tan(value):
    result = math.tan(value)
    log_operation(f'tan({value})', result)
    return result

# Logarithms
def log(value, base=10):
    result = math.log(value, base)
    log_operation(f'log({value}, {base})', result)
    return result

def ln(value):
    result = math.log(value)
    log_operation(f'ln({value})', result)
    return result

# Exponential Functions
def exp(value):
    result = math.exp(value)
    log_operation(f'exp({value})', result)
    return result

def power(base, exponent):
    result = math.pow(base, exponent)
    log_operation(f'power({base}, {exponent})', result)
    return result

# Statistical Functions
def mean(numbers):
    result = sum(numbers) / len(numbers)
    log_operation(f'mean({numbers})', result)
    return result

def median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        result = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        result = sorted_numbers[mid]
    log_operation(f'median({numbers})', result)
    return result

def standard_deviation(numbers):
    mean_val = mean(numbers)
    variance = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
    result = math.sqrt(variance)
    log_operation(f'standard_deviation({numbers})', result)
    return result

# Complex Number Operations
def add_complex(c1, c2):
    try:
        complex1 = complex(c1)
        complex2 = complex(c2)
        result = complex1 + complex2
        log_operation(f'add_complex({c1}, {c2})', result)
        return result
    except ValueError as e:
        return str(e)

def subtract_complex(c1, c2):
    result = c1 - c2
    log_operation(f'subtract_complex({c1}, {c2})', result)
    return result

def multiply_complex(c1, c2):
    result = c1 * c2
    log_operation(f'multiply_complex({c1}, {c2})', result)
    return result

def divide_complex(c1, c2):
    result = c1 / c2
    log_operation(f'divide_complex({c1}, {c2})', result)
    return result

def magnitude_complex(c):
    result = abs(c)
    log_operation(f'magnitude_complex({c})', result)
    return result

def phase_complex(c):
    result = phase(c)
    log_operation(f'phase_complex({c})', result)
    return result

def polar_complex(c):
    result = polar(c)
    log_operation(f'polar_complex({c})', result)
    return result
