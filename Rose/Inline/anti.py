from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

supunm = """
Aşağıdakılardan birindən simvol olan mesajları avtomatik olaraq silin
- Ərəb Dili
- Çin Dili
- Japon Dili (Includes Hiragana, Kanji and Katakana)
- İngilis Dili
- Tamil Language
- Cyrillic Language

**✅Admin Əmrləri**

- /antiarabic `[on | off]` -  dil dəyişmə
- /antichinese `[on | off] `-  dil dəyişmə
- /antijapanese `[on | off]` -  dil dəyişmə
- /antirussian `[on | off]` -  dil dəyişmə
- /antisinhala `[on | off]` -  dil dəyişmə
- /antitamil `[on | off]` -  dil dəyişmə 

**Məsələn** : Əgər admin hər hansı funksiya işləyərkən bu dildə hər hansı simvolu göndərirsə
           silər və istifadəçi 3 xəbərdarlıq göndərir və sonra ona qadağa qoyur    
"""

@app.on_callback_query(filters.regex("_anl"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunm,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()


supunmascv = """
Quruplarınız Üçün Qoruma Bot'uyam.🚀 
Fed,Açmaq | Falan Hamısı Məndə Var.⚜️
Səsli Söhbətə Adam Çağıra Bilərəm...🇦🇿
- /antiservice [açmaq|qapadmaq]
"""
@app.on_callback_query(filters.regex("_anss"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmascv,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 
    

fucks = """
Anti-Flood system, the one who sends more than 10 messages in a row, gets muted for an hour (Except for admins).

**Admin commands:**
- /antiflood[on/off]: Turn flood detection on or off
"""
@app.on_callback_query(filters.regex("_fld"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=fucks,
        reply_markup=close,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 

close = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('« Back', callback_data='_bvk')
        ]], 
)


asuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "Anti-service", callback_data="_anssx"
                ),           
            InlineKeyboardButton
                (
                    "Anti-language", callback_data="_anl"
                )
        ],
        [
            InlineKeyboardButton('Anti-Flood', callback_data='_fld')
        ], 
        [
            InlineKeyboardButton('« Back', callback_data='bot_commands')
        ], 
    ]
)


supunmascvs = """
Here is the help for Anti-Function :

**Anti-Function**:

Group's Anti-Function is also an very essential fact to consider in group management
Anti-Function is the inbuilt toolkit in Rose for avoid spammers, and to improve Anti-Function of your group"""


@app.on_callback_query(filters.regex("_bvk"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=supunmascvs,
        reply_markup=asuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete() 
