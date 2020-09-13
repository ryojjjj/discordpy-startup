import discord
import datetime
import os
import random
import asyncio
from discord.ext import commands
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials 

#https://ja.wikipedia.org/wiki/Unicode%E3%81%AEEmoji%E3%81%AE%E4%B8%80%E8%A6%A7
"""
sheetkey = os.environ['SHEETKEY']
path = os.environ['MAIL']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
gc = gspread.authorize(credentials)
wb = gc.open_by_key(sheetkey)
ws = wb.worksheet("戦績記録")
ws2 = wb.worksheet("交流戦記録")  
"""

sheet = os.environ['SHEETKEY']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']    
credential = {
                "type": "service_account",
                "project_id": os.environ['SHEET_PROJECT_ID'],
                "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
                "private_key": os.environ['SHEET_PRIVATE_KEY'],
                "client_email": os.environ['SHEET_CLIENT_EMAIL'],
                "client_id": os.environ['SHEET_CLIENT_ID'],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url":  os.environ['SHEET_CLIENT_X509_CERT_URL']
             }

credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
gc = gspread.authorize(credentials)
wb = gc.open_by_key(sheet)
ws = wb.worksheet("挙手管理") 

botid=619351049752543234 #fishのid

client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
    await client.change_presence(activity=discord.Game(name='おさかな天国'))

    
@client.command()
async def suse(ctx): #.sの説明
    text='交流戦挙手方法\n挙手: 指定時間に対応するスタンプ(↓↓↓)を押す\n挙手取り下げ: 取り下げる時間のスタンプを再び押す\n↩: 募集文をチャンネルの一番下に持ってくる\n🔁: 募集時間帯の切り替え(21~24 or 20~26)\n\n20→🇴 21→🇦 22→🇧 23→🇨 24→🇩 25→🇪 26→🇫'
    await ctx.send(text)
    
    
@client.command()
async def fish(ctx2, about = "🐟🐟🐟 使い方 🐟🐟🐟"):
  help1 = discord.Embed(title=about,color=0xe74c3c,description=".s,.s2: 交流戦募集開始※再び.s .s2することでリセット 英語スタンプ→挙手 ×スタンプ→挙手全へ\n.list <時間>: 指定時間に挙手した人を返す\n.mention <時間>: 指定時間に挙手した人にメンション\n.cal: 即時集計。順位は16進数でも入力可、recallで呼び戻し、endで終了、backで一回分だけ修正可能\n.ran 数字: ランダムに数字出力\n.dev 数字 リスト: 組み分け\n.choose リスト: 選択\n.vote: 匿名アンケート(2択)\n作成者: さかな(@sakana8dx)\nさかなBot導入: https://discord.com/oauth2/authorize?client_id=619351049752543234&permissions=473152&scope=bot")
  await ctx2.send(embed=help1)       
 

@client.command()
async def ran(ctx,arg):
  a=int(arg)
  await ctx.send(1+random.randrange(a))

    
@client.command()
async def choose(ctx,*args):
  b=len(args)
  await ctx.send(args[random.randrange(b)])

    
