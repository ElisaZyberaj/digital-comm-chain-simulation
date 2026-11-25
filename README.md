# Digital Communication Chain Simulation

Python simulation of a digital communication chain: QPSK/16-QAM over AWGN and
Rayleigh fading channels, with BER vs Eb/N0 compared to theory.

## Status
- [x] QPSK over AWGN
- [ ] 16-QAM over AWGN
- [ ] Rayleigh fading channel
- [ ] Combined comparison plot

## How to run
```
pip install -r requirements.txt
python src/simulate.py
```
The plot is saved to `results/ber_curves.png`.

## Theory
- QPSK BER over AWGN: Pb = Q(sqrt(2 Eb/N0))
