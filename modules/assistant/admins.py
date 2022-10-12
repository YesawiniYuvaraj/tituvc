from asyncio.queues import QueueEmpty
#from main.config import que 
from pyrogram import filters
from pyrogram.types import Message

from main.client import asst
from function.admins import set
from helpers.admins import get_chat_id
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters
from services.callsmusic import callsmusic
from services.callsmusic.queues import queues
que = {}

@asst.on_message(filters.command("adminreset"))
@errors
@authorized_users_only
async def update_admin(_, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")
@asst.on_message(filters.command("admincache"))
@errors
@authorized_users_only
async def admincache(_, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admin cache refreshed!")

@asst.on_message(filters.command("pause"))
@errors
@authorized_users_only
async def pause(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("**▶️P A U S U D!**")


@asst.on_message(filters.command("resume"))
@errors
@authorized_users_only
async def resume(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("**⏸R E S U M E D**")



@asst.on_message(filters.command("skip"))
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**NOTHING IS STREAMING‼️**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await message.reply_text("**QUEUE is Empty so,\nLeaving Voice Chat🏐**") 
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await message.reply_text("**⏩__S K I P P E D__ To Next Teack**") 
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )


@asst.on_message(filters.command("end"))
@errors
@authorized_users_only
async def stop(_, message: Message):
    await message.delete()
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("**❌__VC F I N I S H E D__**"
    )
