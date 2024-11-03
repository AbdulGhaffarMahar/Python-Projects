# import tkinter as tk
# from time import strftime
# root = tk.Tk()
# root.title("Digital Clock")
# def time ():
#     string = strftime('%H:%M:%S%P \n %D')
#     label.config(text=string)
#     label.after(1000,time)

#  label = tk.Label(root,=('calibri',50,'bold'),background='yellow',foreground='black')   
# label.pack(anchor='center')

# time()

# root.mainloop()


import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Define the time function to update the clock every second
def time():
    string = strftime('%H:%M:%S %p \n %D')  # Corrected time format
    label.config(text=string)
    label.after(1000, time)  # Update the label every 1 second (1000 ms)

# Create the label widget with proper font and color settings
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')   
label.pack(anchor='center')

# Start the clock
time()

# Run the tkinter event loop
root.mainloop()
