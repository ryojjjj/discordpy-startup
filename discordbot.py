import discord
import datetime
import os

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

    i=1
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
    await msg2.add_reaction('🥺')
    
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
    #print(msg.id)

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji

    while len(list1)-1 <= 10:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            break
        else:
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
    #print(msg.id)

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji

    while len(list5)-1 <= 10:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            break
        else:
            if msg.id == reaction.message.id:

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


@client.command()
async def fish(ctx2, about = "🐟🐟🐟 使い方 🐟🐟🐟", cnt = 6, settime = 43200):
  help1 = discord.Embed(title=about,color=0xe74c3c,description=".s,.s2,.s3: 交流戦募集開始※12時間で停止\n英語スタンプ: 挙手\n×スタンプ: 挙手全へ\n.rec: 募集開始(.rec 募集名 人数 制限時間(分))\n※募集開始した人の🥺スタンプで募集終了")
  await ctx2.send(embed=help1)
   

token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)
