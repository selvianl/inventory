 There are 2 branches in this repository. `master` for local installation/usage and `heroku` is running at <br>
 https://inv-tracker-app.herokuapp.com/ domain. Project has REST API support as well and you can find out endpoints from postman collection named `postman_collection.json` file.

## Local Installation

* Go your home directory by typing `cd ~`.

* Create virtual enviroment by running `virtualenv --python=python3 inventory`.

* Clone the project by typing `git clone https://github.com/selvianl/inventory.git`.

* Go in the project directory: `cd inventory`.

* Activate the virtual environment by running `source ~/inventory/bin/activate `.

* Create your own database and change veriable values in `db.sh` and type `source db.sh `.

* Install needed packages by typing `pip install -r requirements.txt `.

* Make migrations and migrate by typing `python manage.py makemigrations && python manage.py migrate `.

* Create Super User by typing `python manage.py createsuperuser `.

* Then run it by typing `python manage.py runserver`


## API Endpoints

* **Create a furniture:** http://127.0.0.1:8000/api/furnitures/ [POST]
* **Retrieve all furnitures:** http://127.0.0.1:8000/api/furnitures/ [GET]
* **Update a furniture:** http://127.0.0.1:8000/api/furnitures/id/ [PUT]
* **Detail a furniture:** http://127.0.0.1:8000/api/furnitures/id/ [GET]
* **Delete a furniture:** http://127.0.0.1:8000/api/furnitures/id/ [DELETE]

* **Create a area:** http://127.0.0.1:8000/api/areas/ [POST]    
* **Retrieve all areas:** http://127.0.0.1:8000/api/areas/ [GET]
* **Update a area:** http://127.0.0.1:8000/api/areas/id/ [PUT]  
* **Detail a area:** http://127.0.0.1:8000/api/areas/id/ [GET]  
* **Delete a area:** http://127.0.0.1:8000/api/areas/id/ [DELETE]  

* **Create a room:** http://127.0.0.1:8000/api/rooms/ [POST]    
* **Retrieve all rooms:** http://127.0.0.1:8000/api/rooms/ [GET]
* **Update a room:** http://127.0.0.1:8000/api/rooms/id/ [PUT]  
* **Detail a room:** http://127.0.0.1:8000/api/rooms/id/ [GET]  
* **Delete a room:** http://127.0.0.1:8000/api/rooms/id/ [DELETE] 

* **Create a building:** http://127.0.0.1:8000/api/buildings/ [POST]     
* **Retrieve all buildings:** http://127.0.0.1:8000/api/buildings/ [GET] 
* **Update a building:** http://127.0.0.1:8000/api/buildings/id/ [PUT]   
* **Detail a building:** http://127.0.0.1:8000/api/buildings/id/ [GET]   
* **Delete a building:** http://127.0.0.1:8000/api/buildings/id/ [DELETE]   
