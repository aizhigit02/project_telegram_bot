import telebot
from telebot import types
from information import asasas1, asasas2, asasas3, asasas4, asasas5, asasas6
from information import asasas7, asasas8, asasas9, asasas10, asasas11
from information import asasas12, asasas13, asasas14, asasas15, asasas16
from information import asasas17, asasas18, asasas19, asasas20, asasas21
from information import asasas22, asasas23, asasas24, asasas25, asasas26
from information import asasas27, asasas28, asasas29, asasas30, asasas31
from information import asasas32, asasas33, asasas34, asasas35, asasas36
from information import asasas37, asasas38, asasas39, asasas40, asasas41
from information import asasas42, asasas43, asasas44, asasas45, asasas46
from information import asasas47, asasas48, asasas49, asasas50, asasas51
from information import asasas52, asasas53, asasas54, asasas55, asasas56
from information import asasas57, asasas58, asasas59, asasas60, asasas61
from information import asasas62, asasas63, asasas64, asasas65, asasas66
from information import asasas67, asasas68, asasas69, asasas70, asasas71
from information import asasas72, asasas73, asasas74, asasas75, asasas76
from information import asasas77, asasas78, asasas79, asasas80, asasas81
from information import asasas82, asasas83, asasas84, asasas85, asasas86
from information import asasas87, asasas88, asasas89, asasas90

bot = telebot.TeleBot('1123763968:AAH_v54_D7p0E3SBFunLHFF9IAWtYLi1aWc')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Yes')
    item2 = types.KeyboardButton('No')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Hello, geek', reply_markup=markup)
    a = 'Are you here for the first time?'
    bot.send_message(message.chat.id, f'{a}')


@bot.message_handler(commands=['tutorial'])
def information(message):
    bot.send_message(message.chat.id, asasas90)


