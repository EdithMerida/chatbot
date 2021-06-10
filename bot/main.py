import discord 
from discord.ext import commands
import datetime
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='.', description = "this is a texting bot")
#token=os.getenv("DISCORD_BOT_TOKEN")

token1= os.environ.get('TOKEN1')
token2= os.environ.get('TOKEN2')
token3= os.environ.get('TOKEN3')

fechaActual = datetime.date.today()
fechaInicio = str(fechaActual)
fechaMes = str(fechaActual - datetime.timedelta(days=30))
fechaSemana = str(fechaActual - datetime.timedelta(days=7))

@bot.command()
async def ping(ctx):
     await ctx.send('pong')

#Visitas y usuarios unicos punto trader 
@bot.command()
async def trader(ctx):   
    
    URLVistasMes = 'http://signum-crm.com/Tracker/Home/getViewTime?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntotrader' #configuramos la url
    dataVistasMes = requests.get(URLVistasMes) 
    dataVistasMes = dataVistasMes.json() #convertimos la respuesta en dict
    datosVistasMes = dataVistasMes["data"]
    
    URLVistasSemana = 'http://signum-crm.com/Tracker/Home/getViewTime?fechainicio='+fechaSemana+'&fechafinal='+fechaInicio+'&site=puntotrader' #configuramos la url
    dataVistasSemana = requests.get(URLVistasSemana) 
    dataVistasSemana = dataVistasSemana.json() #convertimos la respuesta en dict
    datosVistasSemana = dataVistasSemana["data"]

    URLUserMes = 'http://signum-crm.com/Tracker/Home/getUserUnicos?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntotrader' #configuramos la url
    dataUserMes = requests.get(URLUserMes) 
    dataUserMes = dataUserMes.json() #convertimos la respuesta en dict
    datosUserMes = dataUserMes["data"]

    URLUserSemana = 'http://signum-crm.com/Tracker/Home/getUserUnicos?fechainicio='+fechaSemana+'&fechafinal='+fechaInicio+'&site=puntotrader' #configuramos la url
    dataUserSemana = requests.get(URLUserSemana) 
    dataUserSemana = dataUserSemana.json() #convertimos la respuesta en dict
    datosUserSemana = dataUserSemana["data"]
    
    mensaje = "PUNTO TRADER\nVistas mes: " + str(datosVistasMes[0]) + "\nVistas semana:" + str(datosVistasSemana[0]) +"\nUsuarios únicos mes: " +str(datosUserMes)+"\nUsuarios únicos semana: "+str(datosUserSemana)
    await ctx.send(mensaje)

#Visitas y usuarios unicos punto casa de bolsa 
@bot.command()
async def casabolsa(ctx):   
    
    URLVistasMes = 'http://signum-crm.com/Tracker/Home/getViewTime?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntocasadebolsa' #configuramos la url
    dataVistasMes = requests.get(URLVistasMes) 
    dataVistasMes = dataVistasMes.json() #convertimos la respuesta en dict
    datosVistasMes = dataVistasMes["data"]
    
    URLVistasSemana = 'http://signum-crm.com/Tracker/Home/getViewTime?fechainicio='+fechaSemana+'&fechafinal='+fechaInicio+'&site=puntocasadebolsa' #configuramos la url
    dataVistasSemana = requests.get(URLVistasSemana) 
    dataVistasSemana = dataVistasSemana.json() #convertimos la respuesta en dict
    datosVistasSemana = dataVistasSemana["data"]

    URLUserMes = 'http://signum-crm.com/Tracker/Home/getUserUnicos?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntocasadebolsa' #configuramos la url
    dataUserMes = requests.get(URLUserMes) 
    dataUserMes = dataUserMes.json() #convertimos la respuesta en dict
    datosUserMes = dataUserMes["data"]

    URLUserSemana = 'http://signum-crm.com/Tracker/Home/getUserUnicos?fechainicio='+fechaSemana+'&fechafinal='+fechaInicio+'&site=puntocasadebolsa' #configuramos la url
    dataUserSemana = requests.get(URLUserSemana) 
    dataUserSemana = dataUserSemana.json() #convertimos la respuesta en dict
    datosUserSemana = dataUserSemana["data"]
    
    mensaje = "PUNTO CASA DE BOLSA\nVistas mes: " + str(datosVistasMes[0]) + "\nVistas semana:" + str(datosVistasSemana[0]) +"\nUsuarios únicos mes: " +str(datosUserMes)+"\nUsuarios únicos semana: "+str(datosUserSemana)
    await ctx.send(mensaje)

#Trafico redes sociales punto trader
@bot.command()
async def redesTrader(ctx):       
    URLTrader = 'http://signum-crm.com/Tracker/Home/getCountDonup?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntotrader' #configuramos la url
    dataTrader = requests.get(URLTrader) 
    dataTrader = dataTrader.json() #convertimos la respuesta en dict
    datosTrader = dataTrader["data"]   
    dataTrader1 = datosTrader[0]
    mensaje = "TRAFICO DE DATOS POR REDES SOCIALES PUNTO TRADER\nFacebook: " + str(dataTrader1['contadorF'])+"\nGooogle: "+ str(dataTrader1['contadorG'])+"\nInstagram: "+ str(dataTrader1['contadorI'])+"\nLinkendin: "+ str(dataTrader1['contadorLink'])+"\nPortal Socio: "+ str(dataTrader1['contadorPortal'])+"\nPunto trader: "+ str(dataTrader1['contadorPuntotrader'])+"\nPunto casa de bolsa: "+ str(dataTrader1['contadorpunto'])
    await ctx.send(mensaje)


#Trafico redes sociales punto casa de bolsa
@bot.command()
async def redesPCB(ctx):       
    URLTrader = 'http://signum-crm.com/Tracker/Home/getCountDonup?fechainicio='+fechaMes+'&fechafinal='+fechaInicio+'&site=puntocasadebolsa' #configuramos la url
    dataTrader = requests.get(URLTrader) 
    dataTrader = dataTrader.json() #convertimos la respuesta en dict
    datosTrader = dataTrader["data"]   
    dataTrader1 = datosTrader[0]
    mensaje = "TRAFICO DE DATOS POR REDES SOCIALES PUNTO CASA DE BOLSA\nFacebook: " + str(dataTrader1['contadorF'])+"\nGooogle: "+ str(dataTrader1['contadorG'])+"\nInstagram: "+ str(dataTrader1['contadorI'])+"\nLinkendin: "+ str(dataTrader1['contadorLink'])+"\nPortal Socio: "+ str(dataTrader1['contadorPortal'])+"\nPunto trader: "+ str(dataTrader1['contadorPuntotrader'])+"\nPunto casa de bolsa: "+ str(dataTrader1['contadorpunto'])
    await ctx.send(mensaje)

@bot.command()
async def api(ctx):    
    URL = 'http://signum-crm.com/Tracker/Home/getAVg' #configuramos la url
    data = requests.get(URL) 
    data = data.json() #convertimos la respuesta en dict
    datos = data["data"]
    datos1= datos[0]
    mostrar = datos1["numero_de_registros"]
    mensaje = "numero de registros: " + str(mostrar)
    await ctx.send("numero de registros: " + str(mostrar))

    print("Si llegue")

#Token chatbot
bot.run(str(token1)+str(token2)+str(token3))
