from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Student


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if (
            username == app.config["ADMIN_USERNAME"]
            and password == app.config["ADMIN_PASSWORD"]
        ):
            flash("Login successful", "success")
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("admin_login.html")


@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html", active_page="home")


@app.route("/register_student", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        # Create a new student instance
        student = Student(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            student_id=request.form["student_id"],
            faculty=request.form["faculty"],
            course=request.form["course"],
            password=request.form[
                "password"
            ],  # Ideally, you should hash passwords before storing them
        )
        # Add to the session and commit
        db.session.add(student)
        db.session.commit()  # This line saves the student to the database

        # Flash a success message
        flash("Student registration successful", "success")

        # Render the registration success page
        return render_template("registration_success.html")

    # For GET requests, render the registration form
    return render_template("student_register_content.html")


@app.route("/update_student", methods=["GET", "POST"])
def update_student():
    student = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "search":
            print("Entered the /update_student route")
            search_value = request.form.get("search")
            student = Student.query.filter(
                (Student.student_id == search_value) | (Student.email == search_value)
            ).first()

            if not student:
                flash("Student not found", "danger")
            else:
                flash("Student found. Update the details as required.", "info")

        elif action == "update":
            student_id_hidden = request.form.get("student_id_hidden")
            student = Student.query.get(student_id_hidden)

            if student:
                student.first_name = request.form["first_name"]
                student.last_name = request.form["last_name"]
                student.email = request.form["email"]
                student.student_id = request.form["student_id"]
                student.faculty = request.form["faculty"]
                student.course = request.form["course"]
                student.password = request.form["password"]
                db.session.commit()
                flash("Student details updated successfully!", "success")
            else:
                flash("Error updating student details!", "danger")

        elif action == "delete":
            student_id_hidden = request.form.get("student_id_hidden")
            student = Student.query.get(student_id_hidden)

            if student:
                db.session.delete(student)
                db.session.commit()
                flash("Student record deleted successfully!", "success")
                return redirect(url_for("update_student"))  # Redirect after delete
            else:
                flash("Error deleting student record!", "danger")

    return render_template("update_student.html", student=student)


@app.route("/admin-logout")
def admin_logout():
    return redirect(url_for("admin_login"))


@app.route("/student-login", methods=["GET", "POST"])
def student_login():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        password = request.form.get("password")
        student = Student.query.filter_by(student_id=student_id).first()
        if student and student.password == password:
            flash("Login successful", "success")
            return redirect(url_for("student_dashboard"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("student_login.html")


@app.route("/student-dashboard", methods=["GET", "POST"])
def student_dashboard():
    # ... Your dashboard logic here ...
    return render_template("student_dashboard.html")
