import discord
from discord.ext import commands

from req_from_dbuff import get_tuple_winrates
from damage_month import get_hero_damage
from most_used_items import get_list_items

from api_key_discord_bot import API_KEY_BOT

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'READY! LOGGED AS {bot.user}')


@bot.command(aliases = ['helpme'])
async def help_command(ctx):
    await ctx.send('/show winrate - get list of heroes winrate\n/show damage - most damage hero this month'
                    '/sborka \'hero\' - get list of most used items on hero')


@bot.command(aliases = ['sborka'])
async def itemlist(ctx, arg):
    list = get_list_items(arg)
    string_out =  f'SBORKA NA {arg.upper()}\nHERO    MATCHES  WINS  WINRATE\n'
    for item in list:
        string_out += item + '\n'
    await ctx.send(string_out)



@bot.command(aliases = ['show'])
async def show_winrate(ctx, arg):
    if arg == 'winrate':
        dict_winrates = get_tuple_winrates()
        await ctx.send(f'{ctx.author} called command \'show winrate\'\n')
        string_out = 'HIGHEST WINRATES THIS MONTH\n' 
        index = 1
        for k,v in dict_winrates.items():
            string_out += f'{index}. {k} - {v[0:4]}%\n'
            index +=1
        await ctx.send(string_out)
    elif arg == 'damage':
        dict_damage = get_hero_damage()
        await ctx.send(f'{ctx.author} called command \'show damage\'\n')
        string_out = 'HIGHEST HEROES\'S DAMAGE PER MINUTE THIS MONTH\n'
        index = 1
        for k,v in dict_damage.items():
            string_out += f'{index}. {k} - {v}\n'
            index += 1
        await ctx.send(string_out)
    else:
        await ctx.send('Unknown command!')


bot.run(API_KEY_BOT)
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}')

#     async def on_message(self,message):
#         print(f'Message from {message.author} : {message.content}')

    

# client = MyClient(intents=discord.Intents.all())  # vajno dlya messag otobrajeniya

#client.run('token')