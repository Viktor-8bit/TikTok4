






import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestLoginRegister(unittest.TestCase):
    
# Ткачев Алексей тестируем проверку что пользователь уже в базе и не может зарегистрироваться повторно
    def test_user_reg_test(self):

        driver = webdriver.Chrome()
        driver.get("http://85.209.9.13/reg/")

        login_input = driver.find_element(By.NAME, "Login")

        email_input = driver.find_element(By.NAME, "email")

        password_input = driver.find_element(By.NAME, "password")

        password1_input = driver.find_element(By.NAME, "password1")

        button = driver.find_element(By.NAME, "sumbit")

        login_input.clear()
        email_input.clear()
        password_input.clear()
        password1_input.clear()

        # пользователь есть в базе но мы пытаемся зарегистрироваться его ещё раз
        login_input.send_keys("amogus")

        email_input.send_keys("amogus@mail.ru")

        password_input.send_keys("123456")
        password1_input.send_keys("123456")

        button.click() 

        alert = driver.find_element(By.NAME, "alert") 
        print(alert.text) # пользователь с таким Login существует в базе !
        self.assertEqual(alert.text, 'пользователь с таким Login существует в базе !')

# Павел потехин тестируем повторный ввод пароля
    def test_user_reg_test_password_validation(self):

        driver = webdriver.Chrome()
        driver.get("http://85.209.9.13/reg/")

        login_input = driver.find_element(By.NAME, "Login")

        email_input = driver.find_element(By.NAME, "email")

        password_input = driver.find_element(By.NAME, "password")

        password1_input = driver.find_element(By.NAME, "password1")

        button = driver.find_element(By.NAME, "sumbit")

        login_input.clear()
        email_input.clear()
        password_input.clear()
        password1_input.clear()

        # пользователя нет в базе
        login_input.send_keys("PavelPotehin")

        email_input.send_keys("PavelPotehin@mail.ru")

        # пароли не совпадают
        password_input.send_keys("123456")
        password1_input.send_keys("123456123")

        button.click() 

        alert = driver.find_element(By.NAME, "alert") 
        print(alert.text) # пароли не совпадают
        self.assertEqual(alert.text, 'пароли не совпадают 💢')

# Иван Кожевников тестируем вход в аккаунт 
    def test_user_login(self):
        # тестовый пользователь:
        # Login Ivan
        # Password Kozhevnikov

        driver = webdriver.Chrome()
        driver.get("http://85.209.9.13/login/")

        username = "Ivan"
        password = "Kozhevnikov"

        login_input = driver.find_element(By.NAME, "Login")
        password_input = driver.find_element(By.NAME, "password")
        sumbit_button = driver.find_element(By.NAME, "sumbit")

        login_input.clear()
        password_input.clear()

        login_input.send_keys(username)
        password_input.send_keys(password)

        sumbit_button.click()
        
        usename = driver.find_element(By.NAME, "hello")
        print(usename.text)
        self.assertEqual(usename.text, f"Добро пожаловать {username}")


if __name__ == '__main__':
    unittest.main()
