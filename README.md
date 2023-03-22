# Prodbs
Prodbs Analytics: A Web Application for Online Product Bundles and Reviews Utilizing Market Basket and Sentiment Analysis.

## Clone
- `git clone https://github.com/dotSIS/Prodbs.git`
## Requirements
- `nodejs`
- `django`
## Installation & Deployment
  ### Frontend
  - `cd Prodbs/frontend`
  - `npm install`
    #### For development
    - `npm run serve`
    - `open http://localhost:8080`
    #### For deployment
    - `npm run build`
    - `open http://localhost:8080`
  ### Backend
  - `cd Prodbs/backbone`
  - `python env\Scripts\activate`
  - `pip install -r requirements.txt`
  - `cd prodbs`
    #### Over the network
    - `python manage.py runserver 0.0.0.0:8000`
    #### Local Host
    - `python manage.py runserver`