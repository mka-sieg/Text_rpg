class Player:
    def __init__(self):
        self._objects = []
        self._previous_room = 0
        self._temp_room = 0
        self.hp = 10
        self.max_hp = 10
        self.encounter = False

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_inventory(self):
        return self._objects

    def where_now(self):
        return self._temp_room

    def where_previous(self):
        return self._previous_room

    def accept(self, visitor):
        visitor.visit(self)

    def update(self, visitor):
        self._previous_room = self._temp_room
        self._temp_room = visitor.next_room

    def update_hp(self, visitor):
        self.hp = visitor.hp

    def update_inventory(self, visitor):
        self._objects.append(visitor.object)