@client.command()
async def dev(ctx,*args):
  a=int(args[0])
  b=len(args)-1
  c=b%a
  list = []
  #print(a,b,c,list,"\n")

  for i in range(b):
    list.append(args[i+1])
  result2 = ''
  for i in range(a):
    result = ''
    for j in range(b//a):
      d = list[random.randrange(len(list))]
      result += str(d)+" "
      #print(result,list,"\n")
      list.remove(d)       
      if c!= 0 :
        d = list[random.randrange(len(list))]
        result += str(d)+" "
        list.remove(d)   
        c -= 1
    result2 +=str(i+1) + " | " + result + "\n"
  await ctx.send(result2)
 
    
@client.command()
async def vote(ctx1):

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:          
            return emoji

    def check3(m):
      return m.author.id == ctx1.author.id        
    test2 = discord.Embed(title="内容を入力してください",colour=0xe74c3c)
    #test2.add_field(name=f"@{cn")
    msg2 = await ctx1.send(embed=test2)
    #await ctx1.send("内容を入力してください")
    about = await client.wait_for('message',check=check3)
    about = about.content
    #await ctx.send
    await ctx1.channel.purge(limit=1)
    test2 = discord.Embed(title="投票終了までの時間を入力してください(分)",colour=0xe74c3c)
    await msg2.edit(embed=test2)
    settime2 = await client.wait_for('message',check=check3)
    settime2 = settime2.content   
    await ctx1.channel.purge(limit=1)
    #print(about)
    settime2 = int(settime2)
    about2 = "\n投票終了まで" + str(settime2) +"分"
    settime2 = 60*settime2
    #print(ctx1.author.name)
    list = []
    list2 = []
    maru = 0
    batu = 0
    time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    #print(datetime.date.today(datetime.timezone(datetime.timedelta(hours=9))))
    test2 = discord.Embed(title=about,colour=0xe74c3c)
    test2.add_field(name=time,value=about2)
    #test2.add_field(name=f"@{cn")
    #msg2 = await ctx1.send(embed=test2)
    await msg2.edit(embed=test2)
    await msg2.add_reaction('🙆')
    await msg2.add_reaction('🙅')
    await msg2.add_reaction('↩')
    await msg2.add_reaction('👋')
    
    check2 = 0

    while check2 == 0:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime2, check=check)
        except asyncio.TimeoutError:
            #await msg2.delete()
            await ctx1.send("投票終了時間")
            break
        else:
            if msg2.id == reaction.message.id:
                if str(reaction.emoji) == '🙆':
                    if str(user.id) in str(list): 
                      pass
                      print("pass")
                    elif str(user.id) in str(list2):
                      #list += str(user.id) + " "
                      list.append(user.id)
                      maru += 1 
                      batu -= 1
                      list2.remove(user.id)                 
                      #list2.replace(str(user.id),'')              
                    else:
                      #list += str(user.id)
                      list.append(user.id)
                      maru += 1 
                elif str(reaction.emoji) == '🙅':
                    if str(user.id) in str(list2):   
                        pass
                        print("pass")

                    elif str(user.id) in str(list):
                      #list2 += str(user.id) + " "
                      list2.append(user.id)                      
                      maru -= 1 
                      batu += 1
                      list.remove(user.id)                 
                      #list.replace(str(user.id),'')
                      #print(list,"\n",list2)
                    else:                                   
                      #list2 += str(user.id) 
                      list2.append(user.id)
                      batu += 1 
                    
                elif str(reaction.emoji) == '↩': 
                    await msg2.delete()
                    msg2 = await ctx1.send(embed=test2)  
                    await msg2.add_reaction('🙆')
                    await msg2.add_reaction('🙅')
                    await msg2.add_reaction('↩')
                    await msg2.add_reaction('👋')
                    
                elif str(reaction.emoji) == '👋': 
                    if user.id == ctx1.author.id:
                      #await msg2.delete()
                      break     

        print("OK") 
        print(list,":1\n",list2,":2")                      
        test2 = discord.Embed(title=about,colour=0xe74c3c,description="🙆:{} 🙅:{}".format(maru,batu))
        test2.add_field(name=time,value=about2)

        #test2.add_field("🙆{maru} 🙅{batu}")
        await msg2.edit(embed=test2)
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg2.remove_reaction(str(reaction.emoji), user)
    
    await ctx1.send(f"投票終了{ctx1.author.mention}")
    
    
