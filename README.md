# Book_Recommendation

**Overview** 

This project implements a **book recommendation system** using both **content-based** and **popularity-based** filtering approaches. Additionally, a **Flask web application** serves as the frontend for the recommendations. To enhance the dataset, a **web scraping script** is provided to collect book details from the **Goodreads website** using **Selenium**.



**Features**  

1. **Content-Based Filtering**  
   - Recommends books similar to the input based on features such as author,title and description.  
   - Implemented in `content based.ipynb`.

2. **Popularity-Based Filtering**  
   - Recommends the most popular and highly rated books from the dataset.  
   - Implemented in `popularity based.ipynb`.

3. **Web Scraping for Data Enrichment**  
   - `scrap.py` extracts book details from the **Goodreads website** using **Selenium**.  
   - It collects information such as book title, author, description, average rating, and total rating count.  
   - You can customize the script to gather additional relevant data for recommendations.

4. **Flask Web Application**  
   - A simple interactive web interface to access the recommendation engine.  
   - Located in the `flask project/` directory, with `app.py` handling backend logic and HTML templates for the frontend.

**Flow Chart**  

  
![popularity based filtering drawio](https://github.com/user-attachments/assets/bc408dee-6960-4a03-9d5a-e75d0d28283f)
![content based filtering drawio](https://github.com/user-attachments/assets/4db5fa0c-fbeb-4a4d-979d-e1d96a04d119)

**Screenshots**


![Screenshot (45)](https://github.com/user-attachments/assets/35fc6c60-7057-4fdb-b589-dd03e10a242f)


![Screenshot (46)](https://github.com/user-attachments/assets/ab637400-d4b7-4611-ba0c-d1e1c48a99e7)


**Dashboard**


![Book_analysis](https://github.com/user-attachments/assets/fb8980ea-7781-476f-8710-38c4fe309367)
