import unittest
import unittest.mock as mock
import source.gotosleep.cogs.misc as misc_cog

class TestMiscCog(unittest.IsolatedAsyncioTestCase):

    @mock.patch("discord.ext.commands.Context", spec=True)    
    async def test_support_server_with_variable_set_sends_invite(self, mock_context):
        support_server_invite = "testinvite"
        test_cog = misc_cog.Misc(support_server_invite)
        await test_cog.support(test_cog, ctx=mock_context)
        mock_context.send.assert_called_with("Here's the invite: " + support_server_invite)

    @mock.patch("discord.ext.commands.Context", spec=True)
    async def test_support_server_without_variable_set_sends_error_message(self, mock_context):
        support_server_invite = ""
        test_cog = misc_cog.Misc(support_server_invite)
        await test_cog.support(test_cog, ctx=mock_context)
        mock_context.send.assert_called_with("Sorry, there doesn't seem to be a support server in this implementation of the bot - this may be a clone of the original source code without one.")

    @mock.patch("discord.ext.commands.Context", spec=True)
    async def test_about_me_sends_message(self, mock_context):
        test_cog = misc_cog.Misc("")
        await test_cog.aboutme(test_cog, ctx=mock_context)
        mock_context.send.assert_called_with('''Hey! I'm the descendant of an older bot, just called "Go To Sleep", and trust me you don't want to see that
            My source is at https://github.com/Lewis-Trowbridge/Go-To-Sleep-Revengeance in case you wanted to know more about me.''')
        
    

if __name__ == '__main__':
    unittest.main()