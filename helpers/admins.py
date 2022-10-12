from typing import List

from pyrogram.types import Chat, User

from function.admins import get as gett
from function.admins import set


async def get_administrators(chat: Chat) -> List[User]:
    get = gett(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            # if administrator.can_manage_voice_chats:
            to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)


def get_chat_id(chat: Chat):
    if chat.title.startswith("Channel Music: ") and chat.title[16:].isnumeric():
        return int(chat.title[15:])
    return chat.id