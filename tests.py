
import unittest
import janet
import plugins


class BasicFullTest(unittest.TestCase):
    def setUp(self):
        self.app = janet.app.test_client()
        self.app.testing = True

    def test_trivial(self):
        response = self.app.get('/')
        assert b"Warning: Not for human consumption!" in response.data

    def test_hello_world(self):
        response = self.app.post("/bot/hello", data=dict(
            token='sesame'
        ))
        assert b"Hello, world!" in response.data

    def tearDown(self):
        pass


class KiranicoFullTest(unittest.TestCase):
    def setUp(self):
        self.monster = plugins.kiranico.Monster("anjanath")

    def test_monster_quests(self):
        anjanath_quests = [
            {'Type': 'Assigned', 'Stars': '4', 'Name': 'The Encroaching Anjanath'},
            {'Type': 'Assigned', 'Stars': '6', 'Name': 'Tickled Pink'},
            {'Type': 'Optional', 'Stars': '4', 'Name': 'One Helluva Sinus Infection'},
            {'Type': 'Optional', 'Stars': '4', 'Name': 'Special Arena: Anjanath'},
            {'Type': 'Optional', 'Stars': '6', 'Name': "It Can't See You if You Don't Move"},
            {'Type': 'Optional', 'Stars': '6', 'Name': 'Trespassing Troublemaker'},
            {'Type': 'Optional', 'Stars': '6', 'Name': 'Special Arena: HR Anjanath'}
        ]
        assert(self.monster.quests() == anjanath_quests)

    def test_monster_weaknesses(self):
        anjanath_weaknesses = {
            'Element Weaknesses': {'Fire': 0, 'Water': 200, 'Thunder': 80, 'Ice': 135, 'Dragon': 35},
            'Status Weaknesses': {'Stun': 200}
        }
        assert(self.monster.weakness() == anjanath_weaknesses)


if __name__ == '__main__':
    unittest.main()
