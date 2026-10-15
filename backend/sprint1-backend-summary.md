
# Sprint 1: Backend Development Summary

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Developer:** Parwana Jafari  
**Sprint:** 1

## Overview

During Sprint 1, I mainly worked on the backend for user signup and login. I connected the frontend forms to Flask and SQLite so users could create accounts and log in to the website.

## Work Completed

### 1. Database

I worked on connecting the Flask backend to the SQLite database.

- Created the `users` table to store user information.
- Created the `listings` table to store clothing listings.
- Connected each listing to the user who created it using `user_id`.
- Made sure the backend could save and retrieve information from the database.

### 2. User Signup

**Route:** `/signup`

I worked on the signup process so new users could register on the website.

- Collected the user's name, email, and password.
- Checked whether the email was already registered.
- Hashed passwords before saving them in the database.
- Saved new user information in the `users` table.
- Returned messages for successful signup or errors.

### 3. User Login

**Route:** `/login`

I also connected the login form to the backend.

- Received the email and password from the login form.
- Checked whether the email existed in the database.
- Verified the entered password against the stored password hash.
- Created a login session when the credentials were correct.
- Returned an error message when the login information was incorrect.
- Redirected users to the homepage after successful login.

### 4. Logout and Page Access

I added logout functionality and worked on controlling access to the selling page.

- Used Flask sessions to keep track of logged-in users.
- Added a logout route to end the session.
- Required users to log in before accessing the Sell page.

## Testing

I tested the signup and login features to check that they worked correctly.

- Tested creating a new account.
- Checked how the system handles an email that is already registered.
- Tested login with correct and incorrect credentials.
- Checked that users could log out.
- Tested access to the Sell page when logged in and logged out.

## Challenges

One challenge was connecting the frontend forms with the Flask backend and making sure the information was handled correctly. I also had to fix some issues while connecting the backend to the database and testing signup and login.

Through this work, I learned more about password hashing, database operations, and managing login sessions in Flask.

## Plans for Sprint 2

In Sprint 2, I planned to continue backend development by working on:

- Search and filtering for clothing listings.
- Retrieving and displaying product information.
- Handling product photo uploads.
- Validating user input and uploaded files.
- Checking the performance of the website.
