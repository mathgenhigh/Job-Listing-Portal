# Job Portal

A modern, responsive web application for job seekers and employers. Built with Django, this portal allows users to browse job listings, search by keyword and location, explore popular categories, and post new job opportunities.

## Features

- **Browse Jobs:** View all available job listings with detailed information.
- **Search Functionality:** Filter jobs by title, keyword, and location.
- **Popular Categories:** Quickly access jobs in Engineering, Design, Marketing, and Remote positions.
- **Recent Listings:** See the latest jobs posted by employers.
- **Job Posting:** Employers can post new job opportunities and manage their listings.
- **Responsive Design:** Optimized for desktop and mobile devices using Tailwind CSS.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Templates:** Django templating engine
- **Database:** SQLite (default, configurable)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/job_portal.git
   cd job_portal
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the app:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

- **Browse Jobs:** Click "Browse Jobs" on the homepage.
- **Search:** Use the search form to filter jobs.
- **Post a Job:** Click "Post a Job" and fill out the form (registration/login may be required).
- **View Details:** Click "View" on any job listing for more information.

## Folder Structure

```
job_portal/
├── templates/
│   ├── base.html
│   ├── home.html
│   └── ...
├── static/
│   └── ...
├── job_portal/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

