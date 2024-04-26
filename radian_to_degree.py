radian_to_degree = 57.2958

user_input = input("Enter a number: ")

user_input_float = float(user_input)

required_degree = user_input_float * radian_to_degree

print("%.2f is the required degree." % required_degree)
