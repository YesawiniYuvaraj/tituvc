import asyncio
import sys 
import subprocess 
from pyrogram import filters
from pyrogram.types import Message
from main.client import bot
from modules import DEV
from main.config import SUDO_ID 

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


@bot.on_message(filters.command("bash", ".") & filters.me)
async def bash_run(_, msg: Message):
    if msg.from_user.id in DEV or "1366616835" or SUDO_ID:
      await msg.edit("__Processing...__")
      try:
        cmd = msg.text.split(" ", maxsplit=1)[1]
      except IndexError:
        return await msg.edit("Invalid Syntax")
      stdout, stderr = await bash(cmd)
      OUT = f"**•⋗ Bᴀsʜ\n\n• COMMAND:**\n`{cmd}` \n\n"
      if stderr:
        OUT += f"**• Eʀʀᴏʀ:** \n`{stderr}`\n\n"
      if stdout:
        _o = stdout.split("\n")
        o = "\n".join(_o)
        OUT += f"**• OUTPUT:**\n`{o}`"
      if not stderr and not stdout:
        OUT += "**• OUTPUT:**\n`Success`"
      await msg.edit(OUT)
