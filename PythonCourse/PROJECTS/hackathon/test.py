import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry("700x700")  # set the size of the window to 500x500


class GraphApp:

  def __init__(self, master):
    self.master = master
    master.title("Graph App")

    # Create widgets
    self.value_label = tk.Label(master, text="Enter your blood sugar level:")
    self.value_entry = tk.Entry(master)
    self.category_label = tk.Label(master, text="Enter date:")
    self.category_entry = tk.Entry(master)
    self.submit_button = tk.Button(master,
                                   text="Submit",
                                   command=self.plot_point)
    self.canvas = tk.Canvas(master, width=700, height=700)

    # Grid layout
    self.value_label.grid(row=0, column=0, padx=10, pady=10)
    self.value_entry.grid(row=0, column=1, padx=10, pady=10)
    self.category_label.grid(row=1, column=0, padx=10, pady=10)
    self.category_entry.grid(row=1, column=1, padx=10, pady=10)
    self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    self.canvas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Initialize data lists
    self.x_data = []
    self.y_data = []

  def plot_point(self):
    # Get data from entry widgets
    value = float(self.value_entry.get())
    category = self.category_entry.get()

    # Add data to lists
    self.x_data.append(category)
    self.y_data.append(value)

    # Clear canvas and plot data
    self.canvas.delete("all")
    plt.plot(self.x_data, self.y_data)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("temp.png")

    # Load image onto canvas
    self.img = tk.PhotoImage(file="temp.png")
    self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)


app = GraphApp(root)
root.mainloop()
