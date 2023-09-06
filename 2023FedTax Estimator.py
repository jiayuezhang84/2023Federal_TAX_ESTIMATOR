import tkinter as tk
from tkinter import ttk

# 2023 bracket rate per IRS 
tax_brackets = {
    "Single": [(0, 11000), (11000, 44725), (44725, 95375), (95375, 182100), (182100, 231250),(231250,578125),(578125,999999999999999)],
    "Head of Household": [(0, 15700), (15700, 59850), (59851, 95350), (95351, 182100), (182101, 231250),(230251,578100),(578101,999999999999999)],
    "Married Filing Jointly": [(0, 22000), (22001, 89450), (89451, 190750), (190751, 364200), (364201, 462500),(462501,693750),(693751,999999999999999)],
    "Married Filing Separately": [(0, 11000), (11000, 44725), (44725, 95375), (95375, 182100), (182100, 231250),(231250,346875),(346875,999999999999999)]
}

tax_rates = [0.1, 0.12, 0.22, 0.24, 0.32,0.35,0.37]

# calculate tax based on filing status and income
def calculate_tax():
    total_income = 0
    for income_entry, label in income_entries:
        income = float(income_entry.get())
        total_income += income

    filing_status = filing_status_var.get()
    selected_brackets = tax_brackets[filing_status]

    tax = 0
    for bracket in selected_brackets:
        if total_income > bracket[1]:
            tax += int((bracket[1] - bracket[0] + 1) * tax_rates[selected_brackets.index(bracket)])
        else:
            tax += int((total_income - bracket[0] + 1) * tax_rates[selected_brackets.index(bracket)])
            break

    result_label.config(text=f"Estimated Tax: ${tax:.2f}")

# Function to switch to the income input page
def switch_to_income_input():
    filing_status_frame.pack_forget()
    input_income_frame.pack()

# Create the main window
root = tk.Tk()
root.title("Tax Estimator")

# Create a frame for the filing status selection page
filing_status_frame = ttk.Frame(root)

filing_status_label = ttk.Label(filing_status_frame, text="Select Filing Status:")
filing_status_label.pack(pady=10)

filing_status_var = tk.StringVar()
filing_status_var.set("Single")

filing_status_combobox = ttk.Combobox(filing_status_frame, textvariable=filing_status_var, values=["Single", "Head of Household", "Married Filing Jointly","Married Filing Separately"])
filing_status_combobox.pack(pady=5)

continue_button = ttk.Button(filing_status_frame, text="Continue", command=switch_to_income_input)
continue_button.pack(pady=10)

filing_status_frame.pack()  # Display the filing status frame initially

# Create a frame for the income input page
input_income_frame = ttk.Frame(root)

note_label1 = ttk.Label(filing_status_frame, text="Please be aware that tax laws and regulations can change, and the information provided may not reflect the most current legal standards or interpretations. Always seek professional advice for accurate and up-to-date guidance on tax-related matters.")
note_label1.config(wraplength=200, font=("Arial", 10, "italic"))
note_label1.pack()

income_entries = []

for income_type in ["W2", "Others, e.g.1099's"]:
    income_label = ttk.Label(input_income_frame, text=f"Income from {income_type}:")
    income_label.pack(pady=5)
    
    income_entry = ttk.Entry(input_income_frame)
    income_entry.pack(pady=5)
    
    income_entries.append((income_entry, income_type))

calculate_button = ttk.Button(input_income_frame, text="Calculate Tax", command=calculate_tax)
calculate_button.pack(pady=10)

note_label2 = ttk.Label(filing_status_frame, text="NOTE: assuming Standard Deduction Is Applied. AMT and state taxes are not inculded.")
note_label2.config(wraplength=200, font=("Arial", 10, "italic"))
note_label2.pack()


result_frame = ttk.Frame(root)
result_frame.pack(pady=20)


result_label = ttk.Label(result_frame, text="", font=("Helvetica", 16))
result_label.pack()


root.mainloop()
