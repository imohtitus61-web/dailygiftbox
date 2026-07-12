from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random

MAX_WINNERS = 20
accepted_users = set()

GROUP_LINK = "https://t.me/YOUR_GROUP_LINK"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Open Gift Box", callback_data="gift")]
    ]

    await update.message.reply_text(
        "🎁 Welcome to Daily Gift Box!\n\n"
        "Tap the button below to see if you are one of today's lucky winners.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def gift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if user_id in accepted_users:
        await query.message.reply_text(
            "✅ You have already opened today's gift."
        )
        return

    if len(accepted_users) >= MAX_WINNERS:
        await query.message.reply_text(
            "❌ Today's giveaway is full.\n\nTry again tomorrow."
        )
        return

    lucky = random.choice([True, False])

    if lucky:
        accepted_users.add(user_id)

        await query.message.reply_text(
            f"🎉 Congratulations!\n\n"
            f"You are Lucky Member #{len(accepted_users)} of {MAX_WINNERS}.\n\n"
            f"Join today's group:\n{https://t.me/+tqi7wRxBCms1NmY0}"
        )
    else:
        await query.message.reply_text(
            "😔 Not selected today.\n\nTry again tomorrow."
        )


app = Application.builder().token("8895841513:AAHugpUpvmozQMaoIcI6Ef1qbTdLTKVl5u4").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(gift, pattern="gift"))

print("Bot is running...")
app.run_polling()
