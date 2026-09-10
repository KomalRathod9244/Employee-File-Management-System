import os
from datetime import date

FOLDER = 'Employee'
today_date = str(date.today())


class IdAlreadyExist(Exception):
   pass

try:
    # Create a folder to store the employee files
    os.makedirs(FOLDER, exist_ok=True)

    # taking input from user
    emp_id = input("Enter employee id : ")
    name = input("Enter employee name : ")
    if "_" in name:
       name.replace("_"," ")
    salary = input("Enter employee salary : ")

    # Validation of user input

    # if nonee of input is empty
    if (not emp_id) or (not name) or (not salary):
     raise ValueError("All details required")

    try:
       emp_id = int(emp_id)
    except ValueError:
       raise ValueError("Id must me a digit")

    try:
       salary = float(salary)
    except ValueError:
       raise ValueError("Employee Salary must be digits")

    if salary <= 0:
       raise ValueError("Salary must be greater that 0")

    file_name = name + "_" + str(emp_id) + "_" + today_date

    # check if file can be created 

    for filename in os.listdir(FOLDER):

      # we will only consider .txt file of employes only
      if not filename.endswith('.txt'):
         continue

      parts = filename.split("_")

      if len(parts) != 3:
         continue
      else:
         existing_id = parts[1]

      # check if already exist
      if existing_id == str(emp_id):
         raise IdAlreadyExist(f"[Error] Employee id {emp_id} already exist")

    # if id doesn't exist , create file
    
    file_path = os.path.join(FOLDER, file_name +'.txt')
    with open(file_path, 'w', encoding='UTF-8') as emp_file:
        emp_file.write(f"Employee_id : {emp_id}\nEmployee_name : {name}\nEmployee_salary : {salary}")
        print("Your file has successfully created")


except IdAlreadyExist as e:
   print(e)

except ValueError as e:
   print(e)

except Exception:
   print("Unexpected error occur")
    

        


        
