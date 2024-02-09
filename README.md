# Mass Compounding Factor Calculation for eVTOL

This repository contains a Python script for calculating the mass compounding factor for an electric vertical take-off and landing (eVTOL) vehicle. The mass compounding factor is defined as the ratio of the final mass removed from the vehicle for every initial 1kg of mass removed from its subsystem.

## Problem Statement

A small eVTOL of max take-off mass (MTOW) 1600kg requires 800kW to hover. There are 8 electrical power units (EPUs) on the aircraft, and each of them weighs 30kg. The battery pack weighs 800kg. The EPU supplier announces their EPU is 1kg over the target mass. We need to calculate the impact on the MTOW of the aircraft.

## Assumptions

All dependencies are linear, that is:

- Battery mass required varies linearly with MTOW.
- Power required to hover varies linearly with MTOW.
- EPU mass varies linearly with power required to hover.

## Solution

The Python script `mass_compounding_factor.py` calculates the mass compounding factor using an iterative process that continues until the change in the MTOW is less than a specified threshold. The new masses of the EPU and the battery, and the new power required to hover are calculated in each iteration given the increase in the EPU mass. The final MTOW is then calculated as the sum of the unchanged mass, the final battery mass, and the total final EPU mass. If the change in the MTOW is less than the threshold, the iterative process stops. The EPU mass is then updated by a factor given by the change in the total mass. Finally, the mass compounding factor is calculated as the ratio of the final MTOW to the initial MTOW.

## Usage

You can run the script in a Python environment to get the result. The script prints the mass compounding factor and the total mass increase.
