import pyautogui as pag
import keyboard
import logging
import time

import config


class Tower:
    def __init__(self, bot, name, hotkey, position):
        self._name = name
        self._bot = bot
        self._bot.wait_for(position)
        self._position = self._bot.wait_location
        self._hotkey = hotkey
        self._upgrades = [0, 0, 0]
        logging.info('Placing {}'.format(self._name))
        pag.moveTo(self._position)
        keyboard.send(self._hotkey)
        time.sleep(1)
        pag.click()

    @staticmethod
    def _upgrade_track(track):
        keyboard.send(config.HOTKEY_UPGRADES[track - 1])

    def _tower_upgrades_to_string(self, track, to_level):
        string = ''
        for i, upgrade_level in enumerate(self._upgrades):
            string += str(to_level) if i + 1 == track else str(upgrade_level)
        return string

    def upgrade(self, track, to_level):
        if track > 3 or to_level > 5:
            logging.error('Track ({}) or level ({}) is too high'.format(track, to_level))
            raise ValueError('Track ({}) or level ({}) is too high'.format(track, to_level))
        pag.click(self._position)
        for i in range(to_level - self._upgrades[track - 1]):
            tower_upgrade_text = self._tower_upgrades_to_string(track, self._upgrades[track - 1] + i + 1)
            logging.info('Waiting for {} {} to become available'.format(self._name, tower_upgrade_text))
            self._bot.wait_for('resources/towers/{}/upgrade_{}_{}.jpg'.format(self._name, track, self._upgrades[track - 1] + i + 1))
            self._upgrade_track(track)
            logging.info('Upgraded {} to {}'.format(self._name, tower_upgrade_text))
        self._upgrades[track - 1] = to_level
        pag.click(self._position)
