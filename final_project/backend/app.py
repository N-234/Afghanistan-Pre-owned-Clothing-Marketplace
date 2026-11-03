from flask import Flask, render_template, request, jsonify, session, send_from_directory, redirect
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from dotenv import load_dotenv
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature


app = Flask(
    __name__,
    template_folder=os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "frontend", "templates")
    ),
    static_folder=os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "frontend", "static")
    )
)
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

app.secret_key = "your-secret-key"

def is_admin():
    if "user_id" not in session:
        return False

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    user = connection.execute("""
        SELECT role, is_active
        FROM users
        WHERE id = ?
    """, (session["user_id"],)).fetchone()

    connection.close()

    return user is not None and user[0] == "admin" and user[1] == 1

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_TIMEOUT"] = 20
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_USERNAME")

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)

def create_database():
    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Admin role and account status to users
    user_columns = connection.execute(
        "PRAGMA table_info(users)"
    ).fetchall()

    user_column_names = [column[1] for column in user_columns]

    if "role" not in user_column_names:
        connection.execute("""
            ALTER TABLE users
            ADD COLUMN role TEXT NOT NULL DEFAULT 'user'
        """)

    if "is_active" not in user_column_names:
        connection.execute("""
            ALTER TABLE users
            ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1
        """)

    # Table for listing reports
    connection.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            listing_id INTEGER NOT NULL,
            reporter_id INTEGER NOT NULL,
            reason TEXT NOT NULL,
            details TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            reviewed_at TIMESTAMP,
            FOREIGN KEY (listing_id) REFERENCES listings(id),
            FOREIGN KEY (reporter_id) REFERENCES users(id)
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL,
            size TEXT NOT NULL,
            condition TEXT NOT NULL,
            city TEXT NOT NULL,
            description TEXT NOT NULL,
            photo TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Status in listing
    columns = connection.execute(
        "PRAGMA table_info(listings)"
    ).fetchall()

    column_names = [column[1] for column in columns]

    if "status" not in column_names:
        connection.execute("""
            ALTER TABLE listings
            ADD COLUMN status TEXT NOT NULL DEFAULT 'available'
        """)

    # Table for saved items
    connection.execute("""
        CREATE TABLE IF NOT EXISTS saved_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            listing_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, listing_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (listing_id) REFERENCES listings(id)
        )
    """)

    # Table for buyer-seller messages
    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            listing_id INTEGER NOT NULL,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (listing_id) REFERENCES listings(id),
            FOREIGN KEY (sender_id) REFERENCES users(id),
            FOREIGN KEY (receiver_id) REFERENCES users(id)
        )
    """)

    # Table for user notifications
    connection.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            type TEXT NOT NULL,
            is_read INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    connection.commit()
    connection.close()


create_database()

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["full_name"]
    email = request.form["email"]
    password = request.form["password"]

    hashed_password = generate_password_hash(password)

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    try:
        connection.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed_password)
        )

        connection.commit()

    except sqlite3.IntegrityError:
        connection.close()

        return jsonify({
            "success": False,
            "message": "An account with this email already exists."
        })

    connection.close()

    return jsonify({
        "success": True,
        "message": "Account created successfully."
    })


@app.route("/forgot-password", methods=["GET"])
def forgot_password_page():
    return render_template("forgot_password.html")


@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    email = request.form.get("email", "").strip().lower()

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    user = connection.execute(
        "SELECT id FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    connection.close()


    if user:
        token = serializer.dumps(email, salt="password-reset")
        reset_link = request.host_url.rstrip("/") + "/reset-password?token=" + token

        message = Message(
            subject="Reset Your Afghan Girls Marketplace Account Password",
            recipients=[email],
            body=(
                "We received a request to reset your password.\n\n"
                f"Open this link to reset it:\n{reset_link}\n\n"
                "This link expires after 15 minutes. "
                "If you did not request this, you can ignore this email."
            )
        )

        try:
            mail.send(message)
        except Exception:
            app.logger.exception("Could not send password reset email")
            return jsonify({
                "success": False,
                "message": "Could not send the email. Please try again later."
            }), 500

    return jsonify({
        "success": True,
        "message": (
            "If an account exists with this email, "
            "you will receive a password reset link."
        )
    })

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        return render_template("reset_password.html")

    token = request.form.get("token", "")

    try:
        email = serializer.loads(
            token,
            salt="password-reset",
            max_age=900
        )
    except (SignatureExpired, BadSignature):
        return jsonify({
            "success": False,
            "message": "This reset link is invalid or has expired."
        }), 400

    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    if len(password) < 8:
        return jsonify({
            "success": False,
            "message": "Password must be at least 8 characters."
        }), 400

    if password != confirm_password:
        return jsonify({
            "success": False,
            "message": "Passwords do not match."
        }), 400

    hashed_password = generate_password_hash(password)

    database_path = os.path.join(
        os.path.dirname(__file__),
        "database.db"
    )

    connection = sqlite3.connect(database_path)

    cursor = connection.execute(
        "UPDATE users SET password = ? WHERE email = ?",
        (hashed_password, email)
    )

    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()

    if not updated:
        return jsonify({
            "success": False,
            "message": "Could not update the password."
        }), 400

    return jsonify({
        "success": True,
        "message": "Password updated successfully. You can now log in."
    })


@app.route("/login")
def login_page():
    message = ""

    if request.args.get("next") == "/sell":
        message = "Please log in first to sell your clothes."

    return render_template("login.html", message=message)


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    user = connection.execute("""
        SELECT id, name, password, role, is_active
        FROM users
        WHERE email = ?
    """, (email,)).fetchone()

    connection.close()

    if user and check_password_hash(user[2], password):

        if user[4] == 0:
            return jsonify({
                "success": False,
                "message": "Your account has been deactivated."
            }), 403

        session["user_id"] = user[0]
        session["user_role"] = user[3]

        next_page = request.args.get("next")

        if next_page != "/sell":
            next_page = "/"

        return jsonify({
            "success": True,
            "message": "Login successful.",
            "role": user[3],
            "redirect": next_page
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password."
    }), 401


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")

@app.route("/sell")
def sell_page():
    if "user_id" not in session:
        return redirect("/login?next=/sell")

    return render_template("sell.html")

@app.route("/sell", methods=["POST"])
def sell():
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in first."
        })

    title = request.form["title"]
    category = request.form["category"]
    price = request.form["price"]
    size = request.form["size"]
    condition = request.form["condition"]
    city = request.form["city"]
    description = request.form["description"]

    photo = request.files.get("photo")

    photo_name = None

    if photo:
        photo_name = photo.filename

        upload_folder = os.path.join(
            os.path.dirname(__file__),
            "uploads"
        )

        photo.save(os.path.join(upload_folder, photo_name))

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    connection.execute("""
        INSERT INTO listings
        (user_id, title, category, price, size, condition, city, description, photo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user_id"],
        title,
        category,
        price,
        size,
        condition,
        city,
        description,
        photo_name
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Listing published successfully."
    })


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    upload_folder = os.path.join(
        os.path.dirname(__file__),
        "uploads"
    )

    return send_from_directory(upload_folder, filename)


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )
    connection.row_factory = sqlite3.Row

    listings = connection.execute("""
        SELECT * FROM listings
        WHERE user_id = ?
        ORDER BY id DESC
    """, (session["user_id"],)).fetchall()

    connection.close()

    return render_template(
        "dashboard.html",
        listings=listings
    )


