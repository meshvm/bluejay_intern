import pandas as pd
import valid_timeframe
import fun_seven_consecutive
import fetch_employee
'''
Write a program that:
1. Take the file as an input
2. Programmatically analyze the file and print in console the name and position of employees 
      a) who has worked for 7 consecutive days.
      b) who have less than 10 hours of time between shifts but greater than 1 hour
      c) Who has worked for more than 14 hours in a single shift
3. Write a clean code with code comments and assumptions (if any) you are making
#Everyday we have to learn.
'''

if __name__ == '__main__':
    # Load the Excel file
    file_path = 'Assignment_Timecard.xlsx'
    df = pd.read_excel(file_path)

    # Sort the data by employee and date
    # df.sort_values(by=['Employee Name', 'Position ID'], inplace=True)

    print("<<!! List of Employees worked for 7 consecutive days !!>>")

    # has worked for 7 consecutive days
    fun_seven_consecutive.consecutive_days(df)

    print("<<!! List of Employees who worked less than 10 hours of time between shifts but greater than 1 hour !!>>")
    #have less than 10 hours of time between shifts but greater than 1 hour
    valid_timeframe.timeperiod(df)

    print("<<!! List of Employees Who worked for more than 14 hours in a single shift!!>>")
    # Who has worked for more than 14 hours in a single shift
    fetch_employee.best_employee(df)


