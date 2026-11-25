"""BER vs Eb/N0 simulation. Run from the project root:  python src/simulate.py"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

from modulation import qpsk_mod, qpsk_demod
from channels import awgn, rng


def qfunc(x):
    return 0.5 * erfc(x / np.sqrt(2))


def simulate_qpsk_awgn(ebn0_db_list, n_bits=1_000_000):
    ber = []
    for ebn0_db in ebn0_db_list:
        bits = rng.integers(0, 2, n_bits)
        rx = awgn(qpsk_mod(bits), ebn0_db)
        ber.append(np.mean(bits != qpsk_demod(rx)))
    return np.array(ber)


def theory_qpsk_awgn(ebn0_db_list):
    ebn0 = 10 ** (np.asarray(ebn0_db_list) / 10)
    return qfunc(np.sqrt(2 * ebn0))


if __name__ == "__main__":
    ebn0_db = np.arange(0, 11, 1)
    ber_sim = simulate_qpsk_awgn(ebn0_db)
    ber_th = theory_qpsk_awgn(ebn0_db)

    plt.figure(figsize=(7, 5))
    plt.semilogy(ebn0_db, ber_th, "k-", label="QPSK AWGN (theory)")
    plt.semilogy(ebn0_db, ber_sim, "bo", label="QPSK AWGN (simulation)")
    plt.grid(True, which="both", alpha=0.3)
    plt.xlabel("Eb/N0 (dB)")
    plt.ylabel("Bit Error Rate")
    plt.title("BER vs Eb/N0")
    plt.ylim(1e-6, 1)
    plt.legend()
    plt.tight_layout()

    os.makedirs("results", exist_ok=True)
    plt.savefig("results/ber_curves.png", dpi=150)
    print("Saved results/ber_curves.png")