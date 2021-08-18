from discord.ext import commands

class Misc(commands.Cog):

    support_server_invite = ""

    def __init__(self, support_server_invite) -> None:
        self.support_server_invite = support_server_invite

    @commands.command(pass_context=True)
    async def support(self, ctx: commands.Context):

        """
        Gives you the link for the support server

        If there's a problem you can't solve, go here to the support server! Try to give as much detail as possible please, as that will make it easier to solve
        """
        if self.support_server_invite != "":
            await ctx.send("Here's the invite: " + self.support_server_invite)
        else:
            await ctx.send("Sorry, there doesn't seem to be a support server in this implementation of the bot - this may be a clone of the original source code without one.")


    @commands.command(pass_context=True)
    async def aboutme(self, ctx: commands.Context):

        """
        Tells you all about me

        There's not much to this one - it's just telling you why I'm named like this and where you can find out more.
        """
        await ctx.send('''Hey! I'm the descendant of an older bot, just called "Go To Sleep", and trust me you don't want to see that
            My source is at https://github.com/Lewis-Trowbridge/Go-To-Sleep-Revengeance in case you wanted to know more about me.''')
