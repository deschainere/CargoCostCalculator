from base_cost_calculator import BaseCostCalculator

weight = float(input("Введите вес груза (кг): "))
cost = BaseCostCalculator.calculate(weight)
print(f"Базовая стоимость: {cost} руб.")