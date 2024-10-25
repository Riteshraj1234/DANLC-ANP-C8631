# Multiple Exception Types in User Input
#
#    - Write a function `get_valid_date` that prompts the user to enter a date in the format `YYYY-MM-DD`. Use exception handling to manage:
#
#      - Invalid format (e.g., not enough parts, non-numeric parts).
#
#      - Invalid date values (e.g., month not in 1-12, day not valid for the given month).
#
#    - Ensure the function keeps asking for input until a valid date is entered and returns a `datetime.date` object.'''
from datetime import datetime


def get_valid_date():
    class InvalidDateValuesError(Exception):
        def __init__(self, message):
            super().__init__(message)

    class InvalidFormatError(Exception):
        def __init__(self):
            super().__init__("Format of time is not in yyyy-mm-dd")

    try:
        date = input("Enter date in yyyy-mm-dd format")
        day = int(date[8:])
        mon = int(date[5:7])
        year = int(date[0:4])
        str = ""
        # dd = datetime.strptime(date, "yyyy-mm-dd")
        # //print("You entered date in write format:", dd)
        if not (1 <= mon <= 12):
            raise InvalidDateValuesError("Input Month is Incorrect!!")
        else:
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                if not (1 <= day <= 31):
                    str = "Valid Date not Found!!!"
                    raise InvalidDateValuesError("Input Date is Incorrect!!!")

                str = "Valid Date Found!!!"
            elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
                if not (1 <= day <= 30):
                    str = "Valid Date not Found!!!"
                    raise InvalidDateValuesError("Input Date is Incorrect!!!")
                str = "Valid Date Found!!!"
            elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if not (1 <= day <= 29):
                    str = "Valid Date not Found!!!"
                    raise InvalidDateValuesError("Input Date is Incorrect!!!")
                str = "Valid Date Found!!!"
            elif not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                if not (1 <= day <= 28):
                    str = "Valid Date Found!!!"
                    raise InvalidDateValuesError("Input Date is Incorrect!!!")
                str = "Valid Date Found!!!"
            else:
                print("Invalid Date Found!!!",date)
        print(str)
    except InvalidDateValuesError as id:
        print(id)
    except InvalidFormatError as ife:
        print(ife)
    except ValueError as ve:
        print("Invalid Date Format")


get_valid_date()
