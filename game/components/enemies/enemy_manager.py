from game.components.enemies.fast_enemy import Enemy_Fast
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies=[]

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies)< 1:
            enemy=Enemy()
            enemy2=Enemy_Fast()
            self.enemies.append(enemy)
            self.enemies.append(enemy2)

