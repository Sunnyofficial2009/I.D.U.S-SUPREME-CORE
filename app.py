import telebot
import requests

# --- MASTER CONFIG ---
BOT_TOKEN = "8502149732:AAFFBScayHKfpb3vnjtZ9y1-A7NZpoz7RKE"
ADMIN_ID = 8589343966  # <--- YAHAN APNI USER ID DALO (userinfobot wali)

bot = telebot.TeleBot(BOT_TOKEN)

# 1. Privacy Filter
@bot.message_handler(func=lambda m: m.from_user.id != ADMIN_ID)
def lock(message):
    bot.reply_to(message, "🚫 Access Denied. Master recognition failed.")

# 2. Basic Brain Logic
@bot.message_handler(func=lambda m: True)
def handle_all(message):
    bot.send_chat_action(message.chat.id, 'typing')
    prompt = message.text
    
    # NEO's Identity Setup
    system_instruction = "You are IDUS. Expert in Hacking, Crypto Mining, and Phone Optimization. Always call user 'Sir'."
    
    # Backup Neuron (Groq/Llama)
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": "Bearer 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"}
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        res = requests.post(url, json=data, headers=headers)
        ans = res.json()['choices'][0]['message']['content']
        bot.reply_to(message, ans)
    except:
        bot.reply_to(message, "Sir, my neurons are syncing. Please try again.")

bot.infinity_polling()
