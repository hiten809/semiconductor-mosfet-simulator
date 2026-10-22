
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# MOSFET device parameters
MU_COX = 200e-6   # A/V^2
W_OVER_L = 10
VTH = 0.7         # Threshold voltage (V)
LAMBDA = 0.02     # Channel-length modulation (1/V)

def drain_current(vgs, vds):
    """Long-channel NMOS model, neglecting subthreshold current."""
    vov = vgs - VTH

    if vov <= 0 or vds <= 0:
        return 0.0

    beta = MU_COX * W_OVER_L

    if vds < vov:
        # Triode region
        return beta * (vov * vds - 0.5 * vds**2)

    # Saturation region
    idsat = 0.5 * beta * vov**2
    return idsat * (1 + LAMBDA * (vds - vov))


def main():
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    vds_values = np.linspace(0, 3, 300)
    gate_voltages = [0.5, 1.0, 1.5, 2.0, 2.5]

    plt.figure(figsize=(9, 6))

    for vgs in gate_voltages:
        currents = [
            drain_current(vgs, vds) * 1000
            for vds in vds_values
        ]

        plt.plot(vds_values, currents, label=f"VGS = {vgs} V")

    plt.xlabel("Drain-Source Voltage VDS (V)")
    plt.ylabel("Drain Current ID (mA)")
    plt.title("NMOS Output Characteristics")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_dir / "mosfet_output.png", dpi=300)
    plt.show()

    print("Simulation completed successfully.")
    print("Plot saved to results/mosfet_output.png")


if __name__ == "__main__":
    main()
