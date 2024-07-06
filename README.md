# Excalibur FRC Scouting System

This is a Flask web application designed for the Excalibur FRC team to facilitate scouting and data collection. The app includes features for user registration, login, profile management, scouting data submission, and QR code scanning for data input.

## Features

- **User Authentication**: Registration and login functionality with password hashing.
- **Profile Management**: Users can upload profile pictures and view their profile details.
- **Scouting Data Submission**: Users can submit scouting data via a form.
- **QR Code Scanning**: Users can scan QR codes to input data directly into the system.

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtualenv

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/excalibur-frc-scouting.git
    cd excalibur-frc-scouting
    ```

2. **Set up a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the Flask app configuration**:
    - Ensure you have the following files and directories created:
        - `users.json`: To store user data.
        - `contacts.json`: To store contact data.
        - `static/Data.JSON`: To store scouting data.
        - `static/profiles`: Directory to store user profile pictures.

    ```bash
    touch /home/yehudarothstein/mysite/users.json
    touch /home/yehudarothstein/mysite/contacts.json
    touch /home/yehudarothstein/mysite/static/Data.JSON
    ```

    Initialize these files with an empty array:
    ```json
    []
    ```

5. **Run the Flask app**:
    ```sh
    flask run
    ```

## Configuration

- **User Data File**: `/home/yehudarothstein/mysite/users.json`
- **Contacts Data File**: `/home/yehudarothstein/mysite/contacts.json`
- **Scouting Data File**: `/home/yehudarothstein/mysite/static/Data.JSON`
- **Profile Pictures Folder**: `/home/yehudarothstein/mysite/static/profiles`

## File Structure

- Excalibur-frc-scouting/
- ├── app.py
- ├── templates/
- │ ├── register.html
- │ ├── login.html
- │ ├── profile.html
- │ ├── scout.html
- │ ├── report.html
- │ ├── scan-qr.html
- │ ├── home.html
- │ ├── sponsors.html
- │ ├── projects.html
- │ ├── contacts.html
- │ └── layout.html
- ├── static/
- │ ├── css/
- │ │ └── scout.css
- │ ├── profiles/
- │ ├── Data.JSON
- ├── requirements.txt
- └── README.md


## Usage

### User Registration and Login

1. **User Registration**:
    - Navigate to `/register` to create a new account.
    - Provide a username, password, full name, and job title.
    - Upon successful registration, log in using your new credentials.

2. **User Login**:
    - Navigate to `/login` to access your account.
    - Enter your username and password to log in.

### Profile Management

- After logging in, navigate to `/profile` to upload a profile picture and view your profile details.

### QR Code Scanning

1. **Scan QR Code**:
    - Go to `/scan-qr`.
    - Use the QR code scanner to scan a code.
    - The scanned data will be automatically submitted and saved to the system.

### Scouting

- Navigate to `/scout` to submit scouting data using the provided form.
- Fill in the necessary details and submit the form.
- The data will be saved to the `Data.JSON` file.

### Bug Reporting

- Navigate to `/report-bugs` to report any issues or bugs encountered.
- Fill in the form with relevant details and submit your report.

### Viewing Sponsors, Contacts, and Projects

- **Sponsors**: Navigate to `/sponsors` to view a list of sponsors.
- **Contacts**: Navigate to `/contacts` to view team contact information.
- **Projects**: Navigate to `/projects` to view team projects.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
