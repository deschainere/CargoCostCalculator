# Версия 2.0 от 29.04.2025
from base_cost_calculator import BaseCostCalculator
from manual_lift_cost_calculator import ManualLiftCostCalculator

weight = float(input("Введите вес груза (кг): "))
floor = int(input("Введите этаж: "))
has_elevator = input("Есть лифт? (да/нет): ").lower() == "да"

if has_elevator:
    cost = BaseCostCalculator.calculate(weight)
else:
    base_cost = BaseCostCalculator.calculate(weight)
    lift_cost = ManualLiftCostCalculator.calculate(weight, floor)
    cost = base_cost + lift_cost

print(f"Итоговая стоимость: {cost} руб.")