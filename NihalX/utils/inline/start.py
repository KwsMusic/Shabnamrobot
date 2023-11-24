from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from NihalX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️𝐀ᴅᴅ ᴍᴜsɪᴄ 𝐁σт⛩️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🔴 ashish 🔴", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🍻 𝐎ωиєя 🍻", user_id=OWNER),
            InlineKeyboardButton(
                text="🍒‌⃰‌˶‌֟፝sᴜᴩᴩᴏʀᴛ⏎‌🝛꯭", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⛩️𝐀ᴅᴅ ᴍᴜsɪᴄ 𝐁σт⛩️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🍻 𝐎ωиєя 🍻", user_id=OWNER),
            InlineKeyboardButton(
                text="🍒‌⃰‌˶‌֟፝sᴜᴩᴩᴏʀᴛ⏎‌🝛꯭", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons
