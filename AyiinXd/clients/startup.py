# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id
from AyiinXd.ayiin.events import fuck
from AyiinXd import BOT_TOKEN
from AyiinXd import BOT_VER as version
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)
from AyiinXd.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nALBY-UserBot v{}, Copyright © 2021-2022 ALBY• <https://github.com/PunyaAlby>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nALBY-UserBot v{}, Copyright © 2021-2025 ALBY• <https://github.com/PunyaAlby>"


async def ayiin_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multiayiin():
    if 5089916692 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001638078842 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 5089916692 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            LOOP.run_until_complete(fuck())
            LOOP.run_until_complete(ayiin_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))


    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        LOGS.info(str(e))
