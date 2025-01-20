import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def close_driver(driver):
    driver.quit()

def get_ads_number(driver, url):
    try:
        # Navegar a la URL objetivo
        driver.get(url)

        # Esperar a que los elementos estén presentes con un selector más amplio
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.x8t9es0.x1uxerd5.xrohxju.x108nfp6.xq9mrsl.x1h4wwuj.x117nqv4.xeuugli"))
        )

        element = driver.find_element(By.CSS_SELECTOR, "div.x8t9es0.x1uxerd5.xrohxju.x108nfp6.xq9mrsl.x1h4wwuj.x117nqv4.xeuugli")
        text = element.text.strip()

        # Extraer solo la parte numérica del texto
        numeric_text = text.replace('.', '')
        numeric_text = re.findall(r'\d+', text)
        if numeric_text:
            print(" ".join(numeric_text))
            #return int(numeric_text[0])  # Convertir el primer número encontrado a entero
            full_number = " ".join(numeric_text)
            print(full_number)
            return full_number
       
        else:
            print("No se encontraron números en el texto.")
            return 0   

    except Exception as e:
        print(f"❌ Se produjo un error: {e}")
        return 0