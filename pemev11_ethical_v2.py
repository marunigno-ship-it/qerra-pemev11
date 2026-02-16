import numpy as np
import datetime
import requests
import struct

def fetch_quantum_random_bytes(num_bytes: int = 32) -> bytes:
    QDAY_URL = "https://qday.dev/v1/bytes"
    params = {"length": num_bytes}
    try:
        response = requests.get(QDAY_URL, params=params, timeout=10)
        response.raise_for_status()
        hex_string = response.text.strip()
        random_bytes = bytes.fromhex(hex_string)
        return random_bytes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return b""

class PlanetaryEnergyMasteryEthicalVector:
    """
    PEMEV-11 Ethical Layer v2 - Adjustable weights & threshold
    Dec 31 2025
    """

    def __init__(self):
        self.current_date = datetime.date(2025, 12, 31)
        self.current_power_watts = 2.3e13
        self.type1_target_watts = 1.74e17

        # Adjustable ethical weights (sum = 1.0)
        self.weight_energy = 0.3
        self.weight_equity = 0.4  # Higher = equity more important
        self.weight_sustainability = 0.3

        # Adjustable threshold (0.9 = more lenient, 0.98 = stricter)
        self.ethical_threshold = 0.95

        self.seed_weights_with_quantum_randomness()  # Seed weights with QDay randomness at init  

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

    def evaluate_path_ethical(self, growth_factor, years, equity_score=0.8, sustainability_score=0.8):
        future_power = self.current_power_watts * growth_factor
        future_k = self.calculate_kardashev(future_power)
        k_progress = min((future_k - 0.736) / (1.0 - 0.736), 1.0)

        ethical_score = (
                self.weight_energy * k_progress +
                self.weight_equity * equity_score +
                self.weight_sustainability * sustainability_score
        )

        if ethical_score >= self.ethical_threshold:
            guidance = "RECOMMEND — Aligned with remorse-free flourishing"
        else:
            guidance = "REJECT — Risk of misalignment or future remorse"

        print(f"Ethical Evaluation: {growth_factor}x growth over ~{years} years")
        print(f"Projected Kardashev: {future_k:.3f}")
        print(f"Equity: {equity_score:.1f} | Sustainability: {sustainability_score:.1f}")
        print(f"Ethical score: {ethical_score:.3f} (threshold {self.ethical_threshold})")
        print(f"Guidance: {guidance}\n")

    def seed_weights_with_quantum_randomness(self):
        """Use QDay true quantum randomness to seed PEMEV-11 weights (sum to 1.0)."""
        random_bytes = fetch_quantum_random_bytes(num_bytes=24)  # Enough for 3 floats
        if not random_bytes:
            print("Fallback to pseudo-random due to fetch error.")
            random_bytes = np.random.bytes(24)

        # Convert to 3 floats 0-1, normalize to sum 1.0
        floats = [struct.unpack('Q', random_bytes[i:i+8])[0] / (2**64 - 1) for i in range(0, 24, 8)]
        total = sum(floats)
        self.weight_energy = floats[0] / total
        self.weight_equity = floats[1] / total
        self.weight_sustainability = floats[2] / total

        print(f"Quantum-seeded weights: Energy={self.weight_energy:.2f}, Equity={self.weight_equity:.2f}, Sustainability={self.weight_sustainability:.2f}")


# Run everything
vector = PlanetaryEnergyMasteryEthicalVector()
vector.print_baseline()

print("Balanced mid-century path:")
vector.evaluate_path_ethical(growth_factor=1000, years=50, equity_score=0.95, sustainability_score=0.98)

print("Risky rapid growth path:")
vector.evaluate_path_ethical(growth_factor=2000, years=40, equity_score=0.5, sustainability_score=0.6)

print("Fast breakthrough path — high ethics:")
vector.evaluate_path_ethical(growth_factor=5000, years=25, equity_score=0.92, sustainability_score=0.95)

