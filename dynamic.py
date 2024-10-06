from selenium.webdriver.common.by import By
from selenium import webdriver

driver: webdriver

# noinspection PyUnboundLocalVariable
element = driver.find_element(By.TAG_NAME, 'h1')
print("Page heading:", element.text)

elements = driver.find_elements(By.CSS_SELECTOR, 'p')
for idx, el in enumerate(elements):
    print(f"Paragraph {idx + 1}: {el.text}")

# driver.quit()
