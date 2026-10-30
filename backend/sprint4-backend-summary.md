# Sprint 4: Backend Development Summary

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Developer:** Parwana Jafari  
**Sprint:** 4

## Overview

During Sprint 4, I mainly worked on the admin features of the marketplace. I added report management, user management, and listing management. I also worked on admin access control to make sure only administrators can manage the platform.

## Work Completed

### 1. Database Updates

I updated the SQLite database to support the new admin features.

- Added a `role` column to the `users` table to distinguish admins from regular users.
- Added an `is_active` column to manage user account status.
- Created a `reports` table to store listing reports.
- Added a `status` column to the `listings` table to manage listing availability.

### 2. Report Management (US-015)

I added functionality that allows users to report inappropriate or suspicious listings.

- Added different report reasons, including inappropriate content, fake listings, and misleading information.
- Saved reports in the database.
- Added a Reports Management section to the Admin Dashboard.
- Allowed admins to review or dismiss reports.
- Added an option to remove reported listings.
- Prevented users from reporting their own listings or submitting duplicate pending reports.

### 3. User Management (US-017)

I added user management features to the Admin Dashboard.

- Displayed registered users and their account statuses.
- Allowed admins to deactivate and reactivate regular user accounts.
- Prevented deactivated users from logging in.
- Prevented admins from changing admin accounts through the User Management section.

### 4. Listing Management (US-018)

I added functionality for admins to manage clothing listings.

- Displayed listings in the Admin Dashboard.
- Allowed admins to remove and restore listings.
- Used listing status to hide removed listings instead of permanently deleting them.
- Updated the homepage database query to display only available listings.

### 5. Admin Access Control (NFR-004)

I added security checks to protect the admin features.

- Created a function to check whether the logged-in user is an active admin.
- Restricted access to the Admin Dashboard to administrators.
- Protected report, user, and listing management routes.
- Tested that regular users cannot access the Admin Dashboard.
- Added a custom confirmation popup before admin actions to help prevent accidental changes.

## Testing

I tested the Sprint 4 features to make sure they worked correctly.

- Tested submitting listing reports.
- Tested reviewing and dismissing reports.
- Tested removing reported listings.
- Tested deactivating and reactivating user accounts.
- Confirmed that deactivated users cannot log in.
- Tested removing and restoring listings.
- Confirmed that removed listings no longer appear on the homepage.
- Tested admin access control using a regular user account.
- Tested the confirmation popup for admin actions.

All the features tested during Sprint 4 worked correctly.

## Challenges

One challenge was updating the existing database to support admin roles, account status, and listing reports. I also had to make sure that admin routes were protected and that removed listings no longer appeared on the public homepage.

## What I Learned

I learned how to manage user roles and permissions in Flask, update SQLite database tables, validate user actions, and protect routes from unauthorized access. I also learned how to manage listing statuses and test admin features.

## Plans for Sprint 5

In Sprint 5, I plan to continue improving the marketplace by working on:

- **Notifications (US-019):** Notify users about important activities, such as receiving new messages and listing status changes.
- **Responsive Design (US-020):** Make sure the website works properly on mobile phones, tablets, and desktop computers.
- **Product Image Improvements (ENHANCE-001):** Improve product image loading, sizing, and display.
- **Sorting Options (ENHANCE-002):** Allow users to sort clothing listings by price, newest listings, and other available options.
- **Mobile Interface Improvements (ENHANCE-003):** Improve navigation and product pages so they are easier to use on smaller screens.
