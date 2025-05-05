import subprocess


constants = {
    "T0": 0.0,
    "TN": 200.0,
    "N0": 400, 
    "EPS": 0.5,
    "STEP": "(TN-T0)/N0",
    "D": 1.15,
    "M": 1.01,
    "sign_1": -1,
    "sign_2": 1,
    "FILENAME": f'"data.csv"'
}

# Write constants to constants.h
with open(f"constants.h", "w") as f:
    f.write("// Auto-generative from main.py\n")
    f.write("#ifndef CONSTANTS_H\n#define CONSTANTS_H\n\n")
    for name, value in constants.items():
        f.write(f"#define {name} {value}\n")
    f.write("\n#endif // CONSTANTS_H\n")

subprocess.run(["make", "all"])
# subprocess.run(["make", "values"])