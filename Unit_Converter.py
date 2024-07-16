from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Unit Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Dropdown lists for unit conversion -> FROM
combo_1 = ttk.Combobox(state="readonly")
combo_1.grid(column=0, row=0)

# Conversion Arrow
label_convertTo = Label(text="➡")
label_convertTo.grid(column=1, row=0)

# Dropdown lists for unit conversion -> TO
combo_2 = ttk.Combobox(state="readonly")
combo_2.grid(column=2, row=0)

# Entry for number
input_data = Entry(width=15)
input_data.grid(column=0, row=1)

# Equal sign
label_doubleArrow = Label(text="🟰")
label_doubleArrow.grid(column=1, row=1)

# Label for converted data
label_convertedDataText = Label()
label_convertedDataText.grid(column=2, row=1)

# Conversion function
def button_clicked():
    try:
        toConvert = float(input_data.get())
        from_unit = combo_1.get()
        to_unit = combo_2.get()

        conversion_factors = {
            ("Mile", "km"): 1.60934,
            ("km", "Mile"): 1 / 1.60934,
            ("km", "m"): 1000,
            ("m", "km"): 1 / 1000,
            ("m", "cm"): 100,
            ("cm", "m"): 1 / 100,
            ("cm", "mm"): 10,
            ("mm", "cm"): 1 / 10,
            ("m", "dm"): 10,
            ("dm", "m"): 1 / 10,
            ("dm", "cm"): 10,
            ("cm", "dm"): 1 / 10,
            ("dm", "mm"): 100,
            ("mm", "dm"): 1 / 100,
            ("km", "cm"): 100000,
            ("cm", "km"): 1 / 100000,
            ("Mile", "m"): 1609.34,
            ("m", "Mile"): 1 / 1609.34,
            ("Mile", "cm"): 160934,
            ("cm", "Mile"): 1 / 160934,
            ("Mile", "dm"): 16093.4,
            ("dm", "Mile"): 1 / 16093.4,
            ("ft", "m"): 0.3048,
            ("m", "ft"): 1 / 0.3048,
            ("ft", "cm"): 30.48,
            ("cm", "ft"): 1 / 30.48,
            ("ft", "dm"): 3.048,
            ("dm", "ft"): 1 / 3.048,
            ("Mile", "ft"): 5280,
            ("ft", "Mile"): 1 / 5280,
            ("Yard", "ft"): 3,
            ("ft", "Yard"): 1 / 3,
            ("Mile", "Yard"): 1760,
            ("Yard", "Mile"): 1 / 1760,
            ("Yard", "m"): 0.9144,
            ("m", "Yard"): 1 / 0.9144,
            ("ft", "in"): 12,
            ("in", "ft"): 1 / 12,
            ("Yard", "in"): 36,
            ("in", "Yard"): 1 / 36,
            ("m", "in"): 39.3701,
            ("in", "m"): 1 / 39.3701,
            ("kg", "g"): 1000,
            ("g", "kg"): 1 / 1000,
            ("lb", "kg"): 0.453592,
            ("kg", "lb"): 1 / 0.453592,
            ("lb", "g"): 453.592,
            ("g", "lb"): 1 / 453.592,
            ("oz", "g"): 28.3495,
            ("g", "oz"): 1 / 28.3495,
            ("oz", "kg"): 0.0283495,
            ("kg", "oz"): 1 / 0.0283495,
            ("oz", "lb"): 0.0625,
            ("lb", "oz"): 1 / 0.0625,
            ("tonne", "kg"): 1000,
            ("kg", "tonne"): 1 / 1000,
            ("lb", "tonne"): 0.000453592,
            ("tonne", "lb"): 1 / 0.000453592,
            ("tonne", "Imperial ton"): 0.984207,
            ("Imperial ton", "tonne"): 1/ 0.984207,
            ("Imperial ton", "lb"): 2240,
            ("lb", "Imperial ton"): 1 / 2240,
            ("Imperial ton", "oz"): 35840,
            ("oz", "Imperial ton"): 1/ 35840,
            ("tonne", "US ton"): 1.10231,
            ("US ton", "tonne"): 1 / 1.10231,
            ("US ton", "Imperial ton"): 0.892857,
            ("Imperial ton", "US ton"): 1 / 0.892857,
            ("US ton", "lb"): 2000,
            ("lb", "US ton"): 1 / 2000,
            ("US ton", "oz"): 32000,
            ("oz", "US ton"): 1 / 32000,
            ("US ton", "kg"): 907.185,
            ("kg", "US ton"): 1 / 907.185,
            ("Imperial ton", "kg"): 1016.05,
            ("kg", "Imperial ton"): 1 / 1016.05,
            ("kJ", "J"): 1000,
            ("J", "kJ"): 1 / 1000,
            ("kJ", "cal"): 239.006,
            ("cal", "kJ"): 1 / 239.006,
            ("J", "cal"): 0.239006,
            ("cal", "J"): 1 / 0.239006,
            ("kJ", "kcal"): 0.239006,
            ("kcal", "kJ"): 1 / 0.239006,
            ("kcal", "cal"): 1000,
            ("cal", "kcal"): 1 / 1000,
            ("Wh", "kJ"): 3.6,
            ("kJ", "Wh"): 1 / 3.6,
            ("kWh", "kJ"): 3600,
            ("kJ", "kWh"): 1 / 3600,
            ("kWh", "Wh"): 1000,
            ("Wh", "kWh"): 1 / 1000,
            ("kWh", "kcal"): 860.421,
            ("kcal", "kWh"): 1 / 860.421,
            ("Wh", "cal"): 860.421,
            ("cal", "Wh"): 1 / 860.421,
            ("BTU", "kJ"): 1.05506,
            ("kJ", "BTU"): 1 / 1.05506,
            ("BTU", "cal"): 252.164,
            ("cal", "BTU"): 1 / 252.164,
            ("BTU", "kcal"): 0.252164,
            ("kcal", "BTU"): 1 / 0.252164,
            ("BTU", "Wh"): 0.293071,
            ("Wh", "BTU"): 1 / 0.293071,
            ("BTU", "kWh"): 0.000293071,
            ("kWh", "BTU"): 1 / 0.000293071,
            ("BTU", "J"): 1055.06,
            ("J", "BTU"): 1 / 1055.06,
            # Add more conversions as needed
        }

        if (from_unit, to_unit) in conversion_factors:
            converted = toConvert * conversion_factors[(from_unit, to_unit)]
        elif from_unit == to_unit:
            converted = toConvert  # No conversion needed
        else:
            converted = "Invalid conversion"

    except ValueError:
        converted = "Invalid input"

    label_convertedDataText.config(text=str(converted))

