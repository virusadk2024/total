import requests
from bs4 import BeautifulSoup
import schedule
from telegram import send_telegram
from telegramchannel import send_channel
from expressvpn import connect
import telebot

# import schedule
# from format_message import format_pred
# bot = telebot.TeleBot('5529829120:AAGsUqlqofBzekr8wSIj2UZL15YOuvQTtRo')

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, text="Выполняю поиск")
#     main()
    
    
def main():
    # message1 = result()
    
    connect ()
    cookies = {
        'cud': 'rBMAD2YCXpW9EQt3B/I3Ag==',
        '_ga': 'GA1.2.698336348.1711431335',
        '_ym_uid': '1711431339727122409',
        '_ym_d': '1711431339',
        'xq_icm': '13000',
        'acceptCookies': 'true',
        'lang': '0',
        '_ga_Y9VSRWL1PZ': 'GS1.2.1711457699.5.1.1711457810.0.0.0',
        '_gid': 'GA1.2.959385001.1712043743',
        '_ym_isad': '2',
        '_ga_NBF6PN1P8S': 'GS1.2.1712043760.4.1.1712045541.0.0.0',
    }

    headers = {
        'authority': 'd.betcity.by',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cud=rBMAD2YCXpW9EQt3B/I3Ag==; _ga=GA1.2.698336348.1711431335; _ym_uid=1711431339727122409; _ym_d=1711431339; xq_icm=13000; acceptCookies=true; lang=0; _ga_Y9VSRWL1PZ=GS1.2.1711457699.5.1.1711457810.0.0.0; _gid=GA1.2.959385001.1712043743; _ym_isad=2; _ga_NBF6PN1P8S=GS1.2.1712043760.4.1.1712045541.0.0.0',
        'origin': 'https://betcity.by',
        'referer': 'https://betcity.by/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Opera";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
    }



    params = {
    'rev': '6',
    'ver': '468',
    'csn': 'lsmif5',
    'id_sp': '46'
    }

    response = requests.get('https://d.betcity.by/api/v1/bets/line', params=params, cookies=cookies, headers=headers, verify=False)

    resultline = response.json()
    # print(resultline)
    tr = 46
    tr1 = str(tr)
    mass_game = []
    list = []
    with open('send.txt','r') as file:
            
        for item in file.readlines():
            line = item.strip()
                # print(line)
            list.append(line)
        file.close()     
                       
    for vid in resultline['reply']['sports'][tr1]['chmps']:
        # liga = resultline['reply']['sports'][tr1]['chmps'][vid]['name_ch']
        # print(vid)
        evts = resultline['reply']['sports'][tr1]['chmps'][vid]['evts']
        # print(evts)
        for ev in evts:
            try:    
                stat = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['stat_link']
                # print(stat)
                ext =  resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['sc_inter']
                # print(ext)
            except:
                pass
            # print(stat)

            url_stat = f'https://betcity.by/ru/mstat/{stat}'
            # print(url_stat)
#             if ext == '0:0':
    
        
        

            cookies = {
                'cud': 'rBMAD2YCXpW9EQt3B/I3Ag==',
                'close-page-text': '1',
                '_ym_uid': '1711431339727122409',
                '_ym_d': '1711431339',
                'xq_icm': '13000',
                'acceptCookies': 'true',
                'lang': '0',
                '_ga_Y9VSRWL1PZ': 'GS1.2.1711457699.5.1.1711457810.0.0.0',
                '_gid': 'GA1.2.959385001.1712043743',
                '_ym_isad': '2',
                'dev': '3b25649755ac9e0bfbb7b95e50a57c44',
                '_gat_gtag_UA_97174776_3': '1',
                '_ga_NBF6PN1P8S': 'GS1.1.1712043760.4.1.1712046207.0.0.0',
                '_ga': 'GA1.1.698336348.1711431335',
            }

            headers = {
                'authority': 'betcity.by',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                # 'cookie': 'cud=rBMAD2YCXpW9EQt3B/I3Ag==; close-page-text=1; _ym_uid=1711431339727122409; _ym_d=1711431339; xq_icm=13000; acceptCookies=true; lang=0; _ga_Y9VSRWL1PZ=GS1.2.1711457699.5.1.1711457810.0.0.0; _gid=GA1.2.959385001.1712043743; _ym_isad=2; dev=3b25649755ac9e0bfbb7b95e50a57c44; _gat_gtag_UA_97174776_3=1; _ga_NBF6PN1P8S=GS1.1.1712043760.4.1.1712046207.0.0.0; _ga=GA1.1.698336348.1711431335',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Opera";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
            }

            response = requests.get(url_stat, cookies=cookies, headers=headers).text
            soup = BeautifulSoup(response, 'lxml')
            # print(soup)
            ov_mass = parse(soup)
            # print(ov_mass)
            kol_ov = kol_ochnyh_vstrech(ov_mass)
            

            
            if kol_ov == 10:
                mass_summ_ov = []
                for game in ov_mass:
                    mass_summ_game = []
                    try:
                        set1 = game.split(' ')[0]
                        set11 = set1.split(':')[0]
                        set12 = set1.split(':')[1]
                        summ = int(set11) + int(set12)
                        mass_summ_game.append(summ)
                    except:
                        pass
                    try:
                        set2 = game.split(' ')[1]
                        set21 = set2.split(':')[0]
                        set22 = set2.split(':')[1]
                        summ = int(set21) + int(set22)
                        mass_summ_game.append(summ)
                    except:
                        pass
                    try:
                        set3 = game.split(' ')[2]
                        set31 = set3.split(':')[0]
                        set32 = set3.split(':')[1]
                        summ = int(set31) + int(set32)
                        mass_summ_game.append(summ)
                    except:
                        pass
                    try:
                        set4 = game.split(' ')[3]
                        set41 = set4.split(':')[0]
                        set42 = set4.split(':')[1]
                        summ = int(set41) + int(set42)
                        mass_summ_game.append(summ)
                    except:
                        pass
                    try:
                        set5 = game.split(' ')[4]
                        set51 = set5.split(':')[0]
                        set52 = set5.split(':')[1]
                        summ = int(set51) + int(set52)
                        mass_summ_game.append(summ)
                    except:
                        pass
                
                    mass_summ_ov.append(mass_summ_game)
                
                bolshe = 0
                for gam in mass_summ_ov:
                    for g in gam:
                        if int(g) > 19:
                            bolshe += 1
                            break
                menshe = 0
                for gam in mass_summ_ov:
                    for g in gam:
                        if int(g) <= 17:
                            menshe += 1
                            break
                



                
                if (int(bolshe) == 10) or (int(menshe) == 10):
                    

