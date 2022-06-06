from telebot import types
import telebot
import datetime
import sqlite3
from random import randint
bot = telebot.TeleBot("5203531297:AAGDvZd71lGY-qO8PkpvgGnnQtseJDxaDe0")

mm = types.ReplyKeyboardMarkup(row_width=2)
resize_keyboard=True
button1 = types.KeyboardButton("time")
button2 = types.KeyboardButton("date")
button3 = types.KeyboardButton("register")
button4 = types.KeyboardButton("close@ChatHelperByRabilint_bot")
button5 = types.KeyboardButton("delete me") #кнопки
button6 = types.KeyboardButton("when i signed up?")
telebot.types.ReplyKeyboardRemove()
mm.add(button1,button2,button3,button4,button5,button6)
reply_markup=mm
telebot.types.ReplyKeyboardRemove()
r = 3

dateToday = datetime.date.today()

toOrdinal = dateToday.toordinal()


#toOrdinal

@bot.message_handler(content_types=['text'])
def handler(message):

    chat_id = message.chat.id



    connect = sqlite3.connect('SS')
    cursor = connect.cursor()
    cursor.execute(f"SELECT id FROM SS WHERE id = '{message.chat.id}'")
    data = cursor.fetchone()

    if data is None:
        cursor.execute(f"INSERT INTO SS VALUES(?,?)",(message.chat.id,0))
        connect.commit()

    languageSS = cursor.execute('SELECT language FROM SS WHERE id=:chat_id',
                               {"chat_id": chat_id}).fetchone()[0]

    if languageSS == 1 :

        if message.text == "/kubik@ChatHelperByRabilint_bot" :
            h = randint(1,6)
            bot.reply_to(message,h)

        if message.text == "/ban":
            bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEvfZiggAB4gHTuu2ZTg1dLENsJ-uBjSwAAjYAA7yRNhfaUtiZ6jK5ryQE")

        if message.text.lower() == "доброе утро" :
            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEvfhiggF9oo0SdYq83HssAwo3PqACtQAC-xgAAiOwMUuozDpOKtjmrCQE")

        if message.text.lower() == "бот рабилинта идиот" :
            bot.send_sticker(message.chat.id,"CAACAgEAAxkBAAEEvfpiggIcbybKYtw-Co5zWwJ3m9AUHwAChQADwKwII6SrOomw-oViJAQ")

        if message.text == "/helpad@ChatHelperByRabilint_bot":
            bot.reply_to(message,"5168755907699322 - privat , Спасибо ")
            bot.send_sticker(message.chat.id,"CAACAgEAAxkBAAEEvftiggId8KDs_sqIoaDpK0YgUvn50QACUgADwKwIIy3tvSk347AcJAQ")

      #  if message.text == "/language" :


        #???????????????????????????????????????????

        #Dev message

        #bot.send_message(message.chat.id , "сейчас работает тестовый сервер всё что вы тут делаете не будет на основном сервере !")

        #?????????????????????????????????????????


        #if message.text == '/start@ChatHelperByRabilint_bot' or "/start" :  #
            #bot.send_message(message.chat.id,"Starting ...", reply_markup=mm)

        if message.text == "/ver@ChatHelperByRabilint_bot" :
            try :
                bot.reply_to(message,"ver : 5.1 ( language update )" )
                print(str(message.from_user.id)+"checking ver ")
            except:
                bot.send_message(message.chat.id,"ver error")

        if message.text == "/idea@ChatHelperByRabilint_bot" :
            bot.reply_to(message,"https://t.me/Rabilint telegram админа \n rabilint#4659 - discord админа ")

        if message.text == "/myid@ChatHelperByRabilint_bot" :
            try:

                bot.reply_to(message,"твой телеграм айди : "+ str(message.from_user.id))
            except:
                bot.send_message(message.chat.id,"( id ) error")

        if message.text == "/help@ChatHelperByRabilint_bot" :
            try:
                print(str(message.from_user.id)+(" need help"))
                bot.reply_to(message," /chlan - сменить язык на Англ  \n /idea - отправить идею \n /helpad - Помочь админу деньгой  \n /kubik - 1-6 \n /register - регистрация \n /deleteme - удалить себя \n /ver - Версия бота \n /myid - твой айди \n /whenisignedup -  когда ты зарегистрировался \n /kazino - сыграть в казино \n /balance - баланc \n /makedick - сыграть в игру  ( член ) \n /howlong - длина члена ")
            except:
                bot.send_message(message.chat.id,"error help")

        if message.text == "/balance@ChatHelperByRabilint_bot":
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                print("balance"+ str(message.from_user.id))
                cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
                data = cursor.fetchone()

                if data is None:
                    bot.reply_to(message,"У вас нету акаунта ")
                else :
                    for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                        bot.reply_to(message,
                                            f"Ваш баланс : {value[0]}",
                                            parse_mode='html')
            except:
                bot.send_message(message.chat.id,"balance error")



        if message.text == "/kazino@ChatHelperByRabilint_bot" :

            tTK = True
            tTl = False
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()

            if data is None:
                a = datetime.datetime.now()
                print("new user play kazino" + str(message.from_user.id))
                b = toOrdinal
                cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)",(message.from_user.id, message.from_user.username, b, 0, 0,0))
                connect.commit()
                a1 = randint(1, 3)
                a2 = randint(1, 3)
                a3 = randint(1, 3)
                try:

                    if a1 and a2 != a3:
                        tTl = True
                    if a2 and a3 != a1:
                        tTl = True
                    if a1 and a3 != a2:
                        tTl = True
                    if tTl == False:
                        if a1 and a2 and a3 == 3:
                            tTK = False
                            cursor.execute(f"UPDATE users SET balance = balance + 500 WHERE id = {message.from_user.id}")
                            bot.reply_to(message,"Джекпот !!!  == 500 \n Номера вашего билета --->\n" + str(a1) + ' ' + str(a2) + " " + str(a3))
                            connect.commit()
                            for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                bot.send_message(message.chat.id,
                                                 f"Your balance : {value[0]}",
                                                 parse_mode='html')
                        if tTK:
                            if a3 and a2 == a1:
                                bot.reply_to(message,"Вы выиграли 100$ \n  Номера вашего билета --->\n" + str(a1) + ' ' + str(a2) + " " + str(a3))
                                cursor.execute(f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                connect.commit()
                                for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                    bot.reply_to(message,
                                                     f"Your balance: {value[0]}",
                                                     parse_mode='html')
                    elif tTl == True:
                        bot.send_message(message.chat.id,"Неудача  \n Номера вашего билета  --->\n" + str(a1) + '\n' + str(a2) + "\n" + str(a3))
                except :
                    bot.send_message(message.chat.id,'error kazino')

            else :
                a1 = randint(1,3)
                print("play kazino "+ str(message.from_user.id))
                a2 = randint(1,3)
                a3 = randint(1,3)
                try :

                    if a1 and a2 != a3 :
                        tTl = True
                    if a2 and a3 != a1 :
                        tTl = True
                    if a1 and a3 != a2 :
                        tTl = True
                    if tTl == False :
                        if a1 and a2 and a3 == 3 :
                            tTK = False
                            cursor.execute(f"UPDATE users SET balance = balance + 500 WHERE id = {message.from_user.id}")
                            bot.reply_to(message, "Джекпот !!! == 500 \n Номера вашего билета --->\n" + str(a1)+" "+ str(a2) + " " + str(a3))
                            connect.commit()

                        if tTK :
                            if a3 and a2 == a1 :
                                bot.reply_to(message,"Вы выиграли 100$ \n Вашы номера билета  --->\n"+str(a1)+" "+str(a2)+ " "+str(a3))
                                cursor.execute(f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                connect.commit()
                    elif tTl ==True :
                        bot.reply_to(message,"неудача \n номера вашего билета  --->\n"+str(a1)+" "+str(a2)+" "+str(a3))
                except :
                    bot.send_message(message.chat.id,'error kazino')





        #if message.text == "/time@ChatHelperByRabilint_bot":  #
        #    a = datetime.datetime.now()
        #    c = str(a.hour) + ' : ' + str(a.minute) + " : " + str(a.second)
        #    bot.send_message(message.chat.id, c)
        #if message.text == "/date@ChatHelperByRabilint_bot":   # ДАта
        #    b = datetime.date.today()
        #    bot.send_message(message.chat.id, b)



        #if message.text == 'close@ChatHelperByRabilint_bot' :  #
            #a = telebot.types.ReplyKeyboardRemove()
            #bot.send_message(message.from_user.id, 'Ending...', reply_markup=a)




        if message.text == "/register@ChatHelperByRabilint_bot" :  #Регистрация
            try :
                connect= sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
                data = cursor.fetchone()

                if data is None :
                    a = datetime.datetime.now()
                    b = toOrdinal
                    cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)", (message.from_user.id, message.from_user.username,b,0,0,0))
                    connect.commit()
                    print("new user)"+str(message.from_user.id))
                    bot.send_message(message.chat.id , "успешная регистрация ")
                else :
                    bot.send_message(message.chat.id,"Вы уже зарегистрированы ")
            except :
                bot.send_message(message.chat.id , "reg error")



        if message.text == "/deleteme@ChatHelperByRabilint_bot":
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"DELETE FROM users WHERE id = {message.from_user.id}")
                connect.commit()
                print("minus user ("+str(message.from_user.id))
                bot.send_message(message.chat.id, "акаунт удалён")
            except :
                bot.send_message(message.chat.id , "error del")




        if message.text == "/whenisignedup@ChatHelperByRabilint_bot" :
            try:
                user_id = message.from_user.id
                a = datetime.datetime.now()
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                print("when signe up"+str(message.from_user.id))
                try :
                    b = cursor.execute('SELECT regdate FROM users WHERE id=:user_id',
                                       {"user_id":user_id}).fetchone()[0]
                    Rabilint = toOrdinal
                    answ = Rabilint - int(b)
                    if answ == 0 :
                        bot.send_message(message.chat.id,'Вы зарегистрировались сегодня ')
                    else :
                        bot.send_message(message.chat.id,str(answ) + " Дней с вашей регистрации ")
                except :
                    bot.send_message(message.chat.id,'пожалуйста зарегистрируйтесь ')
            except :
                bot.send_message(message.chat.id,"when error")



        if message.text == "Rabilint" :
            print("rabilint"+str(message.from_user.id))
            bot.send_message(message.chat.id,'the best')

        if message.text == "Glore to Ukraine" :
            bot.send_message(message.chat.id,"Glore to hero")

        if message.text == "Azov" :
            bot.reply_to(message, "ꑭ")

        if message.text == "/makedick@ChatHelperByRabilint_bot" :

            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()  # проверяем, есть ли такая запись в таблице
            if data is None:  # если такой записи нет, то:
                a1 = randint(-5,10)

                a = datetime.datetime.now()
                b = toOrdinal
                cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)", (message.from_user.id, message.from_user.username,b,0,a1,0))
                connect.commit()
                for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                    bot.send_message(message.chat.id,
                                     f"Твой член увеличился на " + str(a1)+
                                     f" см теперь он : {value[0]} см",
                                     parse_mode='html')
            else :
                a1 = randint(-5, 10)
                d = a1
                user_id = message.from_user.id
                a = datetime.datetime.now()
                b2 = toOrdinal
                b1 = cursor.execute('SELECT timer FROM users WHERE id=:user_id',
                                   {"user_id": user_id}).fetchone()[0]
                if b1 < b2 :
                    cursor.execute(f"UPDATE users SET Dick = Dick + {d} WHERE id = {message.from_user.id}")
                    b = toOrdinal
                    cursor.execute(f"UPDATE users SET timer = {b} WHERE id = {message.from_user.id}")
                    connect.commit()
                    for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                        bot.send_message(message.chat.id,
                                         f"Твой член увеличился на " + str(a1) +
                                         f" см теперь он : {value[0]} см",
                                         parse_mode='html')
                else :
                    bot.send_message(message.chat.id,"приходи на следующий день")

        #//////////////////////////////////
        if message.text == "/howlong@ChatHelperByRabilint_bot" :
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
                data = cursor.fetchone()  # проверяем, есть ли такая запись в таблице
                if data is None:  # если такой записи нет, то:
                    bot.reply_to(message,"У вас нет члена )")
                else :
                    for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                        bot.send_message(message.chat.id,
                                         f"Длина вашего члена : {value[0]} см",
                                         parse_mode='html')

        if message.text == "/chlan@ChatHelperByRabilint_bot" :
            cursor.execute(f"UPDATE SS SET language = {0} WHERE id = {message.chat.id}")
            connect.commit()
            bot.send_message(message.chat.id ,"ок меняю язык на Англ ... ")

    else :

        if message.text == "/kubik@ChatHelperByRabilint_bot":
            h = randint(1, 6)
            bot.reply_to(message, h)

        if message.text == "/ban":
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEvfZiggAB4gHTuu2ZTg1dLENsJ-uBjSwAAjYAA7yRNhfaUtiZ6jK5ryQE")

        if message.text.lower() == "good morning":
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEvfhiggF9oo0SdYq83HssAwo3PqACtQAC-xgAAiOwMUuozDpOKtjmrCQE")

        if message.text.lower() == "Bot idiot":
            bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEEvfpiggIcbybKYtw-Co5zWwJ3m9AUHwAChQADwKwII6SrOomw-oViJAQ")

        if message.text == "/helpad@ChatHelperByRabilint_bot":
            bot.reply_to(message, "5168755907699322 - privat , thanks ")
            bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEEvftiggId8KDs_sqIoaDpK0YgUvn50QACUgADwKwIIy3tvSk347AcJAQ")

        #  if message.text == "/language" :

        # ???????????????????????????????????????????

        # Dev message

        # bot.send_message(message.chat.id , "сейчас работает тестовый сервер всё что вы тут делаете не будет на основном сервере !")

        # ?????????????????????????????????????????

        # if message.text == '/start@ChatHelperByRabilint_bot' or "/start" :  #
        # bot.send_message(message.chat.id,"Starting ...", reply_markup=mm)

        if message.text == "/ver@ChatHelperByRabilint_bot":
            try:
                bot.reply_to(message, "ver : 5.1 ( language update )")
                print(str(message.from_user.id) + "checking ver ")
            except:
                bot.send_message(message.chat.id, "ver error")

        if message.text == "/idea@ChatHelperByRabilint_bot":
            bot.reply_to(message, "https://t.me/Rabilint telegram admin \n rabilint#4659 - discord")

        if message.text == "/myid@ChatHelperByRabilint_bot":
            try:

                bot.reply_to(message, "your id : " + str(message.from_user.id))
            except:
                bot.send_message(message.chat.id, "( id ) error")

        if message.text == "/help@ChatHelperByRabilint_bot":
            try:
                print(str(message.from_user.id) + (" need help"))
                bot.reply_to(message," /chlan - change language to russian \n  /idea - send idea \n /helpad - help admin with money \n /kubik - 1-6 \n /register - register in bot \n /deleteme - delet himself from bot \n /ver - bot version \n /myid - your telegram id \n /whenisignedup -  when you sign up \n /kazino - play casino \n /balance - your virtual money \n /makedick - play at ( dick ) game \n /howlong - how long your dick ")
            except:
                bot.send_message(message.chat.id, "error help")

        if message.text == "/balance@ChatHelperByRabilint_bot":
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                print("balance" + str(message.from_user.id))
                cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
                data = cursor.fetchone()

                if data is None:
                    bot.reply_to(message, "you don't have an account")
                else:
                    for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                        bot.reply_to(message,
                                     f"Your balance : {value[0]}",
                                     parse_mode='html')
            except:
                bot.send_message(message.chat.id, "balance error")

        if message.text == "/kazino@ChatHelperByRabilint_bot":

            tTK = True
            tTl = False
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()

            if data is None:
                a = datetime.datetime.now()
                print("new user play kazino" + str(message.from_user.id))
                b = toOrdinal
                cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)",
                               (message.from_user.id, message.from_user.username, b, 0, 0, 0))
                connect.commit()
                a1 = randint(1, 3)
                a2 = randint(1, 3)
                a3 = randint(1, 3)
                try:

                    if a1 and a2 != a3:
                        tTl = True
                    if a2 and a3 != a1:
                        tTl = True
                    if a1 and a3 != a2:
                        tTl = True
                    if tTl == False:
                        if a1 and a2 and a3 == 3:
                            tTK = False
                            cursor.execute(
                                f"UPDATE users SET balance = balance + 500 WHERE id = {message.from_user.id}")
                            bot.reply_to(message, "You win jackpot == 500 \nYour number --->\n" + str(a1) + ' ' + str(
                                a2) + " " + str(a3))
                            connect.commit()
                            for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                bot.send_message(message.chat.id,
                                                 f"Your balance : {value[0]}",
                                                 parse_mode='html')
                        if tTK:
                            if a3 and a2 == a1:
                                bot.reply_to(message,
                                             "you win 100$ \nYour number --->\n" + str(a1) + ' ' + str(a2) + " " + str(
                                                 a3))
                                cursor.execute(
                                    f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                connect.commit()
                                for value in cursor.execute(
                                        f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                    bot.reply_to(message,
                                                 f"Your balance: {value[0]}",
                                                 parse_mode='html')
                    elif tTl == True:
                        bot.send_message(message.chat.id,
                                         "failure \nYour number --->\n" + str(a1) + '\n' + str(a2) + "\n" + str(a3))
                except:
                    bot.send_message(message.chat.id, 'error kazino')



            else:
                a1 = randint(1, 3)
                print("play kazino " + str(message.from_user.id))
                a2 = randint(1, 3)
                a3 = randint(1, 3)
                try:

                    if a1 and a2 != a3:
                        tTl = True
                    if a2 and a3 != a1:
                        tTl = True
                    if a1 and a3 != a2:
                        tTl = True
                    if tTl == False:
                        if a1 and a2 and a3 == 3:
                            tTK = False
                            cursor.execute(
                                f"UPDATE users SET balance = balance + 500 WHERE id = {message.from_user.id}")
                            bot.reply_to(message, "You win jackpot == 500 \nYour number --->\n" + str(a1) + " " + str(
                                a2) + " " + str(a3))
                            connect.commit()

                        if tTK:
                            if a3 and a2 == a1:
                                bot.reply_to(message,
                                             "you win 100$ \nYour number --->\n" + str(a1) + " " + str(a2) + " " + str(
                                                 a3))
                                cursor.execute(
                                    f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                connect.commit()
                    elif tTl == True:
                        bot.reply_to(message, "failure \nYour number --->\n" + str(a1) + " " + str(a2) + " " + str(a3))
                except:
                    bot.send_message(message.chat.id, 'error kazino')

        # if message.text == "/time@ChatHelperByRabilint_bot":  #
        #    a = datetime.datetime.now()
        #    c = str(a.hour) + ' : ' + str(a.minute) + " : " + str(a.second)
        #    bot.send_message(message.chat.id, c)
        # if message.text == "/date@ChatHelperByRabilint_bot":   # ДАта
        #    b = datetime.date.today()
        #    bot.send_message(message.chat.id, b)

        # if message.text == 'close@ChatHelperByRabilint_bot' :  #
        # a = telebot.types.ReplyKeyboardRemove()
        # bot.send_message(message.from_user.id, 'Ending...', reply_markup=a)

        if message.text == "/register@ChatHelperByRabilint_bot":  # Регистрация
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
                data = cursor.fetchone()

                if data is None:
                    a = datetime.datetime.now()
                    b = toOrdinal
                    cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)",
                                   (message.from_user.id, message.from_user.username, b, 0, 0, 0))
                    connect.commit()
                    print("new user)" + str(message.from_user.id))
                    bot.send_message(message.chat.id, "you was register")
                else:
                    bot.send_message(message.chat.id, "User already registered")
            except:
                bot.send_message(message.chat.id, "reg error")

        if message.text == "/deleteme@ChatHelperByRabilint_bot":
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"DELETE FROM users WHERE id = {message.from_user.id}")
                connect.commit()
                print("minus user (" + str(message.from_user.id))
                bot.send_message(message.chat.id, "account deletion was successful")
            except:
                bot.send_message(message.chat.id, "error del")

        if message.text == "/whenisignedup@ChatHelperByRabilint_bot":
            try:
                user_id = message.from_user.id
                a = datetime.datetime.now()
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                print("when signe up" + str(message.from_user.id))
                try:
                    b = cursor.execute('SELECT regdate FROM users WHERE id=:user_id',
                                       {"user_id": user_id}).fetchone()[0]
                    Rabilint = toOrdinal
                    answ = Rabilint - int(b)
                    if answ == 0:
                        bot.send_message(message.chat.id, 'you was registered today')
                    else:
                        bot.send_message(message.chat.id, str(answ) + " Day(s) ago you were registered")
                except:
                    bot.send_message(message.chat.id, 'please register to use this command')
            except:
                bot.send_message(message.chat.id, "when error")

        if message.text == "Rabilint":
            print("rabilint" + str(message.from_user.id))
            bot.send_message(message.chat.id, 'the best')

        if message.text == "Glore to Ukraine":
            bot.send_message(message.chat.id, "Glore to hero")

        if message.text == "Azov":
            bot.reply_to(message, "ꑭ")

        if message.text == "/makedick@ChatHelperByRabilint_bot":

            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()  # проверяем, есть ли такая запись в таблице
            if data is None:  # если такой записи нет, то:
                a1 = randint(-5, 10)

                a = datetime.datetime.now()
                b = toOrdinal
                cursor.execute(f"INSERT INTO users VALUES(?,?,?,?,?,?)",
                               (message.from_user.id, message.from_user.username, b, 0, a1, 0))
                connect.commit()
                for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                    bot.send_message(message.chat.id,
                                     f"Your dick having grown  " + str(a1) +
                                     f" centimeter Now him : {value[0]} centimeter",
                                     parse_mode='html')
            else:
                a1 = randint(-5, 10)
                d = a1
                user_id = message.from_user.id
                a = datetime.datetime.now()
                b2 =toOrdinal
                b1 = cursor.execute('SELECT timer FROM users WHERE id=:user_id',
                                    {"user_id": user_id}).fetchone()[0]
                if b1 < b2 :
                    cursor.execute(f"UPDATE users SET Dick = Dick + {d} WHERE id = {message.from_user.id}")
                    b = toOrdinal
                    cursor.execute(f"UPDATE users SET timer = {b} WHERE id = {message.from_user.id}")
                    connect.commit()
                    for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                        bot.send_message(message.chat.id,
                                         f"Your dick having grown  " + str(a1) +
                                         f"  centimeter Now him : {value[0]} centimeter ",
                                         parse_mode='html')
                else:
                    bot.send_message(message.chat.id, "come in a day")

        # //////////////////////////////////
        if message.text == "/howlong@ChatHelperByRabilint_bot":
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()  # проверяем, есть ли такая запись в таблице
            if data is None:  # если такой записи нет, то:
                bot.reply_to(message, "You haven`t dick )")
            else:
                for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                    bot.send_message(message.chat.id,
                                     f"Your Dick: {value[0]}",
                                     parse_mode='html')

        if message.text == "/chlan@ChatHelperByRabilint_bot" :
            cursor.execute(f"UPDATE SS SET language = {1} WHERE id = {message.chat.id}")
            connect.commit()
            bot.send_message(message.chat.id ,"ok change language to russian ... ")


bot.polling(none_stop=True)


