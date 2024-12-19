def function_with_uncommon_error_solution(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        return "Invalid input types"
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"