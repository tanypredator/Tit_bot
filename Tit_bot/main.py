from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType, FSInputFile
from random import choice
from os import listdir
from pdb import set_trace
import asyncio

API_TOKEN: str
TIT_PATH = "/home/tanypredator/siski/"
TITIES = listdir(TIT_PATH)

with open("token.txt", "r") as token:
    API_TOKEN = token.read()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Сисько-бот!\nВызывайте меня командой /срач если нужно')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Завалю вас сиськами и жопоньками по команде /срач.\n'
                         'Возможно со временем я научусь замечать срач сам!\n'
                         'А ещё я пришлю одну картинку по команде /покажи ^_^')

# Этот хэндлер будет срабатывать на команду "/срач"
@dp.message(Command(commands=['срач']))
async def shit_command(message: Message):
    for i in range(3):
        r = choice(TITIES)
        photo = FSInputFile(f'{TIT_PATH}{r}')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    for i in range(5):
        await asyncio.sleep(10)
        r = choice(TITIES)
        photo = FSInputFile(f'{TIT_PATH}{r}')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

# Этот хэндлер будет срабатывать на команду "/покажи"
@dp.message(Command(commands=['покажи']))
async def shit_command(message: Message):
    r = choice(TITIES)
    photo = FSInputFile(f'{TIT_PATH}{r}')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

if __name__ == '__main__':
    dp.run_polling(bot)

'''
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
'''
