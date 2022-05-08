import logging
import config
from bot import Bot
from tower import Tower

class InfernoDeflationBot(Bot):

    def __init__(self):
        super().__init__()
        self._name = 'Inferno on Deflation'

    def navigate_to(self):
        logging.info('Navigating to map {}'.format(self._name))
        Bot.click_on(config.BUTTON_MENU_PLAY)
        Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)

        if not Bot._is_present(self, config.MAPS_INFERNO):
            Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)
        
        Bot.click_on(config.MAPS_INFERNO)

        Bot.click_on(config.BUTTON_MENU_DIFF_EASY)
        Bot.click_on(config.BUTTON_MENU_DEFLATION_MODE)

    # Single game
    def _play_game(self):
        self._load_game(self.navigate_to)
        self._wait_for_map_load()

        # Click ok in popup that explains the special mode rules, only on first game
        if self._game_counter == 1:
            logging.info('Dismiss rule popup')
            self.wait_for(config.BUTTON_OVERWRITE_OK)
            self.click_on(config.BUTTON_OVERWRITE_OK)

        logging.info('Place right sniper with path 0-2-4')

        sniperRight = Tower(self, 'sniper', config.HOTKEY_TOWER_SNIPER, config.MAPS_POS_INFERNO_ISLAND_RIGHT_SNIPER)
        sniperRight.upgrade(2, 2)
        sniperRight.upgrade(3, 4)

        logging.info('Starting game')
        self._start_game()

        logging.info('Place left sniper with path 0-2-4')

        sniperLeft = Tower(self, 'sniper', config.HOTKEY_TOWER_SNIPER, config.MAPS_POS_INFERNO_ISLAND_LEFT_SNIPER)
        sniperLeft.upgrade(2, 2)
        sniperLeft.upgrade(3, 4)

        logging.info('Place right alchemist with path 3-2-0')

        alchemistRight = Tower(self, 'alchemist', config.HOTKEY_TOWER_ALCHEMIST, config.MAPS_POS_INFERNO_ISLAND_RIGHT_ALCHEMIST)
        alchemistRight.upgrade(1, 3)
        alchemistRight.upgrade(2, 2)

        logging.info('Place left alchemist with path 2-0-0')

        alchemistLeft = Tower(self, 'alchemist', config.HOTKEY_TOWER_ALCHEMIST, config.MAPS_POS_INFERNO_ISLAND_LEFT_ALCHEMIST)
        alchemistLeft.upgrade(1, 2)

        logging.info('Finished with hero placement')

        logging.info('Deflation mode -> chill')

        self._wait_for_game_completion()
        self._game_completed()


if __name__ == '__main__':
    bot = InfernoDeflationBot()
    bot.main()
