# Matter-soen341projectW2024

## Table of Contents

- [Project Description](#project-description)
- [Team Members and Roles](#team-members-and-roles)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [More Information](#more-information)

## Project Description 

Our project, a cutting-edge Car Rental Platform, aims to revolutionize the way users rent cars for
personal use. By leveraging the latest web technologies, we offer a seamless, intuitive, and comprehensive car
rental experience. Users can effortlessly browse a wide selection of vehicles, read detailed reviews from previous
customers, and choose the perfect car that suits their needs and preferences. Our secure and straightforward
payment process ensures a hassle-free rental experience from start to finish.

## Team Members and Roles

**Front end :** <br>
- Cristina Trofimov 
- Jackson Amirthalingam
- Julia Trinh

**Back end :**<br>
- Leiticia Taleb
- André Assaad
- Antoine Mansour

For more details on our members, please visit our [Wiki](https://github.com/cristina-trofimov/Matter-soen341projectW2024/wiki) page

## Getting Started

### Prerequisites

- Python (3.x is recommended)
- Node.js and npm
- Git

### Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cristina-trofimov/Matter-soen341projectW2024.git
   cd project-name
   ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Django Backend Dependencies:**
   As of Sprint 1, the requirements.txt file is not finalized, but the current version of the file has been   uploaded to Sprint 1. 

    Now, navigate to the project root and install the required Python packages for the Django backend          using the following command:
   ```bash
   pip install -r requirements.txt
   pip install django
   pip install djangorestframework
   pip install pillow
   pip install djoser
   pip install django-cors-headers
   ```

5. **Install Vue.js Frontend Dependencies:**
   
   Move to the `frontend` directory and install the necessary Node.js packages for the Vue.js frontend:
   ```bash
   cd frontend
   npm install
   npm install axios
   npm install bulma
   ```

### Setting Up the Django Backend

Once the dependencies are installed, you can proceed with setting up the Django backend:

1. **Apply Database Migrations:**
   
   In the project root, run the following command to apply migrations and create the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a Superuser (Optional):**
   
   If you want to create a superuser for the Django admin interface, type the following command:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**
   
   Once everything is correctly set up, you can launch the Django development server:
   ```bash
   python manage.py runserver
   ```
   The Django backend will be accessible at [http://localhost:8000/](http://localhost:8000/).

### Setting Up the Vue.js Frontend

Once the Django installation is complete, let's set up the Vue.js frontend:

1. **Start the Vue.js Development Server:**
   
   In the project’s`frontend` directory, run the following command to start the Vue.js development server:
   ```bash
   cd frontend
   npm run serve
   ```
   The Vue.js frontend will be available at [http://localhost:8080/](http://localhost:8080/).

3. **Connect to the Django Backend:**
   
   Update the API endpoint in the Vue.js code to point to your Django backend. 

Once you are done with all these steps, you can now open you browser and go to the following URL [http://localhost:8080/](http://localhost:8080/) to explore the project!

## More information 

For more information on our project, please visit our [Wiki](https://github.com/cristina-trofimov/Matter-soen341projectW2024/wiki) page





---
