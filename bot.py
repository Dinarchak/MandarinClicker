import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings import config

router = Router()

dp = Dispatcher()
dp.include_router(router)

bot = Bot(token=config['bot_token'])

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Кликер',
        web_app=WebAppInfo(url='')
    )

    return builder.as_markup()



@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Ссылка на кликер", reply_markup=webapp_builder())

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


