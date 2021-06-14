
def test_viewer():
    from facade import Facade
    facade = Facade()
    facade.attach(facade)
    facade.button="test"

    assert facade._test == "info"

def test_visitorinventory():
    from player import Player
    from visitor import VisitorInventory

    player = Player()

    visitor = VisitorInventory("coś")
    player.accept(visitor)

    assert player.get_inventory() == ["coś"]


def test_visitorhp():
    from player import Player
    from visitor import VisitorHp

    player= Player()

    visitor = VisitorHp(5)
    player.accept(visitor)

    assert player.get_hp() == 5

def test_visitornextroom():
    from player import Player
    from visitor import VisitorNextRoom

    player = Player()

    visitor = VisitorNextRoom(5)
    player.accept(visitor)

    assert player.where_now() == 5
def test_prototype():
    from prototype import ObjectFactory
    ObjectFactory.initialize()
    instance1=ObjectFactory.get_type1val1()
    instance2 = ObjectFactory.get_type1val1()
    assert instance2.get_type() == instance1.get_type()
def test_builder():
    from builder import Director, ConcreteBuilder1
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder
    director.build_test()
    list=builder.product.list_parts()
    for i in range(len(list)):
        list[i]=list[i].get_type()
    assert list ==["las","karczma"]

def test_decorator():
    from builder import Director, ConcreteBuilder1
    from prototype import EndWrapper
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder
    director.build_test()
    list = builder.product.list_parts()
    list[0]=EndWrapper(list[0])
    assert list[0].get_id() == 3