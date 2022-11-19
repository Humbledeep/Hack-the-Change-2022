import tkinter as tk

# Create the window
window = tk.Tk()

# Create the entry
entry = tk.Entry(window)
entry.pack()

# Create the listbox
listbox = tk.Listbox(window)
listbox.pack()

# Create the scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Add some items to the listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")
listbox.insert(tk.END, "Item 4")

# Run the mainloop
window.mainloop()    