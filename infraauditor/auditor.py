import os
import subprocess
import yaml
import json
from datetime import datetime

report_data={}

def get_system_info():
    cmd=["uname", "-a"]
    output=subprocess.check_output(cmd).decode()
    report_data["system_info"]=output


def get_usage():
    disk=subprocess.check_output(["df","-h"]).decode()
    mem=subprocess.check_output(["free","-h"]).decode()
    report_data["disk_usage"]=disk
    report_data["memory_usage"]=mem

def ping_servers():
    results = {}
    with open("servers.txt") as f:
        servers = f.read().splitlines()

    for s in servers:
        try:
            subprocess.check_output({"ping","-c","1",s})
             results[s]= "UP"
        except:
            results[s]="DOWN"
    
    report_data["server_status"] = results

def analyze_logs():
    count=0
    with open("logs/app.log") as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    report_data["log_errors"] = count


def extract_images():
    with open("deployment.yaml") as f:
        data=yaml.safe_load(f)
    
    containers = data["spec"]["template"]["spec"]["containers"]
    images= [c["image"] for c ]