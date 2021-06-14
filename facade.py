from __future__ import annotations
from abc import ABC, abstractmethod
import text
from player import Player
from plane import Plane
from controls import Controls
from visitor import VisitorNextRoom, VisitorInventory,VisitorHp
import random
import time
import math


class Facade(Controls):
    def __init__(self):
        Controls.__init__(self)
        self._button = "o"
        self.player1 = Player()
        self.player2 = Player()
        self.plane = Plane()
        self.players = [self.player1, self.player2]
        self._test = "o"

    @property
    def button(self):
        return self._button

    @button.setter
    def button(self, value):
        self._button = value
        if value == "s":
            self.notify_s()
        elif value == "i":
            self.notify_i()
        elif value == "k":
            self.notify_k()
        elif value == "test":
            self.notify_test()
        else:
            print("Oops!  Nie właściwy znak.  Spróbuj ponownie...")

    def start(self):
        self.detach(self)
        self.plane.start()
        self.game()

    def info(self):
        print(text.inst)
        time.sleep(2)

    def test(self):
        self._test = "info"

    def exit(self):
        print("The End")
        quit()

    def next_room(self):
        list_next = self.plane.go_next(self.player1.where_now())
        print("Gdzie dalej chcesz isc?")
        self.plane.print_out(list_next, self.player1.where_previous())

        try:
            next_move = input()
            print("Przechodzisz do {}".format(self.plane.get_room_name(list_next[int(next_move)])))
            visitor = VisitorNextRoom(list_next[int(next_move)])
            visitor.visit(self.player1)
            if self.player1.get_hp() != self.player1.get_max_hp():
                visitor_hp = VisitorHp(self.player1.get_hp() + 1)
                visitor_hp.visit(self.player1)
        except IndexError:
            print("Oops!  Nie właściwa liczba.  Spróbuj ponownie...")
        except ValueError:
            print("Oops!  Nie właściwy znak.  Spróbuj ponownie...")

    def encounter(self, name):

        monster_hp = self.plane.get_room(self.player1.where_now()).get_hp()
        monster_max_hp = self.plane.get_room(self.player1.where_now()).get_hp_max()
        monster_diff = self.plane.get_room(self.player1.where_now()).get_diff()
        fight = 0
        while fight == 0:
            print("Masz {}/{} hp. Przeciwnik ma {}/{} hp.".format(self.player1.get_hp(), self.player1.get_max_hp(), monster_hp, monster_max_hp))
            print("Co robisz?")
            print("0 - Uciekasz \n1 - Walczysz ")
            move = input()
            try:
                if int(move) == 0:
                    print("Uciekasz do {}".format(self.plane.get_room_name(self.player1.where_previous())))
                    self.plane.get_room(self.player1.where_now()).set_hp(monster_hp)
                    visitor = VisitorNextRoom(self.player1.where_previous())
                    visitor.visit(self.player1)
                    a = 0
                    fight = 1

                elif int(move) == 1:
                    dice_roll = random.randint(1, 6)
                    if dice_roll >= monster_diff:
                        monster_hp -= math.fabs(dice_roll - monster_diff)
                    else:
                        visitor_hp = VisitorHp(self.player1.get_hp() - math.fabs(dice_roll - monster_diff))
                        visitor_hp.visit(self.player1)
            except IndexError:
                print("Oops!  Nie właściwa liczba.  Spróbuj ponownie...")
            except ValueError:
                print("Oops!  Nie właściwy znak.  Spróbuj ponownie...")
            if monster_hp <= 0:
                print("Udało ci się pokonać {}.".format(name))
                if name == "smok":
                    self.good_end()
                fight = 1
                a = 0
                self.plane.get_room(self.player1.where_now()).set_id(0)
            elif self.player1.get_hp() <= 0:
                print("Koniec gry. Zostałeś pokonany przez {}.".format(name))
                if name=="smok":
                    self.bad_end()
                fight = 1
                a = 1
        return a

    def good_end(self):
        print(text.good_end)

    def bad_end(self):
        print(text.bad_end)

    def game(self):
        print(text.intro)
        a = 0
        while a == 0:
            print(self.plane.get_room(self.player1.where_now()).description())

            if self.plane.get_room(self.player1.where_now()).get_id() == 1:
                visit_chest = VisitorInventory(self.plane.get_room(self.player1.where_now()).get_object())
                visit_chest.visit(self.player1)
                print("Znaleziono {}. Dodne do ekwipunku".format(self.plane.get_room(self.player1.where_now()).get_object()))
                self.plane.get_room(self.player1.where_now()).set_id(0)
                self.next_room()
            elif self.plane.get_room(self.player1.where_now()).get_id() == 2:
                a = self.encounter("bandyci")
                if a == 0:
                    self.next_room()
            elif self.plane.get_room(self.player1.where_now()).get_id() == 4:
                a = self.encounter("smok")
            else:
                self.next_room()


