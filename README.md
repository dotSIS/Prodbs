<div class="info">
    <p align='center'>
        <img src="https://raw.githubusercontent.com/dotSIS/Prodbs/main/frontend/src/assets/logo.svg">
    </p>
</div>

# Prodbs
Prodbs Analytics: A Web Application for Online Product Bundles and Reviews Utilizing Market Basket and Sentiment Analysis.

## Requirements
Click the links for the instructions on how to install each of the requirements on your machine.
- [`Git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [`Python`](https://www.python.org/downloads/)
- [`PIP`](https://pip.pypa.io/en/stable/installation/)
- [`DJango`](https://www.djangoproject.com/download/)
- [`NodeJS`](https://nodejs.org/en/download)
- [`VueJS`](https://cli.vuejs.org/guide/installation.html)
## Clone
- `git clone https://github.com/dotSIS/Prodbs.git`
## Installation & Deployment
  ### Frontend
  - `cd Prodbs/frontend`
  - `npm install`
    #### For development
    - `npm run serve`
    - `open http://localhost:8080 on your browser`
    #### For deployment
    - `npm run build`
    - `open http://localhost:8080 on your browser`
  ### Backend
  - `cd Prodbs/backbone`
  - `source env\bin\activate`
  - `pip install -r requirements.txt`
  - `cd prodbs`
    #### Local Host
    - `python manage.py runserver`
    #### Over the network
    - `python manage.py runserver 0.0.0.0:8000`