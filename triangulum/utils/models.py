from dataclasses import dataclass
from enum import Enum
from typing import List

from triangulum.utils.enums import RomanUnit, TeutonUnit, GaulUnit, MarkerType, MarkerColor, MarkerEditType, \
    MarkerDuration, FieldMessageType, MapFilterValues, AttacksFilterValues, Resource, HeroItemBonus, PlayerTribe, \
    HeroItemType, AuctionStatus, HeroItemSlot, Country, PlayerPunishmentStrikeReason
from triangulum.utils.types import ScalarId, Timestamp
from triangulum.utils.util import unit_id_to_unit_nr


@dataclass
class _Base:
    def __iter__(self):
        for key, val in self.__dict__.items():
            if not key.startswith('_'):
                yield key, val


@dataclass
class _Units(_Base):
    _ENUM: Enum

    def with_zeros(self):
        return {
            str(self._ENUM[unit_name].value): unit_qty
            for unit_name, unit_qty in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[unit_name].value): unit_qty
            for unit_name, unit_qty in dict(self).items() if unit_qty > 0
        }

    def combat_format_with_zeros(self):
        return {
            str(unit_id_to_unit_nr(self._ENUM[unit_name].value)): unit_qty
            for unit_name, unit_qty in dict(self).items()
        }

    def combat_format_without_zeros(self):
        return {
            str(unit_id_to_unit_nr(self._ENUM[unit_name].value)): unit_qty
            for unit_name, unit_qty in dict(self).items() if unit_qty > 0
        }


@dataclass
class RomanUnits(_Units):
    _ENUM: Enum = RomanUnit
    _TRIBE: PlayerTribe = PlayerTribe.ROMAN.value

    LEGIONNAIRE: int = 0
    PRAETORIAN: int = 0
    IMPERIAN: int = 0
    EQUITES_LEGATI: int = 0
    EQUITES_IMPERATORIS: int = 0
    EQUITES_CAESARIS: int = 0
    BATTERING_RAM: int = 0
    FIRE_CATAPULT: int = 0
    SENATOR: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class TeutonUnits(_Units):
    _ENUM: Enum = TeutonUnit
    _TRIBE: PlayerTribe = PlayerTribe.TEUTON.value

    CLUBSWINGER: int = 0
    SPEARFIGHTER: int = 0
    AXEFIGHTER: int = 0
    SCOUT: int = 0
    PALADIN: int = 0
    TEUTONIC_KNIGHT: int = 0
    RAM: int = 0
    CATAPULT: int = 0
    CHIEF: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class GaulUnits(_Units):
    _ENUM: Enum = GaulUnit
    _TRIBE: PlayerTribe = PlayerTribe.GAUL.value

    PHALANX: int = 0
    SWORDSMAN: int = 0
    PATHFINDER: int = 0
    THEUTATES_THUNDER: int = 0
    DRUIDRIDER: int = 0
    HAEDUAN: int = 0
    RAM: int = 0
    TREBUCHET: int = 0
    CHIEFTAIN: int = 0
    SETTLER: int = 0
    HERO: int = 0


@dataclass
class Marker:
    OWNER: int
    TYPE: MarkerType
    COLOR: MarkerColor
    EDIT_TYPE: MarkerEditType
    OWNER_ID: int
    TARGET_ID: int

    def as_dict(self):
        return {
            'owner': self.OWNER,
            'type': self.TYPE,
            'color': self.COLOR,
            'editType': self.EDIT_TYPE,
            'ownerId': self.OWNER_ID,
            'targetId': self.TARGET_ID
        }


@dataclass
class FieldMessage:
    TEXT: str
    TYPE: FieldMessageType
    DURATION: MarkerDuration
    CELL_ID: int
    TARGET_ID: int

    def as_dict(self):
        return {
            'text': self.TEXT,
            'type': self.TYPE,
            'duration': self.DURATION,
            'cellId': self.CELL_ID,
            'targetId': self.TARGET_ID
        }


@dataclass
class _FilterScalar(_Base):
    _ENUM: Enum

    def sum(self):
        scalar = 0

        for toggle_name, toggle_val in dict(self).items():
            if toggle_val:
                scalar += self._ENUM[toggle_name].value

        return scalar


@dataclass
class MapFilter(_FilterScalar):
    _ENUM: Enum = MapFilterValues

    NONE: bool = False
    KINGDOM_BORDERS: bool = True
    CAPITAL_VILAGES: bool = True
    OWN_MARKERS: bool = True
    GAME_MESSAGES: bool = True
    PLAYER_MESSAGES: bool = True
    TREASURES: bool = True


@dataclass
class AttacksFilter(_FilterScalar):
    _ENUM: Enum = AttacksFilterValues

    NONE: bool = False
    KINGDOM: bool = True


@dataclass
class _Resources(_Base):
    _ENUM: Enum

    def with_zeros(self):
        return {
            str(self._ENUM[resource_name].value): resource_qty
            for resource_name, resource_qty in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[resource_name].value): resource_qty
            for resource_name, resource_qty in dict(self).items() if resource_qty > 0
        }


@dataclass
class Resources(_Resources):
    _ENUM = Resource

    WOOD: int
    CLAY: int
    IRON: int
    CROP: int


@dataclass
class Bonuses(_Base):
    _ENUM = HeroItemBonus

    XP: int = None
    BARRACKS: int = None
    STABLE: int = None
    WORKSHOP: int = None
    SPEED_RETURN: int = None
    SPEED_OWN_VILLAGES: int = None
    SPEED_KINGDOM_VILLAGES: int = None
    SPEED_STAMINA: int = None
    RAID: int = None
    NATARS: int = None
    UNIT_ID: int = None
    UNIT_STRENGTH: int = None
    FIGHT_STRENGTH: int = None
    HEALTH_REGEN: int = None
    CULTURE_POINTS: int = None
    ARMOR: int = None
    SPEED_HERO: int = None
    SPEED_HORSE: int = None
    RESKILL: int = None
    TROOP_HEALING: int = None
    EYESIGHT: int = None
    CHICKEN: int = None
    RESOURCES: int = None
    CROP: int = None
    POTION: int = None

    def with_zeros(self):
        return {
            str(self._ENUM[bonus_type].value): bonus_value
            for bonus_type, bonus_value in dict(self).items()
        }

    def without_zeros(self):
        return {
            str(self._ENUM[bonus_type].value): bonus_value
            for bonus_type, bonus_value in dict(self).items() if bonus_value > 0
        }


@dataclass
class Auction(_Base):
    id: ScalarId
    tribe_id: PlayerTribe
    item_type_id: HeroItemType
    strength: int
    bonuses: Bonuses
    amount: int
    status: AuctionStatus
    time_start: Timestamp
    time_end: Timestamp
    price: int
    bids: int
    highest_bid: int
    highest_bidder_player_id: ScalarId
    highest_bidder_name: str
    slot: HeroItemSlot
    images: List[str]  # List of strings such as "artwork", "axe0_2", "helmet2_1" etc
    stackable: bool


@dataclass
class Avatar(_Base):  # Lobby
    user_account_identifier: ScalarId
    avatar_identifier: int
    avatar_name: str
    consumers_id: int
    world_name: str
    country: Country
    account_name: str
    is_banned: bool
    is_suspended: bool
    suspension_time: int
    limitation: int  # TODO: Check what this is, could be an enum, could be PlayerPunishmentType
    ban_reason: PlayerPunishmentStrikeReason
    ban_payment_provider: str