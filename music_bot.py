import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

# Cài đặt thông số cho bot
PREFIX = '$'
TOKEN = 'MTIyNjgzNzA0MDIzMDgzMDEyMQ.Go4rsh.ytf_EbYHDTEUyV6vIHNnlyzfMygrKQKhbW0Qoo'

# Khởi tạo bot
bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("Bạn cần tham gia một kênh thoại trước khi sử dụng lệnh này.")
    else:
        await voice_channel.connect()
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        ydl_opts = {'format': 'bestaudio'}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            voice_client.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('Âm nhạc đã kết thúc'))

@bot.command()
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client is not None:
        await voice_client.disconnect()
    else:
        await ctx.send("Bot không đang ở trong một kênh thoại.")

bot.run(TOKEN)
