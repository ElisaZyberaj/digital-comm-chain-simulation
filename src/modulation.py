"""Modulators and demodulators."""
import numpy as np


def qpsk_mod(bits):
    """Gray-mapped QPSK, unit average symbol energy.
    Bit pair (b0, b1) -> (I, Q) with 0 -> +1 and 1 -> -1."""
    b = np.asarray(bits).reshape(-1, 2)
    i = 1 - 2 * b[:, 0]
    q = 1 - 2 * b[:, 1]
    return (i + 1j * q) / np.sqrt(2)


def qpsk_demod(symbols):
    """Hard-decision QPSK demodulation."""
    b0 = (symbols.real < 0).astype(int)
    b1 = (symbols.imag < 0).astype(int)
    return np.column_stack((b0, b1)).ravel()


# TODO (Stage 2): add qam16_mod(bits) and qam16_demod(symbols)
#   - 4 bits per symbol, Gray coding on each axis, levels -3, -1, +1, +3
#   - normalize by sqrt(10) so average symbol energy is 1