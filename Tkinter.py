from tkinter import *
import psutil
from hurry.filesize import size


def get_disk():
    total, used, free , percent = psutil.disk_usage('/')
    total_space['text'] = size(total)
    used_space['text'] = size(used)
    free_space['text'] = size(free)
    percentage_space['text'] = str(percent) + '%'
    

def battery_info():
    battery_details = psutil.sensors_battery()
    percentage_battery['text'] =  str(battery_details[0]) + '%'
    if int(battery_details[1] ) <= -2:
        seconds_left_battery['text'] = 'Not Aplicable'
    else:
        seconds_left_battery['text'] =  str(battery_details[1]) + ' '+  'seconds'

    if battery_details[2] == 'False':
        power_plugged_battery['text'] = 'No'
    else:
        power_plugged_battery['text'] = 'Yes'


def main():
    get_disk()
    battery_info()

app = Tk()


Disk_label = Label(app, text='Disk Information',font=('bold',22),pady=20)
Disk_label.grid(row=0,column=0,sticky=W)
#disk_entry = Entry(app,textvariable=Disk_space)
#disk_entry.grid(row=0,column=1)

#Disk information
total_space_label = Label(app, text='Total Space',font=('bold',14),pady=10)
total_space_label.grid(row=1,column=0)

total_space = Label(app,text='0GB',font=(14))
total_space.grid(row=1, column=1)

used_space_label = Label(app, text='Used Space',font=('bold',14),pady=10)
used_space_label.grid(row=2,column=0)

used_space = Label(app,text='0GB',font=(14))
used_space.grid(row=2, column=1)

free_space_label = Label(app, text='Free Space',font=('bold',14),pady=10)
free_space_label.grid(row=3,column=0)

free_space = Label(app,text='0GB',font=(14))
free_space.grid(row=3, column=1)

percentage_space_label = Label(app, text='Percentage Space',font=('bold',14),pady=10)
percentage_space_label.grid(row=4,column=0)

percentage_space = Label(app,text='0%',font=(14))
percentage_space.grid(row=4, column=1)

#Battery Information
Battery_label = Label(app, text='Battery Information',font=('bold',22),pady=20)
Battery_label.grid(row=0,column=2,sticky=E)

percentage_battery_label = Label(app, text='Percentage of the Battery',font=('bold',14),pady=10)
percentage_battery_label.grid(row=1,column=2)

percentage_battery = Label(app,text='0%',font=(14))
percentage_battery.grid(row=1, column=3)

seconds_left_battery_label = Label(app, text='Seconds Left',font=('bold',14),pady=10)
seconds_left_battery_label.grid(row=2,column=2)

seconds_left_battery = Label(app,text='0',font=(14))
seconds_left_battery.grid(row=2, column=3)

power_plugged_label = Label(app, text='Power Plugged',font=('bold',14),pady=10)
power_plugged_label.grid(row=3,column=2)

power_plugged_battery = Label(app,text='-',font=(14))
power_plugged_battery.grid(row=3, column=3)



Run_button = Button(app,text='Run',width=12,command=main)
Run_button.grid(row=0,column=20,pady=20)

app.title('Prueba')
app.geometry('950x500')



app.mainloop()