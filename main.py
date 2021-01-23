import discord
import json
import asyncio
import aiohttp
import colorama
import ctypes
import time

from aiohttp import ClientSession
from discord.ext import commands, tasks
from colorama import Fore, Back, Style

colorama.init()

version = .1

ctypes.windll.kernel32.SetConsoleTitleW(f'Trip Self Bot | Version {version} | Loading...')

with open('./config.json') as f:
    config = json.load(f)

prefix = config.get('prefix')
nasakey = config.get('nasa-api')

bot = commands.Bot(description="Trip Self Bot", command_prefix=prefix, self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'''{Fore.RESET}{Fore.MAGENTA}
                                      ███        ▄████████  ▄█     ▄███████▄ 
                                   ▀█████████▄   ███    ███ ███    ███    ███ 
                                      ▀███▀▀██   ███    ███ ███▌   ███    ███ 
                                       ███   ▀  ▄███▄▄▄▄██▀ ███▌   ███    ███ 
                                       ███     ▀▀███▀▀▀▀▀   ███▌ ▀█████████▀  
                                       ███     ▀███████████ ███    ███        
                                      ███       ███    ███ ███    ███        
                                      ▄████▀     ███    ███ █▀    ▄████▀      
                                                 ███    ███                   
                                                    
                                                 
{Fore.BLUE}                                     User | {Fore.CYAN}{bot.user.name}#{bot.user.discriminator}
{Fore.BLUE}                                     Prefix | {Fore.CYAN}{prefix}
{Fore.BLUE}                                     Version | {Fore.CYAN}{version}
  
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'~Trip Self Bot~ | v{version} | Welcome {bot.user.name}#{bot.user.discriminator}')

#text formatting stuff

@bot.command()
async def bold(ctx, *, text: str = "", amount = 0):
    if text == "":
        await ctx.message.delete()
        print(f"{Fore.RED}[Error] {Fore.WHITE}~ {Fore.YELLOW}Include what you want to bold!")
    else:
        await ctx.message.delete()
        await ctx.send(f'**{text}**')

@bot.command()
async def underline(ctx, *, text: str = "", amount = 0):
    if text == "":
        await ctx.message.delete()
        print(f"{Fore.RED}[Error] {Fore.WHITE}~ {Fore.YELLOW}Include what you want to underline!")
    else:
        await ctx.message.delete()
        await ctx.send(f'__{text}__')

@bot.command()
async def italic(ctx, *, text: str = "", amount = 0):
    if text == "":
        await ctx.message.delete()
        print(f"{Fore.RED}[Error] {Fore.WHITE}~ {Fore.YELLOW}Include what you want to italicize!")
    else:
        await ctx.message.delete()
        await ctx.send(f'*{text}*')

#utility

@bot.command(aliases=['av', 'pfp'])
async def avatar(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    await ctx.message.delete()
    userAvatar = member.avatar_url

    embed = discord.Embed(title=f'{member}\'s PFP')
    embed.set_image(url=userAvatar)

    await ctx.send(embed=embed)

@bot.command() #broken
async def bypass(ctx, link):
    await ctx.message.delete()
    url = f'https://bigdonker.herokuapp.com/api?url={link}'

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            bypassedlink = f"{r['bypassedlink'][0]}"

    await ctx.send(f'Bypassed Link - {bypassedlink}')

@bot.command()
async def serverpfp(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.guild.name)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command(aliases=['ip', 'geoip'])
async def iplookup(ctx, *, ip: str):
    await ctx.message.delete()
    url = f'http://ip-api.com/json/{ip}'

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            status = f"{r['status']}"
            ip = f"{r['query']}"
            country = f"{r['country']}"
            city = f"{r['city']}"
            zip = f"{r['zip']}"
            lat = f"{r['lat']}"
            lon = f"{r['lon']}"
            isp = f"{r['isp']}"
            region = f"{r['regionName']}"

    embed = discord.Embed(title=ip)
    embed.add_field(name="Country", value=f'{country}')
    embed.add_field(name="Region", value=f'{region}')
    embed.add_field(name="City", value=f'{city}')
    embed.add_field(name="Zip", value=f'{zip}')
    embed.add_field(name="Lat/Lon", value=f'{lat}, {lon}')
    embed.add_field(name="ISP", value=f'{isp}')
    embed.set_thumbnail(url="https://www.maxpixel.net/static/photo/640/Transceiver-Sender-Gray-Radio-Wifi-Tower-296666.png")

    await ctx.send(embed=embed)

@bot.command()
async def dm(ctx, user: discord.User, message):
    await ctx.message.delete()
    await user.send(message)

#nuke

@bot.command()
async def masschannels(ctx, name="Trip SB On Top"):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=name)
        except:
            return

@bot.command()
async def deletechannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@bot.command()
async def massroles(ctx, name="Trip SB On Top"):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=name)
        except:
            return

@bot.command()
async def deleteroles(ctx):
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

#fun

@bot.command()
async def hug(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/hug"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/kiss"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def slap(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/slap"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def smug(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/smug"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def pat(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/pat"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def tickle(ctx, *, member: discord.Member):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/tickle"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=f'{member}')
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def wallpaper(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/wallpaper"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    url = "https://aws.random.cat/meow?ref=apilist.fun"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['file']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    await ctx.message.delete()
    url = "https://random.dog/woof.json?ref=apilist.fun"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def redditmeme(ctx):
    await ctx.message.delete()
    url = "https://meme-api.herokuapp.com/gimme"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parsetitle = f"{r['title']}"
            parseurl = f"{r['url']}"

    embed = discord.Embed(title=parsetitle)
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def fox(ctx):
    await ctx.message.delete()
    url = "https://randomfox.ca/floof/"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['image']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def insult(ctx):
    await ctx.message.delete()
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            insult = f"{r['insult']}"

    embed = discord.Embed(description=insult)

    await ctx.send(embed=embed)

@bot.command()
async def apod(ctx):
    await ctx.message.delete()
    url = f'https://api.nasa.gov/planetary/apod?api_key={nasakey}'

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            date = f"{r['date']}"
            copyright = f"{r['copyright']}"
            explanation = f"{r['explanation']}"
            image = f"{r['hdurl']}"

    embed = discord.Embed(title="Astronomy Picture of The Day", description=explanation)
    embed.add_field(name="Date", value=date)
    embed.add_field(name="Copyright", value=copyright)
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@bot.command()
async def yesno(ctx):
    await ctx.message.delete()
    url = "https://yesno.wtf/api"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            yesno = f"{r['answer']}"
            gif = f"{r['image']}"

    embed = discord.Embed(title=yesno)
    embed.set_image(url=gif)

    await ctx.send(embed=embed)

@bot.command()
async def whatanime(ctx, link):
    await ctx.message.delete()
    url = f'https://trace.moe/api/search?url={link}'

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            animename = f"{r['docs'][0]['title_english']}"
            episode = f"{r['docs'][0]['episode']}"
            native = f"{r['docs'][0]['title_native']}"
            romaji = f"{r['docs'][0]['title_romaji']}"

    embed = discord.Embed(title=animename)
    embed.add_field(name="Episode", value=episode)
    embed.add_field(name="Native", value=native)
    embed.add_field(name="Romaji", value=romaji)
    embed.set_image(url=link)

    await ctx.send(embed=embed)

@bot.command()
async def uscovid(ctx):
    await ctx.message.delete()
    url = "https://api.covidtracking.com/v1/us/current.json"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            positive = f"{r[0]['positive']}"
            negative = f"{r[0]['negative']}"
            pending = f"{r[0]['pending']}"
            hospitalized = f"{r[0]['hospitalizedCumulative']}"
            inicu = f"{r[0]['inIcuCumulative']}"
            deaths = f"{r[0]['death']}"

    embed = discord.Embed(title="USA Covid-19")
    embed.add_field(name="Confirmed", value=positive)
    embed.add_field(name="Negative", value=negative)
    embed.add_field(name="Pending", value=pending)
    embed.add_field(name="Hospitalized", value=hospitalized)
    embed.add_field(name="In ICU", value=inicu)
    embed.add_field(name="Total Deaths", value=deaths)
    embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/5c4085e585ede1f50f94a4b9/1581018457505-JM3FO6WMFN9BGP3IOE8D/ke17ZwdGBToddI8pDm48kL5hQm_JZO5i_9Equza1B-57gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1URbcWFoTofQNHE0Fe4ADwtkYw2N2aveJw6FaFCcRrQmU3WUfc_ZsVm9Mi1E6FasEnQ/2019-nCoV-CDC-23312_without_background.png")

    await ctx.send(embed=embed)

@bot.command()
async def btc(ctx):
    await ctx.message.delete()
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            usd = f"{r['USD']}"
            eur = f"{r['EUR']}"

    embed = discord.Embed(title="BTC")
    embed.add_field(name="USD", value=f'${usd}')
    embed.add_field(name="EUR", value=f'€{eur}')
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/BTC_Logo.svg/2000px-BTC_Logo.svg.png")

    await ctx.send(embed=embed)

#game stuff

@bot.command()
async def siegestats(ctx, *, username):
    await ctx.message.delete()
    url = f'https://r6.tracker.network/profile/pc/{username}'

    embed = discord.Embed(title=f'{username}\'s Siege Stats', url=url, description=f'Click on the link above!')
    embed.set_thumbnail(url="https://cdn-cf.gamivo.com/image_cover.jpg?f=46475&n=6789365024763794.jpg&h=97e59417aa6eb9d17a7372b2143a7885")

    await ctx.send(embed=embed)

@bot.command()
async def fortnitestats(ctx, *, username):
    await ctx.message.delete()
    url = f'https://fortnitetracker.com/profile/all/{username}'

    embed = discord.Embed(title=f'{username}\'s Fortnite Stats', url=url, description=f'Click on the link above!')
    embed.set_thumbnail(url="https://m.media-amazon.com/images/M/MV5BNTI3YzA5MjAtMzVkYy00MGU5LWJkMTktOTk1M2Y2ZGJkNmRiXkEyXkFqcGdeQXVyOTAzNDAxOTI@._V1_.jpg")

    await ctx.send(embed=embed)

@bot.command()
async def fortniteshop(ctx):
    await ctx.message.delete()
    url = "https://api.nitestats.com/v1/shop/image"

    embed = discord.Embed(title="Todays Item Shop")
    embed.set_image(url=url)

    await ctx.send(embed=embed)

#porn gifs

@bot.command()
async def lesbian(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/les"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def hentai(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/hentai"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def boobs(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/boobs"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command(aliases=['blowjob'])
async def bj(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/bj"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def anal(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/anal"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def trap(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/trap"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

@bot.command()
async def orgasm(ctx):
    await ctx.message.delete()
    url = "https://nekos.life/api/v2/img/gasm"

    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.json()
            parseurl = f"{r['url']}"

    embed = discord.Embed()
    embed.set_image(url=parseurl)

    await ctx.send(embed=embed)

#errors

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        print(f"{Fore.RED}[Error] {Fore.WHITE}~ {Fore.YELLOW}Could not find that user / did not specify correctly!")

token = config.get('token')
bot.run(token, bot=False)