@bot.message_handler(content_types=['text'])
def reaction(message):
    if message.chat.type == 'private':
        if message.text == 'Yes':
            markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            ok = types.KeyboardButton('Continue')
            markup1.add(ok)
            a = 'This bot provides with an information about cars.'
            bot.send_message(message.chat.id, f"{a}", reply_markup=markup1)
        elif message.text == 'No':
            markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            okk = types.KeyboardButton('Continue')
            markup2.add(okk)
            a = 'Happy to see you again'
            bot.send_message(message.chat.id, f"{a}", reply_markup=markup2)
        elif message.text == 'Continue':
            markup21 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            okkk = types.KeyboardButton('Information')
            okkkk = types.KeyboardButton('Go to games')
            okkkkk = types.KeyboardButton('Go to News')
            markup21.add(okkk, okkkk, okkkkk)
            a = 'Please choose what you want'
            bot.send_message(message.chat.id, a, reply_markup=markup21)
        elif message.text == 'Go to games':
            a = 'https://bit.ly/3mUI6xD'
            b = 'You can download games here'
            bot.send_message(message.chat.id, f'{b}\n{a}')
        elif message.text == "Go to News":
            a = 'https://www.autonews.ru/'
            b = 'https://www.zr.ru/news/'
            c = 'https://avtomir.ru/'
            d = 'http://www.motorpage.ru/magazine/news/'
            e = 'https://www.kolesa.ru/news'
            f = 'Here are top-5 websites about car-world:'
            bot.send_message(message.chat.id, f'{f}\n{b}\n{c}\n{d}\n{e}\n{a}')

        elif message.text == 'Information':
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            UAZ = types.InlineKeyboardButton("UAZ", callback_data='66')
            Vo = types.InlineKeyboardButton("Volvo", callback_data='65')
            V = types.InlineKeyboardButton("Volkswagen", callback_data='64')
            Ta = types.InlineKeyboardButton("Toyota", callback_data='63')
            T = types.InlineKeyboardButton("Tesla", callback_data='62')
            Sa = types.InlineKeyboardButton("Suzuki", callback_data='61')
            Su = types.InlineKeyboardButton("Subaru", callback_data='60')
            Sk = types.InlineKeyboardButton("Skoda", callback_data='59')
            S = types.InlineKeyboardButton("SEAT", callback_data='58')
            Ro = types.InlineKeyboardButton("Rolls-Royce", callback_data='57')
            Re = types.InlineKeyboardButton("Renault", callback_data='56')
            R = types.InlineKeyboardButton("Ravon", callback_data='55')
            Por = types.InlineKeyboardButton("Porsche", callback_data='54')
            Po = types.InlineKeyboardButton("Polestar", callback_data='53')
            P = types.InlineKeyboardButton("Peugeot", callback_data='52')
            opel = types.InlineKeyboardButton("Opel", callback_data='51')
            Nissan = types.InlineKeyboardButton("Nissan", callback_data='50')
            Mit = types.InlineKeyboardButton("Mitsubishi", callback_data='49')
            zxc = "Mercedes-Benz"
            Mer = types.InlineKeyboardButton(zxc, callback_data='48')
            MCLare = types.InlineKeyboardButton("MCLaren", callback_data='47')
            Mazda = types.InlineKeyboardButton("Mazda", callback_data='46')
            Mase = types.InlineKeyboardButton("Maserati", callback_data='45')
            Lexus = types.InlineKeyboardButton("Lexus", callback_data='44')
            Lan = types.InlineKeyboardButton("Land Rover", callback_data='43')
            l = types.InlineKeyboardButton("Lamborghini", callback_data='42')
            Lada = types.InlineKeyboardButton("Lada", callback_data='41')
            KIA = types.InlineKeyboardButton("KIA", callback_data='40')
            Jeep = types.InlineKeyboardButton("Jeep", callback_data='39')
            Jaguar = types.InlineKeyboardButton("Jaguar", callback_data='38')
            JAC = types.InlineKeyboardButton("JAC", callback_data='37')
            I = types.InlineKeyboardButton("Infiniti", callback_data='36')
            Hyunda = types.InlineKeyboardButton("Hyundai", callback_data='35')
            Honda = types.InlineKeyboardButton("Honda", callback_data='34')
            Haval = types.InlineKeyboardButton("Haval", callback_data='33')
            G = types.InlineKeyboardButton("Great Wall", callback_data='32')
            GMC = types.InlineKeyboardButton("GMC", callback_data='31')
            Genesi = types.InlineKeyboardButton("Genesis", callback_data='30')
            Geely = types.InlineKeyboardButton("Geely", callback_data='29')
            Ford = types.InlineKeyboardButton("Ford", callback_data='28')
            Fisker = types.InlineKeyboardButton("Fisker", callback_data='27')
            Fiat = types.InlineKeyboardButton("Fiat", callback_data='26')
            Ferrar = types.InlineKeyboardButton("Ferrari", callback_data='25')
            FAW = types.InlineKeyboardButton("FAW", callback_data='24')
            qwe = "DS Automobiles"
            DS = types.InlineKeyboardButton(qwe, callback_data='23')
            Dodge = types.InlineKeyboardButton("Dodge", callback_data='22')
            Datsun = types.InlineKeyboardButton("Datsun", callback_data='21')
            Daewoo = types.InlineKeyboardButton("Daewoo", callback_data='20')
            Dacia = types.InlineKeyboardButton("Dacia", callback_data='19')
            Citro = types.InlineKeyboardButton("Citroen", callback_data='18')
            Chrys = types.InlineKeyboardButton("Chrysler", callback_data='17')
            Chev = types.InlineKeyboardButton("Chevrolet", callback_data='16')
            Chery = types.InlineKeyboardButton("Chery", callback_data='15')
            Chana = types.InlineKeyboardButton("Chana", callback_data='14')
            Cadil = types.InlineKeyboardButton("Cadillac", callback_data='13')
            BYD = types.InlineKeyboardButton("BYD", callback_data='12')
            Buick = types.InlineKeyboardButton("Buick", callback_data='11')
            Buga = types.InlineKeyboardButton("Bugatti", callback_data='10')
            Br = types.InlineKeyboardButton("Brilliance", callback_data='9')
            BMW = types.InlineKeyboardButton("BMW", callback_data='8')
            Bentley = types.InlineKeyboardButton("Bentley", callback_data='7')
            c = 'Automobili Pininfarina'
            a = types.InlineKeyboardButton(c, callback_data='6')
            Audi = types.InlineKeyboardButton("Audi", callback_data='5')
            As = types.InlineKeyboardButton("Aston Martin", callback_data='4')
            Apollo = types.InlineKeyboardButton("Apollo", callback_data='3')
            acura = types.InlineKeyboardButton("Acura", callback_data='1')
            Alfa = types.InlineKeyboardButton("Alfa Romeo", callback_data='2')

            markup3.add(acura, Alfa, Apollo, As, Audi, a, Bentley,
                        BMW, Br, Buga, Buick, BYD, Cadil,
                        Chana, Chery, Chev, Chrys, Citro, Dacia,
                        Daewoo, Datsun, Dodge, DS, FAW, Ferrar,
                        Fiat, Fisker, Ford, Geely, Genesi, GMC,
                        G, Haval, Honda, Hyunda, I,
                        JAC, Jaguar, Jeep, KIA, Lada, l, Lan,
                        Lexus, Mase, Mazda, MCLare, Mer,
                        Mit, Nissan, opel, P, Po, Por, R, Re,
                        Ro, S, Sk, Su, Sa, T, Ta, V, Vo, UAZ)
            asd = 'Please choose the brand of the car'
            bot.send_message(message.chat.id, asd, reply_markup=markup3)

        else:
            ert = "I do not have such kind of command. Please try another one"
            bot.send_message(message.chat.id, ert)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            pho = "https://bit.ly/2HQkR90"
            te = 'For more information: https://www.acura.com/'

            bot.send_message(call.message.chat.id, f'{pho}\n{asasas1}\n{te}')

            markup4 = types.InlineKeyboardMarkup(row_width=1)
            a = "Acura ILX 2018"
            ilx = types.InlineKeyboardButton(a, callback_data='001')
            b = "Acura RDX 2018"
            rdx = types.InlineKeyboardButton(b, callback_data='002')
            c = 'Acura TLX 2014'
            tlx = types.InlineKeyboardButton(c, callback_data='003')
            d = 'Acura RLX 2012'
            rlx = types.InlineKeyboardButton(d, callback_data='004')
            markup4.add(ilx, rdx, tlx, rlx)
            e = 'Editions:'
            bot.send_message(call.message.chat.id, e, reply_markup=markup4)
        elif call.data == '2':
            te = 'For more information: https://www.alfaromeo.com/'
            pho = 'https://bit.ly/3eh3j1t'
            bot.send_message(call.message.chat.id, f'{pho}\n{asasas2}\n{te}')
            markup4 = types.InlineKeyboardMarkup(row_width=1)
            q = "Alfa Romeo Giulia 2016"
            a = types.InlineKeyboardButton(q, callback_data='005')
            w = "Alfa Romeo MiTo 2016"
            b = types.InlineKeyboardButton(w, callback_data='006')
            e = 'Alfa Romeo Stelvio 2017'
            c = types.InlineKeyboardButton(e, callback_data='007')
            r = 'Alfa Romeo Giulietta 2016'
            d = types.InlineKeyboardButton(r, callback_data='008')
            markup4.add(a, b, c, d,)
            t = 'Editions:'
            bot.send_message(call.message.chat.id, t, reply_markup=markup4)
        elif call.data == '3':
            te = 'For more information : https://apollo-automobil.com/'
            pho = 'https://bit.ly/34LzEKW'
            bot.send_message(call.message.chat.id, f'{pho}\n{asasas3}\n{te}')
            zxzx = types.InlineKeyboardMarkup(row_width=1)
            q = "De Tomaso P72"
            d = types.InlineKeyboardButton(q, callback_data='012')
            w = "Apollo Intensa Emozione"
            c = types.InlineKeyboardButton(w, callback_data='011')
            e = "Apollo Arrow"
            b = types.InlineKeyboardButton(e, callback_data='010')
            r = "Gumpert Apollo"
            a = types.InlineKeyboardButton(r, callback_data='009')
            zxzx.add(a, b, c, d,)
            t = 'Editions:'
            bot.send_message(call.message.chat.id, t, reply_markup=zxzx)
        elif call.data == '009':

            te = 'For more information: https://apollo-automobil.com/ '
            ph = 'https://bit.ly/381dypt'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas4}\n{te}')
        elif call.data == '010':
            te = 'For more information: https://apollo-automobil.com/ '
            ph = 'https://bit.ly/3234jS6'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas5}\n{te}')
        elif call.data == '011':
            te = 'For more information: https://apollo-automobil.com/ '
            ph = 'https://bit.ly/2TJP3ou'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas6}\n{te}')
        elif call.data == '012':
            te = 'For more information: https://apollo-automobil.com/ '
            ph = 'https://bit.ly/2HJSdqc'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas7}\n{te}')

        elif call.data == '4':

            te = 'For more information: https://www.astonmartin.com/en/'
            ph = 'https://bit.ly/2TE18vk'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas8}\n{te}')
            zxzx = types.InlineKeyboardMarkup(row_width=1)
            ad = "Aston Martin DBX 2019"
            d = types.InlineKeyboardButton(ad, callback_data='013')
            af = "Aston Martin DBS Superleggera 2018"
            c = types.InlineKeyboardButton(af, callback_data='014')
            ag = "Aston Martin Vanquish 2012"
            a = types.InlineKeyboardButton(ag, callback_data='015')
            ah = "Aston Martin DB11 2016"
            b = types.InlineKeyboardButton(ah, callback_data='016')
            aj = "Aston Martin Vantage 2018"
            z = types.InlineKeyboardButton(aj, callback_data='017')
            ax = "Aston Martin DB11 Volante 2018"
            x = types.InlineKeyboardButton(ax, callback_data='018')
            ac = "Aston Martin Rapide S 2013"
            v = types.InlineKeyboardButton(ac, callback_data='019')

            zxzx.add(a, b, c, d, z, x, v,)
            m = 'Editions:'
            bot.send_message(call.message.chat.id, m, reply_markup=zxzx)
        elif call.data == '013':
            te = 'For more information: https://www.astonmartin.com'
            ph = 'https://bit.ly/2HM0DgK'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas9}\n{te}')
        elif call.data == '014':

            te = 'For more information: https://www.astonmartin.com/'
            ph = 'https://bit.ly/2HS6r8k'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas10}\n{te}')
        elif call.data == '015':
            te = 'For more information: https://www.astonmartin.com'
            ph = 'https://bit.ly/3kQ2zmv'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas11}\n{te}')
        elif call.data == '016':
            te = 'For more information: https://www.astonmartin.com/'
            ph = 'https://bit.ly/3kLEQ77'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas12}\n{te}')
        elif call.data == '017':
            te = 'For more information: https://www.astonmartin.com/'
            ph = 'https://bit.ly/3oKxC5s'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas13}\n{te}')
        elif call.data == '018':
            te = 'For more information: https://www.astonmartin.com'
            ph = 'https://bit.ly/2Gfg9Rg'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas14}\n{te}')
        elif call.data == '019':
            te = 'For more information: https://www.astonmartin.com/'
            ph = 'https://bit.ly/3kO1bke'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas15}\n{te}')
        elif call.data == '5':
            te = 'For more information: https://www.audi.com/en.html'
            ph = 'https://bit.ly/35WMTb4'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas16}\n{te}')

            zxzx = types.InlineKeyboardMarkup(row_width=1)
            z = types.InlineKeyboardButton("Audi S4 2019", callback_data='99')
            ad = "Audi R8 Coupe 2019"
            x = types.InlineKeyboardButton(ad, callback_data='022')
            af = "Audi Q8 2018"
            v = types.InlineKeyboardButton(af, callback_data='021')
            ag = "Audi A3 2016"
            n = types.InlineKeyboardButton(ag, callback_data='020')
            zxzx.add(z, x, v, n)
            zx = 'Editions:'
            bot.send_message(call.message.chat.id, zx, reply_markup=zxzx)
        elif call.data == '020':
            te = 'For more information: https://www.audi.com/'
            ph = 'https://bit.ly/35UUpmy'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas17}\n{te}')
        elif call.data == '021':
            te = 'For more information: https://www.audi.com/ '
            ph = 'https://bit.ly/2JkZYmB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas18}\n{te}')
        elif call.data == '022':
            te = 'For more information: https://www.audi.com/ '
            ph = 'https://bit.ly/3mJspcC'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas19}\n{te}')
        elif call.data == '99':

            te = 'For more information: https://www.audi.com/ '
            ph = 'https://bit.ly/3egh1Sh'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas20}\n{te}')

        elif call.data == '6':
            te = 'For more information: https://automobili-pininfarina.com/'
            ph = 'https://bit.ly/35TAkNB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas21}\n{te}')
        elif call.data == '7':
            te = 'For more information: https://www.bentleymotors.com/en.html'
            ph = 'https://bit.ly/3jKDGrd'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas22}\n{te}')
        elif call.data == '8':
            te = 'For more information:https://www.bmw.com/en/index.html'
            ph = 'https://bit.ly/3oMgtbB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas23}\n{te}')
        elif call.data == '9':
            te = 'For more information: http://www.brillianceauto.com/'
            ph = 'https://bit.ly/35SNGcO'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas24}\n{te}')
        elif call.data == '10':
            te = 'For more information: https://www.bugatti.com/ '
            ph = 'https://bit.ly/34HXarV'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas25}\n{te}')
        elif call.data == '11':
            te = 'For more information: https://www.buick.com/ '
            ph = 'https://bit.ly/2GfCs9D'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas26}\n{te}')
        elif call.data == '12':
            te = 'For more information: https://www.byd.com/en/index.html '
            ph = 'https://bit.ly/35X7Q5I'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas27}\n{te}')
        elif call.data == '13':
            te = 'For more information: https://www.cadillac.com/'
            ph = 'https://bit.ly/35NH1AQ'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas28}\n{te}')
        elif call.data == '14':
            te = 'For more information: '
            ph = 'https://bit.ly/37Yctz1'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas29}\n{te}')
        elif call.data == '15':
            te = 'For more information: https://www.cheryinternational.com/'
            ph = 'https://bit.ly/37ZT7tk'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas30}\n{te}')
        elif call.data == '16':
            te = 'For more information: https://www.chevrolet.com/ '
            ph = 'https://bit.ly/2THMJhK'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas31}\n{te}')
        elif call.data == '17':
            te = 'For more information: https://www.chrysler.com/ '
            ph = 'https://bit.ly/3kKK5nt'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas32}\n{te}')
        elif call.data == '18':
            te = 'For more information: https://www.citroen.com/en/'
            ph = 'https://bit.ly/34Kkndm'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas33}\n{te}')
        elif call.data == '19':
            text = 'For more information: https://www.dacia.co.uk/'
            ph = 'https://bit.ly/3oIzcVB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas34}\n{text}')
        elif call.data == '20':
            te = 'For more information: https://daewoo.com.pk/'
            ph = 'https://bit.ly/2TIAlhH'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas35}\n{te}')
        elif call.data == '21':
            te = 'For more information: https://www.datsun.com/ '
            ph = 'https://bit.ly/3oLotcU'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas36}\n{te}')
        elif call.data == '22':
            te = 'For more information: https://www.dodge.com/ '
            ph = 'https://bit.ly/2GfByK9'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas37}\n{te}')
        elif call.data == '23':
            te = 'For more information: https://www.dsautomobiles.co.uk/ '
            ph = 'https://bit.ly/3jNME6O'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas38}\n{te}')
        elif call.data == '24':
            te = 'For more information: www.faw.com '
            ph = 'https://bit.ly/3kLKVjT'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas39}\n{te}')
        elif call.data == '25':
            te = 'For more information: https://www.ferrari.com/en-EN '
            ph = 'https://bit.ly/3kMr57Y'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas40}\n{te}')
        elif call.data == '26':
            te = 'For more information: https://www.fiat.com/ '
            ph = 'https://bit.ly/3eeDRtu'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas41}\n{te}')
        elif call.data == '27':
            te = 'For more information: https://www.fiskerinc.com/ '
            ph = 'https://bit.ly/2GjDW2G'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas42}\n{te}')
        elif call.data == '28':
            te = 'For more information: https://www.ford.com/ '
            ph = 'https://bit.ly/34LkSn6'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas43}\n{te}')
        elif call.data == '29':
            te = 'For more information: http://global.geely.com/ '
            ph = 'https://bit.ly/2Jpy0X2'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas44}\n{te}')
        elif call.data == '30':
            te = 'For more information: https://www.genesis.com/us/en '
            ph = 'https://bit.ly/34GooPQ'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas45}\n{te}')
        elif call.data == '31':
            te = 'For more information: https://www.gmc.com/ '
            ph = 'https://bit.ly/2TIizuO'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas46}\n{te}')
        elif call.data == '32':
            te = 'For more information: https://www.gwm-global.com/ '
            ph = 'https://bit.ly/3jGdCgB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas47}\n{te}')
        elif call.data == '33':
            te = 'For more information: https://www.haval-global.com/ '
            ph = 'https://bit.ly/3ebQRQC'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas48}\n{te}')
        elif call.data == '34':
            te = 'For more information: https://www.honda.com/ '
            ph = 'https://bit.ly/3kOgNEk'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas49}\n{te}')
        elif call.data == '35':
            te = 'For more information: https://www.hyundai.com/worldwide/en '
            ph = 'https://bit.ly/2JsiAkZ'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas50}\n{te}')
        elif call.data == '36':
            te = 'For more information: https://www.infinitiusa.com/ '
            ph = 'https://bit.ly/322jQBH'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas51}\n{te}')
        elif call.data == '37':
            te = 'For more information: https://jacen.jac.com.cn/ '
            ph = 'https://bit.ly/2JpUZkP'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas52}\n{te}')
        elif call.data == '38':
            te = 'For more information: https://www.jaguar.com/ '
            ph = 'https://bit.ly/2HKZBB7'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas53}\n{te}')
        elif call.data == '39':
            te = 'For more information: https://www.jeep.com/ '
            ph = 'https://bit.ly/3kJFeD6'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas54}\n{te}')
        elif call.data == '40':
            te = 'For more information: https://www.kia.com/us/en '
            ph = 'https://bit.ly/322xoNr'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas55}\n{te}')
        elif call.data == '41':
            te = 'For more information: https://www.lada.ru/en/ '
            ph = 'https://bit.ly/35OqLzv'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas56}\n{te}')
        elif call.data == '42':
            te = 'For more information: https://www.lamborghini.com/en-en '
            ph = 'https://bit.ly/35V8LTW'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas57}\n{te}')
        elif call.data == '43':
            te = 'For more information: https://bit.ly/3kXtEnG '
            ph = 'https://bit.ly/3kXtEnG'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas58}\n{te}')
        elif call.data == '44':
            te = 'For more information: https://www.lexus.com/ '
            ph = 'https://bit.ly/2GiTX92'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas59}\n{te}')
        elif call.data == '45':
            te = 'For more information: https://www.maserati.com/ '
            ph = 'https://bit.ly/35Xs67g'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas60}\n{te}')
        elif call.data == '46':
            te = 'For more information: https://www.mazda.com/ '
            ph = 'https://bit.ly/3oIxyDt'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas61}\n{te}')
        elif call.data == '47':
            te = 'For more information: https://www.mclaren.com/ '
            ph = 'https://bit.ly/3kLp0tb'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas62}\n{te}')
        elif call.data == '48':
            te = 'For more information: https://www.mercedes-benz.com/en/  '
            ph = 'https://bit.ly/34Lt07d'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas63}\n{te}')
        elif call.data == '49':
            te = 'For more information: https://www.mitsubishicars.com/ '
            ph = 'https://bit.ly/3edWWfr'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas64}\n{te}')
        elif call.data == '50':
            te = 'For more information: https://www.nissanusa.com/ '
            ph = 'https://bit.ly/3kKZcgA'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas65}\n{te}')
        elif call.data == '51':
            te = 'For more information: https://www.opel.com/ '
            ph = 'https://bit.ly/3jJulzB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas66}\n{te}')
        elif call.data == '52':
            te = 'For more information: https://www.peugeot.co.uk/ '
            ph = 'https://bit.ly/35LhAj2'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas67}\n{te}')
        elif call.data == '53':
            te = 'For more information: https://www.polestar.com/ '
            ph = 'https://bit.ly/3jSN3oQ'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas68}\n{te}')
        elif call.data == '54':
            te = 'For more infoamtion: https://www.porsche.com/ '
            ph = 'https://bit.ly/323NVRf'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas69}\n{te}')
        elif call.data == '55':
            te = 'For more information: https://www.ravon.az/ '
            ph = 'https://bit.ly/3efMEvf'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas70}\n{te}')
        elif call.data == '56':
            te = 'For more information: https://www.renault.co.uk/ '
            ph = 'https://bit.ly/3mHG6bW'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas71}\n{te}')
        elif call.data == '57':
            te = 'For more information: https://bit.ly/3egRs3B '
            ph = 'https://bit.ly/2Jpsjsa'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas72}\n{te}')
        elif call.data == '58':
            te = 'For more information: https://www.seat.com/ '
            ph = 'https://bit.ly/3mBcIUs'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas73}\n{te}')
        elif call.data == '59':
            te = 'For more information: https://www.skoda-auto.com/ '
            ph = 'https://bit.ly/34PZNIB'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas74}\n{te}')
        elif call.data == '60':
            te = 'For more information: https://www.subaru.com/ '
            ph = 'https://bit.ly/2HRKZQq'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas75}\n{te}')
        elif call.data == '61':
            te = 'For more information: https://www.globalsuzuki.com/ '
            ph = 'https://bit.ly/35WkUIx'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas76}\n{te}')
        elif call.data == '62':
            te = 'For more information: https://www.tesla.com/ '
            ph = 'https://bit.ly/2TICZUw'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas77}\n{te}')
        elif call.data == '63':
            te = 'For more information: https://www.toyota.com/ '
            ph = 'https://bit.ly/35NBGcC'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas78}\n{te}')
        elif call.data == '64':
            te = 'For more information: https://www.vw.com/ '
            ph = 'https://bit.ly/3jIcZ6t'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas79}\n{te}')
        elif call.data == '65':
            te = 'For more information: https://www.volvo.com/home.html '
            ph = 'https://bit.ly/381ncJ4'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas80}\n{te}')
        elif call.data == '66':
            te = 'For more information: https://uaz.global/ '
            ph = 'https://bit.ly/37Yd9Ev'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas81}\n{te}')

        elif call.data == '001':
            te = 'For more information: https://www.acura.com/'
            ph = 'https://bit.ly/3kKRVxq'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas82}\n{te}')
        elif call.data == '002':
            te = 'For more information: https://www.acura.com/'
            ph = 'https://bit.ly/3mCpmTl'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas83}\n{te}')
        elif call.data == '003':
            te = 'For more information: https://www.acura.com/'
            ph = 'https://bit.ly/3mCpLoP'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas84}\n{te}')
        elif call.data == '004':
            te = 'For more information: https://www.acura.com/'
            ph = 'https://bit.ly/3kNW4k7'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas85}\n{te}')
        elif call.data == '005':
            te = 'For more information: https://www.alfaromeo.com/'
            ph = 'https://bit.ly/35NFPgE'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas86}\n{te}')
        elif call.data == '006':
            te = 'For more information: https://www.alfaromeo.com/'
            ph = 'https://bit.ly/3kKbdDd'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas87}\n{te}')
        elif call.data == '007':
            te = 'For more information: https://www.alfaromeo.com/'
            ph = 'https://bit.ly/34JrfHJ'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas88}\n{te}')
        elif call.data == '008':
            te = 'For more information: https://www.alfaromeo.com/'
            ph = 'https://bit.ly/3jEcz0M'
            bot.send_message(call.message.chat.id, f'{ph}\n{asasas89}\n{te}')

bot.polling(none_stop=True)
