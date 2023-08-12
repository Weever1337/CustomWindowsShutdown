import re
from datetime import timedelta
import subprocess

time_units = {"d": "days", "h": "hours", "m": "minutes", "s": "seconds"}

def parse_duration_input(duration_input):
    duration_regex = r"(\d+)([hms])"
    matches = re.findall(duration_regex, duration_input)

    duration_delta = timedelta()
    for value, unit in matches:
        if unit in time_units:
            time_unit = time_units[unit]
            duration_delta += timedelta(**{time_unit: int(value)})
    
    return duration_delta.total_seconds()

def main():
    duration_input = input("How long is it? (Example: 1h1m1s) Choice: ")
    total_seconds = int(parse_duration_input(duration_input))

    if total_seconds <= 0:
        print("Invalid duration. Please provide a positive duration.")
        return
    
    choice = int(input("Reboot: 1 | Turn off: 2. Choice: "))
    if choice == 1:
        subprocess.run(f"shutdown /r /t {total_seconds}")
        print(f"Computer will reboot in {total_seconds} seconds.")
    elif choice == 2:
        subprocess.run(f"shutdown /s /t {total_seconds}")
        print(f"Computer will turn off in {total_seconds} seconds ({duration_input}).")
    else:
        print("Invalid choice. Restart the script and choose 1 or 2.")
    input("Press ENTER to exit...")

if __name__ == "__main__":
    main()
