# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


# list of data aquired
all_emails = []
all_org_names = []
people = []

# scrapes the inital page list with orgs
def scraper(driver):
    people = []
    # find elements with <a> tag
    links = driver.find_elements(By.TAG_NAME, 'a')
    for l in links:

   # gts all href with the links that corespond with the format of the orgs
        if  "https://www.europarl.europa.eu/meps/en/" in l.get_attribute("href") and len(str(l.get_attribute("href"))) <= len("https://www.europarl.europa.eu/meps/en/256810") and "https://www.europarl.europa.eu/meps/en/" != str(l.get_attribute("href")) and str(l.get_attribute("href")) != "https://www.europarl.europa.eu/meps/en/home":
            people.append(l.get_attribute("href"))
            print(l.get_attribute("href"))
    return people
# gets the email and org name
def org_scrape(orgs):
    for org in orgs: 
        driver.get(org)

        a_links = driver.find_elements(By.TAG_NAME, 'a')
        for l in a_links:
            if "@" in str(l.get_attribute("href")):
                tag = l.get_attribute("href")
                email = tag.replace("mailto:", "")
                all_emails.append(email)
                print(email)

        



# instantiate options for Chrome
options = webdriver.ChromeOptions()

# run the browser in headless mode
options.add_argument("--headless")


# instantiate Chrome WebDriver with options
driver = webdriver.Chrome(options=options)
 
# open the specified URL in the browser
driver.get("hhttps://www.europarl.europa.eu/meps/en/full-list/e")

org_scrape(scraper(driver))

"""
# set how many next the pages has
page_amount = 259
click_count = 0

# loops unitl the end of all pages
while click_count < page_amount:
    # goes to the genral tag or any tag you want
    tag = driver.find_element(By.LINK_TEXT, "All organizations in Consultative Status")
    tag.click()
    
    # clicks the next a certain amount of times
    for reps in range(click_count):
        next = driver.find_element(By.LINK_TEXT, "Next")
        next.click()

    # scrape data
    org_scrape(scraper(driver))
    
    # update next click amount
    click_count += 1

    # goes back to main page to reset
    main_page = driver.find_element(By.LINK_TEXT, "Consultative status")
    main_page.click()
"""
# csv fiile
csv_filename = "C:\\Users\\marcm\\OneDrive\\Documents\\Database.csv"

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(all_emails)):
        writer.writerow([all_emails[i], all_org_names[i]])

print(all_emails)
"""
#keeps the browser open for testing
while True: 
    print(1)
"""
# close the browser
driver.quit()