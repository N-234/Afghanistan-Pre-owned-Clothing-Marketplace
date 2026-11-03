# Frontend Design Document

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Prepared By:** Nargis Bunyadi
**Project Type:** Web-Based Marketplace

---

## Overview

The frontend of the Afghan Girls' Pre-Owned Clothes Marketplace is designed to provide a simple and user-friendly platform where users can browse, search, buy, and sell pre-owned clothes.

The website uses HTML, CSS, and JavaScript. It includes different pages for visitors, registered users, and administrators.

This document describes the main pages, their design, and expected behavior.

---

## Screens / Pages

### 1. Home Page

**Header links:**
- Home
- Sell
- Login / Sign Up
- Dashboard
- Inbox
- Notifications
- Account menu

**Main sections include:**
- Website introduction
- Recently added clothing listings
- Clothing categories
- Search and filter section
- Clothing listing cards

**Each clothing card displays:**
- Clothing photo
- Item title
- Price
- Size
- Condition
- City
- View Details option

The homepage allows users to browse available and sold listings.

---

### 2. Login Page

**Fields:**
- Email
- Password

**Options:**
- Login button
- Forgot Password link
- Link to the Sign Up page

After successful login, users are redirected to the appropriate page.

---

### 3. Sign Up Page

**Fields:**
- Full Name
- Email
- Password

**Features:**
- Input validation
- Email uniqueness checking
- Password hashing handled by the backend

After successful registration, users can log in to their accounts.

---

### 4. Forgot Password Page

**Fields:**
- Email address

**Features:**
- User enters their registered email.
- System sends a password reset link.
- User opens the link to enter a new password.
- Reset links expire after a limited time.

---

### 5. Sell / Add Listing Page

**Fields:**
- Clothing title
- Category
- Price
- Size
- Condition
- City
- Description
- Product photo

**Features:**
- Image preview
- Required field validation
- Image format and size validation
- Submit Listing button

After successful submission, the listing is saved and displayed on the marketplace.

---

### 6. Search and Filter Section

Users can find clothes using:

- Search by clothing name
- Category filter
- Size filter
- Maximum price filter
- Condition filter
- City filter
- Sorting options

**Actions:**
- Apply search and filters
- Clear filters

The clothing cards update based on the selected search and filter options.

---

### 7. Listing Details Page

**Displays:**
- Clothing photo
- Item title
- Price
- Category
- Size
- Condition
- City
- Description
- Seller information
- Listing status

**Actions:**
- Contact Seller
- Save Listing
- Report Listing

Users cannot contact themselves about their own listings.

---

### 8. Seller Dashboard

The dashboard allows sellers to manage their own clothing listings.

**Sections include:**
- Active Listings
- Sold Listings
- Other listing statuses

**Actions:**
- Edit Listing
- Mark as Sold
- Mark as Unavailable
- Make Available Again
- Remove Listing

Users can only manage their own listings.

---

### 9. Edit Listing Page

Allows sellers to update information about their existing listings.

**Editable fields include:**
- Clothing title
- Category
- Price
- Size
- Condition
- City
- Description
- Product photo

After saving, the updated information is displayed on the listing.

---

### 10. Contact Seller and Inbox Pages

**Contact Seller Page:**
- Message field
- Send Message button

**Inbox Page:**
- Received messages
- Sender information
- Related clothing listing
- Message content

Users can view messages sent to them about their listings.

---

### 11. Notifications

The notification section informs users about new messages.

**Features:**
- Notification icon
- Unread notification count
- New message notifications
- Mark notifications as read

---

### 12. Admin Dashboard

The admin dashboard provides tools to manage the marketplace.

**Main sections include:**

**Reports Review**
- View reported listings
- Review reports
- Dismiss reports
- Delete reported listings

**User Management**
- View registered users
- Deactivate users
- Reactivate users

**Listing Management**
- View clothing listings
- Remove listings
- Restore listings

Only authorized administrators can access this dashboard.

---

### 13. Manage Admins Page

Allows an authorized administrator to create new admin accounts.

**Fields:**
- Name
- Email
- Password

**Features:**
- Email validation
- Duplicate email checking
- Minimum password length validation
- Password hashing

---

## Tools and Technologies Used

- **HTML** – structure of the website
- **CSS** – styling and page layout
- **JavaScript** – frontend interactions and validation
- **Python Flask** – backend and page routing
- **SQLite** – database storage
- **Jinja2** – displaying dynamic information in HTML templates

---

## Wireframe Sketch (Text-Only Outline)

**User Navigation:**

Home Page → Search / Filter → Listing Details → Contact Seller → Inbox

Home Page → Sign Up / Login → Sell Listing → Seller Dashboard → Edit Listing

Home Page → Listing Details → Save Listing / Report Listing

**Admin Navigation:**

Admin Login → Admin Dashboard → Reports Review

Admin Dashboard → User Management

Admin Dashboard → Listing Management

Admin Dashboard → Manage Admins → Create Admin Account

---

## Design Goals

- Keep the website simple and easy to navigate.
- Use a consistent design across all pages.
- Make clothing listings clear and easy to browse.
- Provide useful feedback after user actions.
- Protect pages and actions based on user permissions.
- Make the website usable on different screen sizes.
