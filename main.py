import asyncio
import base64
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from googletrans import Translator

# 1. Sozlamalar
API_TOKEN = "SIZNING_TOKENINGIZNI_SHU_YERGA_YAZING"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
translator = Translator()

# --- YORDAMCHI FUNKSIYALAR ---

# Shifrlash: Matnni Base64 formatga o'tkazadi (kopya qilish oson)
def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

# Shifrdan ochish: Base64 kodni asl matnga qaytaradi
def decode_base64(code):
    try:
        return base64.b64decode(code.encode('utf-8')).decode('utf-8')
    except:
        return "❌ Xatolik: Noto'g'ri kodlangan matn!"

# Raqamli shifrlash (ASCII): Har bir belgini raqamga o'giradi
def encode_to_numbers(text):
    return " ".join(str(ord(char)) for char in text)

# Raqamli shifrni ochish
def decode_from_numbers(numbers):
    try:
        return "".join(chr(int(num)) for num in numbers.split())
    except:
        return "❌ Xatolik: Noto'g'ri raqamlar!"

# Tarjima
def translate_text(text, dest='en'):
    result = translator.translate(text, dest=dest)
    return result.text

# --- BOT KOMANDALARI ---

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Xush kelibsiz! Bot funksiyalari:\n\n"
        "🔐 /encode [matn] - Matnni Base64 shifrlash\n"
        "🔓 /decode [kod] - Base64 shifrdan ochish\n"
        "🔢 /num [matn] - Matnni raqamli ko'rinishga o'tkazish\n"
        "📝 /denum [raqamlar] - Raqamlarni matnga qaytarish\n"
        "🌐 /tr [til] [matn] - Tarjima (masalan: /tr en salom)"
    )

@dp.message(Command("encode"))
async def cmd_encode(message: types.Message):
    text = message.text.replace("/encode", "").strip()
    if text:
        await message.answer(f"🔐 Shifrlangan:\n`{encode_base64(text)}`", parse_mode="Markdown")
    else:
        await message.answer("Iltimos, matn kiriting.")

@dp.message(Command("decode"))
async def cmd_decode(message: types.Message):
    code = message.text.replace("/decode", "").strip()
    await message.answer(f"🔓 Asl matn:\n{decode_base64(code)}")

@dp.message(Command("num"))
async def cmd_num(message: types.Message):
    text = message.text.replace("/num", "").strip()
    await message.answer(f"🔢 Raqamli ko'rinish:\n`{encode_to_numbers(text)}`", parse_mode="Markdown")

@dp.message(Command("denum"))
async def cmd_denum(message: types.Message):
    nums = message.text.replace("/denum", "").strip()
    await message.answer(f"📝 Matn ko'rinishi:\n{decode_from_numbers(nums)}")

@dp.message(Command("tr"))
async def cmd_translate(message: types.Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) >= 3:
        await message.answer(f"🌐 Tarjima:\n{translate_text(parts[2], parts[1])}")
    else:
        await message.answer("Format: /tr [til_kodi] [matn]\nMasalan: /tr en salom")

# --- ISHGA TUSHIRISH ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 
