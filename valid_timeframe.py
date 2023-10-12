import pandas as pd

def timeperiod(df):

    # Initialize variables to keep track of consecutive days and shift duration
    previous_employee = None
    previous_shift_end = None

    # Define your criteria
    min_time_between_shifts = 1  # Minimum time between shifts in hours
    max_time_between_shifts = 10  # Maximum time between shifts in hours

    # Create a dictionary to store the count for each employee
    employee_counts = {}

    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        employee = row['Employee Name']
        shift_start = row['Time']
        shift_end = row['Time Out']

        if employee == previous_employee:
            # Calculate the time difference between shifts
            time_between_shifts = (shift_start - previous_shift_end).total_seconds() / 3600

            if min_time_between_shifts < time_between_shifts < max_time_between_shifts:
                print(
                    f"Employee: {employee}, Position: {row['Position ID']}, Durations: {time_between_shifts:.2f} hours")
                if employee in employee_counts:
                    employee_counts[employee] += 1
                else:
                    employee_counts[employee] = 1

        previous_employee = employee
        previous_shift_end = row['Time Out']

    # Print the counts for each employee
    for employee, count in employee_counts.items():
        print(f"Employee: {employee}, Count: {count}")
