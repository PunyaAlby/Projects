# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights
from telethon import Button

from AyiinXd import BOT_VER as version
from AyiinXd import BOTLOG_CHATID, BOTLOG, LOGS
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import AYIIN2, AYIIN3, AYIIN4, AYIIN5, AYIIN6, AYIIN7, AYIIN8, AYIIN9, AYIIN10, bot, branch, tgbot
from AyiinXd.ayiin import ayiin_version as py_ver
from AyiinXd.ayiin import HOSTED_ON, checking

MSG_ON = """
❏ ᴀʟʙʏ - ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼┅━━━━━╍━━━━━┅╾
├▹ ᴀʟʙʏ Vᴇʀsɪᴏɴ - {} •[{}]•
├▹ Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {}
├▹ @{}
├▹ **Ketik** `{}ping` **Untuk Mengecek Bot**
├▹ **Ketik** `{}help` **Untuk Melihat Informasi Module**
╰╼┅━━━━━╍━━━━━┅╾
**Powered By:** @ruangprojects
"""


async def startupmessage(tgbot):
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/cbe826936d4de9ec1838a.jpg",
                caption=MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd, cmd, cmd),
                buttons=[(Button.url("ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/ruangdiskusikami"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None


async def ayiin_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            AyiinUBOT = await tgbot.get_me()
            BOT_USERNAME = AyiinUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            AyiinUBOT = await tgbot.get_me()
            BOT_USERNAME = AyiinUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "Assɪsᴛᴀɴᴛ Aʏɪɪɴ"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN2:
            await checking(AYIIN2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN3:
            await checking(AYIIN3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN4:
            await checking(AYIIN4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN5:
            await checking(AYIIN5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN6:
            await checking(AYIIN6)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN7:
            await checking(AYIIN7)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN8:
            await checking(AYIIN8)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN9:
            await checking(AYIIN9)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        if AYIIN10:
            await checking(AYIIN10)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await startupmessage(tgbot)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
