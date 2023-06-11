import datetime
import time
import subprocess

def reminder():
    while True:
        input_text = input("Enter reminder text: ")
        time_input = input("Specify reminder time (HH:MM): ")
        date_input = input("Enter the date for the reminder (DD/MM/YYYY): ")
        
        try:
            date = datetime.datetime.strptime(date_input, "%d/%m/%Y")
            hour, minute = map(int, time_input.split(":"))
            reminder_time = datetime.datetime(date.year, date.month, date.day, hour, minute)
            
            current_time = datetime.datetime.now()
            waiting_time = (reminder_time - current_time).total_seconds()
            
            if waiting_time > 0:
                time.sleep(waiting_time)
                subprocess.call(["powershell", "-c", "(New-Object Media.SoundPlayer 'C:\Windows\Media\chimes.wav').PlaySync()"])
                subprocess.call(["powershell", "-c", "(New-Object -ComObject SAPI.SpVoice).Speak('Reminder: " + input_text + "')"])
            else:
                print("Invalid time! Reminder time cannot be in the past.")
        
        except ValueError:
            print("Invalid input! Please enter the date and time in the correct format.")

reminder()

# MADE BY FALSCH