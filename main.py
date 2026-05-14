from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura o navegador
driver = webdriver.Chrome()

# Acesse seu relatório publicado no Power BI
driver.get("link compartilhavel do dashboard do BI")

#Colocar em tela cheia
driver.fullscreen_window()

# Defina o tempo de exibição por página (em segundos)
tempo_atualizacao = 20

while True:
        try:
            time.sleep(tempo_atualizacao) # Atualizar

            # Verificar se a seta está desativada (última página)
            seta_direita = driver.find_element(By.CSS_SELECTOR, "i.pbi-glyph-chevronrightmedium")
            classes = seta_direita.get_attribute("class")

            if 'inactive' in classes:
                    print("Chegou à última página. Atualizando relatório ...")
                    driver.refresh() #Atualizar o navegador
                    time.sleep(20) #Aguarda recarregar o relatório

            else:
                    # Clica na seta ativa para ir para a próxima página
                    seta_direita.click()

        except Exception as e:
            print("Erro:", e)
            break
