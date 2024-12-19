<h1>Google Search Scraper Script</h1>
<p>This Python script automates the process of scraping Google search results for a query ("hello world") using Playwright. It extracts the titles, descriptions, and URLs of the first 10 search results and saves the data in an Excel file.</p>
<h3>Prerequisites</h3>
<p>Before running the script, ensure you have the following installed on your machine:</p>
<ul>
    <li>Python 3.X</li>
    <li>pip</li>
</ul>

<h3>Installation Instructions</h3>
<p>Follow these steps to set up and run the script:</p>
<ol>
    <li> Clone or Download the Repository</li>
    <code>git clone https://github.com/justjugo/Playwright.git <br> cd Playwright</code>
    <li>Install Dependencies</li>
    <p>run</p>
    <code>pip install -r requirements.txt </code>
    <p>or install the manually :</p>
    <code>pip install playwright pandas openpyxl    </code>
    <p>install browser dependencies:</p>
    <code>python -m playwright install    </code>

    <li>Run the Script</li>
    <p>just tape the command :</p>
    <code>python script.py</code>

    <li> Output :</li>
    <ul>
        <li>The script will search for "hello world" on Google</li>
        <li>It will extract the titles, descriptions, and URLs of the first 10 search results</li>
        <li>The results will be saved in a file named helloWorldResult.xlsx</li>
    </ul>

    <p>If the script runs successfully, you will see an Excel file with the extracted data in the same directory</p>

</ol>

<h2 style="color: red;">Troubleshooting</h2>
<ol>
    <li>Permission Denied Error:</li>
    <p>make sure that the file helloWorldResult.xlsx  is colsed when runing the script otherwise an error will be raised </p>
    <li>Playwright Browser Installation Issue:</li>
    make sur to run the command 
    <code>python -m playwright install    </code>
    <li>Google Captcha:</li>
    <p>If Google shows a CAPTCHA or asks you to verify that you're not a robot, You may want to consider doing it manually
    </p>
</ol>
