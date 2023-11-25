# RateGain
<h1 align="center" id="title">Web Scraping Hackathon Solution</h1>
<br>
<p id="description">Welcome to my solution for the web scraping hackathon! In this challenge I developed a program using Python and the Scrapy library to extract specific information from the "https://rategain.com/blog" webpage. The goal was to collect data from various blog posts including blog titles publication dates image URLs and the number of likes each post has received.</p>


<h2>Project Screenshots:</h2>
<br>
<a href="https://ibb.co/YfyQsvd"><img src="https://i.ibb.co/JrytJXp/image.png" alt="image" border="0"></a>
<br>
<a href="https://ibb.co/ZVbBPZc"><img src="https://i.ibb.co/kxP4fdq/image-1.png" alt="image-1" border="0"></a>

<br>
<br>
<h2>🛠️ Setup:</h2>
<br>
<p>1. Before running the program make sure you have the required dependencies installed. You can install them using the following command:</p>

```
pip install scrapy
```

 <br>

<h2>🧐 How the solution Works</h2>
<br>
<p>1. Navigating Through Pages: The program starts by visiting the target URL and navigates through various pages to gather data comprehensively. It uses Scrapy's capabilities for web crawling and scraping.</p>

<p>2. Extracting Information:</p>
<ul>
<li>Blog Title: The program captures the titles of the blog posts.</li>
<li>Blog Date: It retrieves the publication dates of each blog post.</li>
<li>Blog Image URL: The program extracts the URLs of the images associated with the blogs.</li>
<li>Blog Likes Count: It records the number of likes each blog post has received.</li>
</ul>
<br>
<p>3. Data Management:</p>
<ul>
<li>The extracted data is organized and saved efficiently.</li>
<li>The preferred format for storage is CSV for ease of use and compatibility with various analysis tools.</li>
</ul>
<br>
<h2>🚀 Running the solution</h2>
<br>
<p>1. Clone this repository:</p>

```
git clone https://github.com/your-username/hackathon-web-scraping.git
```
<br>
<p>2. Navigate to the project directory:</p>

```
cd hackathon-web-scraping
```
<br>
<p>3. Run the Scrapy spider:</p>

```
scrapy crawl blog_scraper -o output_data.csv
```
<br>
<p>This command will execute the spider and save the extracted data in a CSV file named output_data.csv.</p>

<h2>Results</h2>
<br>
<p>After running the solution, you will have a CSV file (output_data.csv) containing the organized data extracted from the target webpage. This file is ready for further analysis and exploration.

Feel free to reach out if you have any questions or need assistance with the solution. Happy coding!</p>
  
  
<h2>💻 Built with</h2>
<br>
Technologies used in the project:

*   Python
*   Scrapy
*   Visual Studio Code
*   Web Scraping
*   Data Extraction
<br>
<h2>Reference</h2>
<br>
<ul>
<li><a href = "https://docs.scrapy.org/en/latest/">Scrapy</a></li>
<li><a href = "https://rategain.com/blog/">RateGain Blog</a></li>
<li><a href = "https://www.python.org/">Python</a></li>
</ul>