#                 lv_mass = get_last_vstrechi(soup)
#                 # print(lv_mass)
#                 kol_lv = kol_ochnyh_vstrech(lv_mass)
                
#                 # b,m = kol_set_18_5_bolshe(ov_mass)
#                 # blv,mlv = kol_set_18_5_bolshe(lv_mass)
#                 # bolshe = blv + b
#                 # menshe = mlv + m
#                 # kol = kol_lv + kol_ov
#                 # bk = bolshe / kol
#                 # mk = menshe / kol
#                 # raz = abs (bk - mk)
#                 # ver = raz * 100
#                 # razb = abs(bolshe - menshe)
#                 # summ = bolshe + menshe
#                 # schet = razb / kol * summ * (ver / 100)
#                 # pr = summ / kol
#                 # print('Партии на игры',pr)
#                 # pro = 100 / pr
#                 # deli = schet / pro
#                 # if razb < 5:
#                 #     pass
#                 # else:
                    
#                 #     itog1 = pr / razb
#                 #     print('Партии на игры на разбежку',itog1)
#                 #     itog = itog1 * deli
#                 #     prohod = (1 - itog) * 100
#                 #     print(bolshe, menshe)
                
                    liga = resultline['reply']['sports'][tr1]['chmps'][vid]['name_ch']
                    print(liga)
                    
                    date_ev_str = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['date_ev_str']
                    print(date_ev_str)    
                    
                    name_ht = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_ht']
                    print(name_ht)        
                    
                    name_at = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_at']
                    print(name_at)    
                    #     korr = 0
                    
                    id_ev = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['id_ev']
                    print(id_ev)    
                    print(ov_mass)
                    print(kol_ov)
                    print(mass_summ_ov)
                    print(bolshe,menshe)
                    print('------------------------------------------------------------------')

#                 if g == 10:
                    

# #                 lv_mass = get_last_vstrechi(soup)
# #                 # print(lv_mass)
# #                 kol_lv = kol_ochnyh_vstrech(lv_mass)
                
# #                 # b,m = kol_set_18_5_bolshe(ov_mass)
# #                 # blv,mlv = kol_set_18_5_bolshe(lv_mass)
# #                 # bolshe = blv + b
# #                 # menshe = mlv + m
# #                 # kol = kol_lv + kol_ov
# #                 # bk = bolshe / kol
# #                 # mk = menshe / kol
# #                 # raz = abs (bk - mk)
# #                 # ver = raz * 100
# #                 # razb = abs(bolshe - menshe)
# #                 # summ = bolshe + menshe
# #                 # schet = razb / kol * summ * (ver / 100)
# #                 # pr = summ / kol
# #                 # print('Партии на игры',pr)
# #                 # pro = 100 / pr
# #                 # deli = schet / pro
# #                 # if razb < 5:
# #                 #     pass
# #                 # else:
                    
# #                 #     itog1 = pr / razb
# #                 #     print('Партии на игры на разбежку',itog1)
# #                 #     itog = itog1 * deli
# #                 #     prohod = (1 - itog) * 100
# #                 #     print(bolshe, menshe)
                
#                     liga = resultline['reply']['sports'][tr1]['chmps'][vid]['name_ch']
#                     print(liga)
                    
#                     date_ev_str = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['date_ev_str']
#                     print(date_ev_str)    
                    
#                     name_ht = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_ht']
#                     print(name_ht)        
                    
#                     name_at = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_at']
#                     print(name_at)    
#                     #     korr = 0
                    
#                     id_ev = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['id_ev']
#                     print(id_ev)    
#                     print(ov_mass)
#                     print(kol_ov)
#                     print('Подходит для повтора:',g)
#                     print('------------------------------------------------------------------')
                
