import re

import requests
from bs4 import BeautifulSoup

from . import constants as c


class Monster(object):
    def __init__(self, monster_name):
        self.page = requests.get(
            f'{c.BASE_URL}/monster/{monster_name.lower()}'
        ).content  # TODO: Add check if monster_name is valid

        soup = BeautifulSoup(self.page, 'lxml')

        self.tables = soup.findAll('table')

    def quests(self):
        """
        Find, clean, and return monster quest data
        :return: JSON of quest data
        """

        table = self.tables[0]
        data = []

        for str in table.stripped_strings:
            quest = {
                'Type': str[str.find('[')+1 : str.find(']')].strip(),
                'Stars': re.search(r'\d', str).group(),
                'Name': str[str.find('★')+1:].strip()
            }

            data.append(quest)

        return data

    def weakness(self):
        """
        Find, clean, and return monster weakness data
        :return: JSON of quest data
        """

        # TODO: Build the function

        pass

    def lr_loot(self):
        """
        Find, clean, and return drops from Low Rank
        :return: JSON of LR drop data
        """

        # TODO: The thing

        pass

    def hr_loot(self):
        """
        Find, clean, and return drops from High Rank
        :return: JSON of HR drop data
        """

        # TODO: The other thing

        pass