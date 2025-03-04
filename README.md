# IMDb Movie Rating Finder

This project provides a simple **IMDb Movie Rating Finder** using **Python (Flask)** for the backend and **HTML, CSS, and JavaScript** for the frontend. Users can enter a movie name, and the IMDb rating will be fetched and displayed.

---

## Features
- Fetches IMDb movie ratings using the `IMDbPY` library.
- Simple **Flask API** to serve IMDb data.
- A user-friendly frontend built with **HTML, CSS, and JavaScript**.
- Supports **real-time rating lookup**.

## Result
![Alt text](/screenshots/1.png)
![Alt text](/screenshots/2.png)
---

## Prerequisites
Ensure you have **Python 3.x** installed. Then, install dependencies:

```sh
pip install flask flask-cors IMDbPY
```

---

## Running the Backend (Flask API)

1. Navigate to the **app.py** folder:
  
2. Run the Flask server:
   ```sh
   python app.py
   ```
3. The server will start at:
   ```
   http://127.0.0.1:5000/
   ```

---

## Running the Frontend

1. Open `index.html` in a browser.
2. Enter a movie name in the input field.
3. Click "Get Rating" to fetch and display the IMDb rating.

---

## API Endpoint
### **GET /get-rating?movie=MovieName**
Fetches the IMDb rating for a given movie.

**Example Request:**
```sh
http://127.0.0.1:5000/get-rating?movie=Inception
```

**Example Response:**
```json
{
    "title": "Inception",
    "rating": 8.8
}
```



## Future Enhancements
- **Deploy Backend** to AWS, Heroku, or Render.
- **Improve UI** with Bootstrap/Tailwind CSS.
- **Use FastAPI** for better performance.
- **Add More Movie Details** like year, genre, director.




