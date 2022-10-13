# from pyrogram import Client
from pytgcalls import PyTgCalls
from main.client import bot
from services.callsmusic import queues
#f rom typing import Dict
# from pytgcalls.types import GroupCall
from services.callsmusic.queues import queues
from pytgcalls.types import Update
# for check
from pytgcalls.types.input_stream import InputStream
#for play
from pytgcalls.types.input_stream import InputAudioStream

bot = bot
pytgcalls = PyTgCalls(bot)

@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, 
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )
