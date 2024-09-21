from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.nuuvem.com/br-pt')


input = driver.find_element(By.CLASS_NAME, 'header-search-field')

input.send_keys('LEGO')
input.send_keys(Keys.ENTER)

recomendados = []
valor = []
desconto = []
top = []
destaque = []


for i in range(5):
    jogos = driver.find_elements(By.TAG_NAME, 'h3')[i].text + "  " + driver.find_elements(By.TAG_NAME, 'button')[i+4].text
    recomendados.append(jogos)

sleep(1)
driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="catalog"]/div[3]/div[1]/div[1]/div[3]/div/div/a[6]').click()
sleep(1)
for i in range(5):
    jogos = driver.find_elements(By.TAG_NAME, 'h3')[i].text + "  " + driver.find_elements(By.TAG_NAME, 'button')[i+6].text
    valor.append(jogos)


sleep(1)
driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="catalog"]/div[3]/div[1]/div[1]/div[3]/div/div/a[7]').click()
sleep(1)

for i in range(5):
    jogos = driver.find_elements(By.TAG_NAME, 'h3')[i].text + "  " + driver.find_elements(By.TAG_NAME, 'button')[i+6].text
    desconto.append(jogos)


sleep(1)
driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="catalog"]/div[3]/div[1]/div[1]/div[3]/div/div/a[5]').click()
sleep(1)


for i in range(5):
    jogos = driver.find_elements(By.TAG_NAME, 'h3')[i].text + "  " + driver.find_elements(By.TAG_NAME, 'button')[i+6].text
    top.append(jogos)



for i in range(5):
    for j in range(5):
        if recomendados[i] == valor[j]:
            destaque.append(valor[j])


for i in range(5):
    for j in range(5):
        if recomendados[i] == top[j]:
            destaque.append(valor[j])

for i in range(5):
    for j in range(5):
        if recomendados[i] == desconto[j]:
            destaque.append(valor[j])

for i in range(5):
    for j in range(5):
        if top[i] == valor[j]:
            destaque.append(valor[j])

for i in range(5):
    for j in range(5):
        if desconto[i] == valor[j]:
            destaque.append(valor[j])


for i in range(5):
    for j in range(5):
        if desconto[i] == top[j]:
            destaque.append(valor[j])

print("Jogos em destaque, com base em valor, desconto, recomendação e top vendas")
print(destaque)

driver.close()