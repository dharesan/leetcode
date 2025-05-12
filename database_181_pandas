import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.fillna(0)
    employee.head()

    employeeList = []

    for index, row in employee.iterrows(): 
        if row['managerId'] != 0: 
            empSal = row ['salary']
            empName = row ['name']
            managerIdVal = row['managerId']
        
            managerRow = employee[employee['id'] == managerIdVal]
            print(managerRow)
            managerSal = managerRow ['salary'].values

            print("empSal is", empSal)
            print("managerSal is", managerSal)

            if managerSal: 
                if empSal > managerSal[0]: 
                    employeeList.append(empName)
            


    result = pd.DataFrame({"Employee":employeeList})
        
    return result


