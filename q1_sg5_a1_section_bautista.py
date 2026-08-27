class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def __str__(self):
        return f"{self.name} - HP: {self.hp}"


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(arthur)
print(morgana)
