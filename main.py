from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is Aapada Mitra\n
Click /content for more info
\nHow Can I Help You Today?""")

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is Aapada Mitra
    \nHere are your controls - 
    /start to start the service\n
    /help to get Help\n
    /content to see the menu again
    \nYou can also type keywords like \n'snake bite', 'lightning', 'boat safety', or 'heatwave' \nto get specific guidelines on how to handle these emergencies.
    """)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Call Rahat Helpline 1070 / 112
    Call Police 100
    Call Ambulance 108
    Call Tourist Police 1422""")

async def snake_bite_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
    Snake Bite:\n
    Do's:
    \t- Stay calm; move away from the snake.
    \t- Immobilize the limb and keep it below heart level.
    \t- Seek immediate medical help.
    
    Don'ts:
    \t- Don’t suck out venom.
    \t- Don’t apply ice or a tourniquet.
    \t- Avoid alcohol and caffeine.
    """
    await update.message.reply_text(response)

async def lightning_safety_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
    Lightning Safety:\n
    Do's:
    \t- Seek shelter indoors.
    \t- If outdoors, crouch low.
    
    Don'ts:
    \t- Avoid trees and metal objects.
    \t- Don’t lie flat on the ground.
    """
    await update.message.reply_text(response)

async def boat_safety_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
    Boat Safety:\n
    Do's:
    \t- Wear life jackets.
    \t- Monitor weather conditions.
    \t- Equip with emergency supplies.
    
    Don'ts:
    \t- Do not overload the boat.
    """
    await update.message.reply_text(response)

async def heatwave_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
    Heatwave:\n
    Do's:
    \t- Stay hydrated and indoors.
    \t- Wear light, loose clothing.
    \t- Use fans and block out the sun with curtains.
    
    Don'ts:
    \t- Avoid alcohol and caffeine.
    \t- Don’t leave children or pets in parked vehicles.
    \t- Limit outdoor activities during peak heat hours.
    """
    await update.message.reply_text(response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    snake_bite_keywords = {"snake bite", "snakebite", "snake"}
    lightning_keywords = {"lightning", "storm", "thunder"}
    boat_safety_keywords = {"boat safety", "boating", "boat", "watercraft"}
    heatwave_keywords = {"heatwave", "heat wave", "hot weather", "extreme heat"}

    if any(keyword in text for keyword in snake_bite_keywords):
        await snake_bite_response(update, context)
    elif any(keyword in text for keyword in lightning_keywords):
        await lightning_safety_response(update, context)
    elif any(keyword in text for keyword in boat_safety_keywords):
        await boat_safety_response(update, context)
    elif any(keyword in text for keyword in heatwave_keywords):
        await heatwave_response(update, context)
    else:
        await update.message.reply_text("I'm sorry, I couldn't understand your request. Please try again with more specific keywords.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("content", content))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
