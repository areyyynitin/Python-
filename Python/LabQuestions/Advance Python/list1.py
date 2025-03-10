# You have a list of employee records, and you need to create a new list that contains

# the names of employees who work in the 'Sales' department, all in uppercase



employees = [
{"name": "John Doe", "department": "Sales"},
{"name": "Jane Smith", "department": "Marketing"},
{"name": "Emily Johnson", "department": "Sales"},
{"name": "Michael Brown", "department": "HR"}
]

# print(employees)


for employee in employees:
    if employee["department"] == "Sales":
        print(employee["name"].upper())