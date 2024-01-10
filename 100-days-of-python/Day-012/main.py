from pantry import pantry
# dictionary 
emp_db = {
    "fe01": "Mark Moody",
    "fe02": "Dominic Cork",
    "fe03": "Jhon Doe"
}
print(emp_db["fe01"])
print(emp_db.get("fe02"))

# iterating dictionary
# cannot get the value directly
for key in emp_db:
    print(emp_db.get(key))

print()

# this can be a little less efficient
# there is an extra memory consumption
for key, emp in emp_db.items():
    print("{}: {}".format(key, emp))


# Working with imported data
for item in pantry:
    print(item)
