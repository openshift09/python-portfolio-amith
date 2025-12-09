import yaml
import subprocess
import json

out = subprocess.check_output(["echo", "hello"])
print(out.decode())
