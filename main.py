import subprocess

constants = {
    "T0": 0.0,
    "TN": 1.0,
    "N0": 100,
    "EPS": 0.01,
    "STEP": "(TN-T0)/N0",
    "D": 1.0,
    "M": 1.0,
    "NUM_TRAJECTORY": 1
}

# записываем constants -> constants.h
with open("constants.h", "w") as f:
    f.write("// Автоматически сгенерировано из main.py\n")
    f.write("#ifndef CONSTANTS_H\n#define CONSTANTS_H\n\n")
    for name, value in constants.items():
        f.write(f"#define {name} {value}\n")
    f.write("\n#endif // CONSTANTS_H\n")

subprocess.run(["make", "compute"])