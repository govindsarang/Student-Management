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

## Pay Fees API

This API:

* Creates Fee Record
* Updates Student fees paid
* Automatically changes fee status

Possible statuses:

* Pending
* Partial
* Paid

---

# 4. Hooks System

Implemented hooks inside:

```python
hooks.py
```

Used:

* `doc_events`
* `after_insert`

Learned how Frappe automatically triggers backend logic after document actions.

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
