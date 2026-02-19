import numpy as np
import datetime
import requests
import struct
import os  # safer fallback

def fetch_quantum_random_bytes(num_bytes: int = 32) -> bytes:
    """Fetch true quantum random bytes from QDay API with validation."""
    QDAY_URL = "https://qday.dev/v1/bytes"
    params = {"length": num_bytes}
    headers = {"User-Agent": "PEMEV11-QAI-Project-Marussa"}  # polite + identifiable
    
    try:
        response = requests.get(QDAY_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        hex_string = response.text.strip()
        
        # Validate hex format
        if len(hex_string) != num_bytes * 2 or not all(c in "0123456789abcdefABCDEF" for c in hex_string):
            raise ValueError("Invalid hex response from QDay")
            
        return bytes.fromhex(hex_string)
        
    except Exception as e:
        print(f"QDay fetch failed: {e} → using fallback")
        return b""

class PlanetaryEnergyMasteryEthicalVector:
    """
    PEMEV-11 Ethical Layer v2 
    Quantum-seeded ethical weights for energy, equity and sustainability
    Updated Feb 2026 - QAI Project with Grok 4.2
    """

    def __init__(self, use_quantum: bool = True):
        self.current_date = datetime.date.today()
        self.current_power_watts = 2.3e13
        self.type1_target_watts = 1.74e17

        # Adjustable ethical weights (will be seeded)
        self.weight_energy = 0.3
        self.weight_equity = 0.4
        self.weight_sustainability = 0.3

        # Adjustable threshold (0.9 = more lenient, 0.98 = stricter)
        self.ethical_threshold = 0.95

        if use_quantum:
            self.seed_weights_with_quantum_randomness(debug=True)
        else:
            print("Using default ethical weights (quantum seeding disabled)")

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

    def seed_weights_with_quantum_randomness(self, debug=True):
        """Use QDay true quantum randomness to seed PEMEV-11 weights (sum to 1.0)."""
        random_bytes = fetch_quantum_random_bytes(num_bytes=24)
        
        if not random_bytes:
            print("Fallback to secure pseudo-random (os.urandom).")
            random_bytes = os.urandom(24)

        try:
            # Convert 24 bytes → 3 high-quality floats, normalize
            floats = [struct.unpack('Q', random_bytes[i:i+8])[0] / (2**64 - 1) 
                     for i in range(0, 24, 8)]
            total = sum(floats)
            self.weight_energy = floats[0] / total
            self.weight_equity = floats[1] / total
            self.weight_sustainability = floats[2] / total
        except Exception:
            # Ultra-safe fallback
            self.weight_energy = 0.33
            self.weight_equity = 0.34
            self.weight_sustainability = 0.33

        if debug:
            print(f"Quantum-seeded weights: Energy={self.weight_energy:.3f}, "
                  f"Equity={self.weight_equity:.3f}, "
                  f"Sustainability={self.weight_sustainability:.3f}")

# ========================
if __name__ == "__main__":
    print("=== PEMEV-11 Ethical Vector v2 - QAI Project ===\n")
    
    vector = PlanetaryEnergyMasteryEthicalVector(use_quantum=True)
    vector.print_baseline()

    print("Balanced mid-century path:")
    vector.evaluate_path_ethical(growth_factor=1000, years=50, equity_score=0.95, sustainability_score=0.98)

    print("Risky rapid growth path:")
    vector.evaluate_path_ethical(growth_factor=2000, years=40, equity_score=0.5, sustainability_score=0.6)

    print("Fast breakthrough path — high ethics:")
    vector.evaluate_path_ethical(growth_factor=5000, years=25, equity_score=0.92, sustainability_score=0.95)
