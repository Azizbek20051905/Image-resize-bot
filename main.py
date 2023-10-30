# Yaratuvchi: Azizbek Ilhomjonov
# Botning vazifasi: Tashlagan rasmingizni 3x4 formatda qirqib qaytaruvchi bot.
# Murojaat uchun t.me: https://t.me/A_404_not_found
# /////////////////////////////////////////////////

# bu modul botda nima jarayonlar bo'layotganini konsolda ko'rsatib turadi
import logging
# Aiogram telegram bot kutubxonasini chaqirish
from aiogram import Bot, Dispatcher, executor
from aiogram import types
# os moduli Bot tokenini olish uchun ishlatildi
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from resize import format_img # Bu modulning vazifasi botga jo'natilgan rasmning razmerini 3x4 ga o'zgartirish

logging.basicConfig(level=logging.DEBUG)

# Botning tokenlari olinadi
# BOT_TOKEN deb yozilgan joyga bot tokeni qo'yiladi
bot = Bot(os.getenv("Token",'BOT_TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

# Botga start berilganda javob qaytaradi
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer(
        text=f"Salom {message.from_user.full_name}🖐.\nMen siz Tashlagan rasmingizni 3x4 formatda qirqib qaytaruvchi botman🏙"
    )

# Botga rasm jo'natganda rasmni 3x4 formatga o'tkazib beradi va qayta foydalanuvchiga qaytariladi  
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def download_photo(message: types.Message):
    await message.reply_sticker(sticker="CAACAgEAAxkBAAIBsmU84Y80cMYAAZw1w-B2NCQmYP2u1QAC7QEAAjgOghE8J4BsgBeaAzAE")
    await message.answer(text=f"Iltimos biroz kutib turing!")
    photo = message.photo[-1]
    photo_file = await bot.get_file(photo.file_id)
    photo_path = photo_file.file_path
    new_photo_path = f'new_{photo_path}'
    await bot.download_file(photo_path, new_photo_path)

    photosize = format_img(new_photo_path, "rasm")
    await message.reply_photo(photo = open(photosize, "rb"))


if __name__ == "__main__":
    # botni ishga tushirish
    try:
        executor.start_polling(dispatcher=dp)
    except Exception as e:
        print(e)