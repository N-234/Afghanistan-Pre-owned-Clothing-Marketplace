
# Sprint 2: Backend Work Summary

**Project:** Afghan Girls' Pre-Owned Clothes Marketplace  
**Developer:** Parwana Jafari  
**Sprint:** 2

## Overview

In Sprint 2, I worked on the backend for search, filtering, and clothing listings. I connected these features to the database so users could find clothes and see their information on the homepage. I also worked on handling product photos and checking the information before saving a listing.

## What I Worked On

### 1. Search and Filtering

I connected the search and filtering features to the listings on the website.

- Users can search for clothes by title and location.
- Added filters for category, size, and maximum price.
- Added a Clear Filters option.
- Made sure the displayed listings change based on the search and filters.

### 2. Product Information

I worked on getting clothing information from the database and displaying it on the homepage.

- Retrieved saved listings from SQLite.
- Displayed the title, category, size, condition, price, location, description, and photo.
- Organized clothes into different category sections.
- Displayed the newest listings first.

### 3. Product Photo Uploads

I worked on the backend for uploading and displaying product photos.

- Saved uploaded photos in the uploads folder.
- Connected each photo to its listing.
- Added checks for supported image types and file size.
- Made sure uploaded photos could be displayed with the correct listing.

### 4. Input Validation

I added checks before saving a new listing.

- Required fields must be filled in.
- A photo is required when creating a listing.
- Added validation for positive whole-number prices.
- Added checks for photo type and size.

Some validation cases, especially negative and decimal prices, still need further testing.

### 5. Database and Performance

I continued working with the SQLite database to manage clothing listings.

- Saved new listings in the database.
- Retrieved listings for the homepage.
- Connected search and filters to the displayed listings.
- Displayed the newest listings first.

### 6. Forgot Password Feature

I worked on the backend for the forgot password feature on the login page.

- Added a route for the forgot password page.
- Created the backend logic to handle password reset requests.
- Added checks to make sure the required information is entered.
- Connected the feature to the existing user account system.
- Added a password reset process so users can reset their password if they forget it. 

## Testing

I tested search and filtering and checked that category sections updated when filters were applied. I also tested creating listings and displaying their information. I confirmed that empty required fields and missing photos were rejected.

Some price and photo validation cases still need testing, so I have not marked all validation tests as complete.

## Challenges

One challenge was connecting search and filtering with the listings displayed on the homepage. I also worked on making sure photos were saved and displayed correctly. During validation testing, I found that some price checks still need improvement.

## What I Learned

During this sprint, I learned more about retrieving data from a database, connecting backend features to the frontend, handling uploaded files, and checking user input before saving information.

## Plans for Sprint 3

In Sprint 3, I will work on new features for the marketplace. My tasks will include:

- Working on the seller dashboard so sellers can see their active, sold, and removed listings in one place.
- Adding the option for sellers to edit their own clothing listings.
- Adding the option to mark a clothing item as sold.
- Working on saved items so buyers can save clothes they like and view them later.
- Working on messaging so buyers can contact sellers about specific clothing items.

These features will help sellers manage their listings more easily and make it easier for buyers to interact with sellers.
