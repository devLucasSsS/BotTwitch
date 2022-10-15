from twitchio.ext import commands

def app(event):
    print(event)
    TOKEN = "oauth:o8gapeamhl62m8h2p1mivx3bshn84k"
    class Bot(commands.Bot):
        def __init__(self):
            super().__init__(token=TOKEN, prefix='!', initial_channels=['lucassss14'])
        async def event_ready(self):
            print(f'Logged in as | {self.nick}')
        async def event_message(self, ctx):
            if ctx.echo: #Esto evita que el bot se conteste a si mismo y remplaza la forma anterior
                return
            if(ctx.content.lower() == "!subathon"):
                await ctx.channel.send("DONATION INCENTIVES: $3 (or 1 sub) Guaranteed Map request | $5 (or 2 gift subs) Replay review | $7 (or 3 gift subs) Profile review or 1v1 | $10 (or 5 gift subs) Profile review + Replay review (you choose the replay) + 1v1 | $20 Profile review instantly")
            if(ctx.content.lower() == "!afk"):
                await ctx.channel.send("Mathi will be back in a few minutes.")
            if(ctx.content.lower() == "!ping"):
                await ctx.channel.send("pong.")
            await self.handle_commands(ctx)
    bot = Bot()
    bot.run()