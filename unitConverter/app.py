import streamlit as st

st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔁")
st.title("🔁 Ultimate Unit Converter")
st.markdown("Convert length, weight, and temperature easily!")

# Category selection
category = st.selectbox("Select category", ["Length", "Weight", "Temperature"])

# Define unit options for each category
units = {
    "Length": ["Kilometers", "Miles", "Meters", "Feet"],
    "Weight": ["Kilograms", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", format="%.4f")

def convert(category, from_unit, to_unit, value):
    if category == "Length":
        if from_unit == "Kilometers" and to_unit == "Miles":
            return value * 0.621371
        if from_unit == "Miles" and to_unit == "Kilometers":
            return value / 0.621371
        if from_unit == "Meters" and to_unit == "Feet":
            return value * 3.28084
        if from_unit == "Feet" and to_unit == "Meters":
            return value / 3.28084
        if from_unit == to_unit:
            return value

    elif category == "Weight":
        if from_unit == "Kilograms" and to_unit == "Pounds":
            return value * 2.20462
        if from_unit == "Pounds" and to_unit == "Kilograms":
            return value / 2.20462
        if from_unit == to_unit:
            return value

    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        if from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        if from_unit == to_unit:
            return value

    return "Invalid conversion"

if st.button("Convert"):
    result = convert(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
