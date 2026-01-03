import numpy as np
import matplotlib.pyplot as plt
import datetime


class PlanetaryEnergyMasteryEthicalVector:
    """
    PEMEV-11 Ethical Landscape Visualization (fixed vectorized)
    Jan 03 2026
    """

    def __init__(self):
        self.current_date = datetime.date(2026, 1, 3)
        self.current_power_watts = 2.3e13
        self.type1_target_watts = 1.74e17

        self.weight_energy = 0.3
        self.weight_equity = 0.4
        self.weight_sustainability = 0.3

        self.ethical_threshold = 0.95

        self.current_equity = 0.35
        self.current_sustainability = 0.65

    def calculate_kardashev(self, power_watts):
        return (np.log10(power_watts) - 6) / 10

    def ethical_score(self, growth_factor, equity_score, sustainability_score):
        future_power = self.current_power_watts * growth_factor
        future_k = self.calculate_kardashev(future_power)
        k_progress = np.minimum((future_k - 0.736) / (1.0 - 0.736), 1.0)  # Vectorized

        score = (
                self.weight_energy * k_progress +
                self.weight_equity * equity_score +
                self.weight_sustainability * sustainability_score
        )

        # W-state bonus (simple)
        robustness_bonus = 0.20
        return score + robustness_bonus

    def visualize_ethical_landscape(self):
        growth_factors = np.logspace(0, 4, 100)  # 1x to 10,000x

        high = self.ethical_score(growth_factors, 0.95, 0.98)
        medium = self.ethical_score(growth_factors, 0.7, 0.8)
        low = self.ethical_score(growth_factors, self.current_equity, self.current_sustainability)

        plt.figure(figsize=(10, 6))
        plt.plot(growth_factors, high, label='High equity/sustainability', color='green', linewidth=2)
        plt.plot(growth_factors, medium, label='Medium (improving)', color='orange', linewidth=2)
        plt.plot(growth_factors, low, label='Current real-world hints', color='red', linewidth=2)

        plt.axhline(self.ethical_threshold, color='black', linestyle='--', label='Ethical threshold (0.95)')
        plt.fill_between(growth_factors, self.ethical_threshold, max(high.max(), medium.max(), low.max() + 0.1),
                         color='lightgreen', alpha=0.3, label='Remorse-free zone')

        plt.xscale('log')
        plt.xlabel('Energy Growth Factor (log scale)')
        plt.ylabel('Ethical Score')
        plt.title('PEMEV-11 Ethical Landscape - Safe Growth Zones for Type I Transition')
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.savefig("ethical_landscape.png")
        print("Plot saved as ethical_landscape.png in project folder")
        plt.show()


# Run visualization
vector = PlanetaryEnergyMasteryEthicalVector()
vector.visualize_ethical_landscape()