from datetime import datetime
import time
from openpyxl import load_workbook
import pyttsx3
from plyer import notification


if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please drink water now!!",
             
            message  =  "You should drink 2.5 ltr water in a day.",
            app_icon =  "C:\\Users\\win10\\OneDrive\\Desktop\\Python\\Python projects\\Reminder\\Icon.ico",
            timeout=10   
        )
        time.sleep(60*60)    

