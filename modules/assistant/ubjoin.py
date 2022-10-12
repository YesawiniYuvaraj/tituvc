from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
from main.client import asst, bot
from helpers.decorators import authorized_users_only, errors
# from services.callsmusic.callsmusic import client as USER


@asst.on_message(filters.command(["join"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await bot.get_me()
    except:
        user.first_name = "Music"

    try:
        await bot.join_chat(invitelink)
        await bot.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr manually add o your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your chat</b>",
    )


@bot.on_message(filters.group & filters.command(["leave"]))
async def rem(bot, message):
    try:
        await bot.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return

@asst.on_message(filters.command(["userbotjoinchannel","cjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor channel first</b>",
        )
        return

    try:
        user = await bot.get_me()
    except:
        user.first_name = "Music"

    try:
        await bot.join_chat(invitelink)
        await bot.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nOr manually add  to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    
