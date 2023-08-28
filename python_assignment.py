# Employee data
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary": 44000},
]

def print_employee_data(data):
    print("{:<12} {:<10} {:<4} {:<10}".format("Employee ID", "Name", "Age", "Salary"))
    print("="*40)
    for employee in data:
        print("{:<12} {:<10} {:<4} {:<10}".format(
            employee["Employee ID"], employee["Name"], employee["Age"], employee["Salary"])
        )

def sort_employee_data(data, key):
    return sorted(data, key=lambda x: x[key])

if __name__ == "__main__":
    print("Sorting Options:")
    print("1. Age\n2. Name\n3. Salary")
    sorting_option = int(input("Choose a sorting parameter (1/2/3): "))

    if sorting_option == 1:
        sorted_data = sort_employee_data(employee_data, "Age")
    elif sorting_option == 2:
        sorted_data = sort_employee_data(employee_data, "Name")
    elif sorting_option == 3:
        sorted_data = sort_employee_data(employee_data, "Salary")
    else:
        print("Invalid sorting option selected")
        exit()

    print("\nSorted Employee Data:")
    print_employee_data(sorted_data)
