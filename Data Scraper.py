# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# list of data aquired
all_emails = []
all_org_names = []

# scrapes the inital page list with orgs
def scraper(driver):
    page_orgs = []
    # find elements with <a> tag
    links = driver.find_elements(By.TAG_NAME, 'a')
    for l in links:
   # gts all href with the links that corespond with the format of the orgs
        if  "https://esango.un.org/civilsociety/showProfileDetail.do?method=showProfileDetails&profileCode=" in l.get_attribute("href"):
            page_orgs.append(l.get_attribute("href"))
    return page_orgs

# gets the email and org name
def org_scrape(orgs):
    #gets emails
    for org in orgs:
        driver.get(org)
        a_links = driver.find_elements(By.TAG_NAME, 'a')

        for l in a_links:
            if "@" in l.get_attribute("href"):
                tag = l.get_attribute("href")
                email = tag.replace("mailto:", "")
                all_emails.append(email)
                print(email)
                
    #gets names
        names = (driver.find_element(By.CLASS_NAME, "cso")).text
        all_org_names.append(names)
        print(names)

# instantiate options for Chrome
options = webdriver.ChromeOptions()

# instantiate Chrome WebDriver with options
driver = webdriver.Chrome(options=options)

# open the specified URL in the browser
driver.get("https://esango.un.org/civilsociety/displayConsultativeStatusSearch.do?method=list&show=500&from=list&col=&order=&searchType=csSearch&index=0")
tag = driver.find_element(By.LINK_TEXT, "All organizations in Consultative Status")
tag.click()
driver.get("https://esango.un.org/civilsociety/displayConsultativeStatusSearch.do?method=list&show=6469&from=list&col=&order=&searchType=csSearch&index=0")

org_scrape(scraper(driver))

# csv fiile
csv_filename = "C:\\Users\\marcm\\OneDrive\\Documents\\Database.csv"

# write to 
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    for i in range(len(all_emails)):
        writer.writerow([all_emails[i], all_org_names[i]])

print(all_emails)

# close the browser
driver.quit()