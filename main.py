from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
geckodriver_path = "./geckodriver"

service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://example.com/')

time.sleep(2)


def execute_code_from_file(path):
    with open(path, 'r') as file:
        code = file.read()
        exec(code)


while True:
    input("[" + time.strftime("%H:%M:%S") + "] Read file? (Press Enter to continue) ===============================")
    print("===============================================================================")

    try:
        execute_code_from_file('dynamic.py')

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("[" + time.strftime("%H:%M:%S") + " Done!")
        print("===============================================================================")