@client.command()
async def cal(ctx):
    
  def check(m):
    if m.channel.id != ctx.channel.id:
        return False
    return m.author.id == ctx.author.id
        
  def is_int(s):
    try:
        int(s,16)
        return True
    except ValueError:
        return False
  def is_under12(b):
    if all(elem < 13 for elem in b):
        return True
    else:
        False

  cal = discord.Embed(title="🐟即時集計🐟",color=0xe74c3c,description="0-0 @12")
  result = await ctx.send(embed=cal)
  moji = await ctx.send("結果を入力してください(recall or 777で一番上に、backで修正)")
  msg = await ctx.send("🐟")
  
  f=0
  g=0
  h=''
  j=0
  while j!=12:
    check1 = 0
    while check1 == 0:
        try:
            rank = await client.wait_for('message',timeout=900, check=check)
        except asyncio.TimeoutError:        
            await moji.delete()     
            break
        else:
          #rank = await client.wait_for('message',check=check)    
          a = rank.content
          b = []      
          if len(a)==6 or len(a)==7 or len(a)==8 or len(a)==9:
            if a == 'recall':
              await result.delete()
              await moji.delete()
              result = await ctx.send(embed=cal)
              moji = await ctx.send("結果を入力してください(recall or 777で一番上に、backで修正)")
              await rank.delete()

            elif is_int(a)==True:
              if len(a)==6:
                for i in range(6):
                    b.append(int(a[i],16))    

              elif len(a)==7:
                  for i in range(5):
                      b.append(int(a[i]))
                  b.append(int(a[5:]))

              elif len(a)==8:
                  for i in range(4):
                      b.append(int(a[i]))
                  b.append(int(a[4:6]))
                  b.append(int(a[6:]))

              elif len(a)==9:
                  for i in range(3):
                      b.append(int(a[i]))
                  b.append(int(a[3:5]))
                  b.append(int(a[5:7]))
                  b.append(int(a[7:]))
              await rank.delete()
              if is_under12(b)==True:
                    check1=1
              else:
                miss = await ctx.send("try again")
                await asyncio.sleep(3)
                await miss.delete()
            else:
              miss = await ctx.send("try again")
              await asyncio.sleep(3)
              await miss.delete()

          elif a == 'end':              
              await moji.delete()
              await ctx.send("即時終了")
              break
          elif a == '.cal':
              await moji.delete()                  
              break          
          elif a == '777':
              await result.delete()
              await moji.delete()
              result = await ctx.send(embed=cal)
              moji = await ctx.send("結果を入力してください(recall or 777で一番上に、backで修正)")
              await rank.delete()
          elif a == 'back':
              h=h.replace(h2,'')
              f-=d
              g-=e              
              k = str(f)+"-"+str(g)+"\t("+str(f-g)+")"
              cal = discord.Embed(title="🐟即時集計🐟",color=0xe74c3c,description="{} @{}\n---------------------\n{}".format(k,11-j+2,h))    
              await result.edit(embed=cal)
              msg2 = await ctx.send("修正しました")
              await asyncio.sleep(3)
              await msg2.delete()
              j-=1
    
    await msg.delete()    
    c=str(b[0])+' '+str(b[1])+' '+str(b[2])+' '+str(b[3])+' '+str(b[4])+' '+str(b[5])
    d=0
    
    for i in range(6):
        point=b[i]
        if point == 1:
            point = 15
        elif point == 2:
            point = 12
        else:
            point = 13-point
        d+=point
    e=82-d
    f+=d
    g+=e
    
    h2= "race"+str(j+1).ljust(2)+" | "+str(d)+"-"+str(e)+" ("+str(d-e)+") | "+c+"\n"
    h += h2
    k = str(f)+"-"+str(g)+"\t("+str(f-g)+")"
    cal = discord.Embed(title="🐟即時集計🐟",color=0xe74c3c,description="{} @{}\n---------------------\n{}".format(k,11-j,h))    
    await result.edit(embed=cal)
    msg = await ctx.send(h2)
     
    j+=1
  await msg.delete()
  await moji.delete()
  await ctx.send("即時終了")
         
     
@client.command()
async def list(ctx,n): #.sの機能
    if int(n)>19 and int(n)<27: 
        a=str(ctx.guild.id)
        list=ws.col_values(1)
        row=list.index(a)+1
        b=ws.row_values(row)
        await ctx.send(b[int(n)-18])


@client.command()
async def mention(ctx,n): #.sの機能
    if int(n)>19 and int(n)<27: 
        a=str(ctx.guild.id)
        list=ws.col_values(1)
        row=list.index(a)+1
        b=ws.row_values(row)
        await ctx.send(b[int(n)-11])
        
