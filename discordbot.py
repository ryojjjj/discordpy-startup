import discord
import datetime
import os
import random

#https://ja.wikipedia.org/wiki/Unicode%E3%81%AEEmoji%E3%81%AE%E4%B8%80%E8%A6%A7

#list = []
#apre = 'おさかなのサーバー'

from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  

@client.command()
async def fish(ctx2, about = "🐟🐟🐟 使い方 🐟🐟🐟"):
  help1 = discord.Embed(title=about,color=0xe74c3c,description=".s,.s2,.s3: 交流戦募集開始※12時間で停止 英語スタンプ→挙手 ×スタンプ→挙手全へ\n.rec: 募集開始(.rec 募集名 人数 制限時間(分))\n※募集開始した人の👋スタンプで募集終了\n.cal: 即時集計。順位は16進数で入力、endで強制終了\n.ran 数字: ランダムに数字出力\n.dev 数字 リスト: 組み分け\n.choose リスト: 選択\n.vote: 匿名アンケート(2択)\n作成者: さかな(@sakana8dx)")
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
async def cal(ctx2):
    
  def check(m):
    return m.author.id == ctx2.author.id

  i = 0
  a1 = 0
  a2 = 0
  b1 = 0
  b2 = 0
  c1 = ""
  c2 = str(a2)+"-"+str(b2)
  cal = discord.Embed(title="🐟即時集計🐟",color=0xe74c3c,description="{} @{}\n{}".format(c2,12-i,c1))
  result = await ctx2.send(embed=cal)
  await ctx2.send("結果を入力してください(end or @0 で停止)")

  for k in range(12):
    i += 1
    check1 = 0
    while check1 == 0:
      rank = await client.wait_for('message',check=check)
      rank = rank.content
      await ctx2.channel.purge(limit=1)
      
      #print(rank)
      if len(rank) == 6:        
        check1 = 1
        #print("OK")
      elif rank == 'end':
        await ctx2.send("即時終了")
        break
      elif rank == '.cal':
        break
      else:
        await ctx2.send("try again")
    
    ranklist = ''
    a1 = 0
    for j in range(6):
      ranklist += str(int(rank[j],16))+" "
      point = int(rank[j],16)
      if point == 1:
        point = 15
      elif point == 2:
        point = 12
      else:
        point = 13-point
      a1 += point
      #print(a1)

    b1 = 82-a1
    a2 += a1
    b2 += b1
    c1 += "race"+str(i).ljust(2)+" | "+str(a1)+"-"+str(b1)+" ("+str(a1-b1)+") | "+ranklist+"\n"
    c2 = str(a2)+"-"+str(b2)+"\t("+str(a2-b2)+")"
    cal = discord.Embed(title="🐟即時集計🐟",color=0xe74c3c,description="{} @{}\n---------------------\n{}".format(c2,12-i,c1))
    await result.edit(embed=cal)
    #print(a1,a2,b1,b2,c1,c2)    
        
    
