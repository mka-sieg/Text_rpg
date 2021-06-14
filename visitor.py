class Visitor:
    def __str__(self):
        return self.__class__.__name__


class VisitorNextRoom(Visitor):
    def __init__(self, next_room):
        self._next_room = next_room

    @property
    def next_room(self):
        return self._next_room

    @next_room.setter
    def next_room(self, value):
        self._next_room = value

    def visit(self, crop):
        crop.update(self)


class VisitorInventory(Visitor):
    def __init__(self, ob):
        self._object = ob

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        self._object = value

    def visit(self, crop):
        crop.update_inventory(self)


class VisitorHp(Visitor):
    def __init__(self, hp):
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    def visit(self, crop):
        crop.update_hp(self)
