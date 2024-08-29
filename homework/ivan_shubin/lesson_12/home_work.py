from statistics import mean

class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length  # длина стебля в см
        self.freshness = freshness  # свежесть (в днях с момента среза)
        self.cost = cost  # стоимость в рублях
        self.lifespan = lifespan  # время жизни в днях

    def __repr__(self):
        return f"{self.name}({self.color}, {self.stem_length}cm, {self.freshness}d, {self.cost}₽)"


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__("Rose", color, stem_length, freshness, cost, lifespan=10)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__("Tulip", color, stem_length, freshness, cost, lifespan=7)


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__("Lily", color, stem_length, freshness, cost, lifespan=14)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return mean(flower.lifespan for flower in self.flowers)

    def sort_by(self, attribute):
        if attribute in ['freshness', 'color', 'stem_length', 'cost']:
            self.flowers.sort(key=lambda flower: getattr(flower, attribute))
        else:
            raise ValueError("Invalid attribute to sort by")

    def find_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def __repr__(self):
        return f"Bouquet with flowers: {', '.join([str(flower) for flower in self.flowers])}"

# Пример использования

# Создаем цветы
rose = Rose(color="Red", stem_length=50, freshness=2, cost=100)
tulip = Tulip(color="Yellow", stem_length=30, freshness=1, cost=60)
lily = Lily(color="White", stem_length=40, freshness=3, cost=150)

# Создаем букет
bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)

# Выводим букет
print(bouquet)

# Общая стоимость букета
print(f"Total cost of the bouquet: {bouquet.total_cost()}₽")

# Среднее время жизни букета
print(f"Average lifespan of the bouquet: {bouquet.average_lifespan()} days")

# Сортировка по стоимости
bouquet.sort_by('cost')
print(f"Bouquet sorted by cost: {bouquet}")

# Поиск цветов по времени жизни
flowers_with_lifespan_10 = bouquet.find_by_lifespan(10)
print(f"Flowers with lifespan 10 days: {flowers_with_lifespan_10}")
