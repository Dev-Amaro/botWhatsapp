from os import write
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando o robô prepare o seu celular para escania o qrcode..")

arq = open("mensagem.txt","w")
workbook = xlrd.open_workbook("C:\\Users\\Jefferson Herbert\\Documents\\contatos.xls")
sheet = workbook.sheet_by_name('Planilha1')
rows = sheet.nrows
coluns = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")


driver = webdriver.Chrome('C:\\Users\\Jefferson Herbert\\Desktop\\chromedriver.exe', options=options)
driver.get('https://web.whatsapp.com/')
time.sleep(8)

for contatos in range(0, rows):
     x = sheet.cell_value(contatos, 0)
     pesquisar = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
     time.sleep(1)
     pesquisar.clear()
     time.sleep(1)
     pesquisar.send_keys(x)
     time.sleep(1)
     pesquisar.send_keys(keys.Keys.ENTER)
     time.sleep(1)
     mensagem = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
     time.sleep(1)
     mensagem.send_keys("Olá eu sou um bot de Whatsapp desenvolvido por João Guilherme")
     time.sleep(1)
     mensagem.send_keys(keys.Keys.ENTER)
     texto = "Mensagem enviada com sucesso para: %s\n" %x
     arq.write(texto)

print("Criamos uma lista de mensagens enviadas com sucesso em: mensagem.txt")
arq.close()
driver.close()