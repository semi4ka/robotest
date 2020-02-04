import selenium as se

options = se.webdriver.ChromeOptions()
options.add_argument('headless')

driver = se.webdriver.Chrome(chrome_options=options)