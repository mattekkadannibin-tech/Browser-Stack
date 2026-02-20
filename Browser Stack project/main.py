from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from deep_translator import GoogleTranslator
from collections import Counter
import os

if not os.path.exists("images"):
    os.makedirs("images")

driver = webdriver.Chrome()

driver.get("https://elpais.com/opinion/")
time.sleep(5)

titles_english = []

articles = driver.find_elements(By.CSS_SELECTOR, "article")

print("Found Articles:", len(articles))

for i in range(min(5, len(articles))):

    try:
        articles = driver.find_elements(By.CSS_SELECTOR, "article")
        link = articles[i].find_element(By.TAG_NAME, "a").get_attribute("href")

        driver.get(link)
        time.sleep(4)

        title = driver.find_element(By.TAG_NAME, "h1").text
        print("\nSPANISH TITLE:", title)

        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        content = " ".join([p.text for p in paragraphs[:5]])
        print("CONTENT:", content[:200])

        try:
            img = driver.find_element(By.TAG_NAME, "img").get_attribute("src")
            img_data = requests.get(img).content
            with open(f"images/article_{i+1}.jpg", "wb") as f:
                f.write(img_data)
            print("Image downloaded")
        except:
            print("No image found")

        translated = GoogleTranslator(source='auto', target='en').translate(title)
        titles_english.append(translated)
        print("ENGLISH TITLE:", translated)

        driver.back()
        time.sleep(3)

    except Exception as e:
        print("Error:", e)
        
all_words = " ".join(titles_english).lower().split()
word_count = Counter(all_words)

print("\nWORDS REPEATED MORE THAN TWICE:")
for word, count in word_count.items():
    if count > 2:
        print(word, ":", count)

driver.quit()
