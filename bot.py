import discord
import os
import random 
import requests
from discord.ext import commands
from main import gen_pass
from main import gen_gombalan
from main import transportasi
from main import mengurangi
from main import menghemat

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, count_gen_pass = 10):
    await ctx.send(gen_pass(count_gen_pass))

@bot.command()
async def gombalan(ctx):
    gombalan = gen_gombalan()
    await ctx.send(gombalan)

@bot.command()
async def tips_transportasi(ctx):
    tips_transportasi = transportasi()
    await ctx.send(tips_transportasi)

@bot.command()
async def tips_mengurangi(ctx):
    tips_mengurangi = mengurangi()
    await ctx.send(tips_mengurangi)

@bot.command()
async def tips_menghemat(ctx):
    tips_menghemat = menghemat()
    await ctx.send(tips_menghemat)

@bot.command()
async def coding(ctx):
    random_meme = random.choice(os.listdir('images'))
    with open('images/'+random_meme, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    rando_animals = random.choice(os.listdir('animal_memes'))
    with open('animal_memes/'+rando_animals, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('quack')
async def quack(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('woof')
async def woof(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


bot.run("")
