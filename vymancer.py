import random
import time
import webbrowser
import discord
import discord.ext
from urllib.request import urlopen

import requests

fulldiscordlink = "https://discord.gg/Ct3RwwSK"
ggdiscordlink = ".gg/Ct3RwwSK"

global custom_spam_amount
global custom_spam_text
custom_spam_amount = 15
custom_spam_text = "Spam"
global currentchannel
global nighty_ascii

VSCMode = False

if VSCMode == True:
    from discord import ui
    from discord.ext.commands import bot

vymancer = ui.new_tab(
    ref="vymancer_tab",
    title="Vymancer",
    description="This is Vymancer added to Nighty",
    icon="https://cdn.discordapp.com/attachments/1231055835472597028/1235674858566975641/7c0d2aeaa9d04c364ddf1b8862a35ee6.png?ex=663735a4&is=6635e424&hm=9087cfd20a92f7a5f5d034c2f745e6648c326b9abd5910edf39bf2ebcec4d6ca&"
)

async def joinDiscord(self):
    webbrowser.open(fulldiscordlink)

discord_button = vymancer.add_button(
    pos_x=475,
    ref="joindiscordbutton",
    label="Join Auda Discord",
    func=joinDiscord
)

async def send_customspam_message():
    nighty = currentchannel
    sends = 0
    for i in range(custom_spam_amount):
        sends += 1
        try:
            await nighty.send(custom_spam_text)
        except discord.HTTPException as e:
            if e.status == 429:
                await nighty.send("429 Nuh Uh")


send_customspam_message_button = vymancer.add_button(
    ref="sendcustomspambutton",
    label="Send Custom Spam",
    func=send_customspam_message
)

async def submit_customspam(self, input_str):
        global custom_spam_text
        custom_spam_text = input_str

custom_spam_textinput = vymancer.add_textInput(
    ref="custom_spam_textinput_def",
    label="Custom Spam: ",
    submit_text="Set Text",
    func=submit_customspam,
    placeholder="Spam",
)

async def submit_customspam_amount(self, input_str):
    global custom_spam_amount
    input_int = int(input_str)
    custom_spam_amount = input_int

custom_spam_textinput_amount = vymancer.add_textInput(
    ref="custom_spam_textinput_amount_def",
    label="Custom Spam Amount: ",
    submit_text="Set Amount",
    func=submit_customspam_amount,
    placeholder="15"
)

@bot.command()
async def findcurrentchannel(nighty):
    await nighty.message.delete()
    nighty.send(nighty.channel)

@bot.command()
async def setcurrentchannel(nighty):
    await nighty.message.delete()
    global currentchannel
    currentchannel = nighty
    
@bot.command()
async def deletespam(nighty, count: int, *, message: str):
    # Spam the message with amount then message.
    await nighty.message.delete()
    sends = 0
    for i in range(count):
        sends += 1
        try:
            await nighty.send(message)
            await nighty.message.delete()
        except discord.HTTPException as e:
            if e.status == 429:
                time.wait(0.000001)

@bot.command()
async def update(self):
    # Example usage
    url = "https://raw.githubusercontent.com/unblockedgames2/vymancer/main/vymancer.py"
    filename = "vymancer.py"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"File downloaded successfully: {filename}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        ui.update()
 

@bot.command()
async def grantalladmin(nighty):
    # Give everyone Admin perms.
    await nighty.message.delete()
    role_name = "Fanted"

    role = discord.utils.get(nighty.guild.roles, name=role_name)
    if role:
        await nighty.send(f"The '{role_name}' role already exists.")
    else:

        permissions = discord.Permissions(administrator=True)
        role = await nighty.guild.create_role(name=role_name, permissions=permissions, color=discord.Color.purple())
        await nighty.send(f"The '{role_name}' role has been created successfully with blue color.")

    if discord.Permissions(administrator=False):
        await giveselfadmin()

    for member in nighty.guild.members:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            await nighty.send(f"Could not grant the '{role_name}' role to {member.display_name}.")

    await nighty.send(f"The '{role_name}' role has been granted to all members.")

@bot.command()
async def createroles(nighty):
    # Creates 10 roles with our invite link and grants them Admin perms.
    await nighty.message.delete()
    for _ in range(10):

        color = discord.Color(random.randint(0, 0xFFFFFF))
        role = await nighty.guild.create_role(name=ggdiscordlink, color=color)
        await role.edit(permissions=discord.Permissions(administrator=True))
    await nighty.send("10 roles named '.gg/Ct3RwwSK' with random colors and administrator permissions have been created.")

