Fee Management System
📌 Overview
The Fee Management System is a Python-based application that automates fee status tracking and notification via email. It allows administrators to:

✅ Send OTP-based authentication for secure admin login.
✅ Notify students via email about pending or cleared fees.
✅ Update fee statuses for registered users.
This project uses SMTP, Python-dotenv, and automated email notifications to streamline the fee management process.

🛠️ Features
🔹 OTP Authentication – Ensures only authorized admins can access the system.
🔹 Automated Email Notifications – Sends emails to students based on fee status.
🔹 Admin Dashboard – Provides a simple interface to update and track fee records.
🔹 Secure Credential Handling – Uses .env files to protect sensitive email credentials.

🔧 Tech Stack
Python (Core logic)
SMTP (Email sending)
dotenv (Environment variable management)
🚀 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Mantri-Jayalakshmi/fee-management-system.git
cd fee-management-system
2️⃣ Install Dependencies
bash
Copy
Edit
pip install python-dotenv
3️⃣ Configure Email Credentials
Create a .env file and add your email and app password:

plaintext
Copy
Edit
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
🔹 Use an App Password instead of your Gmail password (for security).

4️⃣ Run the Project
bash
Copy
Edit
python main.py
📬 Contact & Contributions
Feel free to contribute by creating pull requests or reporting issues!
🔗 GitHub: Mantri-Jayalakshmi
📧 Email: mantrijayalakshmi796@gmail.com

💡 Future Enhancements
✅ Add a database to store fee records.
✅ Implement a web-based UI for better user experience.
✅ Support SMS notifications alongside email alerts.

🚀 If you find this project useful, don’t forget to ⭐ it!
