"""Channel models."""
import numpy as np

rng = np.random.default_rng(42)


def awgn(symbols, ebn0_db, bits_per_symbol=2):
    """Add complex AWGN for a given Eb/N0 in dB (average Es = 1)."""
    ebn0 = 10 ** (ebn0_db / 10)
    esn0 = ebn0 * bits_per_symbol
    n0 = 1 / esn0
    noise = np.sqrt(n0 / 2) * (rng.standard_normal(symbols.shape)
                               + 1j * rng.standard_normal(symbols.shape))
    return symbols + noise


# TODO (Stage 3): add rayleigh(symbols) that returns (faded_symbols, h)
#   - h ~ CN(0,1): (randn + 1j*randn) / sqrt(2)
#   - multiply symbols by h, then add noise, then equalize by dividing by h