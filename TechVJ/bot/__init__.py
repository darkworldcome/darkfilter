# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, types
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from aiohttp import web

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os


class TechVJXBot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def set_self(self):
        temp.BOT = self
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
      
TechVJBot = TechVJXBot()



# Function to handle the /start command
def start(update: Update, context: CallbackContext):
    if context.args:
        # Extract the command (e.g., getfile-The-Rana-Daggubati-Show-2024)
        command = context.args[0]
        
        if command.startswith("getfile-"):
            file_name = command.replace("getfile-", "")
            file_path = f"/path/to/your/files/{file_name}.mp4"  # Adjust path to your file directory

            if os.path.exists(file_path):
                # Send the file to the user
                update.message.reply_text(f"Sending the file: {file_name}...")
                update.message.reply_document(open(file_path, 'rb'))
            else:
                update.message.reply_text(f"File {file_name} not found.")
        else:
            update.message.reply_text(f"Unknown command: {command}")
    else:
        update.message.reply_text("Welcome! Please provide a valid command.")

# Main function to set up the bot
def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)  # Replace with your bot's API token
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

# Run the bot
if __name__ == '__main__':
    main()


multi_clients = {}
work_loads = {}
