## Payroll & Commission Engine (PACE)

PACE is a Python-based tool designed to streamline and automate the calculation of commissions based on predefined percentages. It provides an intuitive interface for managing payroll-related commission structures.

### Getting Started

To run the application locally, you will first need to clone the repository to your local machine.

#### Prerequisites

Ensure you have Python installed. You can check the installation using:
```bash
python --version
```

Next, install the required dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Running the Application

Once the dependencies are installed, you can launch the application from your terminal by navigating to the project root directory and running the following command:
```bash
streamlit run src/app.py
```

The application will open in your default web browser at a local address (typically http://localhost:8501).

## Deployment

PACE is a Streamlit application. Deployment is handled by the streamlit service itself and is currently deployed. Deployment is automated based on changes to this repo mased on main branch