#                 p1,p2 = get_ochnye_vstrechi_pob(soup,resultline,id_ev,name_ht,name_at)
#                 # print('Очные встречи:',p1,p2)
#                 lp1,lp2 = get_kol_pob_igr_last_vstrechi(soup)
#                 # print('Личные встречи:',lp1,lp2)
#                 if (kol_lv == 10) and (kol_ov == 10):
#                     if ((abs(lp1 - lp2) >= 2) and (abs(p1-p2) >= 3)) or ((lp1 == lp2) and (p1 ==p2)):
#                         print(date_ev_str)
#                         print(liga)
#                         print(name_ht,' - ',name_at)
#                         print('Количество личных встреч:',kol_lv)
#                         print('Победы личных встреч:',lp1,' - ',lp2)
#                         print('Количество очных встреч:',kol_ov)
#                         print('Победы очных встреч:',p1,' - ',p2)
#                         list = []
                    with open('send.txt','r') as file:
                            
                        for item in file.readlines():
                            line = item.strip()
                                # print(line)
                            list.append(line)
                        file.close()
            

                        if str(id_ev) in list:
                            print('Событие уже отправлено')
                            
                        else:    
                        
                            
                            fdate = f'\U0001F4C6 {date_ev_str} \n'
                            fliga = f'\U0001F3D3 {liga}\n' 
                            fteams = f'\U0001F9D1 {name_ht} - {name_at} \n' 
                            \
                            fkolov = f'Очные встречи:{kol_ov} \n'
                            fbolshe = f'ТБ 19.5:{bolshe} \n'
                            fmenshe = f'ТМ 17.5:{menshe} \n'
            
            
                            mess = fdate + fliga + fteams  + fkolov + fbolshe + fmenshe
                            with open('send.txt','a') as file:
                                file.write(f'\n{id_ev}')            
                                file.close()
                            print('Событие записано в db.txt')
                            send_telegram(mess)
                            send_channel(mess)
#                 #             messchannel = fid_ev + med + fdate + fliga + fteams + frazb + fprob + fprog + fstavka + fzahod + fprob + fprov + fprorazb + fitog + fprohod + fkorrver
#                 #         except:
#                 #             pass
#                 #         # message = message + mess  
#                 #         # bot.send_message(message.chat.id, text=mess,parse_mode="HTML")    
#                 #         part = deli * itog
#                 #         fpart = f'Уточнение партии: {part}\n'
#                 #         fstavkainv = ''
#                 #         # if korrver < 10 and prorazb < 5:
#                 #         #     finv = f'\U0000267B Инверсия ставки \n'
#                 #         if fstavka == 'ТМ 18.5\n':
#                 #             fstavkainv = f'Инв. ставка : ТБ 18.5\n'
#                 #         if fstavka == 'ТБ 18.5\n':
#                 #             fstavkainv = f'Инв. ставка : ТМ 18.5\n'
#                 #         #     med = f'\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\n'
#                 #         messchannelinv = mess + fpart + fstavkainv
#                 #         invprov = f'Инвертировано ранее\n'
#                 #         if utoch <= 1 or utoch > 5:
#                 #             fg = 1
#                 #             utochpart = f'Партия макс. вер.: 1 ({utoch})\n'
#                 #         if 2 >= utoch > 1:
#                 #             fg = 2
#                 #             utochpart = f'Партия макс. вер.: 2 ({utoch})\n'
#                 #         if 3 >= utoch > 2:
#                 #             fg = 3
#                 #             utochpart = f'Партия макс. вер.: 3 ({utoch})\n'
#                 #         if 4 >= utoch > 3:
#                 #             fg = 4
#                 #             utochpart = f'Партия макс. вер.: 4 ({utoch})\n'
#                 #         if 5 >= utoch > 4:
#                 #             fg = 5
#                 #             utochpart = f'Партия макс. вер.: 5 ({utoch})\n'
#                 #         start = ver / korrver *(prohod / 100) * part * itog
#                 #         fstart = f'Стартуем с {start} партии\n'
#                 #         uver = start * part * fg
#                 #         fuver = f'Стабильность: {uver}'
#                 #         final = ver / prohod * itog / deli
#                 #         ffinal =f'Точность:{final}'
#                 #         mess = mess + invprov + utochpart + fstart + fuver + ffinal
#                 #         send_telegram(mess)                       
#                 #         # bot.send_message(message.chat.id, text=mess)
#                 #         if ver > 60:
                            
