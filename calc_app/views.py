from django.shortcuts import render
from .utils import *
from .models import CalculationHistory

def calculate(request):
    result = None
    if request.method == 'POST':
        operation = request.POST['operation']
        value1 = request.POST.get('value1')
        value2 = request.POST.get('value2')
        numbers = request.POST.get('numbers')
       
        try:
            if operation in ['sin', 'cos', 'tan']:
                value1 = float(value1)
                result = globals()[operation](value1)
            elif operation in ['log', 'ln', 'exp']:
                value1 = float(value1)
                if operation == 'log':
                    base = float(value2) if value2 else 10
                    result = log(value1, base)
                else:
                    result = globals()[operation](value1)
            elif operation == 'power':
                base = float(value1)
                exponent = float(value2)
                result = power(base, exponent)
            elif operation in ['add_complex', 'subtract_complex', 'multiply_complex', 'divide_complex']:
                result = globals()[operation](value1, value2)
            elif operation in ['magnitude_complex', 'phase_complex', 'polar_complex']:
                result = globals()[operation](value1)
            elif operation in ['mean', 'median', 'std_dev']:
                numbers = list(map(float, numbers.split(',')))
                result = globals()[operation](numbers)
            else:
                result = 'Invalid operation'
        except Exception as e:
            result = str(e)

    history = CalculationHistory.objects.all()[:50]

    return render(request, 'calc_app/calculate.html', {'result': result, 'history': history})

