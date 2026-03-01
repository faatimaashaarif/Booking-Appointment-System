# Booking & Scheduling Application

## Project Overview
This is a full-stack web application for managing appointments for services, resources, or rooms.  
Users can book, view, and cancel appointments, while admins can manage resources, view schedules, and export booking data.  

The system prevents double-booking and supports **calendar-based scheduling**.  
It uses **Flask** for the backend and **SQLite** for storage, making it lightweight and easy to deploy.

---

## Features
- **Appointment Booking:** Users can schedule appointments with:
  - Name and email
  - Resource or room
  - Date and time
- **Conflict Detection:** Prevents double-booking of resources or time slots.  
- **Admin Panel:** View all appointments, manage bookings, and resources.  
- **JSON Export:** Export all bookings for reporting or integration.  
- **SQLite Backend:** Lightweight database for storing bookings.  
- **Frontend:** Simple HTML/CSS templates for booking and admin views.  

---


## Dependencies
- Python 3.x  
- Flask

Install Flask:

pip install flask

---
## HOW To Run

python app.py

http://127.0.0.1:5000/      -> Booking page
http://127.0.0.1:5000/admin -> Admin panel
http://127.0.0.1:5000/export_json -> Export all bookings as JSON



