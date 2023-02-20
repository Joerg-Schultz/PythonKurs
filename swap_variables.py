first = "Back"
second = "Front"
print(first)
print(second)

# Do something weird here
temp_variable = first
first = second
second = temp_variable

print(first)  # -> should print Front
print(second)  # -> should print Back
