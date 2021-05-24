import discord
from keys import key
from free_games import data

token = key

client = discord.Client()

help_command = """

🎮 `;broke list` for free games list 🎮

🎮 `;broke game #+{game number}` for game details 🎮

"""


def games_printer(games_list):
    string = ':point_down: Currently FREE Games: :point_down: \n'
    for i in range(len(games_list)):
        string += f"🎮  {i + 1})  {games_list[i].game}\n"
    return string


def game_details(games_list, game_number):
    if game_number > len(games_list):
        return ':warning: Number Out Of range :warning:'

    game_number -= 1
    string = f"""
    🎮 Game: {games_list[game_number].game}
:moneybag: Store: {games_list[game_number].store}
:link: Link: {games_list[game_number].link} \n """
    return string


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Overwatch 2", url="https://www.twitch.tv/xqcow"))


@client.event
async def on_message(message):
    isValid = False
    if message.content == ';broke help':
        isValid = True
        await message.channel.send(help_command)

    elif message.content == ';broke list':
        isValid = True
        await message.channel.send(games_printer(data))

    if message.content.startswith(";broke game #"):
        number = message.content[message.content.find('#') + 1:]
        if number.isdigit():
            number = int(number)
            isValid = True
            await message.channel.send(game_details(data, number))

    if message.content.startswith(";broke") and isValid == False:
        await message.channel.send(':warning: Unknown Command, Please Type `;broke help` for help :warning:')


client.run(token)
