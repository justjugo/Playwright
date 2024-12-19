<h1>Google Search Scraper Script</h1>
<p>This Python script automates the process of scraping Google search results for a query ("hello world") using Playwright. It extracts the titles, descriptions, and URLs of the first 10 search results and saves the data in an Excel file.</p>

<h3>Prerequisites</h3>
<p>Before running the script, ensure you have the following installed on your machine:</p>
<ul>
    <li>Python 3.x</li>
    <li>pip (Python package manager)</li>
</ul>

<h3>Installation Instructions</h3>
<p>Follow these steps to set up and run the script:</p>
<ol>
    <li>
        <strong>Clone or Download the Repository</strong><br>
        Run the following commands in your terminal:
        <pre><code>git clone https://github.com/justjugo/Playwright.git
cd Playwright</code></pre>
    </li>
    <li>
        <strong>Install Dependencies</strong><br>
        <p>Run the following command to install all required dependencies:</p>
        <pre><code>pip install -r requirements.txt</code></pre>
        <p>Or, install them manually:</p>
        <pre><code>pip install playwright pandas openpyxl</code></pre>
        <p>Finally, install browser dependencies required by Playwright:</p>
        <pre><code>python -m playwright install</code></pre>
    </li>
    <li>
        <strong>Run the Script</strong><br>
        <p>Run the script using the following command:</p>
        <pre><code>python script.py</code></pre>
    </li>
    <li>
        <strong>Output</strong><br>
        <ul>
            <li>The script will search for "hello world" on Google.</li>
            <li>It will extract the titles, descriptions, and URLs of the first 10 search results.</li>
            <li>The results will be saved in a file named <code>helloWorldResult.xlsx</code>.</li>
        </ul>
        <p>Once the script runs successfully, you will see the Excel file in the same directory.</p>
    </li>
</ol>

<h2 style="color: red;">Troubleshooting</h2>
<ol>
    <li>
        <strong>Permission Denied Error:</strong><br>
        Ensure the <code>helloWorldResult.xlsx</code> file is closed before running the script. Otherwise, an error will occur.
    </li>
    <li>
        <strong>Playwright Browser Installation Issue:</strong><br>
        Ensure you have run the command:
        <pre><code>python -m playwright install</code></pre>
    </li>
    <li>
        <strong>Google CAPTCHA Issue:</strong><br>
        If Google shows a CAPTCHA or asks you to verify that you're not a robot, you may need to complete the CAPTCHA manually.
    </li>
</ol>