"""
async def add(channel,row,n,name,mention):
    b=ws.row_values(row)
    if mention in b[n-11]: #21→3,10,17
        b[n-18]=b[n-18].replace(name,'')
        b[n-11]=b[n-11].replace(mention,'')
        b[n-4] = int(b[n-4])+1

    else:
        b[n-18] += name
        b[n-11] += mention
        b[n-4] = int(b[n-4])-1
        if b[n-4] == 0:
            await channel.send(f'{n}〆 {b[n-11]}')

    ws.update_cell(row,n-17,b[n-18])
    ws.update_cell(row,n-10,b[n-11])
    ws.update_cell(row,n-3,b[n-4])
"""

async def add(channel,row,n,name,mention):
    b=ws.range(row,1,row,24)
    if mention in b[n-11].value: #21→3,10,17
        b[n-18].value=b[n-18].value.replace(name,'')
        b[n-11].value=b[n-11].value.replace(mention,'')
        b[n-4].value = int(b[n-4].value)+1

    else:
        b[n-18].value += name
        b[n-11].value += mention
        b[n-4].value = int(b[n-4].value)-1
        if b[n-4].value == 0:
            await channel.send(f'{n}〆 {b[n-11].value}')
    
    ws.update_cells(b)

@client.command()
async def s(ctx): #.sの機能
    a=str(ctx.guild.id)
    try:
      list=ws.col_values(1)
      row=list.index(a)+1
    except:
      ws.append_row([str(ctx.guild.id)])
      list=ws.col_values(1)
      row=list.index(a)+1
      #for i in range(22):
      #ws.update_cell(row,23,0)

    b=ws.range(row,3,row,24)
    #b=ws.row_values(row)
    for i in range(7):
        b[i].value='> '
    for i in range(7):
        b[i+7].value=''
    for i in range(7):
        b[i+14].value=6
    b[21].value=1
    ws.update_cells(b)
                    
    now=datetime.datetime.now()
    month=now.month
    day=now.day
    text=f"交流戦募集 {month}月{day}日"
    test = discord.Embed(title=text,colour=0x1e90ff)
    test.add_field(name=f"21@6 ", value='>', inline=False)
    test.add_field(name=f"22@6 ", value='>', inline=False)
    test.add_field(name=f"23@6 ", value='>', inline=False)
    test.add_field(name=f"24@6 ", value='>', inline=False)
    msg = await ctx.send(embed=test)
    await msg.add_reaction('🇦')
    await msg.add_reaction('🇧')
    await msg.add_reaction('🇨')
    await msg.add_reaction('🇩')
    await msg.add_reaction('↩')
    await msg.add_reaction('🔁')
    msg2=await ctx.send(f"21@6 22@6 23@6 24@6")
    ws.update_cell(row,2,str(msg.id))                
    ws.update_cell(row,25,str(msg2.id))                


