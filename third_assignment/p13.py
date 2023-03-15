try:
    num1 = int(input())
    num2 = int(input())
    a = max(num1, num2) / min(num1, num2)
    print(a)
except ValueError:
    print("Invalid input,Please enter integers only.")
except ZeroDivisionError:
    print("Division by zero is not allowed")
