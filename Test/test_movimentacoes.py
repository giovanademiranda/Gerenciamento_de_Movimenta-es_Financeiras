import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test_adicionar_movimentacao_credito(browser):
    browser.get("https://seubarriga.wcaquino.me/login")

    login_field = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "email")))
    password_field = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "senha")))
    login_field.send_keys("giovana@exemplo.com")
    password_field.send_keys("teste123")

    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    browser.get("https://seubarriga.wcaquino.me/movimentacao")

    data_transacao_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "data_transacao")))
    data_transacao_input.send_keys("10/05/2024")

    data_pagamento_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "data_pagamento")))
    data_pagamento_input.send_keys("10/05/2024")

    descricao_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "descricao")))
    descricao_input.send_keys("Mesada")

    interessado_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "interessado")))
    interessado_input.send_keys("Giovana")

    valor_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "valor")))
    valor_input.send_keys("100")

    save_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()

    browser.get("https://seubarriga.wcaquino.me/extrato")

    tabela = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "tabelaExtrato")))
    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")

        if len(colunas) > 3 and colunas[3].text == "100.00":
            assert True, "Encontrado uma linha com o valor 100.00"
            break
    else:
        assert False, "Não foi encontrado uma linha com o valor 100.00"


def test_adicionar_movimentacao_debito(browser):
    browser.get("https://seubarriga.wcaquino.me/login")

    login_field = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "email")))
    password_field = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "senha")))
    login_field.send_keys("giovana@exemplo.com")
    password_field.send_keys("teste123")

    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    browser.get("https://seubarriga.wcaquino.me/movimentacao")

    select_element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "tipo")))
    select = Select(select_element)
    select.select_by_value("DESP")

    data_transacao_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "data_transacao")))
    data_transacao_input.send_keys("10/05/2024")

    data_pagamento_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "data_pagamento")))
    data_pagamento_input.send_keys("10/05/2024")

    descricao_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "descricao")))
    descricao_input.send_keys("Coxinha")

    interessado_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "interessado")))
    interessado_input.send_keys("Padaria Real")

    valor_input = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.NAME, "valor")))
    valor_input.send_keys("50")

    save_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()

    browser.get("https://seubarriga.wcaquino.me/extrato")

    tabela = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, "tabelaExtrato")))
    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")

        if len(colunas) > 3 and colunas[3].text == "-50.00":
            assert True, "Encontrado uma linha com o valor -50.00"
            break
    else:
        assert False, "Não foi encontrado uma linha com o valor -50.00"