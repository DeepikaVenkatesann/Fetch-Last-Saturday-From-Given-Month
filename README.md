# Fetch-Last-Saturday-From-Given-Month

## Introduction
This  program utilizes the datetime module to calculate the last Saturday of a specified month and also determines the total number of Saturdays within that month.

timedelta is a class in the datetime module that represents the difference between two dates or times. It's commonly used for performing arithmetic operations with dates and times


## Explanation

Enter the month and year in the format "MMYYYY" when prompted.

lastsaturday(month, year):This function returns the last Saturday of the given month.

totalsaturdays(month, year): This function returns the Total Saturdays of the given month.

## Function Signautre

def lastsaturday(month: int, year: int) -> tuple:

    Calculate the last Saturday of a given month and the number of occurrences of Saturdays.

    Parameters:
        month (int): The month (1 to 12).
        year (int): The year.

    Returns:
        tuple: A tuple containing the day of the last Saturday and the count of Saturdays.

def totalsaturdays(month: int, year: int) -> int:
   
    Calculate the total number of Saturdays in a given month.

    Parameters:
        month (int): The month (1 to 12).
        year (int): The year.

    Returns:
        int: The total number of Saturdays in the month.

## Example
Suppose you want to find the last Saturday and total Saturdays for september 2023:

Enter the month and year (MMYYYY): 062023

Last Saturday: 24

Total Saturdays: 4


