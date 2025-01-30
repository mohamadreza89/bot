from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# جایگزین کردن توکن شما
TOKEN = '8136322119:AAHrRKtXw6SHcGiyBwjzEhytb9ilVI8h7JM'
YOUR_TELEGRAM_ID = 'Mohamadrezazxzx'  # حذف @ از آیدی برای ایجاد لینک مستقیم

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.message.from_user.first_name
    welcome_message = (
        f"سلام {user_first_name}! خوش آمدید به ربات ما 🌟\n\n"
        "راهنمای منو:\n"
        "🤖 **ساخت ربات‌های تلگرام**: ما به شما کمک می‌کنیم ربات‌های فوق‌العاده‌ای برای نیازهای خود بسازید.\n"
        "👥 **درباره ما**: با تیم پرشور و خلاق ما بیشتر آشنا شوید و از کارهای فوق‌العاده‌ای که انجام می‌دهیم، مطلع شوید.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    )

    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown'
    )

    keyboard = [
        [KeyboardButton("👥 درباره ما"), KeyboardButton("🤖 ساخت ربات")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
        reply_markup=reply_markup
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[KeyboardButton("🔙 بازگشت")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "ما یک تیم پرشور و پرانرژی هستیم که به توسعه ربات‌های تلگرام مشغولیم. برای اطلاعات بیشتر با ما تماس بگیرید!",
        reply_markup=reply_markup
    )

async def build_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("📦 سفارش", url=f"https://t.me/{YOUR_TELEGRAM_ID}")],
        [KeyboardButton("🔙 بازگشت")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        'برای ساخت ربات، لطفاً روی دکمه زیر کلیک کنید:',
        reply_markup=reply_markup
    )

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text == "👥 درباره ما":
        await about(update, context)
    elif text == "🤖 ساخت ربات":
        await build_bot(update, context)
    elif text == "🔙 بازگشت":
        await back(update, context)
    else:
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های منو را انتخاب کنید.'
        )

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()