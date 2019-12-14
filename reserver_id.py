from pyrogram import Client,Filters
from pyrogram import errors
import time
username_exest = False
id_user = ''
ida_admin = ''
first_run = True
bot = Client(
    session_name = 'Session',
    api_id=0,
    api_hash='',
)
def decoetor_admin(func):
    def warrper_admin(client,message):
        global ida_admin
        global first_run
        print(ida_admin)

        if first_run == True :            
                ida_admin = message.from_user.id
                first_run = False
                client.send_message(ida_admin,'Manager was selected')
        if ida_admin != message.from_user.id :
                message.reply_text(f'You do not have sufficient access to perform this operation',True)
        elif  ida_admin == message.from_user.id:
            return func(client,message)

    return warrper_admin

@bot.on_message(Filters.regex('change admin @\w'))
@decoetor_admin
def id_admin(client,message):
    id_admin = str(message.text).split(' ')[2]
    client.send_message(message.from_user.id,'Manager was selected')
    


@bot.on_message(Filters.regex('set id @\w'))
@decoetor_admin
def get_id(client,message):
    global id_user
    id_user =str( message.text ).split(' ')[2]
    message.reply_text(f'The desired ID was reserved : {id_user}' ,True)
    username_exest = False



@bot.on_message(Filters.regex('run'))
@decoetor_admin
def set_id_username(client,message):
    global username_exest
    if_1 =True
    username_exest_1 = ''
    username_exest_2 =None
    while  username_exest == False:
        try:
             
            if if_1 == True: 
                
                time.sleep(0.8)
                username_exest_1 = bot.get_chat(id_user.replace('@',''))
                print('log 1 : {username_exest}')
                if_1 =False
        except errors.BadRequest:
                # print('log error')
                client.send_message(message.from_user.id,f'sucsessfuly change usrname to : {id_user}')
                id =id_user.replace('@','')
                bot.update_username(id)  
                username_exest = True
                break
        except errors.exceptions.FloodWait  as erorr:
                second = str(erorr).split(' ')
                print(second)
                text = '  Please try a moment later'.format(second[5])
                client.send_message(message.from_user.id,text)

        try:
            if if_1 != True: 
                try:
                    time.sleep(0.8)
                    username_exest_2 = bot.get_users(id_user.replace('@',''))
                    # print(f'log 2: {username_exest}')
                except:
                    time.sleep(0.8)
                if_1 = True
        except errors.BadRequest:
                # print('log error 2')
                client.send_message(message.from_user.id,f'sucsessfuly change usrname to : {id_user}')
                id =id_user.replace('@','')
                bot.update_username(id) 
                username_exest = True
                break

        except errors.exceptions.FloodWait  as erorr:
                second = str(erorr).split(' ')
                print(second)
                text = '  Please try a moment later'.format(second[5])
                client.send_message(message.from_user.id,text)

                    

bot.run()