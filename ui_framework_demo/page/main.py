from selenium.webdriver.common.by import By

from ui_framework_demo.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, 'tv_search').click()
