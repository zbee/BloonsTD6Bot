import logging

import config
from bot import Bot
from tower import Tower
class DarkCastleBot(Bot):

    def __init__(self):
        super().__init__()
        self._name = 'Dark Castle on Hard'

    def navigate_to(self):
        logging.info('Navigating to map {}'.format(self._name))
        Bot.click_on(config.BUTTON_MENU_PLAY)
        Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)

        if not Bot._is_present(self, config.MAPS_DARK_CASTLE):
            Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)
        
        Bot.click_on(config.MAPS_DARK_CASTLE)

        Bot.click_on(config.BUTTON_MENU_DIFF_HARD)
        Bot.click_on(config.BUTTON_MENU_STANDARD_MODE)

    # Single game
    def _play_game(self):
        self._load_game(self.navigate_to)
        self._wait_for_map_load()

        Tower(self, 'hero', config.HOTKEY_HERO, config.MAPS_POS_DARK_CASTLE_INTERSECTION_TOP)

        logging.info('Starting game')
        self._start_game()

        dart = Tower(self, 'dart', config.HOTKEY_TOWER_DART_MONKEY, config.MAPS_POS_DARK_CASTLE_BOTTOM_RIGHT_MAIN_ROAD)

        logging.info("Waiting until round 6")
        self.wait_for(config.MAPS_ROUND_DARK_CASTLE_6)

        ninja = Tower(self, 'ninja', config.HOTKEY_TOWER_NINJA, config.MAPS_POS_DARK_CASTLE_INTERSECTION_BOTTOM)
        ninja.upgrade(1, 1)
        ninja.upgrade(3, 1)
        ninja.upgrade(1, 3)

        logging.info("Waiting until round 24")
        self.wait_for(config.MAPS_ROUND_DARK_CASTLE_24)

        super_monkey = Tower(self, 'super', config.HOTKEY_TOWER_SUPER_MONKEY, config.MAPS_POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD)
        super_monkey.upgrade(1, 2)
        super_monkey.upgrade(3, 2)

        dart.upgrade(3, 3)

        super_monkey.upgrade(3, 3)

        # maybe an alchemist

        self._wait_for_game_completion()
        self._game_completed()


if __name__ == '__main__':
    bot = DarkCastleBot()
    bot.main(required_hero='obyn')