#-----------------------------------------------------
@client.event  
async def on_raw_reaction_add(payload):
    #print(payload.guild_id)
    channel = client.get_channel(payload.channel_id)
    msg=await channel.fetch_message(payload.message_id)
    if msg.author.id == botid:
        if payload.member.bot == False:
            list=ws.col_values(1)
            row=list.index(str(payload.guild_id))+1
            b=ws.row_values(row)
            if msg.id == int(b[1]):
                await msg.remove_reaction(str(payload.emoji),payload.member)
                name=payload.member.name+' '
                mention='<@!'+str(payload.member.id)+'>'+' '
                if str(payload.emoji) == '🇴':
                    n=20
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇦':
                    n=21
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇧':
                    n=22
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇨':
                    n=23
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇩':
                    n=24
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇪':
                    n=25
                    await add(channel,row,n,name,mention)
                if str(payload.emoji) == '🇫':
                    n=26
                    await add(channel,row,n,name,mention)                   
                      
                b=ws.row_values(row) #21→3,10,17
                now=datetime.datetime.now()
                month=now.month
                day=now.day
                text=f"交流戦募集 {month}月{day}日"
                test = discord.Embed(title=text,colour=0x1e90ff)
                if int(b[23])==2:
                    test.add_field(name=f"20@{b[16]} ", value=b[2], inline=False)
                test.add_field(name=f"21@{b[17]} ", value=b[3], inline=False)
                test.add_field(name=f"22@{b[18]} ", value=b[4], inline=False)
                test.add_field(name=f"23@{b[19]} ", value=b[5], inline=False)
                test.add_field(name=f"24@{b[20]} ", value=b[6], inline=False)
                if int(b[23])==2:
                    test.add_field(name=f"25@{b[21]} ", value=b[7], inline=False)
                    test.add_field(name=f"26@{b[22]} ", value=b[8], inline=False)

                if str(payload.emoji) == '🔁':
                    if int(b[23])==2:
                      ws.update_cell(row,24,1)
                      b[23]=1
                    else:
                      ws.update_cell(row,24,2)  
                      b[23]=2
                    await msg.delete()
                    test = discord.Embed(title=text,colour=0x1e90ff)
                    if int(b[23])==2:
                        test.add_field(name=f"20@{b[16]} ", value=b[2], inline=False)
                    test.add_field(name=f"21@{b[17]} ", value=b[3], inline=False)
                    test.add_field(name=f"22@{b[18]} ", value=b[4], inline=False)
                    test.add_field(name=f"23@{b[19]} ", value=b[5], inline=False)
                    test.add_field(name=f"24@{b[20]} ", value=b[6], inline=False)
                    if int(b[23])==2:
                        test.add_field(name=f"25@{b[21]} ", value=b[7], inline=False)
                        test.add_field(name=f"26@{b[22]} ", value=b[8], inline=False)
                    msg = await channel.send(embed=test)
                    if int(b[23])==2:
                        await msg.add_reaction('🇴')
                    await msg.add_reaction('🇦')
                    await msg.add_reaction('🇧')
                    await msg.add_reaction('🇨')
                    await msg.add_reaction('🇩')
                    if int(b[23])==2:
                        await msg.add_reaction('🇪')
                        await msg.add_reaction('🇫')
                    await msg.add_reaction('↩')
                    await msg.add_reaction('🔁')
                    ws.update_cell(row,2,str(msg.id)) 

                if str(payload.emoji) == '↩':
                    await msg.delete()
                    msg = await channel.send(embed=test)
                    if int(b[23])==2:
                        await msg.add_reaction('🇴')
                    await msg.add_reaction('🇦')
                    await msg.add_reaction('🇧')
                    await msg.add_reaction('🇨')
                    await msg.add_reaction('🇩')
                    if int(b[23])==2:
                        await msg.add_reaction('🇪')
                        await msg.add_reaction('🇫')
                    await msg.add_reaction('↩')
                    await msg.add_reaction('🔁')
                    ws.update_cell(row,2,str(msg.id))
                else:
                    await msg.edit(embed=test)

                msg2=await channel.fetch_message(int(b[24]))
                await msg2.delete()
                if int(b[23])==1:
                    msg2=await channel.send(f"21@{b[17]} 22@{b[18]} 23@{b[19]} 24@{b[20]}")
                else:
                    msg2=await channel.send(f"20@{b[16]} 21@{b[17]} 22@{b[18]} 23@{b[19]} 24@{b[20]} 25@{b[21]} 26@{b[22]}")
                ws.update_cell(row,25,str(msg2.id))    
                
@client.command()
async def rec(ctx1, about, cnt, settime2):
    cnt, settime2 = int(cnt), float(settime2)
    settime2 = 60*settime2
    #print(ctx1.author.name)
    recruiter = ctx1.author.name
    print(recruiter)	
    list = [">"]
    list.append(ctx1.author.name)
    mem = []
    mem.append(ctx1.author.mention)
    test2 = discord.Embed(title=about,colour=0xe74c3c)
    test2.add_field(name=f"@{cnt} ", value=' '.join(list), inline=False)
    msg2 = await ctx1.send(embed=test2)
    await msg2.add_reaction('🐟')
    await msg2.add_reaction('✖')
    await msg2.add_reaction('👋')
     
    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji

    while len(list)-1 <= 100:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime2, check=check)
        except asyncio.TimeoutError:
            await msg2.delete()
            break
        else:
            if msg2.id == reaction.message.id:
                if str(reaction.emoji) == '🐟':
                    list.append(user.name)
                    mem.append(user.mention)
                    cnt -= 1
                    if cnt == 0:
                        member = ' '.join(mem)
                        test2 = discord.Embed(title=about,colour=0xe74c3c)
                        test2.add_field(name=f"@{cnt} ", value=' '.join(list), inline=False)
                        await msg2.edit(embed=test2)
                        await msg2.remove_reaction(str(reaction.emoji), user)
                        await ctx1.send("〆 {}".format(member))  
                        break
                if str(reaction.emoji) == '✖':
                    if user.name in list:
                        list.remove(user.name)
                        mem.remove(user.mention)
                        cnt += 1
                if str(reaction.emoji) == '🥺': 
                    if user.name == recruiter:
                      await msg2.delete()
                      break
                  
                test2 = discord.Embed(title=about,colour=0xe74c3c)
                test2.add_field(name=f"@{cnt} ", value=' '.join(list), inline=False)
                await msg2.edit(embed=test2)
                # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
                await msg2.remove_reaction(str(reaction.emoji), user)
                