#                 #             if (kol > 5) and (razb > 5) and (summ > 50) and (prorazb > 5) and (itog < 0.5):
#                 #                 if prorazb < schet:
#                 #                     part = deli * itog
#                 #                     fpart = f'Уточнение партии: {part}\n'
#                 #                     fstavkainv = ''
#                 #                     # if korrver < 10 and prorazb < 5:
#                 #                     #     finv = f'\U0000267B Инверсия ставки \n'
#                 #                     if fstavka == 'ТМ 18.5\n':
#                 #                         fstavkainv = f'Инв. ставка : ТБ 18.5\n'
#                 #                     if fstavka == 'ТБ 18.5\n':
#                 #                         fstavkainv = f'Инв. ставка : ТМ 18.5\n'
#                 #                     #     med = f'\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\n'
#                 #                     invprov = f'Инвертировано по дополнительной проверке\n'
#                 #                     if utoch <= 1 or utoch > 5:
#                 #                         fg = 1
#                 #                         utochpart = f'Партия макс. вер.: 1 ({utoch})\n'
#                 #                     if 2 >= utoch > 1:
#                 #                         fg = 2
#                 #                         utochpart = f'Партия макс. вер.: 2 ({utoch})\n'
#                 #                     if 3 >= utoch > 2:
#                 #                         fg = 3
#                 #                         utochpart = f'Партия макс. вер.: 3 ({utoch})\n'
#                 #                     if 4 >= utoch > 3:
#                 #                         fg = 4
#                 #                         utochpart = f'Партия макс. вер.: 4 ({utoch})\n'
#                 #                     if 5 >= utoch > 4:
#                 #                         fg = 5
#                 #                         utochpart = f'Партия макс. вер.: 5 ({utoch})\n'
#                 #                     start = ver / korrver * (prohod / 100) * part * itog
#                 #                     fstart = f'Стартуем с {start} партии\n'
#                 #                     uver = start * part * fg
#                 #                     fuver = f'Стабильность: {uver}'
#                 #                     final = ver / prohod * itog / deli
#                 #                     ffinal =f'Точность:{final}'
#                 #                     messchannelinv = mess + fpart + fstavkainv + invprov + utochpart + fstart + fuver + ffinal
#                 #                     with open('send.txt','a') as file:
#                 #                         file.write(f'\n{id_ev}')            
#                 #                         file.close()
#                 #                         print('Событие записано в db.txt') 
#                 #                     send_channel(messchannelinv)
                                   
                                    
                                   
#                 #                 else:
#                 #                     invprov = f'Инвертирование не требуется\n'
#                 #                     if utoch <= 1 or utoch > 5:
#                 #                         utochpart = f'Партия макс. вер.: 1 ({utoch})\n'
#                 #                         fg = 1
#                 #                     if 2 >= utoch > 1:
#                 #                         fg = 2
#                 #                         utochpart = f'Партия макс. вер.: 2 ({utoch})\n'
#                 #                     if 3 >= utoch > 2:
#                 #                         fg = 3
#                 #                         utochpart = f'Партия макс. вер.: 3 ({utoch})\n'
#                 #                     if 4 >= utoch > 3:
#                 #                         fg = 4
#                 #                         utochpart = f'Партия макс. вер.: 4 ({utoch})\n'
#                 #                     if 5 >= utoch > 4:
#                 #                         fg = 5
#                 #                         utochpart = f'Партия макс. вер.: 5 ({utoch})\n'
#                 #                     start = ver / korrver * (prohod / 100) * part * itog
#                 #                     fstart = f'Стартуем с {start} партии\n'
#                 #                     uver = start * part * fg
#                 #                     fuver = f'Стабильность: {uver}'
#                 #                     final = ver / prohod * itog / deli
#                 #                     ffinal =f'Точность:{final}'
#                 #                     mess1 = mess + invprov + utochpart + fstart + fuver + ffinal
#                 #                     with open('send.txt','a') as file:
#                 #                         file.write(f'\n{id_ev}')            
#                 #                         file.close()
#                 #                         print('Событие записано в db.txt')
#                 #                     send_channel(mess1)
                                    
                            
#                 #             else:
#                 #                 part = deli * itog
#                 #                 fpart = f'Уточнение партии: {part}\n'
#                 #                 fstavkainv = ''
#                 #                 # if korrver < 10 and prorazb < 5:
#                 #                 #     finv = f'\U0000267B Инверсия ставки \n'
#                 #                 if fstavka == 'ТМ 18.5\n':
#                 #                     fstavkainv = f'Инв. ставка : ТБ 18.5\n'
#                 #                 if fstavka == 'ТБ 18.5\n':
#                 #                     fstavkainv = f'Инв. ставка : ТМ 18.5\n'
#                 #                 #     med = f'\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\U0001F949\n'
#                 #                 messchannelinv = mess + fpart + fstavkainv
#                 #                 invprov = f'Инвертировано ранее\n'
#                 #                 if utoch <= 1 or utoch > 5:
#                 #                     fg = 1
#                 #                     utochpart = f'Партия макс. вер.: 1 ({utoch})\n'
#                 #                 if 2 >= utoch > 1:
#                 #                     fg = 2
#                 #                     utochpart = f'Партия макс. вер.: 2 ({utoch})\n'
#                 #                 if 3 >= utoch > 2:
#                 #                     fg = 3
#                 #                     utochpart = f'Партия макс. вер.: 3 ({utoch})\n'
#                 #                 if 4 >= utoch > 3:
#                 #                     fg = 4
#                 #                     utochpart = f'Партия макс. вер.: 4 ({utoch})\n'
#                 #                 if 5 >= utoch > 4:
#                 #                     fg = 5
#                 #                     utochpart = f'Партия макс. вер.: 5 ({utoch})\n'
#                 #                 start = ver / korrver *(prohod / 100) * part * itog
#                 #                 fstart = f'Стартуем с {start} партии\n'
#                 #                 uver = start * part * fg
#                 #                 fuver = f'Стабильность: {uver}'
#                 #                 final = ver / prohod * itog / deli
#                 #                 ffinal =f'Точность:{final}'
#                 #                 mess2 = messchannelinv + invprov + utochpart + fstart + fuver + ffinal
#                 # with open('send.txt','a') as file:
#                 #         file.write(f'\n{id_ev}')            
#                 #         file.close()
#                 #         print('Событие записано в db.txt')
#                 # send_channel(mess)
                    
