import unittest
import unittest.mock as mock
import discord
import source.gotosleep.pings as pings

class TestPings(unittest.TestCase):

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_online_returns_true(self, mock_member):
        mock_member.status = discord.Status.online

        real_value = pings.is_available(mock_member, False)

        self.assertTrue(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_offline_returns_false(self, mock_member):
        mock_member.status = discord.Status.offline

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_dnd_returns_false(self, mock_member):
        mock_member.status = discord.Status.dnd

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_idle_returns_false(self, mock_member):
        mock_member.status = discord.Status.idle

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_invisible_returns_false(self, mock_member):
        mock_member.status = discord.Status.invisible

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)
    
    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_online_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.online

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_offline_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.offline

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_dnd_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.dnd

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_idle_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.idle

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member', autospec=True)
    def test_is_available_when_invisible_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.invisible

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

if __name__ == '__main__':
    unittest.main()