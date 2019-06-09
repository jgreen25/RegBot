from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RegBot():
    def __init__(self, username, password, class_id):
        self.username = username
        self.password = password
        self.class_id = class_id
        self.driver = webdriver.Chrome()

    def sign_in(self):
        self.driver.get('https://classschedule.tulane.edu/Search.aspx')
        self.driver.find_element_by_id('ctl00_HeadLoginView_HeadLoginLink').click()
        self.driver.find_element_by_name(
            'ctl00$LoginUser$UserName').send_keys(self.username)
        self.driver.find_element_by_name(
            'ctl00$LoginUser$Password').send_keys(self.password + Keys.ENTER)
        #username_element = self.driver.find_element_by_name('username')
        #password_element = self.driver.find_element_by_name('password')

        #username_element.send_keys(self.username)
        #password_element.send_keys(self.password)
        #password_element.send_keys(Keys.ENTER)

        #self.driver.get('https://gibson.tulane.edu/')
        #self.driver.find_element_by_link_text('Sign In').click()
        return

    def go_to_schedule(self):
        #self.driver.find_element_by_id('layout_7').click()

        #self.driver.find_element_by_partial_link_text(
            #'Schedule of Classes').click()
        self.driver.get('https://classschedule.tulane.edu/Search.aspx')
        return

    def add_class(self):
        #self.driver.get('https://classschedule.tulane.edu/Search.aspx')
        #self.driver.switch_to_window(self.driver.window_handles[1])
        #self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

        self.driver.find_element_by_name('ctl00$MenuContent$ddlterm').click()
        self.driver.find_elements_by_tag_name('option')[1].click()

        course_element = self.driver.find_element_by_name(
            'ctl00$MainContent$tbcourse')
        course_element.send_keys(self.class_id)
        course_element.send_keys(Keys.ENTER)

        #self.driver.find_element_by_id(
            #'ctl00_MainContent_rprResults_ctl03_btnatp').click()
        self.driver.find_element_by_xpath(
            "//button[@class='btnatp JQButtonSmall ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only small-button']").click()
        return
def main():
    bot = RegBot('##########', '############', 'MATH-1110-01')
    bot.sign_in()
    #bot.go_to_schedule()
    #bot.add_class()
    bot.driver.close()
    return

if __name__ == '__main__':
    main()