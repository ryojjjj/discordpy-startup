# インストールした discord.py を読み込む
import discord
list1 = []
list2 = []
list3 = []
list4 = []

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzAzNTQwOTk1NDkyNjc1NjM0.XqWkqw.upwefzO99UYYaug_Wt81fCKR5tc'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    a = 6-len(list1)
    b = 6-len(list2)
    c = 6-len(list3)
    d = 6-len(list4)
    if message.content == '.s2':
        del list1[:]
        del list2[:]
        del list3[:]
        del list4[:]
        await message.channel.send("@everyone\n21@6 {}\n22@6 {}\n23@6 {}\n24@6 {}\n".format(list1,list2,list3,list4))
    if message.content == '.s':
        del list1[:]
        del list2[:]
        del list3[:]
        del list4[:]
        await message.channel.send("21@6 {}\n22@6 {}\n23@6 {}\n24@6 {}\n".format(list1,list2,list3,list4))
    if message.content == '.re':
        del list1[:]
        del list2[:]
        del list3[:]
        del list4[:]
        await message.channel.send("21@6 {}\n22@6 {}\n23@6 {}\n24@6 {}\n".format(list1,list2,list3,list4))
    if message.content == '.l':
        await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))


    if message.content == 'c21':
        list1.append(message.author.name)
        a = 6-len(list1)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')
    if message.content == 'd21':
        list1.remove(message.author.name)
        a = 6-len(list1)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')


    if message.content == 'c22':
        list2.append(message.author.name)
        b = 6-len(list2)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')
    if message.content == 'd22':
        list2.remove(message.author.name)
        b = 6-len(list2)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')


    if message.content == 'c23':
        list3.append(message.author.name)
        c = 6-len(list3)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')
    if message.content == 'd23':
        list3.remove(message.author.name)
        c = 6-len(list3)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')


    if message.content == 'c24':
        list4.append(message.author.name)
        d = 6-len(list4)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')
    if message.content == 'd24':
        list4.remove(message.author.name)
        d = 6-len(list4)
        #await message.channel.send("21@{} {}\n22@{} {}\n23@{} {}\n24@{} {}\n".format(a,list1,b,list2,c,list3,d,list4,))
        await message.add_reaction('🐟')

    if message.content == '.help':
        await message.channel.send(".s・.s2:募集文\n.l:挙手一覧\n.re:挙手リセット\nc21~24,d21~24:の,へ")
 

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
