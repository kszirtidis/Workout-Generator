import tkinter as tk
from tkinter import ttk, messagebox
import backend

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = backend.calculate_bmi(weight, height)
        bmi_label.config(text="Your BMI: {:.2f}".format(bmi))
        bmi_category_label.config(text="You are {}".format(backend.interpret_bmi(bmi)))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

def generate_diet_plan_action():
    # Check if there's already a diet plan generated
    if diet_plan_text.get("1.0", tk.END).strip():
        # Display a confirmation dialog
        confirm = messagebox.askyesno("Warning", "Generating a new diet plan will delete the old plan. Do you want to continue?", icon='warning')
        if not confirm:
            return  # Cancel generation if user chooses No

    # Clear the old diet plan
    diet_plan_text.delete("1.0", tk.END)
    
    # Generate the new diet plan
    weight_goal = weight_goal_var.get()
    diet_plan = backend.generate_diet_plan(weight_goal)
    diet_plan_text.insert(tk.END, diet_plan)

    # Add the generated diet plan to the history
    diet_plan_history.insert(0, diet_plan)
    # Keep only the last three diet plans
    if len(diet_plan_history) > 3:
        diet_plan_history.pop()

def generate_diet_plan_button_clicked(event=None):
    generate_diet_plan_action()

def show_updates_and_fixes():
    updates_window = tk.Toplevel(root)
    updates_window.title("Updates/Fixes")
    updates_text = tk.Text(updates_window, wrap=tk.WORD)
    updates_text.insert(tk.END, """
    Version 1.0:
    - Initial release
    
    Version 1.1:
    - Added BMI calculator
    - Added diet plan generator
    - Added confirmation dialog for generating new diet plan
    """)
    updates_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def show_tutorial():
    tutorial_window = tk.Toplevel(root)
    tutorial_window.title("Tutorial")
    tutorial_text = tk.Text(tutorial_window, wrap=tk.WORD)
    tutorial_text.insert(tk.END, """
    How to Use the App:
    
    1. Enter your weight in pounds and height in inches.
    2. Click 'Calculate BMI' to see your BMI and category.
    3. Select your weight goal (Lose, Maintain, or Gain).
    4. Click 'Generate Diet Plan' to get a personalized diet plan.
    """)
    tutorial_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def show_calculation_info():
    calculation_window = tk.Toplevel(root)
    calculation_window.title("Calculation Information")
    calculation_text = tk.Text(calculation_window, wrap=tk.WORD)
    calculation_text.insert(tk.END, """
    BMI Calculation:
    BMI is calculated using the formula:
    BMI = weight(kg) / height(m)^2

    Diet Plan Generation:
    Diet plans are generated based on the user's weight goal (lose, maintain, or gain). 
    The algorithm takes into account the user's BMI category and recommends a balanced diet plan accordingly.
    """)
    calculation_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create main window
root = tk.Tk()
root.title("Diet Maker")

# Show updates and fixes popup
root.after(100, show_updates_and_fixes)

# Create front page frame
front_frame = ttk.Frame(root, padding="20")
front_frame.pack(fill=tk.BOTH, expand=True)

# Widgets for front page
app_name_label = ttk.Label(front_frame, text="Diet Maker", font=("Arial", 24, "bold"))
app_name_label.pack(pady=20)

message_label = ttk.Label(front_frame, text="This app will generate a diet for you based on your BMI and body goals!")
message_label.pack(pady=10)

# Create and pack frame for BMI calculator
bmi_frame = ttk.Frame(root, padding="20")
bmi_frame.pack(fill=tk.BOTH, expand=True)

# Create widgets for BMI calculator
weight_label = ttk.Label(bmi_frame, text="Weight (lbs):")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
weight_entry = ttk.Entry(bmi_frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = ttk.Label(bmi_frame, text="Height (inches):")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
height_entry = ttk.Entry(bmi_frame)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = ttk.Button(bmi_frame, text="Calculate BMI", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

bmi_label = ttk.Label(bmi_frame, text="")
bmi_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

bmi_category_label = ttk.Label(bmi_frame, text="")
bmi_category_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

weight_goal_label = ttk.Label(bmi_frame, text="Weight Goal:")
weight_goal_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
weight_goal_var = tk.StringVar(value="Lose")
weight_goal_combobox = ttk.Combobox(bmi_frame, textvariable=weight_goal_var, values=["Lose", "Maintain", "Gain"])
weight_goal_combobox.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

generate_diet_plan_button = ttk.Button(bmi_frame, text="Generate Diet Plan", command=generate_diet_plan_button_clicked)
generate_diet_plan_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Bind Enter key to generate_diet_plan_button_clicked function
root.bind("<Return>", generate_diet_plan_button_clicked)

# Create and pack result frame
result_frame = ttk.Frame(root)
result_frame.pack(padx=20, pady=10)

diet_plan_label = ttk.Label(result_frame, text="Diet Plan:")
diet_plan_label.pack(side=tk.TOP, padx=5, pady=5)

diet_plan_text = tk.Text(result_frame, wrap=tk.WORD)  # Remove width specification
diet_plan_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Create and pack frame for diet plan history
history_frame = ttk.Frame(root, padding="20")
history_frame.pack(fill=tk.BOTH, expand=True)

history_label = ttk.Label(history_frame, text="Last 3 Diet Plans:")
history_label.pack(side=tk.TOP, padx=5, pady=5)

diet_plan_history = tk.Listbox(history_frame, height=3)
diet_plan_history.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Create menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Tutorial", command=show_tutorial)
help_menu.add_command(label="Calculation Info", command=show_calculation_info)

# Run the main loop
root.mainloop()
