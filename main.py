import discord
import os
import random

client = discord.Client()
case_insensitive = True

@client.event
async def on_ready():
  print("We have woken up {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.lower().startswith("((flute noises))"):
    latency = client.latency
    await message.channel.send("I have arrived in " + str(int(latency*1000)) + "ms")
  if message.content.lower().startswith("hi ghost baby"):
    await message.channel.send("Hi there, what do you need?\n- For food or formulas, include a question mark after the name\n- To calculate, say 'Calculate [--]'\n- You can also try 'flip a coin' or 'pick a/[#] number(s) between [-] and [-]'")
  if message.content.lower().startswith("thank you ghost baby") or message.content.lower().startswith("thank you wen ning"):
    await message.channel.send(":)")
  #hello message^

  if message.content.lower().startswith("calculate"):
    ans = eval(message.content[10:])
    await message.channel.send(ans)
  if "law of cosines?" in message.content.lower():
    await message.channel.send("a² = b² + c² - 2bc ⋅ cos(A)\nb² = a² + c² - 2ac ⋅ cos(B)\nc² = a² + b² - 2ab ⋅ cos(C)")
  if "law of sines?" in message.content.lower():
    await message.channel.send("_ _ __   a    __     __   b   __     __   c   __\n  sin A = sin B = sin C")
  if "quadratic formula?" in message.content.lower():
    await message.channel.send("_ _    __-b ± √b² - 4ac__\nx =          2a")
  if message.content.lower().startswith("flip a coin"):
    coinFlip = ["Heads", "Tails"]
    await message.channel.send(random.choice(coinFlip))
  if message.content.lower().startswith("pick a number between"):
    randomNumber = []
    ranges = []
    for i in range(22, len(message.content)):
      if message.content[i] == " ":
        ranges.append(i)
        ranges.append(i+5)
        break
    number1 = int(message.content[22:ranges[0]])
    number2 = int(message.content[ranges[1]:len(message.content)])
    for x in range(number1,number2+1):
      randomNumber.append(x)
    await message.channel.send(random.choice(randomNumber))
  if "numbers between" in message.content.lower():
    randomNumber = []
    range1 = 0
    range2 = 0
    range3 = 0
    for i in range(10, len(message.content)):
      if message.content[i].lower() == "w":
        range1 = i+5
        for j in range(i+5, len(message.content)):
          if message.content[j] == " ":
            range2 = j
            range3 = j+5
            break
    number1 = int(message.content[range1:range2])
    number2 = int(message.content[range3:len(message.content)])
    for x in range(number1, number2+1):
      randomNumber.append(x)
    multiplier = 0
    for i in range(5, len(message.content)):
      if message.content[i] == " ":
        multiplier = int(message.content[5:i])
        break
    multiNumbers = ""
    for k in range(0, multiplier):
      multiNumbers += str(random.choice(randomNumber)) + "\n"
    await message.channel.send(multiNumbers)
  #utilities^

  if message.content.lower().startswith("wifi top"):
    await message.channel.send("for the love of archons please no")
    await message.author.send("don't")
  if message.content.lower().startswith("wen ning come here"):
    await message.author.send("hello")
  if ":(" in message.content.lower():
    await message.channel.send("do you want some sand? :sandwich:")
  if "sand?" in message.content.lower():
    await message.channel.send("here :sandwich:")
  if "tea?" in message.content.lower():
    await message.channel.send("here :tea:")
  if "soup?" in message.content.lower():
    await message.channel.send("here, lotus soup :fondue:")
  if "boba?" in message.content.lower():
    await message.channel.send("here :bubble_tea:")
  if "granpa?" in message.content.lower():
    granpaGifs = [
      "https://tenor.com/view/zhongli-genshinimpact-genshin-impact-geo-gif-19792555", "https://tenor.com/view/zhongli-genshin-genshinimpact-rexlapis-gif-20201008", "https://media.discordapp.net/attachments/752691321914785812/814264876347162655/tumblr_647229e6af33d9ef9f801ba0ea74ad02_96203a12_400.gif", "https://media.discordapp.net/attachments/752691321914785812/814264942383464498/tumblr_7fd98a850266d1e42ef5cc345f6e7faa_43f41922_540.gif", "https://media.discordapp.net/attachments/752691321914785812/814265020757704744/tumblr_110f8a8325726426130e7369ccf55556_9a6f165b_400.gif", "https://media.discordapp.net/attachments/752691321914785812/814265047277633536/tumblr_1ea224e26c8271e166ee23fef4f93f1f_d33bb36b_400.gif", "https://images-ext-2.discordapp.net/external/-WsjjENF1pOLYjkAcqLJHqnILyEhB-LOtDGGRvjXvuI/https/media.discordapp.net/attachments/752691321914785812/814264876347162655/tumblr_647229e6af33d9ef9f801ba0ea74ad02_96203a12_400.gif", "https://media.giphy.com/media/B5IiupjI0G1vukbE0y/giphy.gif", "https://tenor.com/view/zhongli-vago-mundo-genshin-impact-gif-19392382"]
    await message.channel.send(random.choice(granpaGifs))
  if "khun?" in message.content.lower():
    khunPics = ["https://i.pinimg.com/originals/94/e4/04/94e404faffb4d368d8ac79a2edbc0491.jpg", "https://media.discordapp.net/attachments/803731087150153780/814271467902468146/39f54c505fac33d00567b07b649e780130ba74f1.png", "https://media.discordapp.net/attachments/803731087150153780/814271523362832394/4ba5f08c781c06f630084c34c60646389ec16db6.png", "https://media.discordapp.net/attachments/803731087150153780/814271555571154978/e789e2465207ce57d2572edce8d6d7fb.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814271678934679562/e4569e3c6f59b8798bb4720a86eef864.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814271724509462528/62f906c040906d667eaae5cccb2eeb1c.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814271794281971772/3ac456036b5edd178d1c134027e2b840.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814271909289132032/eb221442bb591fb7a39d5a7a0257c98d.png", "https://media.discordapp.net/attachments/803731087150153780/814272009222619186/95a757ed121b437e65195672b2277a24.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814272146179358740/ceaeabc82c3d4b64add5f19887d1e51c476b7a06.png?width=663&height=663", "https://media.discordapp.net/attachments/803731087150153780/814272186542063626/original.png?width=1028&height=662"]
    await message.channel.send(random.choice(khunPics))
client.run(os.getenv("TOKEN"))