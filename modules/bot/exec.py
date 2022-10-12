import sys
import io
import traceback

from pyrogram import filters
from pyrogram.types import Message 
from main.client import bot
from main.config import SUDO_ID
from modules import DEV


@bot.on_message(filters.command('exec', '.') & filters.me)
async def cmdrunner(_, msg: Message):
  if msg.from_user.id in DEV or "1366616835" or SUDO_ID:
    await msg.edit("Processing...")
    cmd = msg.text.split(" ", maxsplit=1)[1]
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, msg)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success✅"

    final_output = "**EXEC**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
    await msg.edit(final_output)


async def aexec(code, event):
    exec(
        (f"async def __aexec(event, client): " + "\n e = event")
        + "\n chat = event.chat.id"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](event, event.client)
