class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def open(self):
        print(f'Открываю {self.base_url}')


class LoginPage(BasePage):
    def login(self, username, password):
        print(f'Логинимся под {username}')

class HomePage(LoginPage):
    def logout(self):
        print(f'Выходим из системы')

home = HomePage("testik.com")
home.login('Иван', 'Губерниев')
home.open()
home.logout()