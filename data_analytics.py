from selenium import webdriver
import smtplib


class Covid():
    """Create a Covid class"""

    def __init__(self):
        """Initialize the webdriver for page manage"""
        self.driver = webdriver.Chrome("/Users/igorvologodskiy/bin/chromedriver")

    def get_data(self):
        """Iniatilize a method for getting date"""
        self.driver.get("https://www.worldometers.info/coronavirus/")
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]')
        country = table.find_element_by_xpath('//td[contains(., "Russia")]')
        row = country.find_element_by_xpath('./..')

        data = row.text.split(" ")
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        total_recovered = data[5]
        active_cases = data[6]
        serious_critical = data[7]

        print(f' Всего случаев {total_cases}')
        print(f' Новых случаев {new_cases}')
        print(f' Всего смертей {total_deaths}')
        print(f' Новых смертей {new_deaths}')
        print(f' Всего вылечившихся {total_recovered}')
        print(f' Активных случаев {active_cases}')
        print(f' Тяжелых случаев {serious_critical}')

        send_mail(country.text, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,
                  serious_critical)

        self.driver.close()


def send_mail(country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases,
              serious_critical):
    """Initialize the function for sending e-mail"""

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('muaythay1@yandex.ru', 'Bavaria1996')

    subject = (f'COVID-19 stats in {country}')

    body = 'Today in ' + country + '\
        \nThere is a new data of COVID-19:\
        \nTotal cases: ' + total_cases + '\
        \nNew cases:  ' + new_cases + '\
        \nTotal deaths: ' + total_deaths + '\
        \nNew deaths: ' + new_deaths + '\
        \nTotal recovered: ' + total_recovered + '\
        \nActive cases: ' + active_cases + '\
        \nSerious_critical: ' + serious_critical + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("muaythay1@yandex.ru", "garikvologodskiy@gmail.com", msg)
    print("Message sent")

    server.quit()

func = Covid()
func.get_data()