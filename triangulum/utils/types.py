from datetime import datetime

from triangulum.utils.util import coordinates_to_map_id, filter_value_to_enums


class EmptyType(Exception):
    """Type has been instantiated without any parameters"""


class ScalarId(int):
    pass


class BoolInt(int):
    pass


class LocationId(int):
    pass


class BuildingLvl(int):
    pass


class TroopId(int):
    pass


class MapId(int):
    def __new__(cls, map_id=None, x=None, y=None):
        if not map_id:
            if not x and not y:
                raise EmptyType('map_id or x and y required')

        if not map_id:
            map_id = coordinates_to_map_id(x=x, y=y)

        new = super().__new__(cls, map_id)
        new.x = x
        new.y = y

        return new

    @property
    def as_dict(self):
        return {
            'x': self.x,
            'y': self.y
        }

    @property
    def as_map_id(self):
        return coordinates_to_map_id(x=self.x, y=self.y)


class Timestamp(int):

    @property
    def as_t5_timestamp(self):
        return int('{:.2f}'.format(self.real).replace('.', ''))

    @property
    def as_datetime(self):
        return datetime.fromtimestamp(float(self.real))

    @property
    def as_datetime_string(self):
        return str(self.as_datetime)


class FilterScalar(int):
    def __new__(cls, value, enum):
        new = super().__new__(cls, value)
        new.enum = enum

        return new

    @property
    def as_enums(self):
        return filter_value_to_enums(enum=self.enum, value=self.real)


class ResourceFieldDistribution(int):
    """Denotes the distribution of different resource fields in a given village type

    5346 means there's 5 wood, 3 clay, 4 iron and 6 crop fields
    The different possible types are:
        4446
        5346
        5436
        6336
        3546
        4536
        3636
        3456
        4356
        3366
        11115
        3339
        4337
        3437
        3347
    """

    @property
    def _distribution(self):
        if self.real == 11115:  # 15c
            return 1, 1, 1, 15
        else:
            wood, clay, iron, crop = list(str(self.real))
            return int(wood), int(clay), int(iron), int(crop)

    @property
    def wood(self):
        return self._distribution[0]

    @property
    def clay(self):
        return self._distribution[1]

    @property
    def iron(self):
        return self._distribution[2]

    @property
    def crop(self):
        return self._distribution[3]
