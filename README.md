## **Setup Instructions**

### **Step 1: Clone the Repository**

bash
git clone <repository-url>
cd <repository-directory>

### Step 2: Create a Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### Step 3: Install Dependencies

    pip install django djangorestframework

### Step 4: Run Migrations

    python manage.py makemigrations
    python manage.py migrate

### Step 5: Create SuperUser
    python manage.py createsuperuser
access the admin panel by going to '/admin/' and login using the credentials you just made.

### Step 6 :Run The Development Server
    python manage.py runserver

## **Current Features**
### Event Management

- Create an Event: Add a new event.
- Update an Event: Modify an existing event.
- List Events: Get a list of all events.
- Event Details: View details of a specific event.
- Delete an Event: Remove an event.
- Register for an event.

### Attendance Management

- View Attendance: Check the attendance of an event.
- Edit Attendance: Update the attendance details.

### Feedback

  _note:  Feedback can only be created if attendance is marked as True.<br>_
  - Create Feedback: Add feedback for an event.<br>
  - View Feedback: Retrieve feedback for a specific event.<br>
##  **API ENDPOINTS**
### **Event Management**
| HTTP Method | Endpoint                              | Description                  |
|-------------|---------------------------------------|------------------------------|
| POST        | `/api/events/create/`                    | Create an event.             |
| PUT         | `/api/event/update/<int:eventId>/`       | Update an event.             |
| GET         | `/api/events/all/`                       | List all events.             |
| GET         | `/api/events/<int:eventId>/`             | View event details.          |
| DELETE      | `/api/events/<int:eventId>/delete/`      | Delete an event.             |
| POST        | `/api/events/register/<int:eventId>/`    | Register for a specific event.|


### **Attendance Management**
| HTTP Method | Endpoint                                     | Description               |
|-------------|----------------------------------------------|---------------------------|
| GET         | `/api/events/attendance/view/<int:eventId>/`    | View attendance.          |
| PUT         | `/api/events/attendance/edit/<int:eventId>/`    | Edit attendance.          |

### **Feedback**
| HTTP Method | Endpoint                                     | Description               |
|-------------|----------------------------------------------|---------------------------|
| POST        | `/api/events/feedback/<int:registrationId>/`    | Create feedback.          |
| GET         | `/api/events/feedback/view/<int:eventId>/`      | View feedback for an event.|

