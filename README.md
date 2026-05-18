
# Student Management System - Frappe Framework

## Overview

This is a beginner-friendly backend project built using the Frappe Framework and ERPNext architecture concepts.

The goal of this project was not just to create a CRUD application, but to deeply understand:

* How Frappe works internally
* How DocTypes work
* ORM concepts
* API creation
* Validation flow
* Hooks system
* Scheduled/background jobs
* ERP-style backend architecture

This project was built as a learning journey while exploring the actual architecture used inside ERP systems.

---
About Frappe Framework

Frappe is a full-stack open-source web application framework written in Python and JavaScript. It is the framework on which ERPNext is built.

Unlike traditional backend frameworks, Frappe provides:

Built-in ORM

Automatic database table generation

REST API support

Role and permission management

Background job scheduling

Realtime events

Form and List UI generation

Workflow and ERP architecture support

Frappe follows a metadata-driven architecture where applications are mainly built using DocTypes.

---

# What I Built

## Custom DocTypes

### Student

Stores:

* Student Name
* Age
* Date of Birth
* Course
* Total Fees
* Fees Paid
* Fee Status
* Attendance

### Course

Stores:

* Course Name
* Course Duration
* Course Fees

### Fee Record

Stores:

* Student
* Amount
* Payment Date
* Payment Status

### Attendance Detail

Stores:

* Student
* Date
* Status

---

# Features Implemented

## 1. ORM Operations

Learned and implemented:

* `frappe.get_doc()`
* `frappe.new_doc()`
* `insert()`
* `save()`
* `get_all()`
* `frappe.db.commit()`

Understood how Frappe ORM converts Python objects into database records.

---

## 2. Validation Logic

Implemented custom validations inside Python controllers.

Example:

* Prevent negative fee amounts
* Validate business logic before saving documents

Used:

* `validate()`

---

# 3. REST API Development

Created custom API endpoints using:

```python
@frappe.whitelist()
```

Built API:

## REST APIs & Postman Testing

As part of this project, multiple REST APIs were built using the Frappe Framework and tested using Postman.

### APIs Implemented

#### 1. Create Student API
Creates a new student record dynamically using backend ORM methods.

Features:
- Student creation
- Automatic database insertion
- Type conversion
- Validation handling

#### 2. Get Student API
Fetches complete student details using student ID.

Returns:
- Student Name
- Age
- Course
- Total Fees
- Fees Paid
- Fee Status

#### 3. Update Student Fees API
Updates the total fees of a student and saves changes directly to the database.

#### 4. Pay Fees API
Implements fee payment workflow logic.

Features:
- Creates Fee Record automatically
- Updates student fee status
- Calculates:
  - Pending
  - Partial
  - Paid
- Uses ORM save and insert operations

#### 5. JSON-based POST API
A modern POST API was implemented using:

```python
frappe.request.json

---

# 5. Scheduler / Background Jobs

Implemented scheduled tasks using:

```python
scheduler_events
```

Created automated fee status checker task.

Executed using:

```bash
bench --site mysite.local execute student_management.tasks.check_fee_status
```

This helped understand:

* workers
* schedulers
* background execution
* automation inside ERP systems

---

# 6. Frontend + Backend Connection

Connected:

* JavaScript frontend
* Python backend APIs

Learned how:

* frontend buttons call backend APIs
* responses are returned as JSON
* Frappe connects UI and backend internally

---

# Important Concepts Learned

## ORM

Understood:

* objects
* instances
* database mapping
* save lifecycle
* validation lifecycle

---

## Frappe Architecture

Learned:

* DocType architecture
* controller flow
* hooks flow
* scheduler flow
* API flow
* request lifecycle

---

# Tech Stack

* Frappe Framework
* ERPNext
* Python
* JavaScript
* MariaDB
* Redis
* Bench CLI

---

# Biggest Learning

This project was mainly focused on understanding:

* How enterprise ERP systems are structured
* How backend frameworks automate database operations
* How APIs and ORM work internally
* How event-driven architecture works in Frappe

This was built as a hands-on deep learning project rather than only a UI-based CRUD application.

---



# Author

Govind Sarang

Learning Frappe Framework, ERP architecture, backend systems, and enterprise application development.

# Frappe Student Management System

A beginner-friendly ERP-style Student Management System built using the Frappe Framework and ERPNext architecture.

This project was created as a hands-on learning project to understand how real ERP systems work internally using:
- DocTypes
- ORM
- REST APIs
- Hooks
- Scheduler Events
- Background Workers
- Validation Lifecycle
- Business Logic

## Features

**Student Management**
- Create and manage students
- Store student details
- Link students with courses

**Course Management**
- Manage available courses
- Link courses to students

**Attendance Tracking**
- Track attendance records
- Calculate attendance percentage automatically

**Fee Management**
- Store fee records
- Track paid and pending fees
- Update fee status dynamically

## REST API

Custom API endpoint for fee payment:
`/api/method/student_management.api.pay_fees`

**Example:**
`http://127.0.0.1:8000/api/method/student_management.api.pay_fees?student_name=STUDENT_ID&amount=5000`

## Concepts Learned

This project helped in understanding:
- Frappe ORM
  - `frappe.get_doc()`
  - `insert()`
  - `save()`
  - `frappe.get_all()`
- Validation lifecycle
- Link validation
- API request flow
- Frontend ↔ Backend communication
- Hooks system
- Background workers
- Scheduler events
- Redis queue architecture
- Business logic implementation
- ERP-style workflows

## Tech Stack

- Frappe Framework
- ERPNext
- Python
- JavaScript
- MariaDB
- Redis
- WSL Ubuntu

## Project Structure

```text
student_management/
│
├── api.py
├── hooks.py
├── tasks.py
│
├── student_management/
│   └── doctype/
│       ├── student/
│       ├── course/
│       ├── fee_record/
│       └── attendance_detail/
```

## Background Scheduler Example

Implemented scheduled task using:
```python
scheduler_events = {
    "all": [
        "student_management.tasks.check_fee_status"
    ]
}
```
This automatically checks and prints student fee statuses using Frappe background workers.

## Sample ORM Usage

**Create Document**
```python
student = frappe.get_doc({
    "doctype": "Student",
    "student_name": "Govind",
    "total_fees": 50000
})

student.insert()
```

**Fetch Document**
```python
student = frappe.get_doc("Student", student_name)
```

**Update Document**
```python
student.fees_paid += amount
student.save()
```

## Learning Goals

The goal of this project was not just CRUD development, but understanding:
- how ERP systems work internally
- how Frappe architecture works
- how backend business workflows are implemented

## Current Status

Backend functionality is working:
- APIs
- ORM
- Hooks
- Scheduled jobs
- Validation
- Business logic

*Note: A frontend DocType route resolution issue was previously encountered when transitioning from custom to standard DocTypes, but has been successfully resolved.*

## Author
Govind Sarang