#         else:
#             pass

                            
                
# def get_ochnye_vstrechi_pob(soup,resultline,id_game,name_ht,name_at):
#     team1 = name_ht
#     team11 = team1.split(' ')[1]
#     team2 = name_at
#     team21 = team2.split(' ')[1]
#     # print(team11,team21)
#     # Создаем пустой массив
#     ov_mass = []
#     descr_mass = []
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in soup.find_all('table', class_ = ''):
#         # Пробегаем циклом по тэгу <tr>
#         # for tr in body.find_all('tr', class_ = ''):
#         for ted in body.find_all('td', class_ = 'descr'):
#             # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#             td = ted.get_text()
#             descr_mass.append(td)
#         # print(descr_mass)
#         # Пробегаем циклом по тэгу <td> в классе 'score'
#         for ted in body.find_all('td', class_ = 'score'):
#             # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#             td = ted.get_text()
#             # # Парсим содержимое тега
#             td1 = td.split(' (')[0]
#             # # Удаляем все знаки ' в строке
#             # td2 = td1.replace(')', "")
#             # # Удаляем все знаки , в строке
#             # td3 = td2.replace(',', "")
#             # Добавляем полученный результат в подготовленный нами массив
#             ov_mass.append(td1)
#     # print(descr_mass)
#     # print(ov_mass)
#     i=0
#     p1 = 0
#     p2 = 0

#     for mas in descr_mass:
        
#             i1 = mas.split(' - ')[0]
#             i2 = mas.split(' - ')[1]
#             schet = ov_mass[i]
#             schet1 = schet.split(':')[0]
#             schet2 = schet.split(':')[1]
#             if team11 in i1 and (int(schet1) > int(schet2)):
#                 p1 += 1
                
#             if team11 in i2 and (int(schet2) > int(schet1)):
#                 p1 += 1

#             if team21 in i1 and (int(schet1) > int(schet2)):
#                 p2 += 1
                
#             if team21 in i2 and (int(schet2) > int(schet1)):
#                 p2 += 1
            
#             i += 1
#     # Возвращаем готовый массив
#     # print(p1,p2)
    
#     return(p1,p2)  

# def get_last_vstrechi_pob(soup,resultline,id_game,name_ht,name_at):
#     team1 = name_ht
#     team11 = team1.split(' ')[0]
#     team2 = name_at
#     team21 = team2.split(' ')[0]
#     # print(team11,team21)
#     # Создаем пустой массив
#     ov_mass = []
#     descr_mass = []
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in soup.find_all('table', class_ = 'ev-mstat-tbl'):
#         # Пробегаем циклом по тэгу <tr>
#         # for tr in body.find_all('tr', class_ = ''):
#         for tr in body.find_all('tr', class_ = ''):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
            
#             # for ted in tr.find_all('td', class_ = 'ev-mstat-sc'):
                
              
#             for ted1 in tr.find_all('td', class_ = 'co1'):
#             # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                 ted = ted1.get_text()
#                 # # Парсим содержимое тега
#                 td1 = ted.split(' (')[0]
#             # # Удаляем все знаки ' в строке
#             # td2 = td1.replace(')', "")
#             # # Удаляем все знаки , в строке
#             # td3 = td2.replace(',', "")
#             # Добавляем полученный результат в подготовленный нами массив
#             ov_mass.append(td1)
#     # print(descr_mass)
#     # print(ov_mass)
#     i=0
#     p1 = 0
#     p2 = 0

#     for mas in descr_mass:
        
#             i1 = mas.split(' - ')[0]
#             i2 = mas.split(' - ')[1]
#             schet = ov_mass[i]
#             schet1 = schet.split(':')[0]
#             schet2 = schet.split(':')[1]
#             if team11 in i1 and (int(schet1) > int(schet2)):
#                 p1 += 1
                
#             if team11 in i2 and (int(schet2) > int(schet1)):
#                 p1 += 1

#             if team21 in i1 and (int(schet1) > int(schet2)):
#                 p2 += 1
                
#             if team21 in i2 and (int(schet2) > int(schet1)):
#                 p2 += 1
            
#             i += 1
#     # Возвращаем готовый массив
#     # print(p1,p2)
    
#     return(p1,p2)  

# def get_kol_pob_igr_last_vstrechi(mass_stat):
#     # Создаем пустой массив
#     mass_win_i1 = []
#     mass_false_i1 = []
#     mass_win_i2 = []
#     mass_false_i2 = []
#     mass_test = []
#     mass_co1 = []
#     mass_co1_1 = []
#     mass_co1_2 = []
#     mass_co = []
#     i = 1
#     p1 = 0
#     p2 = 0
#     pob1 = 0
#     pob2 = 0
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in mass_stat.find_all('table', class_ = 'ev-mstat-tbl'):
#         # Пробегаем циклом по тэгу <tr>
        
#         for tr in body.find_all('tr', class_ = ''):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
#             # test = tr.get_text()
#             # for ted in tr.find_all('td', class_ = 'ev-mstat-sc'):
#             mass_test.append(tr)  
#             for ted1 in tr.find_all('td', class_ = 'score'):
#             # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                 # ted11 = ted1.get_text()
#                 mass_co.append(ted1)
#             k = 0
#             for g in mass_co:
#                 k += 1
#             if k == 10:
#                 i = 0
#                 for ga in mass_co:
#                     # print(ga)
                    
