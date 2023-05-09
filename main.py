from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text, italic, bold, spoiler, code
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.full_name}")
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method!")


@dp.message_handler(commands=['info'])
async def info_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text(
                               "Привет\n",
                               italic("Привет\n"),
                               bold("Hello\n"),
                               spoiler("Hi\n"),
                               code("print('Hello world!')\n")
                           ),
                           parse_mode="MarkdownV2"
                           )


@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker="CAACAgQAAxkBAAEI65lkWjCtZUg8ucdN9nUnkmTjNdia9AAC-wADa65eCYShtiXyUU6-LwQ")
    await message.answer_sticker("CAACAgIAAxkBAAEIhVxkMuljwGZFnSoou7p4LED1AAHHjWgAAtguAAK1LqFLRUS7pDThxU8vBA")


@dp.message_handler(commands=['pic'])
async def pic(message: types.Message):
    photo = open('media/cat.jpg', 'rb')
    await message.answer_photo(photo)

    # with open('media/cat.jpg', 'rb') as photo:
    #     await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