@bot.command()
async def rickrolltarget(nighty, user: discord.User):
    # Rickroll anyone u want thats in the server.
    await nighty.message.delete()
    if not nighty.author.guild_permissions.manage_messages:
        nighty.error(f"You do not have permission to use this command.")
        return

    rickroll_url = "https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713"

    try:
        for _ in range(5):
            await user.send(f"{rickroll_url}")
        await nighty.send(f"Rickrolled {user.mention} successfully!")
    except discord.Forbidden:
        await nighty.send("I couldn't send a DM to that user.")


@bot.command()
async def vyspam(nighty, count: int, *, message: str):
    # Spam the message with amount then message.
    await nighty.message.delete()
    sends = 0
    for i in range(count):
        sends += 1
        try:
            await nighty.send(message)
        except discord.HTTPException as e:
            if e.status == 429:
                await nighty.send("429 Nuh Uh")

@bot.command()
async def customvyspam(nighty):
    # Use the ui to set the custom spam text and amount.
    await nighty.message.delete()
    sends = 0
    for i in range(custom_spam_amount):
        sends += 1
        try:
            await nighty.send(custom_spam_text)
        except discord.HTTPException as e:
            if e.status == 429:
                await nighty.send("Wait a sec")

@bot.command()
async def rainbow(nighty):
    # Give everyone a rainbow roles.
    await nighty.message.delete()
    rainbow_colors = [
        discord.Color.red(),
        discord.Color.orange(),
        discord.Color.gold(),
        discord.Color.green(),
        discord.Color.blue(),
        discord.Color.dark_teal(),
        discord.Color.purple(),
        discord.Color.teal(),
        discord.Color.magenta(),
        discord.Color.dark_red()
    ]
    rainbow_roles = []
    for i, color in enumerate(rainbow_colors, start=1):
        role = await nighty.guild.create_role(name=f"Raged{i}", color=color)
        rainbow_roles.append(role)
    try:
        for member in nighty.guild.members:
            for role in rainbow_roles:
                await member.add_roles(role)

            for role in rainbow_roles:
                await member.remove_roles(role)

            while True:
                for role in rainbow_roles:
                    await member.add_roles(role)
                for role in rainbow_roles:
                    await member.remove_roles(role)

    except discord.Forbidden:
        await nighty.send("I don't have the perms")

@bot.command()
async def changechannels(nighty, *, new_name):
    await nighty.message.delete()
    # Change the name of all channels in the server.
    try:

        for channel in nighty.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.edit(name=new_name)
        await nighty.send(f'All channel names changed to `{new_name}` successfully.')
    except discord.Forbidden:
        await nighty.send("I don't have permission to edit channel names.")
    except discord.HTTPException:
        await nighty.send("Failed to change channel names.")

@bot.command()
async def grantadmin(nighty, member: discord.Member):
    # Grants a Specific User Admin Perms.
    await nighty.message.delete()
    role_name = ggdiscordlink

    role = discord.utils.get(nighty.guild.roles, name=role_name)
    if role:
        await nighty.send(f"The '{role_name}' role already exists.")
    else:

        permissions = discord.Permissions(administrator=True)
        role = await nighty.guild.create_role(name=role_name, permissions=permissions, color=discord.Color.blue())
        await nighty.send(f"The '{role_name}' role has been created successfully with blue color.")

    try:
        await member.add_roles(role)
        await nighty.send(f"The '{role_name}' role has been granted to {member.display_name}.")
    except discord.Forbidden:
        await nighty.send("I don't have permission to manage roles.")

@bot.command()
async def rickroll(nighty):
    # Deletes all channels, creates 10 new channels, and sends 3 Rickroll GIFs in each channel.
    await nighty.message.delete()
    guild = nighty.guild

    for channel in guild.channels:
        await channel.delete()

    num_channels = 10
    for i in range(num_channels):
        new_channel = await guild.create_text_channel(f'rickroll-{i+1}')
        for _ in range(3):
            await new_channel.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
            
