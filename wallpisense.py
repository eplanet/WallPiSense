import sense_hat
import time, random

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Hero:
    def __init__(self, sense):
        self.pos = Position(0, 3)
        self.sense = sense
        self.redraw()
    def redraw(self, color=[0,255,0]):
        self.sense.set_pixel(self.pos.x, self.pos.y, color)
    def move(self, event):
        if event.action == "released":
            return
        self.redraw([0,0,0])
        if event.direction == "down" and self.pos.y < 7:
            self.pos.y += 1
        elif event.direction == "up" and self.pos.y > 0:
            self.pos.y -= 1
        elif event.direction == "right" and self.pos.x < 7:
            self.pos.x += 1
        elif event.direction == "left" and self.pos.x > 0:
            self.pos.x -= 1
        self.redraw()

class Wall:
    def __init__(self, sense):
        self.sense = sense
        self.structure = list()
        for i in range(8):
            if random.randint(0,4) > 0:
                self.structure.append(Position(7, i))
        if len(self.structure) == 8:
            del self.structure[random.randint(0,7)]
        self.redraw()
    def redraw(self, color=[255,0,0]):
        for i in self.structure:
            if i.x > -1:
                self.sense.set_pixel(i.x, i.y, color)
    def left(self):
        self.redraw([0,0,0])
        for i in range(len(self.structure)):
            self.structure[i].x -= 1
        self.redraw()
    def is_outside(self):
        return max([i.x for i in self.structure]) < 0
    def collide(self, pos):
        for i in self.structure:
            if i == pos:
                return True
        return False

if __name__ == "__main__":
    sense = sense_hat.SenseHat()
    sense.clear()
    sense.low_light = True
    sense.set_rotation(0)

    hero = Hero(sense)
    wall = Wall(sense)
    while True:
        for event in sense.stick.get_events():
            hero.move(event)
        time.sleep(0.5)
        wall.left()
        hero.redraw()
        if wall.collide(hero.pos):
            sense.show_message("Game over!")
            break
        if wall.is_outside():
            wall = Wall(sense)

