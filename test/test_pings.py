import datetime
import unittest
import unittest.mock as mock
import discord
import source.gotosleep.pings as pings
from freezegun import freeze_time

class TestPings(unittest.TestCase):

    @freeze_time("2000-01-01")
    def test_is_bedtime_with_no_offset_at_midnight_returns_true(self):
        real_result = pings.is_bedtime(datetime.timedelta(), 0, 0, 0)    

        self.assertTrue(real_result)

    @freeze_time("2000-01-01 01:00:00")
    def test_is_bedtime_with_no_offset_not_at_midnight_returns_false(self):
        real_result = pings.is_bedtime(datetime.timedelta(), 0, 0, 0)

        self.assertFalse(real_result)

    @freeze_time("2000-01-01 01:00:00")
    def test_is_bedtime_with_ntp_offset_at_midnight_returns_true(self):
        test_ntp_offset = datetime.timedelta(hours=-1)

        real_result = pings.is_bedtime(test_ntp_offset, 0, 0, 0)

        self.assertTrue(real_result)

    @freeze_time("2000-01-01 01:00:00")
    def test_is_bedtime_with_utc_offset_at_midnight_returns_true(self):
        test_utc_offset = -3600

        real_result = pings.is_bedtime(datetime.timedelta(), test_utc_offset, 0, 0)

        self.assertTrue(real_result)
    
    @freeze_time("1999-12-31 23:00:00")
    def test_is_bedtime_with_dst_offset_at_midnight_returns_true(self):
        test_dst_offset = 3600

        real_result = pings.is_bedtime(datetime.timedelta(), 0, test_dst_offset, 0)

        self.assertTrue(real_result)

    @freeze_time("2000-01-01")
    def test_is_bedtime_with_no_offset_at_midnight_with_bedtime_at_1AM_returns_false(self):
        test_bedtime = 3600

        real_result = pings.is_bedtime(datetime.timedelta(), 0, 0, test_bedtime)

        self.assertFalse(real_result)

    @freeze_time("2000-01-01 01:00:00")
    def test_is_bedtime_with_no_offset_at_1AM_with_bedtime_at_1AM_returns_true(self):
        test_bedtime = 3600

        real_result = pings.is_bedtime(datetime.timedelta(), 0, 0, test_bedtime)

        self.assertTrue(real_result)


    @freeze_time("2000-01-01")
    def test_is_bedtime_with_offset_at_1AM_with_bedtime_at_1AM_returns_true(self):
        test_bedtime = 3600
        test_utc_offset = 3600

        real_result = pings.is_bedtime(datetime.timedelta(), test_utc_offset, 0, test_bedtime)

        self.assertTrue(real_result)

    @mock.patch('discord.Member')
    def test_is_available_when_online_returns_true(self, mock_member):
        mock_member.status = discord.Status.online

        real_value = pings.is_available(mock_member, False)

        self.assertTrue(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_offline_returns_false(self, mock_member):
        mock_member.status = discord.Status.offline

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_dnd_returns_false(self, mock_member):
        mock_member.status = discord.Status.dnd

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_idle_returns_false(self, mock_member):
        mock_member.status = discord.Status.idle

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_invisible_returns_false(self, mock_member):
        mock_member.status = discord.Status.invisible

        real_value = pings.is_available(mock_member, False)

        self.assertFalse(real_value)
    
    @mock.patch('discord.Member')
    def test_is_available_when_online_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.online

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_offline_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.offline

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_dnd_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.dnd

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_idle_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.idle

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

    @mock.patch('discord.Member')
    def test_is_available_when_invisible_with_aggressive_returns_true(self, mock_member):
        mock_member.status = discord.Status.invisible

        real_value = pings.is_available(mock_member, True)

        self.assertTrue(real_value)

if __name__ == '__main__':
    unittest.main()