import asyncio
from pyrogram import filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
# from services.callsmusic.callsmusic import client as parth
from main.client import asst
from main.config import SUDO_ID 

@asst.on_message(filters.command(["gcast", "broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_ID:
        return
    else:
        wtf = await message.reply("** 😘ꜱᴛᴀʀᴛ ʙʀᴏᴀᴅᴄᴀꜱᴛ ʙᴀʙʏ...**")
        if not message.reply_to_message:
            await wtf.edit("**😚 ʀᴇᴘʟʏ ᴋᴀʀᴏ ᴊᴀᴀɴ ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in asst.iter_dialogs():
            try:
                await asst.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**😘ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ ʙᴀʙʏ ...** \n\n**✔️ ꜱᴇɴᴛ ᴛᴏ:** `{sent}` **ᴄʜᴀᴛꜱ** \n**❌ ꜰᴀɪʟᴇᴅ ɪɴ:** `{failed}` **ᴄʜᴀᴛꜱ**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**😚ʙʀᴏᴀᴅᴄᴀꜱᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴊᴀᴀɴᴜ ...**\n\n**✔️ ꜱᴇɴᴛ ᴛᴏ:** `{sent}` **ᴄʜᴀᴛꜱ**\n**❌ ꜰᴀɪʟᴇᴅ ɪɴ:** `{failed}` **ᴄʜᴀᴛꜱ**")
