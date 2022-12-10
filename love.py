__version__ = (1, 0, 0)

#               © Copyright 2022
#
#      https://t.me/codercoffee
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @codermodes
# scope: hikka_only

from .. import loader, utils, main
import asyncio
import logging
import random as r
from telethon.tl.types import Message

logger = logging.getLogger(__name__)


class coderlovemod(loader.Module):
    """
    Покажи девушке какая она прекрасная
    (или им, какие они прекрасные)
    """

    strings = {
        "name": "love",
        "_cfg_doc_for_one_or_more": (
            "Выберите пожалуйста, комплименты будут для 1 человека женского пола, или"
            " для всех людей женского пола в чате \nЕсли для 1 человека--> one \nЕсли"
            " для всех людей женского пола в чате--> more"
        ),
        "_cfg_doc_command_mode": (
            "Выберите пожалуйста режим команды, какая будет анимация: \n Если вы"
            " хотите, чтобы печатался список комплиментов --> 1 \n Если вы хотите,"
            " чтобы каждую секунду комплимент заменялся на другой и в конце вывелся"
            " полный список --> 2"
        ),
    }
    def __init__(self):
        self._ratelimit = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "for_one_or_more",
                "one",
                doc=lambda: self.strings("_cfg_doc_for_one_or_more"),
                validator=loader.validators.Choice(["one", "more"]),
            ),
            loader.ConfigValue(
                "command_mode",
                1,
                doc=lambda: self.strings("_cfg_doc_command_mode"),
                validator=loader.validators.Choice([1, 2]),
            ),
        )

    async def client_ready(self, db, client):
        self.db = db
        if main.__version__ < (1, 3, 0):
            try:
                post = (await client.get_messages("codermodes", ids=[1]))[0]
                reactions = ["❤️‍🔥", "🤩", "🌚", "🔥"]
                reaction = r.choice(reactions)
                await post.react(reaction)
            except Exception:
                logger.debug("Can't react to t.me/codermodes :<")

    async def inline_compliments(self, message: Message):
        om = self.config["for_one_or_more"]
        mode = self.config["command_mode"]
        if om == "one":
            if mode == 1:
                messages = [
                    "Ты...прекрасная, а еще.... ",
                    "{♡} красивая 🌺 ",
                    "🪴заботливая~~ ",
                    "^0^ добрая 👐 ",
                    "👩🏻‍🎓умная $>$ ",
                    "~~трогательная 👉👈 ",
                    "🙀 изумительная 😍 ",
                    "🤯 офигенная и офигительная 🤠 ",
                    "🥵 игривая 😜 ",
                    "~♡~ прелестная 🌹 ",
                    "😍 восторженная 🤭 ",
                    "~~мечтательная ☁️ ",
                    "💋 особенно понимающая 🫂 ",
                    "👥 дружелюбная 🗣 ",
                    "😌 искренняя ♡ ",
                    "🙈 безупречная ",
                    "😋 сладенькая) ",
                    "😊 ласковая ",
                    "😻 симпатичная ",
                    "🦄 сказочная ",
                    "👌 разносторонняя ",
                    "🤔 креативная ",
                    "🌚 весёлая ",
                    "🌸 обалденная ",
                    "🤜🤛 крутая ",
                    "✨ яркая ",
                    "🐱 ангельская ",
                    "🔮 божественная ",
                    "💘 шикарная ",
                    "🙂 незабываемая ",
                    "😎 неповторимая ",
                    "🧸 очаровательная",
                    "❤️ идеальная",
                    "🥺 милая ",
                    "😍 ахуенная ",
                    "🍬 привлекательная ",
                    "😱 головокружительная",
                    "🤩 неотразимая",
                    "☺️ нежная",
                    "😍 обольстительная",
                    "🥵 грациозная",
                    "☀️ солнечная",
                    "🌚 умопомрачительная",
                    "🔥 совершенная",
                    "Я ЛЮБЛЮ ТЕБЯ! ❤️❤️❤️",
                ]

                current = ""
                for i in messages:
                    current += i + "\n"
                    message = await utils.answer(message, current)
                    await asyncio.sleep(0.5)

                await utils.answer(message, f"<i>{current}</i>")
            elif mode == 2:
                await utils.answer(message, "<i>Ты......</i>")
                await asyncio.sleep(1)
                await utils.answer(message, "<i>Ты...прекрасная...</i>")
                await asyncio.sleep(1)
                await utils.answer(message, "<i>Ты...прекрасная, а еще....</i>")
                await asyncio.sleep(1)
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "❤️ идеальная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "🍬 привлекательная",
                    "😱 головокружительная",
                    "🤩 неотразимая",
                    "☺️ нежная",
                    "😍 обольстительная",
                    "🥵 грациозная",
                    "☀️ солнечная",
                    "🌚 умопомрачительная",
                    "🔥 совершенная"
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        f"<i>Ты...прекрасная, а еще....\n{m}</i>",
                    )
                    await asyncio.sleep(1)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    f"<b><i>Ты...прекрасная, а еще.... \n{all_}\nЯ ЛЮБЛЮ ТЕБЯ!"
                    " ❤️❤️❤️</i></b>",
                )
            else:
                await utils.answer(
                    message,
                    "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                    " потому что в конфиге неправильное значение. \nНапишите"
                    " <code>.lovecfg</code>",
                )
        elif om == "more":
            if mode == 1:
                await utils.answer(message, "<i>Каждая девушка/девочка/женщина...</i>")
                await asyncio.sleep(0.5)
                await utils.answer(
                    message, "<i>Каждая девушка/девочка/женщина в этом чате...</i>"
                )
                await asyncio.sleep(0.5)
                await utils.answer(
                    message,
                    "<i>ТКаждая девушка/девочка/женщина в этом чате прекрасна...</i>",
                )
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя ♡",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "❤️ идеальная",
                    "🍬 привлекательная",
                    "😱 головокружительная",
                    "🤩 неотразимая",
                    "☺️ нежная",
                    "😍 обольстительная",
                    "🥵 грациозная",
                    "☀️ солнечная",
                    "🌚 умопомрачительная",
                    "🔥 совершенная"
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        "<i>Каждая девушка/девочка/женщина в этом чате прекрасна..."
                        f" еще, каждая из них...\n{m}</i>",
                    )
                    await asyncio.sleep(0.5)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    "<b><i>Каждая девушка/девочка/женщина в этом чате прекрасна.... еще"
                    f" каждая из них: \n{all_}\nИ САМАЯ ЛУЧШАЯ НА"
                    " СВЕТЕ❤️❤️❤️❤️❤️❤️❤️❤️</i></b>",
                )
            elif mode == 2:
                await utils.answer(message, "<i>Каждая девушка/девочка/женщина...</i>")
                await asyncio.sleep(1)
                await utils.answer(
                    message,
                    "<i>Каждая девушка/девочка/женщина в этом чате прекрасна...</i>",
                )
                await asyncio.sleep(1)
                await utils.answer(
                    message,
                    "<i>Каждая девушка/девочка/женщина в этом чате прекрасна... еще"
                    " каждая из них:</i>",
                )
                await asyncio.sleep(1)
                messages = [
                    "{♡} красивая 🌺",
                    "🪴заботливая~~",
                    "^0^ добрая 👐",
                    "👩🏻‍🎓умная $>$",
                    "~~трогательная 👉👈",
                    "🙀 изумительная 😍",
                    "🤯 офигенная и офигительная 🤠",
                    "🥵 игривая 😜",
                    "~♡~ прелестная 🌹",
                    "😍 восторженная 🤭",
                    "~~мечтательная ☁️",
                    "💋 особенно понимающая 🫂",
                    "👥 дружелюбная 🗣",
                    "😌 искренняя",
                    "🙈 безупречная",
                    "😋 сладенькая)",
                    "😊 ласковая",
                    "😻 симпатичная",
                    "🦄 сказочная",
                    "👌 разносторонняя",
                    "🤔 креативная",
                    "🌚 весёлая",
                    "🌸 обалденная",
                    "🤜🤛 крутая",
                    "✨ яркая",
                    "🐱 ангельская",
                    "🔮 божественная",
                    "💘 шикарная",
                    "🙂 незабываемая",
                    "😎 неповторимая",
                    "🧸 очаровательная",
                    "🥺 милая",
                    "😍 ахуенная",
                    "❤️ идеальная",
                    "🍬 привлекательная",
                    "😱 головокружительная",
                    "🤩 неотразимая",
                    "☺️ нежная",
                    "😍 обольстительная",
                    "🥵 грациозная",
                    "☀️ солнечная",
                    "🌚 умопомрачительная",
                    "🔥 совершенная"
                ]
                for m in messages:
                    message = await utils.answer(
                        message,
                        "<i>Каждая девушка/девочка/женщина в этом чате прекрасна..."
                        f" еще каждая из них:\n{m}</i>",
                    )
                    await asyncio.sleep(1)

                all_ = "\n".join(messages)

                await utils.answer(
                    message,
                    f"<b><i>Каждая девушка/девочка/женщина в этом чате прекрасна... еще"
                    f" каждая из них: \n{{all_}}\nИ САМАЯ ЛУЧШАЯ НА"
                    f" СВЕТЕ❤️❤️❤️❤️❤️❤️❤️❤️</i></b>",
                )
            else:
                await utils.answer(
                    message,
                    "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                    " потому что в конфиге неправильное значение. \nНапишите"
                    " <code>.lovecfg</code>",
                )
        else:
            await utils.answer(
                message,
                "К сожалению, произошла ошибка... \nА именно, эта ошибка произошла"
                " потому что в конфиге неправильное значение. \nНапишите"
                " <code>.lovecfg</code>",
            )

    async def lovecfgcmd(self, message: Message):
        """—>конфиг"""
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    async def ilikecmd(self, message):
        "Инлайн анимация комплиментов(настройка в конфиге)"
        await self.inline.form(
            text="Я хочу кое-что сказать...",
            reply_markup=[
                [{"text": "🥺", "callback": self.inline_compliments}],
                [{"text": "🚫", "action": "close"}],
            ],
            message=message,
            disable_security=True,
        )