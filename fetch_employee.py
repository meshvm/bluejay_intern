import pandas as pd

def best_employee(df):
    # Initialize variables to keep track of consecutive days and shift duration
    previous_employee = None

    # Define your criteria
    min_shift_duration = 14  # Minimum shift duration in hours

    # Create a dictionary to store the count for each employee
    employee_counts = {}

    # Iterate through the rows of the DataFrame
    for index, row in df.iterrows():
        employee = row['Employee Name']
        shift_start = row['Time']
        shift_end = row['Time Out']

        shift_duration = (shift_end - shift_start).total_seconds() / 3600
        if shift_duration > min_shift_duration:
            if employee in employee_counts:
                employee_counts[employee] += 1
            else:
                employee_counts[employee] = 1

    # Print the counts for each employee

    for employee, count in employee_counts.items():
        print(f"Employee Name: {employee}, Position: {row['Position ID']}")
