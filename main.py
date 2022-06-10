
from telebot import types
import telebot
import datetime
import sqlite3
from random import randint

bot = telebot.TeleBot("5203531297:AAGDvZd71lGY-qO8PkpvgGnnQtseJDxaDe0")

mm = types.ReplyKeyboardMarkup(row_width=2)
resize_keyboard = True
button1 = types.KeyboardButton("time")
button2 = types.KeyboardButton("date")
button3 = types.KeyboardButton("register")
button4 = types.KeyboardButton("close@ChatHelperByRabilint_bot")
button5 = types.KeyboardButton("delete me")  # кнопки
button6 = types.KeyboardButton("when i signed up?")
telebot.types.ReplyKeyboardRemove()
mm.add(button1, button2, button3, button4, button5, button6)
reply_markup = mm
telebot.types.ReplyKeyboardRemove()
r = 3

dateToday = datetime.date.today()

toOrdinal = dateToday.toordinal()


# toOrdinal

@bot.message_handler(content_types=['text'])
def handler(message):
    chat_id = message.chat.id

    connect = sqlite3.connect('SS')
    cursor = connect.cursor()
    cursor.execute(f"SELECT id FROM SS WHERE id = '{message.chat.id}'")
    data = cursor.fetchone()

    if data is None:
        cursor.execute(f"INSERT INTO SS VALUES(?,?)", (message.chat.id, 0))
        connect.commit()

    languageSS = cursor.execute('SELECT language FROM SS WHERE id=:chat_id',
                                {"chat_id": chat_id}).fetchone()[0]

    if languageSS == 0:
        connect = sqlite3.connect('languageSS')
        cursor = connect.cursor()
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {1}"):
            len1 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {2}"):
            len2 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {3}"):
            len3 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {4}"):
            len4 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {5}"):
            len5 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {6}"):
            len6 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {7}"):
            len7 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {8}"):
            len8 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {9}"):
            len9 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {10}"):
            len10 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {11}"):
            len11 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {12}"):
            len12 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {13}"):
            len13 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {14}"):
            len14 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {15}"):
            len15 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {16}"):
            len16 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {17}"):
            len17 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {18}"):
            len18 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {19}"):
            len19 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {20}"):
            len20 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {21}"):
            len21 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {22}"):
            len22 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {23}"):
            len23 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {24}"):
            len24 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {25}"):
            len25 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {26}"):
            len26 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {27}"):
            len27 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {28}"):
            len28 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {29}"):
            len29 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {30}"):
            len30 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {31}"):
            len31 = f"{value[0]}"

    elif languageSS == 1 :
        connect = sqlite3.connect('languageSS')
        cursor = connect.cursor()
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {1}"):
            len1 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {2}"):
            len2 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {3}"):
            len3 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {4}"):
            len4 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {5}"):
            len5 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {6}"):
            len6 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {7}"):
            len7 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {8}"):
            len8 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {9}"):
            len9 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {10}"):
            len10 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {11}"):
            len11 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {12}"):
            len12 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {13}"):
            len13 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {14}"):
            len14 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {15}"):
            len15 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {16}"):
            len16 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {17}"):
            len17 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {18}"):
            len18 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {19}"):
            len19 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {20}"):
            len20 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {21}"):
            len21 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {22}"):
            len22 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {23}"):
            len23 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {24}"):
            len24 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {25}"):
            len25 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {26}"):
            len26 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {27}"):
            len27 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {28}"):
            len28 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {29}"):
            len29 = f"{value[0]}"
        for value in cursor.execute(f"SELECT UA FROM languageSS WHERE id = {30}"):
            len30 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {31}"):
            len31 = f"{value[0]}"
    elif languageSS == 2 :
        connect = sqlite3.connect('languageSS')
        cursor = connect.cursor()
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {1}"):
            len1 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {2}"):
            len2 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {3}"):
            len3 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {4}"):
            len4 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {5}"):
            len5 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {6}"):
            len6 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {7}"):
            len7 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {8}"):
            len8 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {9}"):
            len9 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {10}"):
            len10 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {11}"):
            len11 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {12}"):
            len12 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {13}"):
            len13 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {14}"):
            len14 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {15}"):
            len15 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {16}"):
            len16 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {17}"):
            len17 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {18}"):
            len18 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {19}"):
            len19 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {20}"):
            len20 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {21}"):
            len21 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {22}"):
            len22 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {23}"):
            len23 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {24}"):
            len24 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {25}"):
            len25 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {26}"):
            len26 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {27}"):
            len27 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {28}"):
            len28 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {29}"):
            len29 = f"{value[0]}"
        for value in cursor.execute(f"SELECT BEL FROM languageSS WHERE id = {30}"):
            len30 = f"{value[0]}"
        for value in cursor.execute(f"SELECT ENG FROM languageSS WHERE id = {31}"):
            len31 = {value[0]}

    connect = sqlite3.connect('SS')
    cursor = connect.cursor()

    if message.text == "/kubik@ChatHelperByRabilint_bot":
        h = randint(1, 6)
        bot.send_message(message.chat.id, str(h))

    if message.text == "/ban":
        bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEvfZiggAB4gHTuu2ZTg1dLENsJ-uBjSwAAjYAA7yRNhfaUtiZ6jK5ryQE")

    if message.text.lower() == len1:
        bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEEvfhiggF9oo0SdYq83HssAwo3PqACtQAC-xgAAiOwMUuozDpOKtjmrCQE")

    if message.text.lower() == len2:
        bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEEvfpiggIcbybKYtw-Co5zWwJ3m9AUHwAChQADwKwII6SrOomw-oViJAQ")

    if message.text == "/helpad@ChatHelperByRabilint_bot":
        bot.reply_to(message, len3)
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
            bot.send_message(message.chat.id , len4)
            print(str(message.from_user.id) + "checking ver ")
        except:
            bot.send_message(message.chat.id, "ver error")

    if message.text == "/idea@ChatHelperByRabilint_bot":
        bot.reply_to(message, len5)

    if message.text == "/myid@ChatHelperByRabilint_bot":
        try:

            bot.reply_to(message, len6 + " : " + str(message.from_user.id))
        except:
            bot.send_message(message.chat.id, "( id ) error")

    if message.text == "/help@ChatHelperByRabilint_bot":
        try:
            print(str(message.from_user.id) + (" need help"))
            bot.reply_to(message,len7)

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
                bot.reply_to(message, len8)
            else:
                for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                    bot.reply_to(message,
                                    len9+f" : {value[0]}",
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
                            bot.send_message(message.chat.id,
                                         len10+" \n "+len11+ "--->\n" + str(a1) + " " + str(
                                             a2) + " " + str(a3))
                            connect.commit()
                            for value in cursor.execute(f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                bot.send_message(message.chat.id,
                                                 len9+f" : {value[0]}",
                                                 parse_mode='html')
                        if tTK:
                            if a3 and a2 == a1:
                                bot.send_message(message.chat.id,
                                             len12+" \n "+len11+" --->\n" + str(a1) + " " + str(
                                                 a2) + " " + str(a3))
                                cursor.execute(
                                    f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                connect.commit()
                                for value in cursor.execute(
                                        f"SELECT balance FROM users WHERE id = {message.from_user.id}"):
                                    bot.send_message(message.chat.id,
                                                 len9+f": {value[0]}",
                                                 parse_mode='html')
                    elif tTl == True:
                        bot.send_message(message.chat.id,
                                     len13+" \n "+len11+"  --->\n" + str(a1) + " " + str(a2) + " " + str(
                                         a3))
            else:
                        a1 = randint(1, 3)
                        print("play kazino " + str(message.from_user.id))
                        a2 = randint(1 , 3)
                        a3 = randint(1, 3)

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
                                bot.send_message(message.chat.id,str(len10)+"\n"+str(len11)+" --->\n" + str(a1) + " " + str( a2) + " " + str(a3))
                                connect.commit()

                            if tTK:
                                if a3 and a2 == a1:
                                    bot.send_message(message.chat.id,str(len12)+"\n"+str(len11)+"  --->\n" + str(a1) + " " + str(a2) + " " + str(a3))
                                    cursor.execute(
                                        f"UPDATE users SET balance = balance + 100 WHERE id = {message.from_user.id}")
                                    connect.commit()
                        elif tTl == True:
                            bot.send_message(message.chat.id,str(len13)+"\n"+str(len11)+"  --->\n" + str(a1) + " " + str(a2) + " " + str(a3))

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
                    bot.send_message(message.chat.id, len14)
                else:
                    bot.send_message(message.chat.id, len15)
            except:
                bot.send_message(message.chat.id, "reg error")

    if message.text == "/deleteme@ChatHelperByRabilint_bot":
            try:
                connect = sqlite3.connect('users.db')
                cursor = connect.cursor()
                cursor.execute(f"DELETE FROM users WHERE id = {message.from_user.id}")
                connect.commit()
                print("minus user (" + str(message.from_user.id))
                bot.send_message(message.chat.id, len16)
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
                        bot.send_message(message.chat.id, len17)
                    else:
                        bot.send_message(message.chat.id, str(answ) + len18)
                except:
                    bot.send_message(message.chat.id, len19)
            except:
                bot.send_message(message.chat.id, "when error")

    if message.text == "Rabilint":
            print("rabilint" + str(message.from_user.id))
            bot.send_message(message.chat.id, 'the best')

    if message.text == len20:
            bot.send_message(message.chat.id, len21)

    if message.text == "AZOV":
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
                                     str(len23)+f" " + str(a1) +" "+str(len28)+" "+
                                     str(len24)+f" : {value[0]} см",
                                     parse_mode='html')
            else:
                a1 = randint(-5, 10)
                d = a1
                user_id = message.from_user.id
                a = datetime.datetime.now()
                b2 = toOrdinal
                b1 = cursor.execute('SELECT timer FROM users WHERE id=:user_id',
                                    {"user_id": user_id}).fetchone()[0]
                if int(b1) < int(b2):
                    cursor.execute(f"UPDATE users SET Dick = Dick + {d} WHERE id = {message.from_user.id}")
                    b = toOrdinal
                    cursor.execute(f"UPDATE users SET timer = {b} WHERE id = {message.from_user.id}")
                    connect.commit()
                    for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                        bot.send_message(message.chat.id,
                                         str(len23) + f" " + str(a1) + " " + str(len28) + " " +
                                         str(len24) + f" : {value[0]} см",
                                         parse_mode='html')
                else:
                    bot.send_message(message.chat.id, len25)

        # //////////////////////////////////
    if message.text == "/howlong@ChatHelperByRabilint_bot":
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute(f"SELECT id FROM users WHERE id = '{message.from_user.id}'")
            data = cursor.fetchone()  # проверяем, есть ли такая запись в таблице
            if data is None:  # если такой записи нет, то:
                bot.reply_to(message, len26)
            else:
                for value in cursor.execute(f"SELECT Dick FROM users WHERE id = {message.from_user.id}"):
                    bot.send_message(message.chat.id,
                                     str(len27) + f" : {value[0]} ",
                                     parse_mode='html')

    if message.text == "/chlanUA@ChatHelperByRabilint_bot":
            cursor.execute(f"UPDATE SS SET language = {1} WHERE id = {message.chat.id}")
            connect.commit()
            bot.send_message(message.chat.id, len29)
    if message.text == "/chlanBEL@ChatHelperByRabilint_bot":
            cursor.execute(f"UPDATE SS SET language = {2} WHERE id = {message.chat.id}")
            connect.commit()
            bot.send_message(message.chat.id, len30)
    if message.text == "/chlanENG@ChatHelperByRabilint_bot":
        cursor.execute(f"UPDATE SS SET language = {0} WHERE id = {message.chat.id}")
        connect.commit()
        bot.send_message(message.chat.id, len31)


bot.polling(none_stop=True)
