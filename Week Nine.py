import WeekNineFunction

# My inputs.
loan_amount_input = input('Enter the total loan amount: ')
fixed_APR_input = input('Enter the APR for a fixed mortgage: ')
APR_points_input = input('Enter the APR for a mortgage by points: ')
points_input = input('Enter the number of points: ')
years_input = input('Enter the number of years: ')

# Converting inputs from strings to integers/ floats.
loan_amount_input = int(loan_amount_input)
fixed_APR_input = float(fixed_APR_input)
years_input = int(years_input)
APR_points_input = float(APR_points_input)
points_input = float(points_input)

# Pulling function from WeekNineFunction and giving to a variable.
inputs = WeekNineFunction.Mortgage(loan_amount_input, fixed_APR_input, years_input)
point_inputs = WeekNineFunction.Points_Mortgage(loan_amount_input, fixed_APR_input, years_input, points_input, APR_points_input)

# Getting percentages for outputs.
fixed_APR_percentage = fixed_APR_input * 100
APR_points_percentage = APR_points_input * 100

# Outputs.
print('Fixed', '%.1f' % fixed_APR_percentage, '%')
print('Total payment is $', '%.1f' % inputs.set_pay_monthly())
print('')
print('Fixed', '%.1f' % APR_points_percentage, '%', '+', points_input, 'points')
print('Total payment is $', '%.1f' % point_inputs.set_include_points())
