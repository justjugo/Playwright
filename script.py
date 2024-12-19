from playwright.async_api import async_playwright
import pandas as pd
import logging
import asyncio
import os

#  logging for  error tracking on the terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

async def scrape_google_search():
    try:
        async with async_playwright() as p:
            # Launch the browser 
            logger.info("Launching the browser...")
            browser = await p.chromium.launch(headless=True)  # headless=True to run in the background 
            page = await browser.new_page()

            # Step 1: Open Google
            URL ="https://www.google.com"
            try:

                logger.info("Opening Google...")
                await page.goto(URL,timeout=5000) #try to open the url 
            except Exception as e:
                logger.warning(f"couldnt open the {URL} error: {e}") #raise an exception if the url didnt open
                return #exit if we can reach the url 

            # Step 2: Locat the search box 
            logger.info("Locating the search box...")
            search_box =  page.locator('[name="q"]')
            if not search_box:
                raise Exception("Search box not found") #if in case the bow isnt on the page raise an error
            await search_box.click()

            # Step 3: Type the search query "hello world"
            logger.info("Entering search query: 'hello world'...")
            await search_box.fill("Hello World")

            # Step 4: Press Enter to execute the search
            logger.info("Pressing Enter to execute the search...")
            await search_box.press("Enter")

            # Step 5: Wait for results to load (Wait for a search result to appear)
            logger.info("Waiting for results to load...")
            await page.wait_for_selector('.g')  # Wait for the search result container to be visible

            # Extract the first 10 search results
            logger.info("Extracting the first 10 results...")
            results = []
            for i in range(1, 11):  # Results are usually indexed from 1 to 10
                
                try:
                    title =  page.locator('.LC20lb').nth(i-1)
                
                    description=page.locator('.VwiC3b').nth(i-1)
                   
                    link=page.locator('[jsname="UWckNb"]').nth(i-1)
                   

                    if title and description and link:
                        results.append(
                            {
                                'Title': await title.text_content(),
                                'Description':await description.text_content(),
                                'Link':await link.get_attribute('href')
                            }
                        )
                    else:
                        logger.warning(f"Result {i} is missing some elements (title/description/url). Skipping.")
                except Exception as e:
                    logger.error(f"Error extracting result {i}: {e}")
                        
            #saving the results to an Excel file
            if results:
                logger.info('saving result to Excel file')
                df=pd.DataFrame(results) #convert the list of dictionaries into a structured table
                file_path = 'helloWorldResult.xlsx'
                #Verify if the link Excel file exist and already open 
                if os.path.exists(file_path):
                    try:
                        os.rename(file_path, file_path)
                    except OSError: #if the file is Open then ask to close it 
                        print("The file is currently open. Please close it and try again.")
                        exit(1)
                df.to_excel(file_path, index=False)
               
                logger.info('result saved !')
            else:
                logger.warning('No result extracted ')
            # Close the browser
            await browser.close()
           

    except Exception as e:
        logger.error(f"An error occurred during the scraping process: {e}")
        raise

# Run the async function
if __name__ == "__main__":
    try:
        asyncio.run(scrape_google_search())
    except Exception as e:
        logger.error(f"Script failed with error: {e}")
