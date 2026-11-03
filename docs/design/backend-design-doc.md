# Backend Design Document

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Prepared By:** Parwana Jafari
**Project Type:** Web-Based Marketplace

---

## Overview

The backend of the Afghan Girls' Pre-Owned Clothes Marketplace handles the main operations of the website. It connects the frontend to the database and processes user requests.

The backend is developed using Python Flask and SQLite. It manages user accounts, authentication, clothing listings, messages, notifications, reports, and admin activities.

This document describes the main backend features, database structure, and technologies used.

---

## 1. User Authentication and Account Management

The backend handles user registration, login, and logout.

**Main Functions:**
- Register new users.
- Check whether an email is already registered.
- Validate login information.
- Store passwords securely using password hashing.
- Manage user sessions.
- Log users out and clear their sessions.

**Security:**
- Passwords are hashed before being stored.
- Protected pages require users to be logged in.
- User access is checked before performing restricted actions.

---

## 2. Password Reset

The backend provides a password reset system through email.

**Main Functions:**
- Receive the user's email address.
- Generate a secure password reset token.
- Send a reset link through email.
- Check whether the reset token is valid.
- Allow users to create a new password.
- Save the new hashed password.

Reset links expire after 15 minutes.

**Technologies:**
- Flask-Mail
- itsdangerous
- Werkzeug password hashing

---

## 3. Clothing Listing Management

The backend manages the creation and storage of clothing listings.

**Main Functions:**
- Receive listing information from the frontend.
- Validate required fields.
- Save listing information in the database.
- Handle uploaded clothing photos.
- Store photo filenames and upload files in the uploads folder.
- Connect each listing to its seller.

**Listing Information Includes:**
- Title
- Category
- Price
- Size
- Condition
- City
- Description
- Photo
- Seller ID
- Listing status

---

## 4. Search and Filtering

The backend retrieves clothing listings based on users' search and filter selections.

**Supported Options:**
- Search by clothing name.
- Filter by category.
- Filter by size.
- Filter by maximum price.
- Filter by condition.
- Filter by city.
- Sort listings by price or upload time.

The backend uses database queries to return matching listings.

---

## 5. Listing Details

The backend retrieves the information for a selected clothing listing.

**Main Functions:**
- Find a listing using its ID.
- Retrieve its details from the database.
- Retrieve seller information.
- Check the listing status.
- Display the information through the frontend.

---

## 6. Seller Dashboard

The backend allows sellers to manage their own listings.

**Main Functions:**
- Retrieve listings belonging to the logged-in seller.
- Separate listings based on their status.
- Allow sellers to edit their own listings.
- Mark listings as sold.
- Mark listings as unavailable.
- Make unavailable listings available again.
- Remove listings.

**Listing Statuses:**
- Available
- Sold
- Unavailable
- Removed

The backend checks listing ownership before allowing changes.

---

## 7. Messaging System

The backend handles communication between buyers and sellers.

**Main Functions:**
- Receive messages from buyers.
- Check that the listing exists and is available.
- Prevent users from messaging themselves about their own listings.
- Validate message content.
- Save messages in the database.
- Retrieve received messages for the inbox.
- Connect each message to its sender, receiver, and listing.

---

## 8. Notification System

The backend manages notifications for users.

**Main Functions:**
- Create a notification when a new message is received.
- Retrieve notifications for the logged-in user.
- Return the unread notification count.
- Mark notifications as read.

The frontend displays the notification information using the backend data.

---

## 9. Saved Listings

The backend handles users' saved clothing listings.

**Main Functions:**
- Save a listing for a user.
- Remove a listing from the user's saved list.
- Retrieve saved listings.
- Connect saved listings to their users.

---

## 10. Reporting System

The backend allows users to report clothing listings.

**Main Functions:**
- Receive a listing report.
- Store the report information.
- Connect the report to the reported listing and reporting user.
- Allow administrators to review reports.
- Allow administrators to dismiss reports.

---

## 11. Admin Management

The backend provides restricted functions for administrators.

**Admin Dashboard Functions:**

**Reports Management**
- Retrieve submitted reports.
- Review reports.
- Dismiss reports.
- Remove reported listings.

**User Management**
- Retrieve registered users.
- Deactivate users.
- Reactivate users.

**Listing Management**
- Retrieve clothing listings.
- Remove listings.
- Restore removed listings.

Only authorized administrators can access these functions.

---

## 12. Admin Account Management

The backend allows authorized administrators to create additional admin accounts.

**Main Functions:**
- Receive admin account information.
- Validate the name, email, and password.
- Check for duplicate email addresses.
- Require a password with at least 8 characters.
- Hash the password before storing it.
- Save the new admin account in the database.

---


## 13. Database Design

The project uses SQLite to store and manage information. The database contains six main tables:

| Table | Purpose |
|---|---|
| users | Stores user account information, login details, and account status. |
| listings | Stores clothing listing information, including title, category, price, size, condition, city, description, photo, seller, and status. |
| messages | Stores messages sent between buyers and sellers. |
| notifications | Stores notifications related to user activities, such as new messages. |
| reports | Stores reports submitted by users about clothing listings. |
| saved-items | Stores clothing listings saved by users. |

The tables are connected through IDs to associate users with their listings, messages, notifications, reports, and saved items.

## 14. Backend Routes and Request Handling

Flask routes receive requests from the frontend and process the required operations.

**Main Operations Include:**
- User registration and authentication.
- Creating and retrieving listings.
- Updating listing information.
- Changing listing status.
- Sending and retrieving messages.
- Managing notifications.
- Saving and reporting listings.
- Admin dashboard operations.

Flask processes the requests, communicates with SQLite, and returns the appropriate page or response.

---

## Tools and Technologies Used

- **Python** – backend programming language
- **Flask** – web framework and route handling
- **SQLite** – database management
- **Werkzeug** – password hashing and security utilities
- **Flask-Mail** – sending password reset emails
- **itsdangerous** – generating and validating password reset tokens
- **Jinja2** – connecting backend data with HTML templates
- **OS and secure filename utilities** – handling uploaded files

---

## Backend Workflow

**User Registration:**

Sign Up Form → Flask Route → Input Validation → Password Hashing → SQLite Database → Response to User

**User Login:**

Login Form → Flask Route → Check Email and Password → Create Session → Redirect User

**Creating a Listing:**

Sell Form → Flask Route → Validate Information and Photo → Save Photo → Save Listing in SQLite → Display Listing

**Sending a Message:**

Contact Seller Form → Flask Route → Validate Message → Save Message → Create Notification → Display in Seller's Inbox

**Admin Operations:**

Admin Dashboard → Check Admin Permission → Process Admin Action → Update SQLite Database → Return Updated Information

---

## Design Goals

- Store user and listing information correctly.
- Protect user accounts and passwords.
- Check user permissions before restricted actions.
- Validate information before saving it.
- Keep the frontend and backend connected.
- Handle listing photos safely.
- Make database operations reliable.
- Keep the backend simple and maintainable.
