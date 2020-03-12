from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

clist = [[], [], [], [], [], []]
l_strip = ["@everyone 挙手一覧", "21:", "22:", "23:", "24:"]


def listopen():
    print(clist)
    l_sum = ''
    clist_sum = ''

    # 名前を入れる処理

    for i in range(len(clist)):
        for item in clist[i]:
            clist_sum += item + ' '

    for index, item in enumerate(l_strip):
        if clist[index]:
            l_sum += item + clist_sum + '\n'
        else:
            l_sum += item + '\n'
    return l_sum


@bot.command(name="c")
async def can(ctx, arg):
    kyosyu = ctx.message.author.name
    index = int(arg)-20
    print(index)
    clist[index].append(kyosyu)
    await ctx.send(f'{ctx.message.author.name}さんが \n挙手しました\n')


@bot.command(name="l")
async def mogilist(ctx):
    l_sum = listopen()
    await ctx.send(l_sum)


@commands.command()
async def test(ctx):
    await ctx.send("test")


# 取得したトークンを「TOKEN_HERE」の部分に記入
bot.run('token')
