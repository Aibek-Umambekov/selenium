from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://tutorialsninja.com/demo')


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


def registration():
    driver.get('http://tutorialsninja.com/demo')

    # open registration page
    my_account = driver.find_element(By.CLASS_NAME, 'dropdown')
    my_account.click()
    register = driver.find_element(By.LINK_TEXT, 'Register')
    register.click()

    # filling in the fields
    firstname_input = driver.find_element(By.NAME, 'firstname')
    firstname_input.send_keys('Adam')
    lastname_input = driver.find_element(By.NAME, 'lastname')
    lastname_input.send_keys('Sender')
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys('adam.sender@gmail.com')
    telephone_input = driver.find_element(By.NAME, 'telephone')
    telephone_input.send_keys('+996779454451')

    # enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('Adam000777')
    confirm_input = driver.find_element(By.NAME, 'confirm')
    confirm_input.send_keys('Adam000777')

    # pointing checkbox privacy policy
    agree_checkbox = driver.find_element(By.NAME, 'agree')
    agree_checkbox.click()

    # clicking Continue button
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary')
    submit_button.click()
    print("Test #2 registration is complete! ")


def login():
    pass


registration()
send_product_to_shopping_cart()
driver.close()
