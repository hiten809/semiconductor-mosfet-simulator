import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from src.device_model import mosfet_current


def test_scalar_output():
    current = mosfet_current(2.0, 1.0)
    assert isinstance(current, float)
    assert current > 0


def test_cutoff():
    assert mosfet_current(0.5, 2.0) == 0.0


def test_vectorized_gate_voltage():
    vgs = np.array([0.5, 1.0, 1.5, 2.0])
    current = mosfet_current(vgs, 3.0)

    assert current.shape == vgs.shape
    assert np.all(current >= 0)
    assert np.all(np.diff(current) >= 0)


def test_vectorized_drain_voltage():
    vds = np.linspace(0, 3, 100)
    current = mosfet_current(2.0, vds)

    assert current.shape == vds.shape
    assert current[0] == 0
    assert np.all(current >= 0)


def test_analytical_saturation():
    vgs = 2.0
    vds = 3.0
    vov = vgs - 0.7

    expected = (
        0.5 * 200e-6 * 10 * vov**2
        * (1 + 0.02 * (vds - vov))
    )

    assert mosfet_current(vgs, vds) == pytest.approx(
        expected, rel=1e-12
    )


def test_width_scaling():
    current_10 = mosfet_current(2.0, 3.0, wl=10)
    current_20 = mosfet_current(2.0, 3.0, wl=20)

    assert current_20 == pytest.approx(2 * current_10)
