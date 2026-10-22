
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from src.device_model import mosfet_current

st.set_page_config(
    page_title="MOSFET Device Simulator",
    layout="wide"
)

st.title("MOSFET Device Physics Simulator")
st.caption("Interactive long-channel NMOS electrical characterization")

st.sidebar.header("Device Parameters")

vth = st.sidebar.slider(
    "Threshold voltage Vth (V)", 0.2, 1.5, 0.7, 0.05
)
wl = st.sidebar.slider(
    "Width-to-length ratio W/L", 1.0, 50.0, 10.0, 1.0
)
mu_cox = st.sidebar.slider(
    "Mobility × oxide capacitance (µA/V²)",
    50.0, 500.0, 200.0, 10.0
)
lam = st.sidebar.slider(
    "Channel-length modulation λ (1/V)",
    0.0, 0.1, 0.02, 0.005
)
fixed_vds = st.sidebar.slider(
    "Fixed drain voltage VDS (V)",
    0.1, 5.0, 2.0, 0.1
)

def current(vgs, vds):
    return mosfet_current(
        vgs=vgs,
        vds=vds,
        vth=vth,
        wl=wl,
        mu_cox=mu_cox * 1e-6,
        lam=lam
    )

vgs_values = np.linspace(0, 5, 250)
vds_values = np.linspace(0, 5, 250)

transfer_current = current(vgs_values, fixed_vds)
gm = np.gradient(transfer_current, vgs_values)

st.subheader("Device Characteristics")

col1, col2 = st.columns(2)

with col1:
    fig_transfer = go.Figure()
    fig_transfer.add_trace(go.Scatter(
        x=vgs_values,
        y=transfer_current * 1e3,
        mode="lines",
        name="Drain current"
    ))
    fig_transfer.update_layout(
        title="Transfer Characteristics",
        xaxis_title="VGS (V)",
        yaxis_title="ID (mA)"
    )
    st.plotly_chart(fig_transfer, use_container_width=True)

with col2:
    fig_output = go.Figure()

    for gate_voltage in [1.0, 1.5, 2.0, 3.0, 4.0, 5.0]:
        ids = current(gate_voltage, vds_values)
        fig_output.add_trace(go.Scatter(
            x=vds_values,
            y=ids * 1e3,
            mode="lines",
            name=f"VGS = {gate_voltage:.1f} V"
        ))

    fig_output.update_layout(
        title="Output Characteristics",
        xaxis_title="VDS (V)",
        yaxis_title="ID (mA)"
    )
    st.plotly_chart(fig_output, use_container_width=True)

fig_gm = go.Figure()
fig_gm.add_trace(go.Scatter(
    x=vgs_values,
    y=gm * 1e3,
    mode="lines",
    name="Transconductance"
))
fig_gm.update_layout(
    title="Transconductance",
    xaxis_title="VGS (V)",
    yaxis_title="gm (mS)"
)
st.plotly_chart(fig_gm, use_container_width=True)

st.subheader("Simulation Data")

data = pd.DataFrame({
    "VGS_V": vgs_values,
    "ID_A": transfer_current,
    "gm_S": gm
})

st.dataframe(data, use_container_width=True)

st.download_button(
    "Download CSV",
    data=data.to_csv(index=False),
    file_name="mosfet_transfer_data.csv",
    mime="text/csv"
)

st.success("MOSFET simulation completed successfully.")
