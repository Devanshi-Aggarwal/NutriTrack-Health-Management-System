# NutriTrack – Health Management System

## Overview

NutriTrack is a Python-based health management system designed to help users monitor and improve their daily lifestyle through data-driven insights. The system allows users to track calorie intake, monitor nutrition, analyze BMI, log workouts, and receive personalized health recommendations.

This project was developed as part of an AI/ML internship evaluation to demonstrate Python programming skills, problem-solving ability, modular code design, and practical application development.

---

## Problem Statement

Maintaining a healthy lifestyle requires tracking multiple factors such as:

* Daily calorie intake
* Nutritional balance
* Physical activity
* Body health metrics

Most people struggle to manually calculate and monitor these regularly. NutriTrack addresses this problem by providing a centralized system for health analytics and daily tracking.

---

## Key Features

### User Profile Management

* Stores user details such as:

  * Name
  * Age
  * Gender
  * Weight
  * Height
  * Fitness Goal

### BMI Analysis

* Calculates Body Mass Index (BMI)
* Categorizes health status into:

  * Underweight
  * Normal Weight
  * Overweight
  * Obese

### Meal Tracking

* Log meals for:

  * Breakfast
  * Lunch
  * Dinner
  * Snacks
* Supports quantity-based food tracking

### Nutrition Analysis

Tracks:

* Total Calories
* Protein Intake
* Carbohydrates
* Fat Consumption

### Food Database

Built-in nutritional database containing common foods with:

* Calories
* Protein
* Carbs
* Fat

### Workout Tracking

Users can log workouts such as:

* Walking
* Running
* Cycling
* Swimming
* Strength Training
* Yoga

System calculates calories burned based on workout duration.

### Health Recommendations

Provides rule-based personalized suggestions based on:

* Calorie intake
* Workout activity
* BMI range
* User fitness goals

---

## Project Structure

```bash
NutriTrack-Health-Management-System/
│
├── main.py
├── validation.py
├── calculations.py
├── food_database.py
├── fitness_database.py
└── README.md
```

### Module Description

#### `main.py`

Controls the complete program flow and user interaction.

#### `validation.py`

Handles all user input validation to ensure safe and correct data entry.

Examples:

* Invalid age detection
* Negative weight prevention
* Incorrect height handling

#### `calculations.py`

Contains all computational logic such as:

* BMI calculation
* Calorie calculation
* Macronutrient calculation
* Health analytics

#### `food_database.py`

Stores nutritional values of food items.

#### `fitness_database.py`

Stores workout data and calories burned per activity.

---

## Technologies Used

* Python
* Functions
* Dictionaries
* Lists
* Conditional Statements
* Loops
* Modular Programming

---

## Core Concepts Demonstrated

This project demonstrates understanding of:

* Data structures
* Functional decomposition
* Input validation
* Modular architecture
* Business logic implementation
* Problem solving

---

## Future Enhancements

Planned future upgrades include:

* Web-based dashboard using HTML/CSS/JavaScript
* Database integration for long-term history tracking
* Weekly and monthly analytics
* AI-powered nutrition recommendations
* User authentication system
* Graph-based visual reports

---

## Prototype UI

A frontend prototype for NutriTrack was also designed to visualize how the application could look as a production-ready health analytics platform with:

* Interactive dashboard
* Nutrition charts
* Workout analytics
* Health reports

---

## Conclusion

NutriTrack is more than a calorie calculator - it is a complete health analytics system that combines nutrition, fitness, and health insights into one platform. The project demonstrates both technical implementation and product-thinking skills, making it a strong example of practical Python application development.
