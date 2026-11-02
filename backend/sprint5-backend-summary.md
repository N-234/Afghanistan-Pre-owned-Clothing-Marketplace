# Sprint 5: Backend Work Summary

Project: Afghan Girls' Pre-Owned Clothes Marketplace
Developer: Parwana Jafari
Sprint: 5

## Overview

In Sprint 5, I worked on notifications, listing management, and improving the backend functionality of the marketplace. I also made some improvements to help users manage their listings more easily.

## 1. Notifications (US-019)

- Created a notifications table in the database.
- Added a notification when a seller receives a new message.
- Created an API route to load notifications for the logged-in user.
- Connected the notification bell to the backend.
- Displayed the number of unread notifications.
- Marked notifications as read when the user opens the Inbox.

## 2. Responsive Design (US-020)

- Checked the website on smaller screens.
- Improved the mobile navigation.
- Adjusted the admin dashboard layout.
- Checked that tables can scroll horizontally on smaller screens.

## 3. Product Image Improvements (ENHANCE-001)

- Improved how product photos are displayed on the homepage and dashboard.
- Used `object-fit: contain` to show the full product image without cropping.
- Added a white background around product images.

## 4. Sorting Options (ENHANCE-002)

- Added sorting options to the homepage:
  - Newest First
  - Oldest First
  - Price: Low to High
  - Price: High to Low
- Connected sorting to JavaScript so product cards are reordered without reloading the page.
- Reset sorting to Newest First when filters are cleared.

## 5. Admin Account Management

- Created a protected page for managing admin accounts.
- Added a backend route to create new admin accounts.
- Added password hashing for security.
- Added validation for required fields and password length.
- Checked whether an email already exists before creating an account.
- Added a link to Manage Admins in the admin dashboard.

## 6. Listing Status Management

- Added the option to mark a listing as Sold.
- Added the option to mark a listing as Unavailable.
- Added the option to make an unavailable listing Available again.
- Added the option to remove a listing by changing its status to `removed`, instead of permanently deleting it.
- Added confirmation messages before changing listing status.
- Updated the homepage query so both available and sold listings remain visible.
- Kept unavailable and removed listings hidden from the homepage.

## 7. Login Before Selling

- Updated the Sell page so users must log in before accessing it.
- Added a message asking users to log in first.
- Updated the login process to redirect users to the Sell page after successful login.

## Next Steps

- Test the website in Chrome, Edge, and Firefox.
- Review the whole code and make sure it is organized.
- Complete the final project documentation and testing.
