from dataclasses import dataclass
from datetime import datetime
from time import time
from typing import Union

from triangulum.utils.util import map_id_to_coordinates, coordinates_to_map_id


class EmptyType(Exception):
    """Type has been instantiated without any parameters"""


@dataclass
class _Base:
    pass


@dataclass
class ScalarId(_Base):
    id: int


@dataclass
class BoolInt(_Base):
    value: bool

    @property
    def as_bool(self):
        return self.value

    @property
    def as_int(self):
        if self.value:
            return 1
        else:
            return 0


@dataclass
class VillageId(_Base):
    x: int = None
    y: int = None
    id: Union[int, str] = None

    @property
    def as_coords(self):
        if self.x and self.y:
            return self.x, self.y
        elif self.id:
            return map_id_to_coordinates(map_id=int(self.id))
        else:
            raise EmptyType('id or x and y required')

    @property
    def as_id(self):
        if self.id:
            return int(self.id)
        elif self.x and self.y:
            return coordinates_to_map_id(x=self.x, y=self.y)
        else:
            raise EmptyType('id or x and y required')


@dataclass
class Timestamp(_Base):
    value: float = time()

    @property
    def as_t5_timestamp(self):
        return int('{:.2f}'.format(self.value).replace('.', ''))

    @property
    def as_datetime(self):
        return datetime.fromtimestamp(self.value)

    @property
    def as_datetime_string(self):
        return str(self.as_datetime)
