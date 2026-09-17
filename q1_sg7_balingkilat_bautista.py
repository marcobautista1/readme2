class Glassware:
    def __init__(self, material, capacity):
        self.material = material
        self.capacity = capacity

    def display_info(self):
        print("Material:", self.material)
        print("Capacity:", self.capacity, "mL")


class Beaker(Glassware):
    def __init__(self, material, capacity, name):
        super().__init__(material, capacity)
        self.name = name

    def display_info(self):
        print("Beaker:", self.name)
        super().display_info()


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker("Glass", 100, "Beaker 1"),
            Beaker("Glass", 100, "Beaker 2"),
            Beaker("Glass", 100, "Beaker 3"),
            Beaker("Glass", 100, "Beaker 4"),
            Beaker("Glass", 100, "Beaker 5")
        ]

    def display_beakers(self):
        print("Tray contains", len(self.beakers), "beakers.")
        
        for beaker in self.beakers:
            beaker.display_info()
            print()


tray = Tray()


tray.display_beakers()


del tray
