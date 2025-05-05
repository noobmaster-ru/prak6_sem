import re
# Road to file constants.h
header_file = f"constants.h"
output_file = f"constants.py"

# Redular equation fot search #define
define_pattern = re.compile(r"#define\s+(\w+)\s+(.+)")

# Dictionary for store constants
constants = {}

# Reading file constants.h
with open(header_file, 'r') as file:
    for line in file:
        match = define_pattern.match(line)
        if match:
            key, value = match.groups()
            constants[key] = value

# Generate file constants.py
with open(output_file, 'w') as file:
    file.write("# This file is auto-generated from constants/constants.h\n\n")
    for key, value in constants.items():
        file.write(f"{key} = {value}\n")

print(f"Constants from constants/constants.h save to {output_file}")