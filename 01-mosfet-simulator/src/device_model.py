
import numpy as np


def mosfet_current(
    vgs,
    vds,
    vth=0.7,
    wl=10.0,
    mu_cox=200e-6,
    lam=0.02
):
    """
    Long-channel NMOS drain-current model.

    Parameters
    ----------
    vgs : float or array
        Gate-source voltage (V)
    vds : float or array
        Drain-source voltage (V)
    vth : float
        Threshold voltage (V)
    wl : float
        Width-to-length ratio
    mu_cox : float
        Mobility-capacitance product (A/V^2)
    lam : float
        Channel-length modulation parameter (1/V)

    Returns
    -------
    float or ndarray
        Drain current (A)
    """

    vg, vd = np.broadcast_arrays(
        np.asarray(vgs, dtype=float),
        np.asarray(vds, dtype=float)
    )

    vov = vg - vth
    beta = mu_cox * wl

    current = np.zeros_like(vov, dtype=float)

    active = (vov > 0) & (vd > 0)
    linear = active & (vd < vov)
    saturation = active & ~linear

    current[linear] = beta * (
        vov[linear] * vd[linear]
        - 0.5 * vd[linear]**2
    )

    current[saturation] = (
        0.5 * beta * vov[saturation]**2
        * (1 + lam * (vd[saturation] - vov[saturation]))
    )

    if current.ndim == 0:
        return float(current)

    return current
