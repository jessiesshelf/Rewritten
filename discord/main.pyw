import discord; import json; import infoitens;
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="s!", intents=intents)
guild = discord.Object(id=1532353620857716746)

@bot.tree.command(name="info",description="* Checar um item?", guild=guild)
@app_commands.describe(item="Que item checar?", alt="Com quem checar?")
async def checarItem(interaction:discord.Interaction, item:str, alt:str=""):
    _desc = infoitens.InfoCreate(infoitens.ItemGet(item),alt)

    if _desc == "Item não encontrado ou descorberto.":
        await interaction.response.send_message(_desc, silent=True, ephemeral=True)
    else:
        await interaction.response.send_message(_desc, silent=True)

@bot.tree.command(name="listaitem",description="* Cria uma lista de itens", guild=guild)
@app_commands.checks.has_permissions(manage_messages=True)
async def listaCriar(interaction:discord.Interaction, section:str="???", mode:str="Reload"):

    _itemschannel = bot.get_channel(1532937244237627565)
    _path = r'D:\Coders\rewritten\chapter1\messageids.json'
    _list = infoitens.ItemListCreate(section)

    if mode == "Create":
        await interaction.response.defer(ephemeral=True)
        with open(_path) as f:
            ids = json.load(f)

        if ids["itemlist"] == 0:
            _message = await _itemschannel.send(_list)
            ids["itemlist"] = _message.id
            with open(_path, "w") as f:
                json.dump(ids,f,indent=4)
            await interaction.followup.send("Feito.", ephemeral=True)
        else:
            await interaction.followup.send("Já existe uma lista de itens criada para esse capitulo.", silent=True,ephemeral=True)
    elif mode == "Reload":
        with open(_path) as f:
            _ids = json.load(f)
    _message = await _itemschannel.fetch_message(_ids["itemlist"])
    await _message.edit(content=_list)

@bot.tree.command(name="adicionaritem",description="* Adicionar um item?", guild=guild)
@app_commands.checks.has_permissions(administrator=True)
async def itemCriar(interaction:discord.Interaction,name:str,desc:str,alt:bool=False,at:int=0,df:int=0,mg:int=0,pages:int=0,vt:int=0,heal:int=0, iframes:float=0.0, dices:str="", effects:str="",type:str="Weapon", vtype:str="Weapon", disc:bool=False):
    
    infoitens.ItemCreate(name,desc,alt,at,df,mg,pages,vt,heal,iframes,dices,effects,vtype,type,disc)
    await interaction.response.send_message("Feito",ephemeral=True)

@bot.event
async def on_ready():
    print(f"Bot started!")
    await bot.tree.sync(guild=guild)

bot.run('MTUzMjg3NDU1MTcwNzQzOTEzNQ.GyipCg.9KbN66mlDnlVouRxoz5E0Vwuxh6wDrV11eo1-4')