import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEOnXRj0K3rOj2KzPQEII_mzUUJf65_0AACUAcAAjA5gFZaJKzDHxVmBC0E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , ⚔️\n\n
๏ This is [{bn}](t.me/{bu})
➻ #ʏᴇ ᴊσ ᴛυᴍ ɪᴛɴᴇ #ᴘᴀʏᴀʀᴇ ʜσ.!🔥👅💋🥵ᴍ*ᴅʜ*ʀ #çʜ **ᴅ🖕ᴋσυղ sᴇ ʜᴀᴍᴀяᴇ ʜσ...☠️✨🥀.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🫶🏻 by : [𝐈𝛕ᷟ͢𝚣⃪ꙴ 𓄂 ⃝⃪𝐂𝐇𝐎𝐂𝐇𝐎𝐋𝐈𝐓𝐘🍫𝐁𝐎𝐈](https://t.me/ll_Ur_Chocolaty_ll) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚Add Me To Your Group✚  ", url=f"https://t.me/CHOCOLATY_OWNER_MUSIC_BOT?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "⚔️ Support My Channel  ", url=f"https://t.me/ABOUT_CHOCOLATY"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Support My Group ", url=f"https://t.me/CHOCOLATY_SPAMER"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Real Owner ", url=f"https://t.me/ll_Ur_Chocolaty_ll"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/ll_Ur_Chocolaty_ll"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4"
                    )]
            ]
       ),
    )

