
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_book_details(url):
    try:
        # Set up Selenium WebDriver with options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome( )

        # Open the URL
        driver.get(url)

        # Wait for the main content to load
        wait = WebDriverWait(driver, 2)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".BookPageTitleSection__title")))

        # Extract book details
        book_details = {}

        # Title
        title_element = driver.find_element(By.CSS_SELECTOR, ".BookPageTitleSection__title .Text__title1")
        book_details['title'] = title_element.text.strip()

        # Author
        try:
            author_element = driver.find_element(By.CSS_SELECTOR, ".ContributorLink__name")
            book_details['author'] = author_element.text.strip()
        except Exception as e:
            pass

        # Description
        try:
            description_element = driver.find_element(By.CSS_SELECTOR, ".DetailsLayoutRightParagraph .Formatted")
            book_details['description'] = description_element.text.strip()
        except Exception as e:
            pass

        # Image URL
        try:
            image_element = driver.find_element(By.CSS_SELECTOR, ".BookCover img")
            book_details['image'] = image_element.get_attribute("src")
        except Exception as e:
            pass

        # Average Rating
        try:
            average_rating_element = driver.find_element(By.CSS_SELECTOR, ".RatingStatistics__rating")
            book_details['average_rating'] = average_rating_element.text.strip()
        except Exception as e:
            pass

        # Total Rating Count
        try:
            rating_count_element = driver.find_element(By.CSS_SELECTOR, ".RatingStatistics__meta span[data-testid='ratingsCount']")
            book_details['rating_count'] = rating_count_element.text.strip().split()[0]
        except Exception as e:
            pass

        return book_details

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

    finally:
        # Close the driver
        driver.quit()

def scrape_shelf_page(url, output_file):
    try:
        # Start a Selenium webdriver
        driver = webdriver.Chrome()

        # Open the URL
        driver.get(url)

        # Find all parent elements containing the left-aligned images
        parent_elements = driver.find_elements(By.CLASS_NAME, 'leftAlignedImage')

        print(f"Found {len(parent_elements)} parent elements")  # Debugging line

        # Extract href attributes
        hrefs = []
        for index, parent in enumerate(parent_elements):
            if index == 50:  # Limit to the first 50 elements
                break
            try:
                href = parent.find_element(By.XPATH, '..').find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                hrefs.append(href)
            except Exception as e:
                print(f"Exception occurred while extracting href: {str(e)}")

        print(f"Extracted {len(hrefs)} href attributes")  # Debugging line

        # Scrape book details for each href link
        with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'author', 'description', 'image', 'average_rating', 'rating_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for href in hrefs:
                book_details = scrape_book_details(href)
                if book_details:
                    writer.writerow(book_details)

    except Exception as e:
        print(f"Exception occurred: {str(e)}")

    finally:
        # Close the webdriver
        driver.quit()

if __name__ == "__main__":
    # URL of the shelf
    shelf_url = "https://www.goodreads.com/shelf/show/greece"

    # Output file path
    output_file = "Book_Details.csv"

    # Scrape shelf page and append book details to CSV file
    scrape_shelf_page(shelf_url, output_file)





