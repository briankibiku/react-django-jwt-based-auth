# Time tracker app

### Simple app to manage your daily tasks making sure you get the best productivity our of your time

## How to run
### The frontend
1. cd to frontend folder
2. run ```npm install``
3. run ```npm start```

Access frontend http://localhost:3000/


### The backend using docker
1. cd to backend folder
2. run ```sudo docker-compose build```
3. run ```sudo docker-compose up```

Access app on http://localhost:8000/
### The backend the normal way
1. run ```pip install -r requirements.txt```
2. cd to backend folder
3. run ```python manage.py migrate```
4. run ```python manage.py createsuperuser```
5. run ```python manage.py runserver```

Access app on http://localhost:8000/

From there open the frontend app on your browser and start updating tasks