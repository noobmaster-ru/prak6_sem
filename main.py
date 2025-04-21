import subprocess
begin = 1.0
for i in range(1,20):

    constants = {
        "T0": 0.0,
        "TN": 1.0,
        "N0": 1000,
        "EPS": 0.01,
        "STEP": "(TN-T0)/N0",
        "D": begin + i*0.05,
        "M": 1.0
    }

    with open("constants.h", "w") as f:
        f.write("// Автоматически сгенерировано из Python\n")
        f.write("#ifndef CONSTANTS_H\n#define CONSTANTS_H\n\n")
        for name, value in constants.items():
            f.write(f"#define {name} {value}\n")
        f.write("\n#endif // CONSTANTS_H\n")

    # Или запуск с конкретной целью, например:
    subprocess.run(["make", "plot"])