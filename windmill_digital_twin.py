# Save this file as: windmill_digital_twin.py

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="🌪️ Windmill Digital Twin Dashboard", layout="centered")
st.title("🌪️ Windmill Digital Twin Dashboard")

st.markdown("""
This model simulates real-time performance, diagnostics, and efficiency tracking for a basic windmill setup.
Use the controls below to simulate windmill operation.
""")

# --- Input Parameters ---
wind_speed = st.slider("🌬️ Wind Speed (m/s)", 0.0, 25.0, 10.0, 0.5)
blade_angle = st.slider("🌀 Blade Angle (degrees)", 0.0, 90.0, 30.0, 1.0)
generator_efficiency = st.slider("⚙️ Generator Efficiency (%)", 50, 100, 85, 1)
rotor_rpm = st.slider("🔄 Rotor RPM", 0, 300, 150, 5)
runtime_hours = st.number_input("⏱️ Runtime (hours)", min_value=0.0, step=1.0)
temperature = st.number_input("🌡️ Generator Temperature (°C)", min_value=0.0, step=1.0)

# --- Constants & Calculations ---
air_density = 1.225  # kg/m^3 (at sea level)
rotor_radius = 10    # meters (example)
area = np.pi * rotor_radius**2

power_output = 0.5 * air_density * area * (wind_speed**3) * (generator_efficiency / 100) * np.cos(np.radians(blade_angle))
efficiency_rating = (power_output / (wind_speed * rotor_rpm + 1)) * 10

# --- Status Display ---
st.subheader("📊 Windmill Performance Summary")
st.success(f"Estimated Power Output: {power_output/1000:.2f} kW")
st.info(f"Efficiency Rating: {efficiency_rating:.2f} (arbitrary scale)")

# --- Warnings ---
if wind_speed < 3:
    st.warning("⚠️ Wind speed too low for efficient operation!")
if wind_speed > 20:
    st.error("🛑 High wind speed! Risk of turbine failure.")
if temperature > 80:
    st.error("🔥 Generator overheating! Immediate maintenance needed.")
if rotor_rpm > 250:
    st.warning("⚠️ Rotor RPM approaching critical speed limit!")

# --- Graphs ---
st.subheader("📈 Simulation Graphs")

# Graph 1: Power output vs Wind speed
wind_range = np.linspace(0, 25, 50)
power_range = 0.5 * air_density * area * (wind_range**3) * (generator_efficiency / 100) * np.cos(np.radians(blade_angle))

fig1, ax1 = plt.subplots()
ax1.plot(wind_range, power_range / 1000)
ax1.set_title("Power Output vs Wind Speed")
ax1.set_xlabel("Wind Speed (m/s)")
ax1.set_ylabel("Power Output (kW)")
ax1.grid(True)
st.pyplot(fig1)

# Graph 2: Efficiency rating vs Blade angle
angles = np.linspace(0, 90, 50)
efficiency_curve = (0.5 * air_density * area * (wind_speed**3) * (generator_efficiency / 100) * np.cos(np.radians(angles))) / (wind_speed * rotor_rpm + 1) * 10

fig2, ax2 = plt.subplots()
ax2.plot(angles, efficiency_curve)
ax2.set_title("Efficiency Rating vs Blade Angle")
ax2.set_xlabel("Blade Angle (°)")
ax2.set_ylabel("Efficiency Rating")
ax2.grid(True)
st.pyplot(fig2)

# --- Status Conclusion ---
st.subheader("🔎 Conclusion")
if power_output < 10000:
    st.info("Windmill is producing low power. Try adjusting the blade angle or wait for higher wind speed.")
elif power_output > 300000:
    st.warning("High power output! Monitor closely to prevent overload.")
else:
    st.success("Windmill operating within optimal range.")

st.markdown("""
---
🛠️ *This dashboard is a simulated digital twin for educational/testing use. Add IoT sensor data for real-time applications.*
""")