@app.route("/api/listings/<int:listing_id>", methods=["GET", "POST"])
def edit_listing_api(listing_id):
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please log in."}), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )
    connection.row_factory = sqlite3.Row

    if request.method == "GET":
        listing = connection.execute("""
            SELECT * FROM listings
            WHERE id = ?
        """, (listing_id,)).fetchone()
    else:
        listing = connection.execute("""
            SELECT * FROM listings
            WHERE id = ? AND user_id = ?
        """, (listing_id, session["user_id"])).fetchone()


    if listing is None:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Listing not found."
        }), 404

    if request.method == "GET":
        listing_data = dict(listing)
        connection.close()
        return jsonify({
            "success": True,
            "listing": listing_data
        })

    title = request.form.get("title", "").strip()
    category = request.form.get("category", "").strip()
    price = request.form.get("price", "").strip()
    size = request.form.get("size", "").strip()
    condition = request.form.get("condition", "").strip()
    city = request.form.get("city", "").strip()
    description = request.form.get("description", "").strip()

    if not all([
        title, category, price, size,
        condition, city, description
    ]):
        connection.close()
        return jsonify({
            "success": False,
            "message": "Please fill in all required fields."
        }), 400

    try:
        price = int(price)
        if price < 1:
            raise ValueError
    except ValueError:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Please enter a valid price."
        }), 400

    photo_name = listing["photo"]
    photo = request.files.get("photo")

    if photo and photo.filename:
        extension = os.path.splitext(photo.filename)[1].lower()
        allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}

        if extension not in allowed_extensions:
            connection.close()
            return jsonify({
                "success": False,
                "message": "Please upload a JPG, PNG, or WebP image."
            }), 400

        import uuid

        photo_name = str(uuid.uuid4()) + extension
        upload_folder = os.path.join(
            os.path.dirname(__file__), "uploads"
        )
        os.makedirs(upload_folder, exist_ok=True)
        photo.save(os.path.join(upload_folder, photo_name))

    connection.execute("""
        UPDATE listings
        SET title = ?, category = ?, price = ?, size = ?,
            condition = ?, city = ?, description = ?, photo = ?
        WHERE id = ? AND user_id = ?
    """, (
        title, category, price, size, condition,
        city, description, photo_name,
        listing_id, session["user_id"]
    ))

    connection.commit()
    connection.close()

    return jsonify({"success": True})


