from Navegador import Navegador
from selenium.webdriver.common.by import By

# Crear instancia del navegador
bot = Navegador()


# Abrir la página web
bot.abrir_pagina("https://redeem.tcg.pokemon.com/")
input("Presiona Enter para cerrar el navegador...")  
bot.cerrar()