#-----------------------------------------------------    
@client.command()
async def mt(ctx): #ラウンジの集計
    def check(m):
        return m.author.id == ctx.author.id

    await ctx.send("MogiBotの'Poll Ended!'から始まる文章をコピーして貼り付けてください.\ncopy the message, starts with 'Poll Ended!'' and paste here")
    msg = await client.wait_for('message',check=check)
    msg=msg.content
    if '!scoreboard' in msg and 'Poll Ended!' in msg:
        a=msg.find('!scoreboard')
        msg2=msg[a+12:]
        msg=msg2.split()
        team=int(msg[0])
        num=int(12/team)
        ok=0
        ok2=0
        while ok==0:
            await ctx.send(f'下記順番通りに得点を入力してください. Type scores.(例: 100 90 12+70 ...)\n{msg2[2:]}')
            try:
                score=await client.wait_for('message',timeout=300,check=check)
            except asyncio.TimeoutError:
                await ctx.send('timeout') 
                ok2=1
                break
            else:
                score=score.content
                score=score.split()
                if len(score)==12:
                    ok=1
                else:
                    await ctx.send('エラー: もう一度入力してください. 12名分の得点を正しく入力してください.')
        if ok2==0:
            text=''
            k=0
            if team==1:
                for i in range(12):
                    text=f'{text}{msg[i+1]} {score[i]}\n'
            else:
                for i in range(team):
                    text=f'{text}Team{i+1}\n'
                    for j in range(num):
                        k=k+1
                        text=f'{text}{msg[k]} {score[k-1]}\n'
            await ctx.send(text)
            await ctx.send("上記内容をコピーし 'https://hlorenzi.github.io/mk8d_ocr/table.html' にペーストしてください")
        
    else:
        await ctx.send('エラー')

