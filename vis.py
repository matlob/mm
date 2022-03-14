import random
import telebot
from telebot import types
ToKen="1894082224:AAEmXvFMPzFkHeFbsLe4Isq6VCTHg3vvM"
bot = telebot.TeleBot(ToKen)
@bot.message_handler(commands = ["start"])
def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="✅  المبرمج" , url = "t.me/F_7_U")
 C = types.InlineKeyboardButton(text ="✅ قناة مبرمج  " , url = "https://t.me/PR2_NET")
 D =  types.InlineKeyboardButton(text = "✅ الحصول على كومبو  فيزات",callback_data="y")
 A.add(B,C,D)
 bot.reply_to(message, """  
*- اهلا عزيزي ( {} )                             
- في بوت صنع فيزات
- قم بــ ضغط على الحصول على كومبو فيزات               
- معرفك : [ @{} ]                                    
- ايديك : [ {} ]                                        *
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
P  = types.InlineKeyboardButton(text = "الحصول على كومبو", callback_data= 'Iran')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(P)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Choose**",parse_mode='markdown',reply_markup=O0)          
def Iran(message):
	abc='1234567890'
	an='123456789'
	ak="23456789"
	savefile = open('VisaX.txt','a')
	for v in range(1000):
		uss = str(''.join((random.choice(abc) for i in range(15))))
		us = str(''.join((random.choice(abc) for i in range(1))))
		uk = str(''.join((random.choice(ak) for i in range(1))))
		am = str(''.join((random.choice(abc) for i in range(3))))
		xn = ('5'+uss+'|'+'0'+us+'|'+'202'+uk+'|'+am)
		savefile.write(xn + "\n")
	file = open('VisaX.txt','rb')
	bot.send_document(message.chat.id,file,caption="<strong>New Combo</strong>",parse_mode="html")
bot.polling()
