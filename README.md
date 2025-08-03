#  House Price Prediction App

A simple web application that predicts the price of a house based on user inputs like number of rooms, location, area, etc., using a **Linear Regression** model.

---

##  Features

- Predicts house price based on user input
- Built using Python and Flask
- Trained using a Linear Regression model
- Clean and intuitive web interface

---

##  Prerequisites

Make sure the following are installed:

- Python 3.6 or higher
- pip (Python package manager)

---

##  Installation

### 1. Clone the Repository

```
git clone https://github.com/kanish-20/house-price-predictor.git
cd house-price-predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Train the model (optional)

A pre-trained model (`model.pkl`) is already included. If you want to retrain the model:

```
python train_model.py
```

---

## Running the Application

Start the Flask development server:

```
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How It Works

- The app uses a **Linear Regression** trained on sample data from `House_dataset.csv`.  
- When a user submits how many room they want and then Squarefeet(Area):
- The model predicts a house price.
- The app displays the predicted price.

---

## File Structure
```
house-price-predictor/

├── app.py # Flask web app
├── train_model.py # Script to train and save the model
├── model.pkl # Saved Linear Regression model
├── requirements.txt # Dependencies
├── House_dataset.csv # Dataset used for training
├── templates/
│ └── index.html # Frontend form (HTML)
├── static/
│ └── style.css # (optional) Styling for the form
└── README.md # You're here!
```

---

## Future Improvements

-Add advanced features like location, property type

-Use other models like Ridge, Lasso, ElasticNet for comparison

-Deploy the app on Render or Hugging Face Spaces

-Improve UI with Bootstrap or React

---

## Step-by-Step Guide

Step 1: Input Form
![WhatsApp Image 2025-08-03 at 21 52 51](https://github.com/user-attachments/assets/115f44ca-0b9a-43fa-9525-1ad8cc22bb23)


Step 2: Filled Form
![WhatsApp Image 2025-08-03 at 21 55 15](https://github.com/user-attachments/assets/4d8ba873-0490-490d-840d-7b153de71eac)


Step 3: Prediction Result
![WhatsApp Image 2025-08-03 at 21 57 52](https://github.com/user-attachments/assets/7866ece8-6bfb-4244-b98f-24a3b91a5d07)
