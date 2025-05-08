import datetime

def days_between(date1_str, date2_str):
   """
   Calculate the number of days between two dates.

   Parameters:
       date1_str (str): The first date in 'YYYY-MM-DD' format.
       date2_str (str): the second date in 'YYYY-MM-DD' format.

   Returns:
        int: The absolute number of days between the two dates.

   Raises :
        ValueError: If the date format is invalid.

   Example:
       days_between("2025-01-01", "2025-05-04")

   """
   try:
        d1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
        return abs((d2-d1).days)
   except ValueError:
       raise ValueError("Invalid date format. Use 'YYYY-MM-DD' .")
   
#Example

if __name__== "__main__":
   
   print("Enter two dates to find the number of days between them.")
   date1 = input("Enter the first date(YYYY-MM-DD): ")
   date2 = input("Enter the second date (YYYY-MM-DD): ")
   
   try:
    
    difference = days_between(date1, date2)
    print(f"\n There are {difference} day(s) between {date1} and {date2}.")
    
   except ValueError as e:
    
    print("Error:", e)

