# Full Stack Authentication System (FastAPI + Next.js)

A robust authentication application featuring secure User Registration, Login with JWT tokens, and a protected Dashboard. Built for scalability and clean architecture.

## Tech Stack

### Backend
- **Python**
- **FastAPI**
- **SQLAlchemy** (with SQLite)
- **Pydantic**
- **Passlib** (with Bcrypt for password hashing)
- **JWT** for token-based authentication

### Frontend
- **Next.js 14** (App Router)
- **Tailwind CSS**
- **React Hooks**

## Installation

### Backend

1.  **Navigate to the project root and create a virtual environment:**
    ```bash
    python -m venv venv
    ```
    ```bash
    venv\Scripts\activate
    ```
    (On macOS/Linux, use `source venv/bin/activate`)

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the FastAPI server:**
    ```bash
    uvicorn backend.main:app --reload
    ```
    The backend API will be available at `http://127.0.0.1:8000`.
    Interactive API documentation (Swagger UI) is available at `http://127.0.0.1:8000/docs`.

### Frontend

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install the required npm packages:**
    ```bash
    npm install
    ```

3.  **Run the Next.js development server:**
    ```bash
    npm run dev
    ```
    The frontend application will be available at `http://localhost:3000`.

## Key Features

- **Secure Password Hashing**: User passwords are securely hashed using Bcrypt before being stored.
- **JWT Token Implementation**: Authentication is handled via JSON Web Tokens, ensuring secure and stateless communication between the frontend and backend.
- **Protected Routes**: The frontend dashboard is a protected route that requires a valid JWT token for access.
- **CORS Configuration**: The FastAPI backend is configured to allow requests from the frontend application.
- **Clean Architecture**: A clear separation of concerns between the frontend and backend applications.