#                     if i <=4:
#                         if 'co1' in f'{ga}':
                      
#                             pob1 += 1                          
#                     if i > 4:
#                         if 'co1' in f'{ga}':
#                             pob2 += 1
#                     i+=1
#         # else:
#         #     mass_co1_2.append(ted12)
                                

#     # print(mass_test)
#     # print(mass_win_i1)
#     # print(mass_win_i2)
#     # print(mass_win_i2)
#     # print('-----------------------')
#     # print(mass_co)
#     # print(mass_co1)
#     # print('-----------------------')
#     # print(pob1,'-',pob2)
    
#     # print(k)
#     for game in mass_win_i1:
#         p1 += 1
#     for game1 in mass_win_i2:
#         p2 += 1
#     # print (mass_win_i1)
                
                
#     return (pob1,pob2)

# # Функция получения имени первого игрока, либо команды
# def get_name_team1(resultline,id):
#     try: 
#         # Перебираем в цикле ветку массива с событиями
#         for event in resultline['data']['events']:
#             try:
#                 id_game = event['id']
#                 try:
#                     if id_game == id:
#                         try:
#                             team1 = event['team1']
#                             return (team1)
#                         except:
#                             pass
#                 except:
#                     pass
#             except:
#                 pass
#     except:
#         pass

# # Функция получения имени второго игрока, либо команды
# def get_name_team2(resultline,id):
#     try: 
#         # Перебираем в цикле ветку массива с событиями
#         for event in resultline['data']['events']:
#             try:
#                 id_game = event['id']
#                 try:
#                     if id_game == id:
#                         try:
#                             team1 = event['team2']
#                             return (team1)
#                         except:
#                             pass
#                 except:
#                     pass
#             except:
#                 pass
#     except:
#         pass            
#     # send_telegram('Поиск завершен')
# #         # print('send')            
# #         print(mess)         
def parse(soup):
    ov_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in soup.find_all('table', class_ = ''):
        # print(body)
        # Пробегаем циклом по тэгу <tr>
        for tr1 in body.find_all('tr', class_ = 'line'):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr1.find_all('td', class_ = 'score'):
                try:
                    # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                    td = ted.get_text()
                    # Парсим содержимое тега
                    td1 = td.split(' (')[1]
                    # Удаляем все знаки ' в строке
                    td2 = td1.replace(')', "")
                    # Удаляем все знаки , в строке
                    td3 = td2.replace(',', "")
                    # Добавляем полученный результат в подготовленный нами массив
                    ov_mass.append(td3)
                except:
                    pass
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'score'):
                try:
                    # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                    td = ted.get_text()
                    # Парсим содержимое тега
                    td1 = td.split(' (')[1]
                    # Удаляем все знаки ' в строке
                    td2 = td1.replace(')', "")
                    # Удаляем все знаки , в строке
                    td3 = td2.replace(',', "")
                    # Добавляем полученный результат в подготовленный нами массив
                    ov_mass.append(td3)
                except:
                    pass
    return ov_mass    
# def get_last_vstrechi(mass_stat):
#     # Создаем пустой массив
#     lv_mass = []
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in mass_stat.find_all('table', class_ = 'ev-mstat-tbl'):
#         # Пробегаем циклом по тэгу <tr>
#         for tr in body.find_all('tr', class_ = ''):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
#             for ted in tr.find_all('td', class_ = 'ev-mstat-sc'):
#                 # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                 try:
#                     td = ted.get_text()
#                     # Парсим содержимое тега
#                     td1 = td.split(' (')[1]
#                     # Удаляем все знаки ' в строке
#                     td2 = td1.replace(')', "")
#                     # Удаляем все знаки , в строке
#                     td3 = td2.replace(',', "")
#                     # Добавляем полученный результат в подготовленный нами массив
#                     lv_mass.append(td3)
#                 except:
#                     pass
#     # Возвращаем готовый массив 
#     return(lv_mass)

