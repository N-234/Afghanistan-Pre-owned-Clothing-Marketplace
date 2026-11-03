# Afghan Girls' Marketplace

## Project Overview

Afghan Girls' Marketplace is a web-based platform for buying and selling pre-owned clothes. Users can create accounts, browse clothing listings, upload their own clothes for sale, contact sellers, and manage their listings.

This project was developed as a Software Engineering course project using the Scrum methodology.

## Main Features

- User registration and login
- Password reset through email
- Browse available and sold clothing listings
- Search and filter clothes by different options
- View listing details
- Upload clothing photos
- Create, edit, and manage personal listings
- Mark listings as sold or unavailable
- Save and unsave listings
- Contact sellers and exchange messages
- Inbox and notifications
- Report listings
- Admin dashboard
- Admin management of users, listings, and reports

## Technologies Used

**Frontend:**
- HTML
- CSS
- JavaScript
- Jinja2

**Backend:**
- Python
- Flask
- SQLite

## Project Structure

```text
final_project/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   └── uploads/
│
├── frontend/
│   ├── templates/
│   └── static/
│       ├── css/
│       └── js/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- PyCharm or another Python IDE
- Packages listed in `requirements.txt`

## How to Run the Project

1. Download or clone the repository.
2. Open the `final_project` folder in PyCharm.
3. Open the PyCharm terminal.
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a local `.env` file in the appropriate project location and add the required environment variables for email configuration.
6. Open `backend/app.py`.
7. Run the Flask application.
8. Open the local URL displayed in the terminal in your browser.

## Database

The project uses SQLite as its database. The database file is located in the `backend` folder.

## Important Notes

- The `.env` file is not included in the repository because it contains private configuration and email credentials.
- Email features require your own email configuration in the local `.env` file.
- Do not upload passwords, email credentials, or private user information to GitHub.
