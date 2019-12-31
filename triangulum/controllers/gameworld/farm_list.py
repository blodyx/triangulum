from typing import Union, Callable

from triangulum.controllers.base import BaseController
from triangulum.utils.dataclasses import RomanUnits, TeutonUnits, GaulUnits


class FarmList(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='farmList')

    def toggle_entry(self, village_id: int, list_id: int) -> dict:
        """UNKNOWN

        Args:
            village_id: ID of a village
            list_id: ID of a farm list

        Returns:
            dict
        """
        return self.invoke_action(
            action='toggleEntry',
            params={
                'villageId': village_id,
                'listId': list_id,
            }
        )

    def get_attack_info(self, current_village_id: int, farm_list_ids: list) -> dict:
        """Get info about a potential attack before launching, which will inform you
        of any errors such as unable to attack due to player having been banned

        Args:
            current_village_id: ID of the village the farm list is being accessed from
            farm_list_ids: List of farm list IDs to run checks for

        Returns:
            dict
        """
        return self.invoke_action(
            action='getAttackInfo',
            params={
                'currentVillageId': current_village_id,
                'farmlistIds': farm_list_ids,
            }
        )

    def edit_troops(self, entry_ids: list, units: Union[RomanUnits, TeutonUnits, GaulUnits]) -> dict:
        """Edit the assignment of attack units for entries in a farm list

        Args:
            entry_ids: List of IDs of entries in the farm list
            units: Units assigned for the entries in entry_ids

        Returns:
            dict
        """
        return self.invoke_action(
            action='editTroops',
            params={
                'entryIds': entry_ids,
                'units': units.without_zeros(),
            }
        )

    def create_list(self, name: str) -> dict:
        """Create a new farm list

        Args:
            name: Name of the farm list

        Returns:
            dict
        """
        return self.invoke_action(
            action='createList',
            params={
                'name': name,
            }
        )

    def copy_entry(self, village_id: int, new_list_id: int, entry_id: int) -> dict:
        """Copy a farm list entry from one farm list into another

        Args:
            village_id: ID of the village the farm list is being accessed from *
            new_list_id: ID of the farm list an entry is to be copied into
            entry_id: ID of the entry in the farm list from which we're copying over

        Returns:
            dict
        """
        return self.invoke_action(
            action='copyEntry',
            params={
                'villageId': village_id,
                'newListId': new_list_id,
                'entryId': entry_id,
            }
        )

    def delete_list(self, list_id: int) -> dict:
        """Delete a farm list

        Args:
            list_id: ID of the farm list

        Returns:
            dict
        """
        return self.invoke_action(
            action='deleteList',
            params={
                'listId': list_id,
            }
        )

    def delete_entry(self, entry_id: int) -> dict:
        """Delete an entry in a farm list

        Args:
            entry_id: ID of a farm list entry to be deleted

        Returns:
            dict
        """
        return self.invoke_action(
            action='deleteEntry',
            params={
                'entryId': entry_id,
            }
        )

    def check_target(self, village_id: int) -> dict:
        """UNKNOWN, possibly target check done prior to adding an entry to a farm list *

        Args:
            village_id: ID of a farm list entry candidate

        Returns:
            dict
        """
        return self.invoke_action(
            action='checkTarget',
            params={
                'villageId': village_id,
            }
        )

    def add_entry(self, village_id: int, list_id: int) -> dict:
        """Add a new entry to a farm list

        Args:
            village_id: ID of a village to be added to the farm list
            list_id: ID of the farm list

        Returns:
            dict
        """
        return self.invoke_action(
            action='addEntry',
            params={
                'villageId': village_id,
                'listId': list_id,
            }
        )

    def edit_list(self, name: str, list_id: int) -> dict:
        """Edit the name of a farm list

        Args:
            name: New name for the farm list
            list_id: ID of the farm list

        Returns:

        """
        return self.invoke_action(
            action='editList',
            params={
                'name': name,
                'listId': list_id,
            }
        )

    def change_list_order(self, list_ids: list) -> dict:  # TODO: Check this
        """Change the order of farm lists in your farm lists view

        Args:
            list_ids: Ordered list of farm list IDs in which to sort the farm lists

        Returns:
            dict
        """
        return self.invoke_action(
            action='changeListOrder',
            params={
                'listIds': list_ids,
            }
        )
