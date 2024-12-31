from selenium import webdriver

def test_create_record():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    # Lógica para interactuar con la página y validar resultados
    driver.quit()
