from collections import Callable

from triangulum.controllers.base import BaseController


class Login(BaseController):
    def __init__(self, action_handler: Callable):
        super().__init__(action_handler=action_handler, controller='login')

    async def logout(self) -> dict:
        """Logs you out of the game

        This invalidates your session
        """
        return await self.invoke_action(
            action='logout'
        )