@app.route("/edit_listing")
def edit_listing_page():
    if "user_id" not in session:
        return redirect("/login")

    listing_id = request.args.get("id", "")

    if not listing_id.isdigit() or int(listing_id) < 1:
        return "Invalid listing ID.", 400

    return render_template("edit_listing.html")


@app.route("/api/listings/<int:listing_id>/sold", methods=["POST"])
def mark_listing_sold(listing_id):
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please log in."}), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT status FROM listings
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"])).fetchone()

    if listing is None:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Listing not found."
        }), 404

    if listing[0] != "available":
        connection.close()
        return jsonify({
            "success": False,
            "message": "This listing is not available."
        }), 400

    connection.execute("""
        UPDATE listings
        SET status = 'sold'
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"]))

    connection.commit()
    connection.close()

    return jsonify({"success": True})


@app.route("/api/listings/<int:listing_id>/unavailable", methods=["POST"])
def mark_listing_unavailable(listing_id):
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please log in."}), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT status FROM listings
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"])).fetchone()

    if listing is None:
        connection.close()
        return jsonify({"success": False, "message": "Listing not found."}), 404

    if listing[0] != "available":
        connection.close()
        return jsonify({"success": False, "message": "This listing is not available."}), 400

    connection.execute("""
        UPDATE listings
        SET status = 'unavailable'
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"]))

    connection.commit()
    connection.close()

    return jsonify({"success": True})

@app.route("/api/listings/<int:listing_id>/available", methods=["POST"])
def mark_listing_available(listing_id):
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please log in."}), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT status FROM listings
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"])).fetchone()

    if listing is None:
        connection.close()
        return jsonify({"success": False, "message": "Listing not found."}), 404

    if listing[0] != "unavailable":
        connection.close()
        return jsonify({
            "success": False,
            "message": "Only unavailable listings can be made available."
        }), 400

    connection.execute("""
        UPDATE listings
        SET status = 'available'
        WHERE id = ? AND user_id = ?
    """, (listing_id, session["user_id"]))

    connection.commit()
    connection.close()

    return jsonify({"success": True})

@app.route("/api/listings/<int:listing_id>/delete", methods=["POST"])
def delete_listing(listing_id):
    if "user_id" not in session:
        return jsonify({"success": False, "message": "Please log in."}), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    cursor = connection.execute("""
        UPDATE listings
        SET status = 'removed'
        WHERE id = ? AND user_id = ?
          AND status IN ('available', 'unavailable', 'sold')
    """, (listing_id, session["user_id"]))

    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return jsonify({
            "success": False,
            "message": "Listing not found."
        }), 404

    return jsonify({"success": True})


@app.route("/api/listings/<int:listing_id>/messages", methods=["POST"])
def send_listing_message(listing_id):
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in."
        }), 401

    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message or len(message) > 2000:
        return jsonify({
            "success": False,
            "message": "Please enter a message up to 2000 characters."
        }), 400

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT user_id, status
        FROM listings
        WHERE id = ?
    """, (listing_id,)).fetchone()

    if listing is None:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Listing not found."
        }), 404

    seller_id = listing[0]
    status = listing[1]

    if status != "available":
        connection.close()
        return jsonify({
            "success": False,
            "message": "This item is no longer available."
        }), 400

    if seller_id == session["user_id"]:
        connection.close()
        return jsonify({
            "success": False,
            "message": "You cannot message yourself about your own listing."
        }), 400

    connection.execute("""
        INSERT INTO messages (
            listing_id, sender_id, receiver_id, message
        )
        VALUES (?, ?, ?, ?)
    """, (
        listing_id,
        session["user_id"],
        seller_id,
        message
    ))

    # Create a notification for the seller
    connection.execute("""
        INSERT INTO notifications (user_id, message, type)
        VALUES (?, ?, ?)
    """, (
        seller_id,
        "You have a new message! Check your inbox.",
        "new_message"
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Message sent successfully."
    }), 201

@app.route("/api/notifications")
def get_notifications():
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in."
        }), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )
    connection.row_factory = sqlite3.Row

    notifications = connection.execute("""
        SELECT id, message, type, is_read, created_at
        FROM notifications
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (session["user_id"],)).fetchall()

    connection.close()

    return jsonify({
        "success": True,
        "notifications": [dict(notification) for notification in notifications]
    })


