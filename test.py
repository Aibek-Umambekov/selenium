from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def send_product_to_shopping_cart():
    driver.get('http://tutorialsninja.com/demo')

    search_field = driver.find_element(By.NAME, 'search')
    search_field.send_keys('macbook')
    search_field.send_keys(Keys.RETURN)

    # should be normal id not Xpath
    buy_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]')
    buy_btn.click()

    shopping_cart = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
    shopping_cart.click()

    assert 'Product 16' in driver.page_source
    print("Test #1 send_product_to_shopping_cart is complete!")


send_product_to_shopping_cart()
driver.close()