# Function to set up length conversion options
def length_conversion():
    combo_1.config(values=["Mile", "km", "m", "dm", "cm", "mm", "ft", "Yard", "in"])
    combo_2.config(values=["Mile", "km", "m", "dm", "cm", "mm", "ft", "Yard", "in"])
    combo_1.current(0)
    combo_2.current(1)

# Function to set up mass conversion options
def mass_conversion():
    combo_1.config(values=["kg", "g", "lb", "oz", "tonne", "Imperial ton", "US ton"])
    combo_2.config(values=["kg", "g", "lb", "oz", "tonne", "Imperial ton", "US ton"])
    combo_1.current(0)
    combo_2.current(1)

# Function to set up energy conversion options
def energy_conversion():
    combo_1.config(values=["J", "kJ", "cal", "kcal", "Wh", "kWh", "BTU"])
    combo_2.config(values=["J", "kJ", "cal", "kcal", "Wh", "kWh", "BTU"])
    combo_1.current(0)
    combo_2.current(1)

# Buttons to select conversion type
button_length = Button(text="Length", command=length_conversion)
button_length.grid(column=0, row=3, pady=10)

button_mass = Button(text="Mass", command=mass_conversion)
button_mass.grid(column=1, row=3, pady=10)

button_mass = Button(text="Energy", command=energy_conversion)
button_mass.grid(column=2, row=3, pady=10)

# Button to trigger conversion
conversion_button = Button(text="Convert", command=button_clicked)
conversion_button.grid(column=1, row=2)

# Initialize with length conversion options
length_conversion()

window.mainloop()
