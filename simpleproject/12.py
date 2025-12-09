import yaml

with open("deployment.yaml") as f:
    data = yaml.safe_load(f)

print(data["spec"]["replicas"])