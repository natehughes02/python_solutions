# https://codecombat.com/play/level/alpine-rally?

while True:
    if hero.canCast("haste", self):
        hero.cast("haste", self)
    if hero.canCast("invisibility", self):
        hero.cast("invisibility", self)
    if hero.pos.x > 160 and hero.pos.x < 170:
        hero.wait(5)
    direction = Vector(hero.pos.x + 30, hero.pos.y)
    hero.move(direction)
