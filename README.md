# Shelf Buddy: Smart Expiry Tracker

### 🔴 Live Demo: [https://shelf-buddy.onrender.com/](https://shelf-buddy.onrender.com/)
---

##  About The Project

I was tired of finding expired food in my pantry and fridge, so I decided to build a solution.

I created **Shelf Buddy**, a free and simple web app that tracks your items and provides accurate shelf-life data from its built-in database. You can use it to manage your food, medicine, and any other perishable items to help reduce waste and save money.

This was a full-stack project for me, and I also configured it with a sitemap and meta tags for Google (SEO).

##  Key Features
*  **Expiry Prediction:** Get accurate shelf-life data based on storage (room temp, refrigerated, or frozen).
*  **Reduce Waste:** Get a clear view of what's expiring soon.
*  **Seamless Deployment** Deployed in free tier of Render
*  **Responsive UI** Clean, mobile-friendly interface built.
  
##  Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask Framework) |
| **Database** | SQLite |
| **Deployment** | Render (Free Tier) |
| **SEO** | Sitemap + Meta Tags for Google Indexing |

##  Project Structure

Here is the folder structure for the Shelf Buddy project:

```text
Shelf_Buddy/
├── app.py                # The main Flask application logic
├── populate_db.py        # Script to create and populate the database
├── database.db           # The SQLite database file
├── Procfile              # Tells Render how to run the app
├── requirements.txt      # List of all Python libraries needed
├── README.md            
│
├── static/
│   ├── style.css         # CSS file 
|   ├── script.js         # JavaScript filw  
│   ├──shelfbuddy.png     # ShelfBuddy Logo and Favicon
|   ├── robots.txt        # Rules for search engine crawlers
│   └── sitemap.xml       # Sitemap for Google
│
└── templates/
    └── main.html         # The main homepage
```

---

##  How To Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PraneethVarma5/Shelf_Buddy.git](https://github.com/PraneethVarma5/Shelf_Buddy.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Shelf_Buddy
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create and populate the database:**
    (This only needs to be run one time)
    ```bash
    python populate_db.py
    ```

5.  **Run the app:**
    ```bash
    python app.py
    ```
    Your app will now be running at `http://127.0.0.1:5000` (or a similar local address).

## Project Images
<img width="1854" height="842" alt="image" src="https://github.com/user-attachments/assets/95de0517-db8c-4411-ba50-f74f1718bf9b" />

---

<div align="center"><img width="372" height="927" alt="image" src="https://github.com/user-attachments/assets/70fd27a5-eaeb-4bc5-b380-62484847b773" /></div>

---

<img width="1701" height="971" alt="image" src="https://github.com/user-attachments/assets/562f899a-556a-4ef5-9fcb-899d2b2c6d2f" />

---

<img width="1698" height="971" alt="image" src="https://github.com/user-attachments/assets/3185e01b-fcd3-49d7-a657-4a2238fc22ff" />

