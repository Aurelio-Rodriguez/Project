Unitrack

Unitrack is a web application that allows users to register, log in, and access a menu system tailored for students. This is the current draft of the application, and it is a work in progress.

Project Structure

The project has the following folder and file structure:

unitrack/
│
├── templates/          # Contains HTML templates
│   ├── register.html   # For creating new accounts
│   ├── login.html      # For logging in
│   └── studentmenu.html# For student users
│
├── venv/               # Virtual environment folder
│
└── app.py              # Backend code for the application

How to Run the Code

To run this project locally on your device, follow these steps:

Prerequisites
- Ensure you have the latest versions of Python, pip, and Flask installed on your computer.

Step-by-Step Instructions

1. Clone this repository:
   git clone https://github.com/your-username/unitrack.git

2. Navigate to the project folder:
   Open a command prompt or terminal and run:
   cd unitrack

3. Set up the virtual environment:
   (This step is optional if you have already created a virtual environment.)
   python -m venv venv

4. Activate the virtual environment:
   On Windows Command Prompt:
   venv\Scripts\activate
   On macOS/Linux Terminal:
   source venv/bin/activate

5. Install dependencies:
   Make sure the required packages are installed, including Flask:
   pip install -r requirements.txt

6. Run the application:
   After setting everything up, run the following command:
   py app.py

7. Access the app:
   Once the server is running, open your browser and go to the following URL:
   http://127.0.0.1:5000

Note:
- This is a development server. For production environments, it is advised to use a production WSGI server (e.g., Gunicorn).
- Ensure that your Python, pip, and Flask installations are up-to-date for the app to run smoothly.

Features (So Far)

1. Register New Account: Users can create an account with roles of either Student or Admin.
2. Login Page: A page where users can log in with their credentials.
3. Student Menu: Displays a specific menu for users who register as students.

Future Plans

- Add more templates and features as the project progresses.
- Improve security for production deployment.

License

This project is licensed under the MIT License - see the LICENSE file for details.
