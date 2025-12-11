
# 📧 Emaildoot
**Your Email Agent and Tool for Multipurpose Management**

Emaildoot is a powerful, Django-based email management tool designed to streamline your communication workflow. Whether you need AI assistance to draft error-free emails or need to send personalized bulk emails to thousands of recipients for free, Emaildoot handles it all with ease.

## 🚀 Features

### 1. ✍️ AI-Powered Email Drafting
Never worry about typos or tone again. Emaildoot integrates with **LLMs (via Groq AI)** to help you generate professional, error-free emails in seconds. Just type your prompt, let the AI draft it, and hit send.

### 2. 📨 Free Email Sender
Manage and send thousands of emails without expensive subscription fees.
* **Current Support:** Seamless integration with **Gmail**.
* **Scalable:** The architecture is designed to easily connect with other mail clients (Outlook, SMTP, etc.) as per your requirements.

### 3. 📊 Bulk Emails with CSV & Variables
Personalize your outreach at scale.
* Upload a **CSV or Excel file** containing your contact list.
* Use dynamic **variables** (e.g., `{name}`, `{company}`) in your email template.
* Emaildoot automatically replaces these variables with data from your spreadsheet for each recipient.

---

## 🛠️ Technologies Used

* **Backend:** [Django](https://www.djangoproject.com/) (Python)
* **AI Integration:** [Groq](https://groq.com/) (LLM)
* **Frontend:** Bootstrap, CSS3, HTML5

---

## ⚙️ Installation & Usage

Follow these steps to set up Emaildoot locally on your machine.

### Prerequisites
* Python 3.x installed
* Git installed

### Step 1: Clone the Repository
```bash
git clone [https://github.com/trixsearch/emaildoot.git](https://github.com/trixsearch/emaildoot.git)
cd emaildoot
````

### Step 2: Create a Virtual Environment

It is recommended to run this project in a virtual environment to manage dependencies.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install Django and any other required packages.

```bash
pip install django
# If you have a requirements.txt file, run: pip install -r requirements.txt
```

### Step 4: Run the Application

Start the local development server.

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to start using Emaildoot\!

-----

## 📬 Contact & Support

If you have any questions, suggestions, or feedback, feel free to reach out:

  * **Portfolio:** [@trixsearch](https://www.google.com/search?q=https://trixsearch.github.io)
  * **Email:** [inforatme@gmail.com](mailto:inforatme@gmail.com)

-----

*Made with ❤️ by Trixsearch*


