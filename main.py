from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random

search_text = input("what to look for on Wikipedia (enter your search term): ")

browser = webdriver.Chrome()
url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
browser.get(url)
assert "Википедия" in browser.title
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search_text)
search_box.send_keys(Keys.RETURN)

try:
    links = browser.find_elements(By.TAG_NAME, "a")
    matching_links = [link for link in links if search_text.lower() in link.text.lower()]
    if matching_links:
        matching_links[0].click()
    else:
        print("No matching links found")
        browser.quit()
        exit()

except Exception as e:
    print(f"Error: {e}")
    browser.quit()
    exit()

while True:

    print("1. Scroll through paragraphs of the current article")
    print("2. Go to one of the related pages")
    print("3. Exit the program")
    action = input("Select an action (1, 2 or 3): ")

    if action == "1":
        print("Scrolling through paragraphs...")
        try:
            paragraphs = browser.find_elements(By.TAG_NAME, "p")

            for paragraph in paragraphs:
                print(paragraph.text)
                next_action = input("Press Enter to next paragraph or q to exit: ")
                if next_action == "q":
                    print("\n")
                    break
            else:
                print("End of the article.\n")

        except Exception as e:
            # print(f"Error: {e}")
            print("Paragraphs not found\n")

    elif action == "2":
        print("Going to one of the related pages...")
        try:
            related_pages = browser.find_elements(By.TAG_NAME, "a")
            random_link = random.choice(related_pages).get_attribute("href")
            browser.get(random_link)

        except Exception as e:
            # print(f"Error: {e}")
            print("No related pages found")

    elif action == "3":
        print("Exiting the program...")
        break
    else:
        print("Wrong input, try again\n")

browser.quit()