@app.route("/api/messages/inbox")
def get_inbox_messages():
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in."
        }), 401

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )
    connection.row_factory = sqlite3.Row

    messages = connection.execute("""
        SELECT
            messages.message,
            messages.created_at,
            users.name AS sender_name,
            listings.title AS listing_title
        FROM messages
        JOIN users
            ON messages.sender_id = users.id
        JOIN listings
            ON messages.listing_id = listings.id
        WHERE messages.receiver_id = ?
        ORDER BY messages.created_at DESC
    """, (session["user_id"],)).fetchall()

    connection.close()

    return jsonify({
        "success": True,
        "messages": [dict(message) for message in messages]
    })


@app.route("/inbox")
def inbox_page():
    if "user_id" not in session:
        return redirect("/login")

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    # Mark new-message notifications as read
    connection.execute("""
        UPDATE notifications
        SET is_read = 1
        WHERE user_id = ?
        AND type = 'new_message'
    """, (session["user_id"],))

    connection.commit()
    connection.close()

    return render_template("inbox.html")


@app.route("/contact-seller")
def contact_seller_page():
    if "user_id" not in session:
        return redirect("/login")

    listing_id = request.args.get("id", "")

    if not listing_id.isdigit() or int(listing_id) < 1:
        return "Invalid listing ID.", 400

    return render_template(
        "contact_seller.html",
        current_user_id=session["user_id"]
    )

