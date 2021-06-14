import copy
import random
import text


class Prototype:

    def clone(self):
        pass

    def get_id(self):
        pass

    def set_id(self, num):
        pass

    def set_hp(self, num):
        pass

    def description(self):
        pass

    def get_type(self):
        pass

    def get_info(self):
        pass


class ChestWrapper(Prototype):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self._id = 1
        r = random.randint(0, 3)
        if r == 0:
            self.object = "klejnot"
        elif r == 1:
            self.object = "moneta"
        elif r == 2:
            self.object = "pierścień"

    def description(self):
        if self._id != 1:
            return self._wrapped.description()
        else:
            return "{} Znajdujesz skarb!" .format(self._wrapped.description())

    def get_type(self):
        return self._wrapped.get_type()

    def get_id(self):
        return self._id

    def get_object(self):
        return self.object

    def set_id(self, num):
        self._id = num


class BanditsWrapper(Prototype):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.hp = 5
        self.hp_max = 5
        self.diff = 2
        self._id = 2

    def description(self):
        if self._id != 2:
            return self._wrapped.description()
        else:
            return "{} Zostajesz zaatakowany przez bandytów!" .format(self._wrapped.description())

    def get_type(self):
        return self._wrapped.get_type()

    def get_id(self):
        return self._id

    def set_id(self, num):
        self._id = num

    def set_hp(self, num):
        self.hp = num

    def get_hp(self):
        return self.hp

    def get_hp_max(self):
        return self.hp_max

    def get_diff(self):
        return self.diff


class EndWrapper(Prototype):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self._id = 3

    def description(self):
        if self._id != 3:
            return self._wrapped.description()
        else:
            return "{} Musisz zawrócić." .format(self._wrapped.description())

    def get_type(self):
        return self._wrapped.get_type()

    def get_id(self):
        return self._id

    def set_id(self, num):
        self._id = num


class DragonWrapper(Prototype):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.hp = 10
        self.hp_max = 10
        self.diff = 4
        self._id = 4

    def description(self):
        if self._id != 4:
            return self._wrapped.description()
        else:
            return "{} Przed tobą pojawia się smok!".format(self._wrapped.description())

    def get_type(self):
        return self._wrapped.get_type()

    def get_id(self):
        return self._id

    def set_id(self, num):
        self._id = num

    def set_hp(self, num):
        self.hp = num

    def get_hp(self):
        return self.hp

    def get_hp_max(self):
        return self.hp_max

    def get_diff(self):
        return self.diff


class RoomForest(Prototype):
    def __init__(self, info):
        self._type = "las"
        self._info = info
        self._id = 0

    def clone(self):
        return copy.copy(self)

    def description(self):
        return"{}".format(self.get_info())

    def get_type(self):
        return self._type

    def get_info(self):
        return self._info

    def get_id(self):
        return self._id


class RoomDungeon(Prototype):
    def __init__(self, info):
        self._type = "jaskinia"
        self._info = info
        self._id = 0

    def clone(self):
        return copy.copy(self)

    def description(self):
        return"{}".format(self.get_info())

    def get_type(self):
        return self._type

    def get_info(self):
        return self._info

    def get_id(self):
        return self._id


class RoomStreet(Prototype):
    def __init__(self, info):
        self._type = "droga"
        self._info = info
        self._id = 0

    def clone(self):
        return copy.copy(self)

    def description(self):
        return"{}".format(self.get_info())

    def get_type(self):
        return self._type

    def get_info(self):
        return self._info

    def get_id(self):
        return self._id


class RoomMountain(Prototype):
    def __init__(self, info):
        self._type = "góra"
        self._info = info
        self._id = 0

    def clone(self):
        return copy.copy(self)

    def description(self):
        return"{}".format(self.get_info())

    def get_type(self):
        return self._type

    def get_info(self):
        return self._info

    def get_id(self):
        return self._id


class RoomTavern(Prototype):
    def __init__(self, info):
        self._type = "karczma"
        self._info = info
        self._id = 0

    def clone(self):
        return copy.copy(self)

    def description(self):
        return"{}".format(self.get_info())

    def get_type(self):
        return self._type

    def get_info(self):
        return self._info

    def get_id(self):
        return self._id


class ObjectFactory:

    __type1Val = None
    __type2Val = None
    __type3Val = None
    __type4Val = None
    __type5Val = None

    @staticmethod
    def initialize():

        ObjectFactory.__type1Val1 = RoomForest(text.forest1)
        ObjectFactory.__type1Val2 = RoomForest(text.forest2)
        ObjectFactory.__type2Val1 = RoomDungeon(text.dungeon1)
        ObjectFactory.__type2Val2 = RoomDungeon(text.dungeon2)
        ObjectFactory.__type3Val1 = RoomStreet(text.street1)
        ObjectFactory.__type3Val2 = RoomStreet(text.street2)
        ObjectFactory.__type4Val1 = RoomMountain(text.mountain1)
        ObjectFactory.__type4Val2 = RoomMountain(text.mountain2)
        ObjectFactory.__type5Val = RoomTavern(text.tavern)

    @staticmethod
    def get_type1val1():
        return ObjectFactory.__type1Val1.clone()

    @staticmethod
    def get_type2val1():
        return ObjectFactory.__type2Val1.clone()

    @staticmethod
    def get_type3val1():
        return ObjectFactory.__type3Val1.clone()

    @staticmethod
    def get_type4val1():
        return ObjectFactory.__type4Val1.clone()

    @staticmethod
    def get_type1val2():
        return ObjectFactory.__type1Val2.clone()

    @staticmethod
    def get_type2val2():
        return ObjectFactory.__type2Val2.clone()

    @staticmethod
    def get_type3val2():
        return ObjectFactory.__type3Val2.clone()

    @staticmethod
    def get_type4val2():
        return ObjectFactory.__type4Val2.clone()

    @staticmethod
    def get_type5val():
        return ObjectFactory.__type5Val.clone()


