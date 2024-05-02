import tkinter as tk
from tkinter import ttk, messagebox
import CourseProject.backend as backend

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = backend.calculate_bmi(weight, height)
        bmi_label.config(text="Your BMI: {:.2f}".format(bmi))
        bmi_category_label.config(text="You are {}".format(backend.interpret_bmi(bmi)))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

def generate_diet_plan_button_clicked():
    weight_goal = weight_goal_var.get()
    diet_plan_text.delete("1.0", tk.END)
    diet_plan = backend.generate_diet_plan(weight_goal)
    diet_plan_text.insert(tk.END, diet_plan)

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Styling
style = ttk.Style(root)
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("TButton", background="#007bff", foreground="black", font=("Arial", 12))

# Create and pack frame
frame = ttk.Frame(root)
frame.pack(padx=20, pady=10)

# Create widgets
weight_label = ttk.Label(frame, text="Weight (lbs):")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
weight_entry = ttk.Entry(frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = ttk.Label(frame, text="Height (inches):")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
height_entry = ttk.Entry(frame)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

bmi_label = ttk.Label(frame, text="")
bmi_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

bmi_category_label = ttk.Label(frame, text="")
bmi_category_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

weight_goal_label = ttk.Label(frame, text="Weight Goal:")
weight_goal_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
weight_goal_var = tk.StringVar(value="Lose")
weight_goal_combobox = ttk.Combobox(frame, textvariable=weight_goal_var, values=["Lose", "Maintain", "Gain"])
weight_goal_combobox.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

generate_diet_plan_button = ttk.Button(frame, text="Generate Diet Plan", command=generate_diet_plan_button_clicked)
generate_diet_plan_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create and pack result frame
result_frame = ttk.Frame(root)
result_frame.pack(padx=20, pady=10)

diet_plan_label = ttk.Label(result_frame, text="Diet Plan:")
diet_plan_label.pack(side=tk.TOP, padx=5, pady=5)

diet_plan_text = tk.Text(result_frame, wrap=tk.WORD)  # Remove width specification
diet_plan_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


# Run the main loop
root.mainloop()
