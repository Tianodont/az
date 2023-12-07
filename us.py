import os
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except Exception:
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
import az 


driver = webdriver.Chrome() 
chrome_options = Options()
chrome_options.add_argument("window-size=1200x600")
driver.get("https://math-ege.sdamgia.ru/")


try:
    element = WebDriverWait(driver, 100000).until(
        EC.presence_of_element_located((By.ID, "tophref"))
    )
finally:
    n = driver.page_source
    #inps = driver.find_elements(By.CLASS_NAME, "test_inp")
    ans = az.get_ans(n)
    for i in range(len(ans)):
        print("N"+str(i+1)+" "+ans[i+1])
        #inps[i].send_keys(ans[i+1].split()[0])

input()
