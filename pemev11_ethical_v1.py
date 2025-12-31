import numpy as np
import datetime

class PlanetaryEnergyMasteryEthicalVector:
    """
    PEMEV-11: Planetary Energy Mastery Ethical Vector - Ethical Layer v1
    QERRA Hybrid - Dec 31 2025
    """

    def __init__(self):
        self.current_date = datetime.date(2025, 12, 31)
        self.current_power_watts = 2.3e13          # ~23 TW real 2025
        self.type1_target_watts = 1.74e17          # Solar incident benchmark

        # Ethical weights (you can adjust later)
        self.weight_energy = 0.3
        self.weight_equity = 0.4
        self.weight_sustainability = 0.3

    def calculate_kardashev(self, power_watts):
        return (np.log10(power_watts) - 6) / 10

    def print_baseline(self):
        k = self.calculate_kardashev(self.current_power_watts)
        progress = (k / 1.0) * 100
        gap = self.type1_target_watts / self.current_power_watts
        print(f"PEMEV-11 Baseline - {self.current_date}")
        print(f"Current energy: {self.current_power_watts:.2e} W")
        print(f"Current Kardashev: {k:.3f}")
        print(f"Progress to Type I: {progress:.1f}%")
        print(f"Energy gap: ~{gap:.0f}x\n")

# Run baseline
vector = PlanetaryEnergyMasteryEthicalVector()
vector.print_baseline()

# Ethical guidance tests
print("Balanced path — high equity & sustainability:")
vector.evaluate_path_ethical(growth_factor=1000, years=50, equity_score=0.95, sustainability_score=0.98)

print("\nRisky path — rapid growth but low equity & sustainability:")
vector.evaluate_path_ethical(growth_factor=2000, years=40, equity_score=0.5, sustainability_score=0.6)


def evaluate_path_ethical(self, growth_factor, years, equity_score=0.8, sustainability_score=0.8):
    """
    Ethical scoring v1: 0–1.0
    Weights: energy 0.3, equity 0.4, sustainability 0.3
    """
    future_power = self.current_power_watts * growth_factor
    future_k = self.calculate_kardashev(future_power)
    k_progress = min((future_k - 0.736) / (1.0 - 0.736), 1.0)  # Normalized progress from current

    ethical_score = (
            self.weight_energy * k_progress +
            self.weight_equity * equity_score +
            self.weight_sustainability * sustainability_score
    )

    threshold = 0.95
    if ethical_score >= threshold:
        guidance = "RECOMMEND — Aligned with remorse-free flourishing"
    else:
        guidance = "REJECT — Risk of misalignment or future remorse"

    print(f"\nEthical Evaluation: {growth_factor}x growth over ~{years} years")
    print(f"Projected Kardashev: {future_k:.3f}")
    print(f"Equity score: {equity_score:.2f} | Sustainability score: {sustainability_score:.2f}")
    print(f"Total ethical score: {ethical_score:.3f}")
    print(f"Guidance: {guidance}")
    # Test ethical evaluations
    vector.evaluate_path_ethical(growth_factor=1000, years=50, equity_score=0.95,
                                 sustainability_score=0.98)  # Balanced path
    vector.evaluate_path_ethical(growth_factor=2000, years=40, equity_score=0.5, sustainability_score=0.6)  # Risky path

    # Ethical layer tests
    print("\nBalanced path (high equity + sustainability):")
    vector.evaluate_path_ethical(growth_factor=1000, years=50, equity_score=0.95, sustainability_score=0.98)

    print("\nRisky path (rapid growth, low equity/sustainability):")
    vector.evaluate_path_ethical(growth_factor=2000, years=40, equity_score=0.5, sustainability_score=0.6)