
# Gym Reservation Bot

An automated gym slot booking system built using Python and Selenium WebDriver.

## Project Overview

Gym Reservation Bot automates the process of logging into a gym booking website, selecting a preferred date and time slot, and confirming a reservation.

## Features

- Automated browser control using Selenium
- Automatic login form filling
- Gym booking date selection
- Time slot selection
- Booking confirmation verification
- Automatic screenshot generation
- Error handling and browser cleanup

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- python-dotenv
- HTML and JavaScript

## Project Structure

gym_bot/
│
├── bot.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
├── gym_booking_demo.html
└── README.md

## Installation

1. Install Python.
2. Install Google Chrome.
3. Open the project folder in VS Code.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure your `.env` file.

## Environment Variables

Create a `.env` file containing:

```env
GYM_BOOKING_URL=your_booking_url
GYM_USERNAME=your_username
GYM_PASSWORD=your_password
BOOKING_DATE=2026-11-10
TIME_SLOT_TEXT=11:00 AM
HEADLESS=false
```

## Run the Project

```bash
python bot.py
```

## Output

The bot automatically performs the login and booking workflow and saves a screenshot named `booking_confirmation.png`.

## Disclaimer

This project currently uses a local HTML demo website to simulate gym reservations. It does not make real gym reservations.

## Author

Asesh Kumar Mondal
B.Tech CSE (AIML)
