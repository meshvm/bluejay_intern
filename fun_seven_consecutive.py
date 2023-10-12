
#
#
#
def consecutive_days(df):
    # Initialize variables to keep track of consecutive days
    previous_employee = None
    consecutive_days = 0

    # Define your criteria
    min_consecutive_days = 7

    # Create a dictionary to store the consecutive days for each employee
    employee_consecutive_days = {}

    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        employee = row['Employee Name']
        position = row['Position ID']

        if employee == previous_employee:
            consecutive_days += 1
        else:
            consecutive_days = 1

        employee_consecutive_days[employee] = max(consecutive_days, employee_consecutive_days.get(employee, 0))

        previous_employee = employee

    # Find employees with >= 7 consecutive days
    consecutive_employees = {k: v for k, v in employee_consecutive_days.items() if v >= min_consecutive_days}

    # Print the results
    for employee, days in consecutive_employees.items():
        print(f"Employee: {employee},Position : {position}")
