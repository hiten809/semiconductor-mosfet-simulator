
import pytest

from src.mosfet import drain_current, MU_COX, W_OVER_L, VTH, LAMBDA



def test_cutoff_region():
    assert drain_current(0.5, 2.0) == 0.0
    assert drain_current(VTH, 2.0) == 0.0


def test_zero_drain_voltage():
    assert drain_current(2.0, 0.0) == 0.0


def test_gate_voltage_response():
    low = drain_current(1.0, 2.0)
    high = drain_current(2.0, 2.0)
    assert high > low


def test_linear_region():
    low = drain_current(2.0, 0.2)
    high = drain_current(2.0, 0.5)
    assert high > low


def test_saturation_continuity():
    vgs = 2.0
    boundary = vgs - VTH

    below = drain_current(vgs, boundary - 1e-7)
    above = drain_current(vgs, boundary + 1e-7)

    assert below == pytest.approx(above, rel=1e-5)


def test_analytical_linear_current():
    vgs = 2.0
    vds = 0.5

    beta = MU_COX * W_OVER_L
    expected = beta * (
        (vgs - VTH) * vds - 0.5 * vds**2
    )

    assert drain_current(vgs, vds) == pytest.approx(
        expected, rel=1e-12
    )


def test_nonnegative_current():
    for vgs in [0.0, 0.5, 1.0, 2.0, 3.0]:
        for vds in [0.0, 0.5, 1.0, 2.0, 3.0]:
            assert drain_current(vgs, vds) >= 0.0
