from builder import Director, ConcreteBuilder1
from prototype import DragonWrapper, BanditsWrapper, EndWrapper, ChestWrapper


def get_wrapper(list_rooms):
    list_rooms[5] = EndWrapper(list_rooms[5])
    list_rooms[6] = EndWrapper(list_rooms[6])
    list_rooms[10] = BanditsWrapper(list_rooms[10])
    list_rooms[13] = ChestWrapper(list_rooms[13])
    list_rooms[14] = ChestWrapper(list_rooms[14])
    list_rooms[15] = DragonWrapper(list_rooms[15])
    return list_rooms


class Plane:
    def __init__(self):
        self._num_rooms = 20
        self._rooms_list = []
        self._rooms_map = {0:[1,3,2],1:[0,6],2:[0,7],3:[0,4,7,10],4:[3,5,9],5:[4],6:[1],7:[2,3,9,8],8:[7,0],9:[4,7,11],10:[3],11:[9,12],12:[11,13,15],13:[12,14],14:[13,15],15:[12,14]}

    def set_room_list(self, list_r):
        self._rooms_list = list_r

    def get_room_list(self):
        return self._rooms_list

    def get_room_map(self):
        return self._rooms_map

    def set_num_rooms(self, num):
        self._num_rooms = num

    def start(self):
        print("tworzenie planszy")
        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder
        director.build_easy()
        list_rooms = builder.product.list_parts()
        list_rooms = get_wrapper(list_rooms)
        self.set_room_list(list_rooms)
        self.set_num_rooms(len(list_rooms))

    def get_room(self, num):
        list_r = self.get_room_list()
        return list_r[num]

    def go_next(self, now):
        return self.get_room_map()[now]

    def print_out(self, list_r, prev_room):
        for i in range(0,len(list_r)):
            if list_r[i] == prev_room:
                print(i, " - ", self.get_room(list_r[i]).get_type(), "(powrót)")
            else:
                print(i, " - ", self.get_room(list_r[i]).get_type())

    def get_room_name(self, num):
        list_r = self.get_room_list()
        return list_r[num].get_type()