@client.command()
async def s(ctx, about = "交流戦募集 {}".format(datetime.date.today()), cnt1 = 6, settime = 43200):
    cnt1, settime = int(cnt1), float(settime)
    a = ctx.guild.name
    #print(a)
    #list.append(0)
    #b = len(list)
    #print(b)
  
    list1 = [">"]
    list2 = [">"]
    list3 = [">"]
    list4 = [">"]
    mem1 = []
    mem2 = []
    mem3 = []
    mem4 = []
    cnt2 = 6
    cnt3 = 6
    cnt4 = 6
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0

    test = discord.Embed(title=about,colour=0x1e90ff)
    test.add_field(name=f"21@{cnt1} ", value=' '.join(list1), inline=False)
    test.add_field(name=f"22@{cnt2} ", value=' '.join(list2), inline=False)
    test.add_field(name=f"23@{cnt3} ", value=' '.join(list3), inline=False)
    test.add_field(name=f"24@{cnt4} ", value=' '.join(list4), inline=False)
    msg = await ctx.send(embed=test)
    #投票の欄

    await msg.add_reaction('🇦')
    await msg.add_reaction('🇧')
    await msg.add_reaction('🇨')
    await msg.add_reaction('🇩')
    await msg.add_reaction('✖')
    await msg.add_reaction('👋')
    #print(msg.id)

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji

    i=0
    while len(list1)-1 <= 10:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            break
        else:
            
            if str(reaction.emoji) == '👋':
                  if ctx.author.id == user.id:
                    break
                  else:
                    i+=1
                    if(i>=10):
                      await ctx.send("👋で遊ぶな😡")
                    else:
                      await ctx.send("募集開始した人が👋を押すと動作を停止します。こまめに停止させることでbot全体の動作が軽くなります。")    
            
            if msg.id == reaction.message.id:
                if str(reaction.emoji) == '🇦':
                    list1.append(user.name)
                    mem1.append(user.mention)
                    cnt1 -= 1
                    if cnt1 == 0:
                      if check1 == 0:
                        member1 = ' '.join(mem1)
                        await ctx.send("21〆 {}".format(member1))
                        check1 +=1
                   
                if str(reaction.emoji) == '🇧':
                    list2.append(user.name)
                    mem2.append(user.mention)
                    cnt2 -= 1
                    if cnt2 == 0:
                      if check2 == 0:
                        member2 = ' '.join(mem2)
                        await ctx.send("22〆 {}".format(member2))
                        check2 +=1

                if str(reaction.emoji) == '🇨':
                    list3.append(user.name)
                    mem3.append(user.mention)
                    cnt3 -= 1
                    if cnt3 == 0:
                      if check3 == 0:
                        member3 = ' '.join(mem3)
                        await ctx.send("23〆 {}".format(member3))
                        check3 +=1

                if str(reaction.emoji) == '🇩':
                    list4.append(user.name)
                    mem4.append(user.mention)
                    cnt4 -= 1
                    if cnt4 == 0:
                      if check4 == 0:
                        member4 = ' '.join(mem4)
                        await ctx.send("24〆 {}".format(member4))
                        check4 +=1
      
                elif str(reaction.emoji) == '✖':
                    if user.name in list1:
                        list1.remove(user.name)
                        mem1.remove(user.mention)
                        cnt1 += 1
                    if user.name in list2:
                        list2.remove(user.name)
                        mem2.remove(user.mention)
                        cnt2 += 1
                    if user.name in list3:
                        list3.remove(user.name)
                        mem3.remove(user.mention)
                        cnt3 += 1
                    if user.name in list4:
                        list4.remove(user.name)
                        mem4.remove(user.mention)
                        cnt4 += 1        
                    else:
                        pass

        test = discord.Embed(title=about,colour=0x1e90ff)
        test.add_field(name=f"21@{cnt1} ", value=' '.join(list1), inline=False)
        test.add_field(name=f"22@{cnt2} ", value=' '.join(list2), inline=False)
        test.add_field(name=f"23@{cnt3} ", value=' '.join(list3), inline=False)
        test.add_field(name=f"24@{cnt4} ", value=' '.join(list4), inline=False)
        await msg.edit(embed=test)
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)

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

        
@client.command()
async def s2(ctx, about = "交流戦募集 {}".format(datetime.date.today()), cnt1 = 6, settime = 43200):
    cnt1, settime = int(cnt1), float(settime)
    a = ctx.guild.name
    print(a)
    #list.append(0)
    #b = len(list)
    #print(b)
  
    list1 = [">"]
    list2 = [">"]
    list3 = [">"]
    list4 = [">"]
    list5 = [">"]
    list6 = [">"]
    mem1 = []
    mem2 = []
    mem3 = []
    mem4 = []
    mem5 = []
    mem6 = []
    cnt2 = 6
    cnt3 = 6
    cnt4 = 6
    cnt5 = 6
    cnt6 = 6
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    check5 = 0
    check6 = 0
    

    test = discord.Embed(title=about,colour=0x1e90ff)
    test.add_field(name=f"21@{cnt1} ", value=' '.join(list1), inline=False)
    test.add_field(name=f"22@{cnt2} ", value=' '.join(list2), inline=False)
    test.add_field(name=f"23@{cnt3} ", value=' '.join(list3), inline=False)
    test.add_field(name=f"24@{cnt4} ", value=' '.join(list4), inline=False)
    test.add_field(name=f"25@{cnt5} ", value=' '.join(list5), inline=False)
    test.add_field(name=f"26@{cnt6} ", value=' '.join(list6), inline=False)
    msg = await ctx.send(embed=test)
    #投票の欄

    await msg.add_reaction('🇦')
    await msg.add_reaction('🇧')
    await msg.add_reaction('🇨')
    await msg.add_reaction('🇩')
    await msg.add_reaction('🇪')
    await msg.add_reaction('🇫')
    await msg.add_reaction('✖')
    await msg.add_reaction('👋')
    
    #print(msg.id)

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji
    i=0
    while len(list1)-1 <= 10:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            break
        else:
            
            if msg.id == reaction.message.id:
                
                if str(reaction.emoji) == '👋':
                  if ctx.author.id == user.id:
                    break
                  else:
                    i+=1
                    if(i>=10):
                      await ctx.send("👋で遊ぶな😡")
                    else:
                      await ctx.send("募集開始した人が👋を押すと動作を停止します。こまめに停止させることでbot全体の動作が軽くなります。")
                
                if str(reaction.emoji) == '🇦':
                    list1.append(user.name)
                    mem1.append(user.mention)
                    cnt1 -= 1
                    if cnt1 == 0:
                      if check1 == 0:
                        member1 = ' '.join(mem1)
                        await ctx.send("21〆 {}".format(member1))
                        check1 +=1
                   
                if str(reaction.emoji) == '🇧':
                    list2.append(user.name)
                    mem2.append(user.mention)
                    cnt2 -= 1
                    if cnt2 == 0:
                      if check2 == 0:
                        member2 = ' '.join(mem2)
                        await ctx.send("22〆 {}".format(member2))
                        check2 +=1

                if str(reaction.emoji) == '🇨':
                    list3.append(user.name)
                    mem3.append(user.mention)
                    cnt3 -= 1
                    if cnt3 == 0:
                      if check3 == 0:
                        member3 = ' '.join(mem3)
                        await ctx.send("23〆 {}".format(member3))
                        check3 +=1

                if str(reaction.emoji) == '🇩':
                    list4.append(user.name)
                    mem4.append(user.mention)
                    cnt4 -= 1
                    if cnt4 == 0:
                      if check4 == 0:
                        member4 = ' '.join(mem4)
                        await ctx.send("24〆 {}".format(member4))
                        check4 +=1
                        
                if str(reaction.emoji) == '🇪':
                    list5.append(user.name)
                    mem5.append(user.mention)
                    cnt5 -= 1
                    if cnt5 == 0:
                      if check5 == 0:
                        member5 = ' '.join(mem5)
                        await ctx.send("25〆 {}".format(member5))
                        check5 +=1        
                                          
                if str(reaction.emoji) == '🇫':
                    list6.append(user.name)
                    mem6.append(user.mention)
                    cnt6 -= 1
                    if cnt6 == 0:
                      if check6 == 0:
                        member6 = ' '.join(mem6)
                        await ctx.send("26〆 {}".format(member6))
                        check6 +=1                                              
      
                elif str(reaction.emoji) == '✖':
                    if user.name in list1:
                        list1.remove(user.name)
                        mem1.remove(user.mention)
                        cnt1 += 1
                    if user.name in list2:
                        list2.remove(user.name)
                        mem2.remove(user.mention)
                        cnt2 += 1
                    if user.name in list3:
                        list3.remove(user.name)
                        mem3.remove(user.mention)
                        cnt3 += 1
                    if user.name in list4:
                        list4.remove(user.name)
                        mem4.remove(user.mention)
                        cnt4 += 1        
                    if user.name in list5:
                        list5.remove(user.name)
                        mem5.remove(user.mention)
                        cnt5 += 1
                    if user.name in list6:
                        list6.remove(user.name)
                        mem6.remove(user.mention)
                        cnt6 += 1            
                    else:
                        pass

        test = discord.Embed(title=about,colour=0x1e90ff)
        test.add_field(name=f"21@{cnt1} ", value=' '.join(list1), inline=False)
        test.add_field(name=f"22@{cnt2} ", value=' '.join(list2), inline=False)
        test.add_field(name=f"23@{cnt3} ", value=' '.join(list3), inline=False)
        test.add_field(name=f"24@{cnt4} ", value=' '.join(list4), inline=False)
        test.add_field(name=f"25@{cnt5} ", value=' '.join(list5), inline=False)
        test.add_field(name=f"26@{cnt6} ", value=' '.join(list6), inline=False)
        await msg.edit(embed=test)
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)


