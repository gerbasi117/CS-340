# CS-340
CS-340 Final Dashboard and CRUD Python Module

Project Overview

This project consists of a CRUD (Create, Read, Update, Delete) Python module and an interactive Dash dashboard for managing and analyzing animal shelter data. The CRUD module connects to a MongoDB database, enabling efficient data storage and retrieval, while the dashboard provides a user-friendly interface for visualizing and filtering animal records.

The project was designed to meet the client requirements of Grazioso Salvare, a company specializing in rescue and adoption services. By leveraging MongoDB and Dash, we created a scalable and flexible solution for processing and visualizing shelter animal data.

Features and Functionality

CRUD Python Module

Establishes a connection to a MongoDB database.

Provides methods to insert, retrieve, update, and delete animal records.

Implements query filtering to allow users to search by specific attributes (e.g., breed, age, outcome).

Uses pymongo for database interactions.

Dash Dashboard

Connects to the MongoDB database using the CRUD module.

Displays animal data in an interactive table.

Provides filtering options using radio buttons (e.g., Adoption, Transfer, Euthanasia).

Implements data visualizations, such as a pie chart for breed distribution.

Includes an interactive map for geolocation data.

Tools and Technologies Used

1. MongoDB

A NoSQL database used for storing animal records.

Chosen for its flexibility in handling semi-structured data.

Allows efficient querying using find() and aggregation pipelines.

2. Dash (Plotly)

A Python framework for building web applications.

Used to create an interactive dashboard UI.

Supports data visualization through charts and maps.

3. Pymongo

A Python library for interacting with MongoDB.

Used for CRUD operations and retrieving animal records dynamically.

4. Jupyter Notebook & JupyterDash

Facilitates development and testing in an interactive Python environment.

Allows Dash applications to run inside Jupyter Notebooks.

Steps Taken to Complete the Project

Developed the CRUD module:

Established MongoDB connection.

Implemented CRUD operations.

Verified database queries using pymongo.

Created the Dash dashboard:

Connected the UI to the CRUD module.

Implemented interactive filtering and data visualization.

Tested and debugged the system:

Ensured database queries returned correct results.

Verified UI elements displayed expected data.

Documented the project:

Created this README file.

Captured screenshots of working queries and dashboards.

Challenges and Solutions

1. MongoDB Connection Issues

Problem: Encountered connection errors when trying to import data.

Solution: Ensured MongoDB was running and used correct credentials.

2. Incorrect Query Formatting

Problem: Some queries did not return the expected results.

Solution: Debugged syntax errors and verified data structures.

3. Dash Layout Issues

Problem: UI elements were not displaying correctly.

Solution: Adjusted layout settings and used proper Dash components.

Reflection on Computer Science Concepts

Writing Maintainable Code

This project reinforced the importance of writing modular, reusable, and readable code. The CRUD module was designed to be reusable for future projects that require MongoDB integration.

Problem-Solving Approach

As a computer scientist, breaking down the project into manageable components (CRUD, UI, visualization) helped in systematically solving problems.

Real-World Impact

This project demonstrates how data management and visualization can improve decision-making for organizations like Grazioso Salvare, making their rescue operations more efficient.

Submission Instructions

GitHub Repository Link: git@github.com:gerbasi117/CS-340.git

README File: This document

Final Dashboard Code: Submitted as part of Project Two

By completing this project, I gained valuable experience in working with MongoDB, Dash, and data visualization. This knowledge will be useful for future database-driven web applications and analytical dashboards.
