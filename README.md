# Diet App

Diet App is a Django-based web application to help users track their food consumption and manage their dietary goals.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Resetting Consumed Calories and Foods](#resetting-consumed-calories-and-foods)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Diet App is designed to assist users in maintaining a healthy lifestyle by tracking their daily food intake and helping them achieve their dietary goals. It provides a user-friendly interface for managing food consumption, setting dietary targets, and visualizing nutritional information.

## Features

Key features of Diet App include:

- **Food Consumption Tracking:** Users can log the foods they consume, including details such as quantity and time.

- **Dietary Goal Management:** Set and manage dietary goals based on specific criteria such as calorie intake, macronutrient distribution, or weight management.

- **User Authentication and Authorization:** Secure user authentication and authorization to ensure privacy and personalized user experiences.

- **Food Details and Nutritional Information:** View detailed information about individual foods, including nutritional values, allergens, and categories.

- **Admin Panel:** Access an admin panel for administrative tasks, such as managing users and viewing system statistics.


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sanjai002/Diet-app.git
   cd Diet-app

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
 
3. **Apply migrations:**

   ```bash
   python manage.py migrate
4. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
Follow the prompts to create an admin user for Django Admin.

5. **Download gpt4all model**
   Download gpt4all model from
   https://spdx.org/licenses/CC-BY-NC-SA-4.0
   and copy it to train folder

## Usage
1. **Run the development server:**

   ```bash
   python manage.py runserver
The project will be accessible at http://localhost:8000/

2. **Access the admin panel:**

Visit http://localhost:8000/admin/
Log in with the superuser credentials created earlier.

Index page: http://localhost:8000/
Food list: http://localhost:8000/food_list/

