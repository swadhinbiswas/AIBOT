# name=f"""
# dhkahdkladkahdkahdhakdhaiudguyctyuwydywsd



# """

# x=f"""<b><i>Hi! @{name}👋 </i>
#                        I am The Professor The BOT</b>
# <b><i>I can help you with the following things:</i> </b>
# <b> 🖼 I can create images from text</b>.
# <b> 🧾I can create text from images.</b>
# <b> 🎉 I can create memes.</b>
# <b> 📚I can translate text.</b>
# <b> I can generate text from audio.🎙</b>
# <b> I can generate audio from text.📒🎙</b>
# <b> I can manupulate images.</b>
# <b> I can generate text from text.</b>

# """



# print(x)

from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

# Define the command descriptions
command_descriptions = {
    "start": "Get started with the bot.",
    "help": "Get a list of available commands and their descriptions.",
    "stop": "Stop interacting with the bot."
}


def create_menu(commands):
    """
    Creates an InlineKeyboardMarkup object with buttons for each command.

    Args:
        commands: A dictionary containing command names as keys and descriptions as values.

    Returns:
        An InlineKeyboardMarkup object with command buttons.
    """
    keyboard = InlineKeyboardMarkup()
    buttons = []
    for command, description in commands.items():
        buttons.append(InlineKeyboardButton(f"{command} - {description}", callback_data=command))
    keyboard.add(*buttons)
    return keyboard


async def handle_callback(client, callback, commands):
    """
    Handles callback queries for the command buttons.

    Args:
        client: The Pyrogram client object.
        callback: The callback query object.
        commands: A dictionary containing command names as keys and their corresponding functions as values.
    """
    command = callback.data
    if command in commands:
        await commands[command](client, callback.message)
    else:
        await callback.message.reply_text("Invalid command.")
    await callback.answer()


async def handle_message(client, message, commands):
    """
    Handles incoming messages from the user.

    Args:
        client: The Pyrogram client object.
        message: The message object received from the user.
        commands: A dictionary containing command names as keys and their corresponding functions as values.
    """
    if message.text.startswith("/"):
        command = message.text.split()[0][1:]
        if command in commands:
            await commands[command](client, message)
        else:
            await message.reply_text("Invalid command.")
    else:
        await message.reply_text("Use a command to interact with the bot. Type /help for a list of commands.")


async def start_command(client, message):
    """
    Example function for the /start command.

    Args:
        client: The Pyrogram client object.
        message: The message object received from the user.
    """
    await message.reply_text("Welcome to the bot! Use the menu below to explore available commands.")


async def help_command(client, message):
    """
    Example function for the /help command.

    Args:
        client: The Pyrogram client object.
        message: The message object received from the user.
    """
    menu = create_menu(command_descriptions)
    await message.reply_text("Here's a list of available commands:", reply_markup=menu)


async def stop_command(client, message):
    """
    Example function for the /stop command.

    Args:
        client: The Pyrogram client object.
        message: The message object received from the user.
    """
    await message.reply_text("Goodbye! See you next time.")
    # You can optionally add logic to stop the bot interaction here


# Define your actual command functions here (replace with your specific logic)
commands = {
    "start": start_command,
    "help": help_command,
    "stop": stop_command,
}


# Register your event handlers (modify as needed)
@client.on_message()
async def message_handler(client, message):
    await handle_message(client, message, commands)


@client.on_callback_query()
async def callback_handler(client, callback):
    await handle_callback(client, callback, commands)