# def get_ochnye_vstrechi(mass_stat):
#     # Создаем пустой массив
#     ov_mass = []
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in mass_stat.find_all('table', class_ = ''):
#         # Пробегаем циклом по тэгу <tr>
#         for tr in body.find_all('tr', class_ = ''):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
#             for ted in tr.find_all('td', class_ = 'score'):
#                 # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                 td = ted.get_text()
#                 # Парсим содержимое тега
#                 td1 = td.split(' (')[1]
#                 # Удаляем все знаки ' в строке
#                 td2 = td1.replace(')', "")
#                 # Удаляем все знаки , в строке
#                 td3 = td2.replace(',', "")
#                 # Добавляем полученный результат в подготовленный нами массив
#                 ov_mass.append(td3)
#     # Возвращаем готовый массив 
#     return(ov_mass)


    
# # def parse(soup):
# #     ov_mass = []
# #     # Цикл переборки массива, переданного в функцию
# #     # Пробегаем циклом по тэгу <table>
# #     for body in soup.find_all('table', class_ = ''):
# #         # print(body)
# #         # Пробегаем циклом по тэгу <tr>
# #         for tr1 in body.find_all('tr', class_ = 'line'):
# #             # Пробегаем циклом по тэгу <td> в классе 'score'
# #             for ted in tr1.find_all('td', class_ = 'score'):
# #                 try:
# #                     # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
# #                     td = ted.get_text()
# #                     # Парсим содержимое тега
# #                     td1 = td.split(' (')[1]
# #                     # Удаляем все знаки ' в строке
# #                     td2 = td1.replace(')', "")
# #                     # Удаляем все знаки , в строке
# #                     td3 = td2.replace(',', "")
# #                     # Добавляем полученный результат в подготовленный нами массив
# #                     ov_mass.append(td3)
# #                 except:
# #                     pass
# #         for tr in body.find_all('tr', class_ = ''):
# #             # Пробегаем циклом по тэгу <td> в классе 'score'
# #             for ted in tr.find_all('td', class_ = 'score'):
# #                 try:
# #                     # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
# #                     td = ted.get_text()
# #                     # Парсим содержимое тега
# #                     td1 = td.split(' (')[1]
# #                     # Удаляем все знаки ' в строке
# #                     td2 = td1.replace(')', "")
# #                     # Удаляем все знаки , в строке
# #                     td3 = td2.replace(',', "")
# #                     # Добавляем полученный результат в подготовленный нами массив
# #                     ov_mass.append(td3)
# #                 except:
# #                     pass
# #     return ov_mass
def summ_point_set_mass(set_mass):
    # Создаем пустой массив
    summ_set_mass = []
    # Цикл переборки полученного массива
    for si in (set_mass):
        
        # Обработка исключений счетчика сумм
        try:
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
            s1 = si.split(':')[0] 
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
            s2 = si.split(':')[1]    
            # Получаем сумму переменных    
            summ = int(s1) + int(s2)
            # Добавляем полученную сумму в массив
            summ_set_mass.append(summ)
        # Выполняется в случае возникновения исключения
        except:
            # Пропустить - ничего не выполнять
            pass
    # Возвращаем полученный массив значений
    return(summ_set_mass)

def kol_ochnyh_vstrech(ov_mass):
    # Создаем переменную и присваиваем ей 0
    i = 0
    # Цикл переборки полученного массива
    for vstrecha in ov_mass:
        # Прибавляем 1 к переменной при пробегании массива
        i = i + 1
    # Возвращаем полученный массив значений
    return(i)

def kol_game_3_sets(ov_mass):
    # Создаем пустой массив
    
    g = 0
    # Цикл переборки полученного массива
    for game in ov_mass:
        game_mass = []
        try:
            set = game.split(' ')[0]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            game_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            game_mass.append(set)
        except:
            pass
        
        i = 0
        sets_mass = []
        for sets in game_mass:
            
            
            if ':' in sets:
                i += 1
            
        if i == 3:
            g += 1

        
    # Возвращаем полученный массив значений
    return(g)

# def kol_set_18_5_bolshe(lv_mass):
#     # Создаем пустой массив
#     set_mass = []
#     # Цикл переборки полученного массива
#     for game in lv_mass:
        
#         try:
#             set = game.split(' ')[0]
            
#             set_mass.append(set)
#         except:
#             pass
#         try:
#             set = game.split(' ')[1]
            
#             set_mass.append(set)
#         except:
#             pass
#         try:
#             set = game.split(' ')[2]
            
#             set_mass.append(set)
#         except:
#             pass
#         try:
#             set = game.split(' ')[3]
            
#             set_mass.append(set)
#         except:
#             pass
#         try:
#             set = game.split(' ')[4]
            
#             set_mass.append(set)
#         except:
#             pass
        
#     # print(set_mass)
#     sum_point = summ_point_set_mass(set_mass)
#     b = 0
#     m = 0
#     for sum_set_point in sum_point:
#         if sum_set_point >= 19:
#             b+=1
#         if sum_set_point <= 18:
#             m+=1
        
#     # Возвращаем полученный массив значений
#     return(b,m)


# def summ_point_set_mass(set_mass):
#     # Создаем пустой массив
#     summ_set_mass = []
#     # Цикл переборки полученного массива
#     for si in (set_mass):
        
#         # Обработка исключений счетчика сумм
#         try:
#             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#             s1 = si.split(':')[0] 
#             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
#             s2 = si.split(':')[1]    
#             # Получаем сумму переменных    
#             summ = int(s1) + int(s2)
#             # Добавляем полученную сумму в массив
#             summ_set_mass.append(summ)
#         # Выполняется в случае возникновения исключения
#         except:
#             # Пропустить - ничего не выполнять
#             pass
#     # Возвращаем полученный массив значений
#     return(summ_set_mass)

# # # Функция формирования массива со счетом первых партий очных встреч
# # def get_o_v_1set(ov_mass):
# #     # Создаем пустой массив
# #     ov_1set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_1 in ov_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_1_1 = set_1.split(' ')[0]
# #         # Добавляем полученное значение в массив
# #         ov_1set_mass.append(set_1_1)
# #     # Возвращаем полученный массив значений    
# #     return(ov_1set_mass)
    
# # # Функция формирования массива со счетом вторых партий очных встреч
# # def get_o_v_2set(ov_mass):
# #     # Создаем пустой массив
# #     ov_2set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_2 in ov_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_2_1 = set_2.split(' ')[1]
# #         # Добавляем полученное значение в массив
# #         ov_2set_mass.append(set_2_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_2set_mass)

