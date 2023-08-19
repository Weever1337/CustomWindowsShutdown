import re
from datetime import timedelta
import subprocess
import tkinter

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
    duration_input = owner.get()
    total_seconds = int(parse_duration_input(duration_input))
    
    choice = int(lang.get())
    if choice == 1:
        subprocess.run(f"shutdown /r /t {total_seconds}")
    elif choice == 2:
        subprocess.run(f"shutdown /s /t {total_seconds}")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Custom Windows Shutdown")
    root.geometry("370x370")
    label = tkinter.Label(root, text="\n\nPlease complete all fields below!\n\nReboot: 1, Turn off: 2\n")
    labol = tkinter.Label(root, text="How long is it? (Example: 1h1m1s):")
    owner = tkinter.Entry(root)
    restop = tkinter.Label(root, text="Reboot or turn off (1/2):")
    lang = tkinter.Entry(root)
    label3 = tkinter.Label(root)
    tombolrun = tkinter.Button(root, text="Run!", command= lambda: main())
    label4 = tkinter.Label(root, text="\n\nMade with ♥ by weever")

    label.pack()
    labol.pack()
    owner.pack()
    restop.pack()
    lang.pack()
    label3.pack()
    tombolrun.pack()
    label4.pack()
    root.mainloop() #💀💀💀 this code is trashhh ☠️☠️☠️