@client.command()
async def s3(ctx, about = "交流戦募集 {}".format(datetime.date.today()), cnt5 = 6, settime = 43200):
    cnt5, settime = int(cnt5), float(settime)
    a = ctx.guild.name
    print(a)
    #list.append(0)
    #b = len(list)
    #print(b)
  
    list5 = [">"]
    list6 = [">"]
    mem5 = []
    mem6 = []
    cnt5 = 6
    cnt6 = 6
    check5 = 0
    check6 = 0
    

    test = discord.Embed(title=about,colour=0x1e90ff)
    test.add_field(name=f"25@{cnt5} ", value=' '.join(list5), inline=False)
    test.add_field(name=f"26@{cnt6} ", value=' '.join(list6), inline=False)
    msg = await ctx.send(embed=test)
    #投票の欄

    await msg.add_reaction('🇪')
    await msg.add_reaction('🇫')
    await msg.add_reaction('✖')
    await msg.add_reaction('👋')
    
    #print(msg.id)

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji

    i=0
    while len(list5)-1 <= 10:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            break
        else:
            if msg.id == reaction.message.id:

                if str(reaction.emoji) == '👋':
                  if ctx.author.id == user.id:
                    break
                  else:
                    i+=1
                    if(i>=10):
                      await ctx.send("👋で遊ぶな😡")
                    else:
                      await ctx.send("募集開始した人が👋を押すと動作を停止します。こまめに停止させることでbot全体の動作が軽くなります。")
                
                
                if str(reaction.emoji) == '🇪':
                    list5.append(user.name)
                    mem5.append(user.mention)
                    cnt5 -= 1
                    if cnt5 == 0:
                      if check5 == 0:
                        member5 = ' '.join(mem5)
                        await ctx.send("25〆 {}".format(member5))
                        check5 +=1        
                                          
                if str(reaction.emoji) == '🇫':
                    list6.append(user.name)
                    mem6.append(user.mention)
                    cnt6 -= 1
                    if cnt6 == 0:
                      if check6 == 0:
                        member6 = ' '.join(mem6)
                        await ctx.send("26〆 {}".format(member6))
                        check6 +=1                                              
      
                elif str(reaction.emoji) == '✖':          
                    if user.name in list5:
                        list5.remove(user.name)
                        mem5.remove(user.mention)
                        cnt5 += 1
                    if user.name in list6:
                        list6.remove(user.name)
                        mem6.remove(user.mention)
                        cnt6 += 1            
                    else:
                        pass

        test = discord.Embed(title=about,colour=0x1e90ff)       
        test.add_field(name=f"25@{cnt5} ", value=' '.join(list5), inline=False)
        test.add_field(name=f"26@{cnt6} ", value=' '.join(list6), inline=False)
        await msg.edit(embed=test)
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)


token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)