# # # Функция формирования массива со счетом третьих партий очных встреч
# # def get_o_v_3set(ov_mass):
# #     # Создаем пустой массив
# #     ov_3set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_3 in ov_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_3_1 = set_3.split(' ')[2]
# #         # Добавляем полученное значение в массив
# #         ov_3set_mass.append(set_3_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_3set_mass)

# # # Функция формирования массива со счетом четвертых партий очных встреч
# # def get_o_v_4set(ov_mass):
# #     # Создаем пустой массив
# #     ov_4set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_4 in ov_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_4_1 = set_4.split(' ')[3]
# #         # Добавляем полученное значение в массив
# #         ov_4set_mass.append(set_4_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_4set_mass)

# # # Функция формирования массива со счетом пятых партий очных встреч
# # def get_o_v_5set(ov_mass):
# #     # Создаем пустой массив
# #     ov_5set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_5 in ov_mass:
# #         try:# Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #             set_5_1 = set_5.split(' ')[4]
# #             # Добавляем полученное значение в массив
# #             ov_5set_mass.append(set_5_1)
# #         except:
# #             pass
# #     # Возвращаем полученный массив значений
# #     return(ov_5set_mass)

# # # Функция получения количества партий с тоталом меньше 18.5 из переданного массива с суммами очков по партиям
# # def get_kol_menshe(summ_point):
# #     # Создаем переменную и присваиваем ей 0
# #     i = 0
# #     # Цикл переборки полученного массива
# #     for bolshe in summ_point:
# #         # Проверяем число полученное циклом
# #         if int(bolshe) <= 18:
# #             # Если условие выполняется прибавляем 1 к переменной
# #             i+=1
# #     # Возвращаем полученное количество
# #     return (i)

# # # Функция получения количества партий с тоталом больше 18.5 из переданного массива с суммами очков по партиям
# # def get_kol_bolshe(summ_point):
# #     # Создаем переменную и присваиваем ей 0
# #     i = 0
# #     # Цикл переборки полученного массива
# #     for bolshe in summ_point:
# #         # Проверяем число полученное циклом
# #         if int(bolshe) >= 19:
# #             # Если условие выполняется прибавляем 1 к переменной
# #             i+=1
# #             # Возвращаем полученное количество
# #     return (i)


# # # Функцтя формирования массива с суммами очков по партиям
# # def summ_point_set_mass(set_mass):
# #     # Создаем пустой массив
# #     summ_set_mass = []
# #     # Цикл переборки полученного массива
# #     for si in (set_mass):
        
# #         # Обработка исключений счетчика сумм
# #         try:
# #             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #             s1 = si.split(':')[0] 
# #             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
# #             s2 = si.split(':')[1]    
# #             # Получаем сумму переменных    
# #             summ = int(s1) + int(s2)
# #             # Добавляем полученную сумму в массив
# #             summ_set_mass.append(summ)
# #         # Выполняется в случае возникновения исключения
# #         except:
# #             # Пропустить - ничего не выполнять
# #             pass
# #     # Возвращаем полученный массив значений
# #     return(summ_set_mass)

# # def get_l_v_1set(lv_mass):
# #     # Создаем пустой массив
# #     ov_1set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_1 in lv_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_1_1 = set_1.split(' ')[0]
# #         # Добавляем полученное значение в массив
# #         ov_1set_mass.append(set_1_1)
# #     # Возвращаем полученный массив значений    
# #     return(ov_1set_mass)
    
# # # Функция формирования массива со счетом вторых партий очных встреч
# # def get_l_v_2set(lv_mass):
# #     # Создаем пустой массив
# #     ov_2set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_2 in lv_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_2_1 = set_2.split(' ')[0]
# #         # Добавляем полученное значение в массив
# #         ov_2set_mass.append(set_2_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_2set_mass)

# # # Функция формирования массива со счетом третьих партий очных встреч
# # def get_l_v_3set(lv_mass):
# #     # Создаем пустой массив
# #     ov_3set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_3 in lv_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_3_1 = set_3.split(' ')[2]
# #         # Добавляем полученное значение в массив
# #         ov_3set_mass.append(set_3_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_3set_mass)

# # # Функция формирования массива со счетом четвертых партий очных встреч
# # def get_l_v_4set(lv_mass):
# #     # Создаем пустой массив
# #     ov_4set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_4 in lv_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_4_1 = set_4.split(' ')[3]
# #         # Добавляем полученное значение в массив
# #         ov_4set_mass.append(set_4_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_4set_mass)

# # # Функция формирования массива со счетом пятых партий очных встреч
# # def get_l_v_5set(lv_mass):
# #     # Создаем пустой массив
# #     ov_5set_mass = []
# #     # Цикл переборки полученного массива
# #     for set_5 in lv_mass:
# #         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
# #         set_5_1 = set_5.split(' ')[3]
# #         # Добавляем полученное значение в массив
# #         ov_5set_mass.append(set_5_1)
# #     # Возвращаем полученный массив значений
# #     return(ov_5set_mass)
if __name__ == '__main__':
    main()
# bot.polling(none_stop=True)
# schedule.every(10).seconds.do(main)
# while True:
 
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     # time.sleep(1) 