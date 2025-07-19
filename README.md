Price Prediction of Non-Residential Properties in Kazakhstan

Author’s Note
--------
This project was my diploma work and marked my first real experience combining Machine Learning and Django.

Previously, I worked as a Django backend developer, but during my studies, I became deeply interested in Machine Learning. 

This project was a bridge between my backend expertise and my new ML skills, allowing me to deploy an ML model into production for the first time.

Overview
--------
This project predicts the price of non-residential properties in Kazakhstan based on various features (location, area, property type, etc.).

It is based on real-world data parsed from krysha.kz. After data preprocessing and feature engineering, a machine learning model was trained using TensorFlow and Scikit-learn.

The model is deployed as a Django web application, allowing users to input property details and get a real-time price prediction.

Key Features
------------
- Scraped & cleaned property data from krysha.kz
- Trained a price prediction model with TensorFlow & Scikit-learn
- Built a REST API and web UI with Django
- Real-time predictions for user input
- Scalable, modular design for future improvements

Tech Stack
----------
- Python 3.8+
- TensorFlow – Deep learning model for regression
- Scikit-learn – Feature preprocessing & baseline ML models
- Pandas & NumPy – Data cleaning & feature engineering
- Django – Web framework for deployment
- SQLite (optional) – Django backend database

Installation & Setup
--------------------
1. Clone the repo
   git clone https://github.com/yourusername/price-prediction-kz.git
   cd price-prediction-kz

2. Create a virtual environment & install dependencies
   python -m venv venv
   source venv/bin/activate  # on Mac/Linux
   venv\Scripts\activate   # on Windows
   pip install -r requirements.txt

3. Run migrations & start Django server
   cd webapp
   python manage.py migrate
   python manage.py runserver

4. Access the web app
   Open http://127.0.0.1:8000/

How the Model Works
-------------------
1. Data Collection
   - Parsed non-residential property listings from krysha.kz
   - Extracted features: location, total_area, property_type, floor, year_built, etc.

2. Preprocessing & Feature Engineering
   - Handled missing values
   - Encoded categorical features
   - Normalized numerical features

3. Model Training
   - Baseline: Linear Regression, RandomForestRegressor (Scikit-learn)
   - Final model: Deep Neural Network (TensorFlow)

4. Deployment
   - Saved model with joblib/tf.saved_model
   - Integrated into Django view for live predictions

Future Improvements
-------------------
- Add map-based visualization
- Implement geospatial features (distance to city center, etc.)
- Support more property types
- Deploy on Heroku / AWS / Docker

Author
------
Sanzhar Karibay
Email: your.email@example.com
LinkedIn: https://linkedin.com/in/yourprofile
GitHub: https://github.com/yourusername
