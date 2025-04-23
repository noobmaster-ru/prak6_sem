import subprocess


for i in range(10):
    constants = {
        "T0": 0.0,
        "TN": 1.0,
        "N0": 1000,
        "EPS": 0.01,
        "STEP": "(TN-T0)/N0",
        "D": 1.5,
        "M": 1.0,
        "FILENAME": f'"datas/data{i}.csv"'
    }

    # Write constants to constants.h
    with open(f"constants/constants{i}.h", "w") as f:
        f.write("// Auto-generative from main.py\n")
        f.write("#ifndef CONSTANTS_H\n#define CONSTANTS_H\n\n")
        for name, value in constants.items():
            f.write(f"#define {name} {value}\n")
        f.write("\n#endif // CONSTANTS_H\n")

    # subprocess.run(["make", "compute"])
    subprocess.run(["make", "values"])