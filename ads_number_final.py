import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
#from proxies import ProxyV6Manager



#proxy nuevo
username = 'spjgsbjcg4'
password = '42wsTn=v9HqBr6cdTb'
proxy = f"http://{username}:{password}@gate.smartproxy.com:10001"

# Opciones de Chrome
options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--disable-accelerated-2d-canvas")
options.add_argument("--disable-accelerated-video-decode")
options.add_argument("--use-gl=swiftshader")


options.add_argument('--lang=en')
options.add_argument(f'--proxy-server={proxy}')

# Iniciar el navegador con las opciones configuradas
driver = webdriver.Chrome(options=options)



def close_driver(driver):
    driver.quit()

def get_ads_number(url):
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

        close_driver(driver)   

    except Exception as e:
        print(f"❌ Se produjo un error: {e}")
        return 0

if __name__ == '__main__':
    query="https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&source=page-transparency-widget&view_all_page_id=194709120392912"
    numero_anuncios = get_ads_number(query)
    close_driver(driver)