@app.route("/report-listing")
def report_listing_page():
    if "user_id" not in session:
        return redirect("/login")

    listing_id = request.args.get("id", "")

    if not listing_id.isdigit() or int(listing_id) < 1:
        return "Invalid listing ID.", 400

    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = conn.cursor()

    cursor.execute(
        """SELECT title, category, price, size, condition, city, user_id
           FROM listings WHERE id = ?""",
        (int(listing_id),)
    )

    listing = cursor.fetchone()

    if listing is None:
        conn.close()
        return "Listing not found.", 404

    if listing[6] == session["user_id"]:
        conn.close()
        return "You cannot report your own listing.", 403

    conn.close()

    return render_template(
        "report_listing.html",
        listing=listing[:6],
        listing_id=int(listing_id)
    )


@app.route("/api/listings/<int:listing_id>/report", methods=["POST"])
def report_listing(listing_id):
    if "user_id" not in session:
        return jsonify({
            "success": False,
            "message": "Please log in first."
        }), 401

    data = request.get_json(silent=True) or {}

    reason = data.get("reason", "")
    details = data.get("details", "")

    if not isinstance(reason, str) or not isinstance(details, str):
        return jsonify({
            "success": False,
            "message": "Invalid report information."
        }), 400

    reason = reason.strip()
    details = details.strip()

    allowed_reasons = [
        "Inappropriate content",
        "Fake listing",
        "Misleading information",
        "Other"
    ]

    if reason not in allowed_reasons:
        return jsonify({
            "success": False,
            "message": "Please select a valid reason."
        }), 400

    if len(details) > 1000:
        return jsonify({
            "success": False,
            "message": "Details cannot exceed 1000 characters."
        }), 400

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT user_id FROM listings
        WHERE id = ?
    """, (listing_id,)).fetchone()

    if listing is None:
        connection.close()
        return jsonify({
            "success": False,
            "message": "Listing not found."
        }), 404

    if listing[0] == session["user_id"]:
        connection.close()
        return jsonify({
            "success": False,
            "message": "You cannot report your own listing."
        }), 400

    existing_report = connection.execute("""
        SELECT id FROM reports
        WHERE listing_id = ?
        AND reporter_id = ?
        AND status = 'pending'
    """, (listing_id, session["user_id"])).fetchone()

    if existing_report:
        connection.close()
        return jsonify({
            "success": False,
            "message": "You have already reported this listing."
        }), 400

    connection.execute("""
        INSERT INTO reports (
            listing_id, reporter_id, reason, details
        )
        VALUES (?, ?, ?, ?)
    """, (
        listing_id,
        session["user_id"],
        reason,
        details
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Your report has been submitted successfully."
    }), 201


@app.route("/admin")
def admin_dashboard():
    if "user_id" not in session:
        return redirect("/login")

    if not is_admin():
        return "Access denied. Admins only.", 403

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    connection.row_factory = sqlite3.Row

    # Get all reports
    reports = connection.execute("""
        SELECT
            reports.id,
            reports.listing_id,
            reports.reporter_id,
            reports.reason,
            reports.details,
            reports.status,
            reports.created_at,
            listings.title,
            users.name AS reporter_name
        FROM reports
        JOIN listings ON reports.listing_id = listings.id
        JOIN users ON reports.reporter_id = users.id
        ORDER BY reports.created_at DESC
    """).fetchall()

    # Get all users
    users = connection.execute("""
        SELECT id, name, email, role, is_active
        FROM users
        ORDER BY id DESC
    """).fetchall()

    # Get all listings
    listings = connection.execute("""
        SELECT
            listings.id,
            listings.title,
            listings.category,
            listings.price,
            listings.status,
            users.name AS seller_name
        FROM listings
        JOIN users ON listings.user_id = users.id
        ORDER BY listings.id DESC
    """).fetchall()

    connection.close()

    return render_template(
        "admin_dashboard.html",
        reports=reports,
        users=users,
        listings=listings
    )

# Page for managing admins
@app.route("/admin/manage-admins", methods=["GET", "POST"])
def manage_admins():
    if "user_id" not in session:
        return redirect("/login")

    if not is_admin():
        return "Access denied. Admins only.", 403

    if request.method == "POST":
        name = request.form["full_name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        if not name or not email or not password:
            return render_template(
                "manage_admins.html",
                message="Please fill in all fields."
            )

        if len(password) < 8:
            return render_template(
                "manage_admins.html",
                message="Password must be at least 8 characters long."
            )

        hashed_password = generate_password_hash(password)

        connection = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), "database.db")
        )

        try:
            connection.execute("""
                INSERT INTO users (name, email, password, role)
                VALUES (?, ?, ?, 'admin')
            """, (name, email, hashed_password))

            connection.commit()
            message = "Admin account created successfully."

        except sqlite3.IntegrityError:
            message = "An account with this email already exists."

        connection.close()

        return render_template(
            "manage_admins.html",
            message=message
        )

    return render_template("manage_admins.html")


@app.route("/admin/reports/<int:report_id>/update", methods=["POST"])
def update_report(report_id):
    if "user_id" not in session:
        return redirect("/login")

    if not is_admin():
        return "Access denied. Admins only.", 403

    action = request.form.get("status", "")

    if action not in ["reviewed", "dismissed", "delete_listing"]:
        return "Invalid action.", 400

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    report = connection.execute("""
        SELECT listing_id
        FROM reports
        WHERE id = ?
    """, (report_id,)).fetchone()

    if report is None:
        connection.close()
        return "Report not found.", 404

    if action == "delete_listing":
        connection.execute("""
            UPDATE listings
            SET status = 'removed'
            WHERE id = ?
        """, (report[0],))

        connection.execute("""
            UPDATE reports
            SET status = 'reviewed',
                reviewed_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (report_id,))

    else:
        connection.execute("""
            UPDATE reports
            SET status = ?,
                reviewed_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (action, report_id))

    connection.commit()
    connection.close()

    return redirect("/admin#reports")

@app.route("/admin/users/<int:user_id>/update", methods=["POST"])
def update_user(user_id):
    if "user_id" not in session:
        return redirect("/login")

    if not is_admin():
        return "Access denied. Admins only.", 403

    action = request.form.get("action", "")

    if action not in ["deactivate", "activate"]:
        return "Invalid action.", 400

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    # Find the selected user
    user = connection.execute("""
        SELECT role, is_active
        FROM users
        WHERE id = ?
    """, (user_id,)).fetchone()

    if user is None:
        connection.close()
        return "User not found.", 404

    # Do not allow changing admin accounts
    if user[0] == "admin":
        connection.close()
        return "Admin accounts cannot be changed here.", 403

    if action == "deactivate":
        connection.execute("""
            UPDATE users
            SET is_active = 0
            WHERE id = ?
        """, (user_id,))

    else:
        connection.execute("""
            UPDATE users
            SET is_active = 1
            WHERE id = ?
        """, (user_id,))

    connection.commit()
    connection.close()

    return redirect("/admin#users")

@app.route("/admin/listings/<int:listing_id>/update", methods=["POST"])
def update_listing_status(listing_id):
    if "user_id" not in session:
        return redirect("/login")

    if not is_admin():
        return "Access denied. Admins only.", 403

    action = request.form.get("action", "")

    if action not in ["remove", "restore"]:
        return "Invalid action.", 400

    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listing = connection.execute("""
        SELECT id FROM listings
        WHERE id = ?
    """, (listing_id,)).fetchone()

    if listing is None:
        connection.close()
        return "Listing not found.", 404

    if action == "remove":
        status = "removed"
    else:
        status = "available"

    connection.execute("""
        UPDATE listings
        SET status = ?
        WHERE id = ?
    """, (status, listing_id))

    connection.commit()
    connection.close()

    return redirect("/admin#listings")
@app.route("/")
def home():
    connection = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), "database.db")
    )

    listings = connection.execute(
        """
        SELECT * FROM listings
        WHERE status IN ('available', 'sold')
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        listings=listings,
        logged_in="user_id" in session
    )


if __name__ == "__main__":
    app.run(debug=True)