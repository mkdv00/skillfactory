class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def __add__(self, other):
        self.proteins + other.proteins
        self.carbs + other.carbs
        self.fats + other.fats

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)



apple = NutritionInfo(0, 25, 0)
tvorog_9 = NutritionInfo(18, 3, 9)

apple_calories = apple.energy()
tvorog_9_calories = tvorog_9.energy()
breakfast = apple_calories + tvorog_9_calories

print(breakfast)
