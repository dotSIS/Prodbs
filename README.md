# Prodbs
Prodbs Analytics: A Web Application for Online Product Bundles and Reviews Utilizing Market Basket and Sentiment Analysis.

## Clone
- `git clone https://github.com/dotSIS/Prodbs.git`
# FRONTEND
## Requirements
- `nodejs`
- `npm`
## Installation
- `npm install -g @vue/cli`
- `npm install -g json-server`

- `cd Prodbs/frontend`
- `npm install`
  #### For development
  - `npm run serve`
  - `open http://localhost:8080`
  #### For deployment
  - `npm run build`
  - `open http://localhost:8080`
# BACKEND
  - `cd Prodbs/backbone`
  - `python env\Scripts\activate`
  - `cd prodbs`
  ## Over the network
  - `python manage.py runserver 0.0.0.0:8000`
  ## Local Host
  - `python manage.py runserver`
  ## API call E.g.
  - `http://localhost:8000/products` for getting all the products
  - `http://localhost:8000/products/<id>` for getting specific the product
  - `http://localhost:8000/products` 
     E.g. POST REQUEST
     
    - ` {
        "id": "221ys",
        "brand": "Esse sit possimus",
        "category": "Iure facere labore q",
        "asin": "Magni aut sapiente a",
        "modelNumber": 405,
        "productURL": "Quia sint ex quia te",
        "spec": "Non cupidatat aut ad",
        "technicalDetails": "Voluptate voluptatum",
        "about": "Nemo quo corporis re",
        "price": 705.0,
        "sellerID": "221x"
     }`
    ### Sentiment Analysis for specific product   
  - `http://localhost:8000/analizeproductreviews/?product=221ys` by default it will just response list of sentiment
  - `http://localhost:8000/analizeproductreviews/?product=221ys&autosave=true` by adding autosave=true, it will response and save the sentiment
