with open("app.log") as f:
    for line in f:
        if "ERROR" in line:
            print(line)