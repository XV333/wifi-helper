import subprocess

def run_script(script_number):
    if script_number == 1:
        subprocess.Popen(["python", "cutnet.py"])
    elif script_number == 2:
        subprocess.Popen(["python", "ip-mac"])
    elif script_number == 3:
        subprocess.Popen(["python", "sc-po"])
    else:
        print("Script number is invalid.")

script_number = int(input("Enter the script number: "))
run_script(script_number)
