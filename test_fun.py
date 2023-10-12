#Import required packages
import pandas as pd
import valid_timeframe
import fun_seven_consecutive
import fetch_employee
import sys

if __name__ == '__main__':

    # Define the name of the output text file
    output_file = 'output.txt'

    # Redirect the standard output to the text file
    original_stdout = sys.stdout
    with open(output_file, 'w') as f:
        sys.stdout = f
        # Load the Excel file
        file_path = 'Assignment_Timecard.xlsx'
        df = pd.read_excel(file_path)

        # Sort the data by employee and date
        df.sort_values(by=['Employee Name', 'Position ID'], inplace=True)

        print("<<!! List of Employees worked for 7 consecutive days !!>>")

        # has worked for 7 consecutive days
        fun_seven_consecutive.consecutive_days(df)

        print("<<!! List of Employees who worked less than 10 hours of time between shifts but greater than 1 hour !!>>")
        #have less than 10 hours of time between shifts but greater than 1 hour
        valid_timeframe.timeperiod(df)

        print("<<!! List of Employees Who worked for more than 14 hours in a single shift!!>>")
        # Who has worked for more than 14 hours in a single shift
        fetch_employee.best_employee(df)

    # Reset the standard output to the original
    sys.stdout = original_stdout
