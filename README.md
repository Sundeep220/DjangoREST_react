# Twitter Search Engine:


This is an search engine that list out the twitter accounts of all twitter users by taking data from twitter api. This app is made using Django in backend and React
frontend. The backend consists of APIs that return all the twitter users till now present in database. The APIs were made using Django Rest framework. The frontend of 
this application was designed using React. This application has Search functionality through which users can be searched with their usernames.

- Before running this project: Go to cados_api/ folder and then \

  -> Create a virtual environment, in Windows command is as follows: \
    `pythom -m venv env` \
   -> To activate: \
     `env/Scripts/activate`
     
- To run the backend part do the following:

    Pre-requisites: Python, pip and django should be installed in your system. All the coding is done using VScode.
    1. To install the dependencies: \
       `pip install -r requirements.txt` 
    2. Make the migrations:\
        `python manage.py makemigrations` 
    3. Migrate the tables: \
        `python manage.py migrate` 
    4. Create a superuser for your project: \
        `python manage.py createsuperuser`   
        This will prompt you to enter username, email and password for the superuser.  
    5. Run the server using: \
        `python manage.py runserver` \
        
- To run frontend part: \
  
  Pre-requisites: NPM(Node package manager) should be installed in your system. All the coding is done using VScode.
    1. To install the dependencies: \
        `npm i axios` \
        `npm i react-router-dom` 
    2. Run the application: \
        `npm start`
        
        
        
 - #Application Preview:
    
   ![screencapture-localhost-3000-2022-11-16-03_58_45](https://user-images.githubusercontent.com/93663329/202162630-6fd86543-46e3-40b7-929b-56a1b0c13131.png)
