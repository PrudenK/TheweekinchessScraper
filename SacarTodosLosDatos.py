import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request

from utils.UserAgents import user_agents

descargas_dir = os.path.join(os.getcwd(), "descargas")
os.makedirs(descargas_dir, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://theweekinchess.com/twic")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.results-table"))
    )

    filas = driver.find_elements(By.CSS_SELECTOR, "table.results-table tbody tr")

    for fila in filas:
        if "TWIC Date Read PGN CBV Games Stories" not in fila.text and "PGN" in fila.text:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            if len(celdas) >= 4:
                fecha = celdas[1].text.strip()
                enlace_tag = celdas[3].find_element(By.TAG_NAME, "a")
                enlace_zip = enlace_tag.get_attribute("href")
                nombre_archivo = enlace_zip.split("/")[-1]
                ruta_archivo = os.path.join(descargas_dir, nombre_archivo)

                user_agent = random.choice(user_agents)

                print(f"Descargando {nombre_archivo} - Fecha: {fecha} con User-Agent: {user_agent}")

                req = urllib.request.Request(
                    enlace_zip,
                    headers={"User-Agent": user_agent}
                )
                with urllib.request.urlopen(req) as response, open(ruta_archivo, 'wb') as out_file:
                    out_file.write(response.read())

    print("Descargas finalizadas.")
finally:
    driver.quit()
