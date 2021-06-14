from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from prototype import ObjectFactory


class Builder(ABC):

    def product(self) -> None:
        pass


class ConcreteBuilder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_forest(self) -> None:
        self._product.add(ObjectFactory.get_type1val1())

    def produce_dungeon(self) -> None:
        self._product.add(ObjectFactory.get_type2val1())

    def produce_street(self) -> None:
        self._product.add(ObjectFactory.get_type3val1())

    def produce_mountain(self) -> None:
        self._product.add(ObjectFactory.get_type4val1())

    def produce_forest2(self) -> None:
        self._product.add(ObjectFactory.get_type1val2())

    def produce_dungeon2(self) -> None:
        self._product.add(ObjectFactory.get_type2val2())

    def produce_street2(self) -> None:
        self._product.add(ObjectFactory.get_type3val2())

    def produce_mountain2(self) -> None:
        self._product.add(ObjectFactory.get_type4val2())

    def produce_tavern(self) -> None:
        self._product.add(ObjectFactory.get_type5val())


class Product1:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        return self.parts


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_easy(self) -> None:
        ObjectFactory.initialize()
        self.builder.produce_tavern()
        self.builder.produce_street()
        self.builder.produce_street2()
        self.builder.produce_forest2()
        self.builder.produce_mountain()
        self.builder.produce_mountain2()
        self.builder.produce_street2()
        self.builder.produce_forest()
        self.builder.produce_forest2()
        self.builder.produce_dungeon()
        self.builder.produce_forest()
        self.builder.produce_dungeon2()
        self.builder.produce_dungeon()
        self.builder.produce_dungeon2()
        self.builder.produce_dungeon2()
        self.builder.produce_dungeon()

    def build_test(self) -> None:
        ObjectFactory.initialize()
        self.builder.produce_forest()
        self.builder.produce_tavern()
