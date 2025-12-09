containers = data["spec"]["template"]["spec"]["containers"]

for c in containers:
    print(c["image"])