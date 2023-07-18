import operators

result_add = operators.addOperator(5, 3)
result_divide = operators.divideOperator(10, 2)

print("Using the whole module:")
print("Addition result:", result_add)
print("Division result:", result_divide)


from operators import addOperator, divideOperator

result_add = addOperator(5, 3)
result_divide = divideOperator(10, 2)

print("\nUsing specific functions:")
print("Addition result:", result_add)
print("Division result:", result_divide)


import operators as ops

result_add = ops.addOperator(5, 3)
result_divide = ops.divideOperator(10, 2)

print("\nUsing alias for the module:")
print("Addition result:", result_add)
print("Division result:", result_divide)