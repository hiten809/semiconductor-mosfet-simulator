# MOSFET Device Physics Simulator

An interactive Python-based simulator for studying
long-channel NMOS transistor characteristics.

## Features

- Drain current versus drain-source voltage (ID-VDS)
- Drain current versus gate-source voltage (ID-VGS)
- Transconductance analysis
- Threshold-voltage estimation
- Interactive Streamlit dashboard
- CSV export
- Automated tests using pytest

## Technology Stack

Python, NumPy, Matplotlib, SciPy, Pandas,
Plotly, Streamlit, pytest.

## Physics

The simulator implements the long-channel MOSFET
square-law model with a simplified channel-length
modulation correction in saturation.

The model is intended for educational device
characterization, not calibrated industrial
transistor modelling.

## Installation

Create and activate a Python virtual environment,
then run:

    pip install -r requirements.txt

## Launch Dashboard

    python -m streamlit run app.py

## Run Tests

    python -m pytest tests/ -v

## Verification

13 automated tests passed during development.

## Future Work

- PMOS modelling
- Temperature dependence
- SPICE comparison
- Experimental data fitting
