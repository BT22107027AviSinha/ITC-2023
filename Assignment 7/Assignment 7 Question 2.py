import tkinter as tk
import calendar

def show_calendar():
    year = int(year_entry.get())
    cal = calendar.calendar(year)
    calendar_text.delete("1.0", tk.END)
    calendar_text.insert(tk.END, cal)

# Create the main window
window = tk.Tk()
window.title("Calendar Application")

# Create the label and entry field
year_label = tk.Label(window, text="Enter the Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Create the show button
show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

# Create the text widget to display the calendar
calendar_text = tk.Text(window, height=100, width=100)
calendar_text.pack()

# Start the main event loop
window.mainloop()
