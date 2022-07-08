from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

texts = """
Xoş Gəldin Mesajı Qarşılama:

Üzvlərinizə salamlama modulu ilə xoş qarşılayın!  Ya da kədərli bir vida... Asılıdır!

Admin commands:
- /welcome : Xoş qarşılama mesajlarını aktivləşdirin/deaktiv edin.
- /goodbye : Vida mesajlarını aktivləşdirin/deaktiv edin.
- /setwelcome : Yeni salamlama mesajı təyin edin.  İşarələmə, düymələr və doldurmaları dəstəkləyir.
- /resetwelcome: Xoş gəlmisiniz mesajını sıfırlayın.
- /setgoodbye : Yeni vida mesajı təyin edin.  İşarələmə, düymələr və doldurmaları dəstəkləyir.
- /resetgoodbye: Vida mesajını sıfırlayın.
- /cleanservice : Bütün xidmət mesajlarını silin.  İnsanlar qoşulduqda gördüyünüz zəhlətökən "x qrupa qoşuldu" bildirişləridir.
- /cleanwelcome : Köhnə salamlama mesajlarını silin.  Yeni şəxs qoşulduqda və ya 5 dəqiqədən sonra əvvəlki mesaj silinəcək.

Məsələn:
- Heç bir formatlaşdırmadan salamlama mesajını alın
-> /welcome XoşGəldiniz 🎉
"""

fbuttonss = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('captcha', callback_data="_filling"),
        InlineKeyboardButton('Formatting', callback_data='_mdownsl')
        ]]
  
)

@app.on_callback_query(filters.regex("_mdowns"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=texts,
        reply_markup=fbuttonss,
        disable_web_page_preview=True,
        parse_mode="html"
    )
    await CallbackQuery.message.delete()

tetz = """
Yeni Qrup Üzvlərindən emoji həll edərək onları təsdiqləmələrini xahiş edəcək Rose sayı captcha.

- /captcha - captcha-nı yandırın: İki növ captcha var
- /remove - captcha-nı söndürün

daha çox kömək üçün dəstək qrupumdan soruşun.🧑🏻‍💻
"""
@app.on_callback_query(filters.regex("_filling"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=tetz,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()

close = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('« Geri', callback_data='_mdowns')
        ]], 
)
