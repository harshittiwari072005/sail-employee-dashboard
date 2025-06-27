# 🛡️ SAIL Employee Dashboard

A modern web dashboard built with **Django** for visualizing and analyzing employee data of Steel Authority of India Limited (SAIL).  

This project demonstrates how Django can power data-driven dashboards with interactive charts, dynamic filters, and real-time KPIs.

---

## ✨ Features

✅ Upload employee data (Excel) into the system  
✅ Filter by Department and Chart Category dynamically  
✅ Interactive **Bar**, **Pie**, and **Line Charts** using Chart.js  
✅ Clean KPI cards showing:
- Average Years Left for Retirement
- Average Experience
- Total Employees  
✅ Responsive design suitable for laptops and desktops  
✅ Built with Django views and templates for fast server-side rendering  

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Data:** Pandas for Excel parsing
- **Hosting:** Local server / can be deployed on Heroku or any Django-compatible hosting

---

Sure—here’s the **How to Run Locally** section written fully in plain text (not fenced code), so you can copy it as-is without the code blocks:

---

## 🚀 How to Run Locally

1. **Clone the repository**

   Open your terminal or command prompt and run:

   `git clone https://github.com/your-username/sail-dashboard.git`

   Then change into the project directory:

   `cd sail-dashboard`

2. **Create a virtual environment**

   In the project directory, create a virtual environment by running:

   `python -m venv venv`

   Activate the virtual environment:

   * On **Windows**:

     `venv\Scripts\activate`

   * On **MacOS / Linux**:

     `source venv/bin/activate`

3. **Install the dependencies**

   Install all required Python packages:

   `pip install -r requirements.txt`

4. **Run the database migrations**

   Prepare the Django database by running:

   `python manage.py migrate`

5. **Start the Django development server**

   Launch the server with:

   `python manage.py runserver`

6. **Open the application**

   In your web browser, go to:

   `http://127.0.0.1:8000/`

---