"""                       
@client.command()
async def fish2(ctx, about = "🐟🐟🐟 戦績記録使い方 🐟🐟🐟"):
  help1 = discord.Embed(title=about,color=0xe74c3c,description=".p 点数: 個人の結果記録,符号＋点数を入力する(負けた試合は負),例:.p 100,.p -77\n.r 点差 チーム名: 交流戦の結果記録,例:.r 40 IsK,.r -50 Lv\n.revise 点数: 個人の結果修正,例:.p -80を消す→.revise -80\n.stats/.teamstats/.history: 戦績\n.vs チーム名: 対象チームとの戦績確認\n.rename/.teamrename: 名前の変更\n.reset/.teamreset: 戦績(statsの内容)リセット\n.teamdelete: 対戦履歴削除\n作成者: さかな(@sakana8dx)\nさかなBot導入: https://discord.com/oauth2/authorize?client_id=619351049752543234&permissions=473152&scope=bot")
  await ctx.send(embed=help1)


@client.command()
async def p(ctx,a):

  def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
  try:
    cell=ws.find(str(ctx.author.id+ctx.guild.id)) 
  except:
    ws.append_row([str(ctx.author.id+ctx.guild.id),ctx.guild.name,ctx.author.name])
    cell=ws.find(str(ctx.author.id+ctx.guild.id))
    for i in range(10):
      ws.update_cell(cell.row,len(ws.row_values(cell.row))+1,0)

  #C2:totalnum	D3:winnum	E4:losenum	F5:winrate	G6:ave	H7:winave	I8:loseave	J9:total	K10:wintotal	L11:losetotal

  b=ws.row_values(cell.row)
  if is_int(a)==False:
    msg = await ctx.send("エラー")
    await asyncio.sleep(3)
    await msg.delete()
  else:
    b[3]=int(b[3])+1
    a=int(a)
    if a>0:
      b[4]=int(b[4])+1
      b[11]=int(b[11])+a
      b[8]=b[11]//b[4]
    else:
      a=-1*int(a)
      b[5]=int(b[5])+1
      b[12]=int(b[12])+a
      b[9]=b[12]//b[5]
    b[10]=int(b[10])+a
    b[6]=int(b[4])*100//b[3]
    b[7]=b[10]//b[3]
    for i in range(13):
      ws.update_cell(cell.row,i+1,b[i])
 
    msg = await ctx.send("記録しました")
    await asyncio.sleep(3)
    await msg.delete()
  
  await ctx.channel.purge(limit=1)


@client.command()
async def stats(ctx):
  cell=ws.find(str(ctx.author.id+ctx.guild.id))
  b=ws.row_values(cell.row)
  msg = discord.Embed(title="stats",colour=0x1e90ff)
  msg.add_field(name="name", value=b[2], inline=True)
  msg.add_field(name="play", value=b[3], inline=True)
  msg.add_field(name="win rate", value=b[6]+"%", inline=True)
  msg.add_field(name="average", value=b[7], inline=True)
  msg.add_field(name="win-ave", value=b[8], inline=True)
  msg.add_field(name="lose-ave", value=b[9], inline=True)
  await ctx.channel.purge(limit=1)  
  msg = await ctx.send(embed=msg)  
  await asyncio.sleep(15)
  await msg.delete() 


@client.command()
async def rename(ctx):
  cell=ws.find(str(ctx.author.id+ctx.guild.id))
  ws.update_cell(cell.row,2,ctx.author.name)
  msg = await ctx.send("名前を修正しました")
  await asyncio.sleep(3)
  await msg.delete()


@client.command()
async def revise(ctx,a):
  def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

  try:
    cell=ws.find(str(ctx.author.id+ctx.guild.id)) 
  except:
    ws.append_row([str(ctx.author.id+ctx.guild.id),ctx.guild.name,ctx.author.name])
    cell=ws.find(str(ctx.author.id+ctx.guild.id))
    for i in range(10):
      ws.update_cell(cell.row,len(ws.row_values(cell.row))+1,0)

  #C2:totalnum	D3:winnum	E4:losenum	F5:winrate	G6:ave	H7:winave	I8:loseave	J9:total	K10:wintotal	L11:losetotal

  b=ws.row_values(cell.row)
  if is_int(a)==False:
    msg = await ctx.send("エラー")
    await asyncio.sleep(3)
    await msg.delete()
  else:
    b[3]=int(b[3])-1
    a=int(a)
    if a>0:
      b[4]=int(b[4])-1
      b[11]=int(b[11])-a
      b[8]=b[11]//b[4]
    else:
      a=-1*int(a)
      b[5]=int(b[5])-1
      b[12]=int(b[12])-a
      b[9]=b[12]//b[5]
    b[10]=int(b[10])-a
    b[6]=int(b[4])*100//b[3]
    b[7]=b[10]//b[3]
    for i in range(13):
      ws.update_cell(cell.row,i+1,b[i])
 
    msg = await ctx.send("修正しました")
    await asyncio.sleep(3)
    await msg.delete()
  
  await ctx.channel.purge(limit=1)


@client.command()
async def result(ctx):
  cell=ws.find(str(ctx.guild.id))
  b=ws.row_values(cell.row)
  msg = discord.Embed(title="stats",colour=0x1e90ff)
  msg.add_field(name="name", value=b[2], inline=True)
  msg.add_field(name="play", value=b[3], inline=True)
  msg.add_field(name="win rate", value=b[6]+"%", inline=True)
  await ctx.channel.purge(limit=1)  
  msg = await ctx.send(embed=msg)  
  await asyncio.sleep(15)
  await msg.delete() 


@client.command()
async def reset(ctx):
  cell=ws.find(str(ctx.author.id+ctx.guild.id))
  for i in range(10):
    ws.update_cell(cell.row,i+4,0)

  msg = await ctx.send("リセットしました")
  await asyncio.sleep(3)
  await msg.delete()


@client.command()
async def r(ctx,a,a2):
  def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

  try:
    cell=ws.find(str(ctx.guild.id)) 
  except:
    ws.append_row([str(ctx.guild.id),ctx.guild.name,"None"])
    cell=ws.find(str(ctx.guild.id))
    for i in range(4):
      ws.update_cell(cell.row,len(ws.row_values(cell.row))+1,0)

  b=ws.row_values(cell.row)
  if is_int(a)==False:
    msg = await ctx.send("エラー ※.r 点差 チーム名")
    await asyncio.sleep(3)
    await msg.delete()
  else:
    date=str(datetime.date.today())
    ws2.append_row([date,str(ctx.guild.id),ctx.guild.name,a,a2])

    b[3]=int(b[3])+1
    a=int(a)
    if a>0:
      b[4]=int(b[4])+1      
    else:      
      b[5]=int(b[5])+1
    b[6]=int(b[4])*100//int(b[3])
  for i in range(7):
      ws.update_cell(cell.row,i+1,b[i])
  
  msg = await ctx.send("記録しました")
  await asyncio.sleep(3)
  await msg.delete()
  
  await ctx.channel.purge(limit=1)


@client.command()
async def teamstats(ctx):
  cell=ws.find(str(ctx.guild.id))
  b=ws.row_values(cell.row)
  msg = discord.Embed(title="stats",colour=0x1e90ff)
  msg.add_field(name="name", value=b[1], inline=True)
  msg.add_field(name="play", value=b[3], inline=True)
  msg.add_field(name="win rate", value=b[6]+"%", inline=True)
  await ctx.channel.purge(limit=1)  
  msg = await ctx.send(embed=msg)  
  await asyncio.sleep(15)
  await msg.delete()


@client.command()
async def vs(ctx,a):
  w=0
  l=0
  b=''
  cell=ws2.findall(str(ctx.guild.id))
  for i in range(len(cell)):
    c=ws2.row_values(cell[i].row)
    if c[4]==a:
      if int(c[3])>0:
        w+=1
      else:
        l+=1
      b+=c[0]+" "+c[3]+"\n"
  b=f'戦績: vs {a} {w}-{l}\n'+b
  msg = await ctx.send(b)
  await asyncio.sleep(20)
  await msg.delete() 


@client.command()
async def teamreset(ctx):
  cell=ws.find(str(ctx.guild.id))
  for i in range(4):
    ws.update_cell(cell.row,i+4,0)
  msg = await ctx.send("リセットしました")
  await asyncio.sleep(3)
  await msg.delete()


@client.command()
async def teamdelete(ctx):
  cell=ws.find(str(ctx.guild.id))
  b=ws.row_values(cell.row)
  msg = discord.Embed(title="stats",colour=0x1e90ff)
  msg.add_field(name="name", value=b[1], inline=True)
  msg.add_field(name="play", value=b[3], inline=True)
  msg.add_field(name="win rate", value=b[6]+"%", inline=True)
  await ctx.channel.purge(limit=1)  
  msg = await ctx.send(embed=msg)
  
  for i in range(4):
    ws.update_cell(cell.row,i+4,0)
  cell=ws2.findall(str(ctx.guild.id))
  for i in range(len(cell)):    
    ws2.delete_row(cell[len(cell)-i-1].row)
  msg = await ctx.send("リセットしました")
  await asyncio.sleep(3)
  await msg.delete()


@client.command()
async def history(ctx):
  b=''
  cell=ws2.findall(str(ctx.guild.id))
  a=min(len(cell),100)
  for i in range(a):
    c=ws2.row_values(cell[a-i-1].row)
    b+=c[4]+" "+c[3]+" , "
  b=f'戦績:\n'+b
  msg = await ctx.send(b)


@client.command()
async def teamrename(ctx):
  cell=ws.find(str(ctx.guild.id))
  ws.update_cell(cell.row,2,ctx.guild.name)
  msg = await ctx.send("名前を修正しました")
  await asyncio.sleep(3)
  await msg.delete()
"""

token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)