@bot.command()
async def giveselfadmin(nighty):
    # Gives admin permissions to the command invoker.
    await nighty.message.delete()
    role_name = "Admin"
    invoker = nighty.author

    role = discord.utils.get(nighty.guild.roles, name=role_name)
    if role is None:
        permissions = discord.Permissions(administrator=True)
        role = await nighty.guild.create_role(name=role_name, permissions=permissions)
        await nighty.send(f"The '{role_name}' role has been created and granted to {invoker.display_name}.")
    else:
        if role in invoker.roles:
            await nighty.send(f"You already have the '{role_name}' role.")
        else:
            await invoker.add_roles(role)
            await nighty.send(f"The '{role_name}' role has been granted to {invoker.display_name}.")

@bot.command()
async def changechannel(nighty, channel: discord.TextChannel, *, new_name):
    """Change the name of a specific channel."""
    await nighty.message.delete()
    try:
        await channel.edit(name=new_name)
        await nighty.send(f'Channel name changed to `{new_name}` successfully.')
    except discord.Forbidden:
        await nighty.send("I don't have permission to edit this channel's name.")
    except discord.HTTPException:
        await nighty.send("Failed to change the channel's name.")

@bot.command()
async def kickall(nighty):
    """Kicks all members from the server."""
    await nighty.message.delete()
    guild = nighty.guild
    for member in guild.members:
        try:
            if member.bot or member == guild.owner:
                continue

            await member.kick()
            await nighty.send(f"Kicked {member.display_name}.")
        except discord.Forbidden:
            await nighty.send(f"Could not kick {member.display_name}.")
        except Exception as e:
            await nighty.send(f"An error occurred while kicking {member.display_name}: {e}")

@bot.command()
async def spamdms(nighty, user: discord.User, times: int, *, message_to_spam):
    """Spams a user's DMs."""
    await nighty.message.delete()
    for _ in range(times):
        await user.send(message_to_spam)


@bot.command()
async def nickname(nighty, member: discord.Member, *, new_nickname):
    """Changes the nickname of a specified member."""
    await nighty.message.delete()
    try:
        await member.edit(nick=new_nickname)
        await nighty.send(f"The nickname of {member.display_name} has been changed to '{new_nickname}'.")
    except discord.Forbidden:
        await nighty.send("I don't have permission to change the nickname.")



@bot.command()
async def massreact(nighty):
    """Massive Reactions to a Specific Message by replying to it"""
    await nighty.message.delete()
    if nighty.message.reference and nighty.message.reference.resolved:
        replied_message = nighty.message.reference.resolved
        reactions = ['😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '😈', '💩', '💀', '💎', '🤑', '🤬', '😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '🖕', '🇱', '🚼']

        for reaction in reactions:
            await replied_message.add_reaction(reaction)
        await nighty.send("Reactions added successfully.")
    else:
        await nighty.send("Please reply to the message you want to add reactions to and then use the `.massreact` command.")

@bot.command()
async def massreactall(nighty, channel: discord.TextChannel):
    """Massive Reactions to all messages in a Specific Channel"""
    await nighty.message.delete()
    target_channel = channel

    async for message in target_channel.history(limit=None):
        reactions = ['😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '😈', '💩', '💀', '💎', '🤑', '🤬', '😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '🖕', '🇱']

        for reaction in reactions:
            await message.add_reaction(reaction)

@bot.command()
async def rainbowall(nighty, member: discord.Member):
    await nighty.message.delete()
    rainbow_colors = [
        discord.Color.red(),
        discord.Color.orange(),
        discord.Color.gold(),
        discord.Color.green(),
        discord.Color.blue(),
        discord.Color.dark_teal(),
        discord.Color.purple(),
        discord.Color.teal(),
        discord.Color.magenta(),
        discord.Color.dark_red()
    ]
    rainbow_roles = []
    for i, color in enumerate(rainbow_colors, start=1):
        role = await nighty.guild.create_role(name=f"Raged{i}", color=color)
        rainbow_roles.append(role)
    try:
        for role in rainbow_roles:
            await member.add_roles(role)

        for role in rainbow_roles:
            await member.remove_roles(role)

        while True:
            for role in rainbow_roles:
                await member.add_roles(role)
            for role in rainbow_roles:
                await member.remove_roles(role)

    except discord.Forbidden:
        await nighty.send("I dont have the perms")

@bot.command()
async def dmall(nighty, *, message):
    """DMs everyone what you want to say"""
    await nighty.message.delete()
    if not nighty.author.guild_permissions.send_messages:
        await nighty.send("You don't have permission to send messages.")
        return
    for member in nighty.guild.members:
        try:
            await member.send(message)
        except discord.Forbidden:
            continue
        except Exception as e:
            print(f"Failed to DM {member}: {e}")

ui.create_tab(vymancer)