import click
from pyautogui import keyDown
from pyautogui import keyUp
from pyautogui import typewrite
from selenium import webdriver
import time


class Flooblecrank:
    """spin up a webdriver for specified profile"""

    def __init__(
        self, profile_dir: str, email: str, pw: str, url: str, cell_id: str,
    ):
        self.profile_dir = profile_dir
        self.email = email
        self.pw = pw
        self.url = url
        self.cell_id = cell_id

    def setup(self):
        profile = webdriver.FirefoxProfile(self.profile_dir)
        self.driver = webdriver.Firefox(profile)

    def run(self):
        self.driver.get(self.url)
        if "Sign in - Google Accounts" in self.driver.title:
            click.echo(self.driver.title)
            self.driver.find_element_by_id("identifierId").send_keys(self.email)
            self.driver.find_element_by_id("identifierNext").click()
            timer = time.time()
            while time.time() - timer < 120:
                try:
                    self.driver.find_element_by_id("password").click()
                    typewrite(self.pw)
                    self.driver.find_element_by_id("passwordNext").click()
                    break
                except:
                    pass
            timer = time.time()
            while time.time() - timer < 120:
                try:
                    assert "teenyverse" in self.driver.title
                    break
                except:
                    pass
        if "teenyverse" in self.driver.title:
            click.echo(self.driver.title)
            timer = time.time()
            while time.time() - timer < 120:
                try:
                    self.driver.find_element_by_id(
                        "cell-{}".format(self.cell_id)
                    ).click()
                    break
                except:
                    pass
            keyDown("shift")
            keyDown("enter")
            keyUp("shift")
            keyUp("enter")

    def teardown(self):
        self.driver.close()
        self.driver.quit()


@click.command()
@click.argument("profile_dir", nargs=1)
@click.argument("email", nargs=1)
@click.argument("pw", nargs=1)
@click.argument("url", nargs=1)
@click.argument("cell_id", nargs=1)
def main(profile_dir: str, email: str, pw: str, url: str, cell_id: str):
    crank = Flooblecrank(profile_dir, email, pw, url, cell_id)
    crank.setup()
    crank.run()
