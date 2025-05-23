from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    """
    Меню сбоку от клавиатуры
    """
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
