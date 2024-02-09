# Initial parameters
mtow_initial = 1600  # kg
power_hover = 800  # kW
epu_mass_initial = 30  # kg
battery_mass_initial = 800  # kg
epu_mass_delta = 1  # kg
num_epus = 8

# Calculate the unchanged mass (MTOW - Battery mass - Total EPU mass)
unchanged_mass = mtow_initial - battery_mass_initial - num_epus * epu_mass_initial

# Initialize variables for the iterative process
mtow = mtow_initial
epu_mass = epu_mass_initial + epu_mass_delta
battery_mass = battery_mass_initial
power_hover = power_hover

# Set a threshold for convergence
threshold = 0.001  # kg

while True:
    # Calculate the new masses and power
    mtow_new = unchanged_mass + battery_mass + num_epus * epu_mass
    # Check for convergence
    if abs(mtow_new - mtow) < threshold:
        break

    power_hover_new = power_hover * (mtow_new / mtow)
    battery_mass_new = battery_mass * (mtow_new / mtow)
    epu_mass_new = epu_mass * (mtow_new / mtow)

    # update variables for the loop
    battery_mass = battery_mass_new
    epu_mass = epu_mass_new
    mtow = mtow_new
    print(mtow)


# Calculate the mass compounding factor
mass_compounding_factor = mtow_new / mtow_initial
total_mass_increase = mtow_new - mtow_initial

print(f"The mass compounding factor is {mass_compounding_factor:.5f}.")
print(f"The mass increased from {mtow_initial} to {
      mtow_new} with a mass increase of {total_mass_increase:.3f}.")
