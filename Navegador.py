import time
import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from webbrowser import Chrome

class Navegador:
    def __init__(self):
        # Cargar variables del archivo .env
        load_dotenv()

        # Obtener las variables de entorno
        CHROMIUM_PATH = os.getenv("CHROMIUM_PATH")
        CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
        PASSWORD = os.getenv("PASSWORD")
        USERNAME = os.getenv("USERNAME")

        # Configurar opciones de Chromium
        options = Options()
        options.binary_location = CHROMIUM_PATH
        options.add_argument("--start-maximized")  # Abre en pantalla completa
        options.add_argument("--disable-infobars")  # Deshabilita banners molestos
        options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detección de bot

        # Iniciar servicio y crear el driver
        service = Service(CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service, options=options)

    def abrir_pagina(self, url):
        """Abre una página web en el navegador."""
        self.driver.get(url)
        time.sleep(5)

    def cerrar(self):
        """Cierra el navegador."""
        time.sleep(5)
        self.driver.quit()
