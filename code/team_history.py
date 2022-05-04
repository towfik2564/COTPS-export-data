from helpers.scraper import Scraper
import csv
import time
import os

output_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\output\\team_history.csv'

with open('code/credential.txt') as f:
    code = f.readline().strip()
    phone = f.readline().strip()
    password = f.readline().strip()
code = code
phone = phone
password = password

scraper = Scraper('https://cotps.com/#/pages/login/login?originSource=userCenter')
scraper.element_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text')
scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-input/div/input', code)
scraper.element_click_by_xpath("//uni-button[contains(text(), 'Confirm')]")
scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input', phone)
scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input', password)
scraper.element_click_by_xpath('//uni-button[contains(text(), "Log in")]')
scraper.element_click_by_xpath('//*[contains(text(), "Mine")]')
scraper.element_click_by_xpath('//*[contains(text(), "Team incomes")]')

while True:
    if scraper.find_element_by_xpath("//uni-button[contains(text(),'More')]", False):
        scraper.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        scraper.element_click_by_xpath("//uni-button[contains(text(),'More')]")
        time.sleep(2)
    else:
        break

elements = scraper.find_elements('uni-view.itemList.list')
team_data = []
for element in elements:
    data = element.split('\n')
    team_data.append(data)

with open(output_path, "r+") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Grade', 'Time', 'Amount'])
    writer.writerows(team_data)
print('Team income history exported successfully')
