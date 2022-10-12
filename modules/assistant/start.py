import asyncio
from datetime import datetime
from pyrogram import filters
from main.client import asst
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@asst.on_message(filters.command("start") & filters.private)
async def sstart(_,message : Message):
    await message.reply_photo(
    photo=f"https://telegra.ph/file/704737b53366a184e9c4a.jpg",
    caption=f"""**ᴀ ᴡᴀʀᴍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ Sᴀʀᴠᴇsʜ !!
ɪ'ᴍ ʏᴏᴜʀ ᴀᴅᴠᴀɴᴄᴇ ɢʀᴏᴜᴘ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ\n\nɪ ᴀᴍ ᴠᴇʀʏ ғᴀsᴛ ᴀɴᴅ ʀᴇʟᴀɪʙʟᴇ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇᴅ ғᴇᴀᴛᴜʀᴇs!!!
ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘʏᴛʜᴏɴ3 ᴀɴᴅ ᴘʏʀᴏɢʀᴀᴍ!\n\n

ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ➪ [Sᴀʀᴠᴇsʜ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/SA_MODS01)

          ☺️ ᴋᴇᴇᴘ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ Aʟᴡᴀʏs ☺️ **""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♢🇦 🇩 🇩   🇲 🇪♢", url=f"https://t.me/titudeveloper633?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "♢🇸 🇺 🇵 🇵 🇴 🇷 🇹♢", url=f"https://t.me/tmusicstudio53")
                ]

            ]
         ),
     )
