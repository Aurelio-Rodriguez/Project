from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users_db = {}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        role = request.form.get('role')
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Username and password are required!")
            return redirect(url_for('register'))

        if username in users_db:
            flash("Username already exists. Please choose another one.")
            return redirect(url_for('register'))

        if role == 'student':
            student_name = request.form.get('student_name')
            student_number = request.form.get('student_number')
            student_email = request.form.get('student_email')

            users_db[username] = {
                'role': 'student',
                'password': password,
                'student_name': student_name,
                'student_number': student_number,
                'student_email': student_email
            }

        elif role == 'admin':
            admin_name = request.form.get('admin_name')
            employee_id = request.form.get('employee_id')

            users_db[username] = {
                'role': 'admin',
                'password': password,
                'admin_name': admin_name,
                'employee_id': employee_id
            }

        flash("Account created successfully! Please log in.")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users_db and users_db[username]['password'] == password:
            flash("Login successful!")
            if users_db[username]['role'] == 'student':
                return redirect(url_for('student_dashboard'))
            else:
                return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid credentials, please try again.")

    return render_template('login.html')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('studentmenu.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return "Admin Dashboard (Work in Progress)"

@app.route('/logout', methods=['POST'])
def logout():
    flash("Logged out successfully!")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
