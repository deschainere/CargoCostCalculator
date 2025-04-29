class ManualLiftCostCalculator:
    @staticmethod
    def calculate(weight, floor):
        cost_per_100kg = 300
        multiplier = (weight // 100) + 1
        return cost_per_100kg * (floor - 1) * multiplier