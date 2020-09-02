#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/29 20:15'


class Game:
    hp = 1000
    power = 200

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print(" I win")
        elif final_hp < enemy_final_hp:
            print(" I defeat")
        else:
            print(" no winner")


game = Game()
print(game.fight(1000, 200))
