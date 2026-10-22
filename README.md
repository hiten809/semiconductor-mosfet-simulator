# MOSFET Device Physics Simulator

A Python-based semiconductor device simulator for analyzing
long-channel NMOS transistor characteristics.

## Project Overview

This project implements the classical MOSFET square-law model
and provides interactive visualization of transistor behavior.

### Features

- NMOS cutoff, triode, and saturation modeling
- Drain current versus drain-source voltage (ID-VDS)
- Transfer characteristics (ID-VGS)
- Transconductance analysis
- Threshold-voltage estimation
- Interactive Streamlit dashboard
- CSV export
- Automated testing with pytest

## Simulation Results

### Output Characteristics

![MOSFET Output](01-mosfet-simulator/results/mosfet_output.png)

### Transfer Characteristics

![Transfer Analysis](01-mosfet-simulator/results/transfer_analysis.png)

## Technology Stack

Python | NumPy | Matplotlib | SciPy | Plotly | Streamlit | pytest

## Getting Started

The project source code and detailed setup instructions are
available in the [project directory](01-mosfet-simulator/).

## Verification

13 automated tests passed during development.

## Author

Hiten Kaistha

B.Tech — Engineering Physics / Physics & Photonic Sciences

National Institute of Technology Hamirpur
