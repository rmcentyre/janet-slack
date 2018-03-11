import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

from . import constants as c


class Monster(object):

    def __init__(self, monster_name):
        self.page = requests.get(
            f'{c.BASE_URL}/monster/{monster_name.lower()}'
        ).content  # TODO: Add check if monster_name is valid

        soup = BeautifulSoup(self.page, 'html.parser')

        self.tables = soup.findAll('table')

    def quests(self):
        """
        Find, clean, and return monster quest data
        :return: JSON of quest data
        """

        table = self.tables[0]
        data = []

        for string in table.stripped_strings:
            quest = {
                'Type': string[string.find('[')+1 : string.find(']')].strip(),
                'Stars': re.search(r'\d', string).group(),
                'Name': string[string.find('★')+1:].strip()
            }

            data.append(quest)

        return data

    def weakness(self):
        """
        Find, clean, and return monster weakness data
        :return: JSON of quest data
        """

        element_columns = {'Fir': 'Fire', 'Wat': 'Water', 'Thn': 'Thunder', 'Ice': 'Ice', 'Drg': 'Dragon'}
        # status_columns = {'Poison': 'Poison', 'Sleep': 'Sleep', 'Paralysis': 'Paralysis', 'Blast': 'Blast', 'Stun': 'Stun'}
        status_columns = {'Stun': 'Stun'}  # other status affects aren't listed

        table = self.tables[1]
        data = pd.read_html(str(table), skiprows=1)[0]
        element_data = data[list(element_columns.keys())].rename(columns=element_columns)
        element_data = element_data.sum()
        status_data = data[list(status_columns.keys())].rename(columns=status_columns)
        status_data = status_data.sum()

        return {'Element Weaknesses': element_data.to_dict(), 'Status Weaknesses': status_data.to_dict()}

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