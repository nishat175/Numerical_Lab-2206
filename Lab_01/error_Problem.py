true_val = float(input("Enter true value: "))
approx_val = float(input("Enter approx value: "))

absolute_error = abs(true_val - approx_val)
relative_error = absolute_error / true_val
percentage_error = relative_error * 100

print("Absolute Error: %.3f" % absolute_error)
print("Relative Error: %.3f" % relative_error)
print("Percentage Error: %.3f" % percentage_error)
