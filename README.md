# Calendar Schedule Management API

## Link:- https://schedulemgmt.herokuapp.com/

This is a Calendar Schedule Management API for Users

Following are the features provided:
1. Users can register themselves with a unique username and emailId along with strong password.
2. Users can create their own events by providing event date and title.
3. Session Authentication has been applied so that a user will only be able to see his/her events when he/she is authentcated , plus    only owner of an event will be able to see or make any changes to the event.
4. A user can Login, Logout, Create, Update and Delete scheduled Events.

```
Flow of Links for API :-

    baseUrl = https://schedulemgmt.herokuapp.com
    
    Home Page = baseUrl (returns links to "users list", "events list", "registration list")
    User Registration = baseUrl/users/register/ ("username", "email", "password")
    Login = baseUrl/login    (Login)
    Logout = baseUrl/logout  (Logout)
    List of Events = baseUrl/events (User must be authenticated)
    Create Event    = baseUrl/events (Send a Post request with following data {"title", "event_date"(YYYY-MM-DD)})
    Detail of an Event = baseUrl/events/<event_id>  (Authentication required)+(User must be owner of the event)
    Update an Event = baseUrl/event/<event_id> (PUT request with following data {"title", "event_date"})
    Delete an Event = baseUrl/event/<event_id> (DELETE request)
    
``` 

Instructions to access API's

>1. USER REGISTRATION:
```
https://schedulemgmt.herokuapp.com/users/register 
POST Request :-  
  {
    "username" : (must be unique)
    "email" : (must be unique)
    "password" : (Should be of minimum 8 characters)
  }

```
  
>2. HOME PAGE:

```
https://schedulemgmt.herokuapp.com 
GET request allowed will return following data

{
    "users": "https://schedulemgmt.herokuapp.com/users/",
    "events": "https://schedulemgmt.herokuapp.com/events",
    "register": "https://schedulemgmt.herokuapp.com/users/register/"
}

```

>3. USERS LIST:

```
https://schedulemgmt.herokuapp.com/users/ 

Accepts GET request and returns all registered users, following information is returned

{
        "url": "https://schedulemgmt.herokuapp.com/users/2/",
        "id": 2,
        "username": "dummyuser"
}

```

>4. USER DETAIL:

```
https://schedulemgmt.herokuapp.com/users/<user_id>

Accepts GET request and returns detail of a user

{
    "url": "https://schedulemgmt.herokuapp.com/users/2/",
    "id": 2,
    "username": "dummyuser"
}

```


>5. EVENT LIST + CREATE NEW EVENT:

```
https://schedulemgmt.herokuapp.com/events

GET :- Returns list of all the events created by requesting user
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "url": "https://schedulemgmt.herokuapp.com/events/4/",
        "title": "Anniversary",
        "event_date": "2020-06-13",
        "author": "https://schedulemgmt.herokuapp.com/users/2/",
        "author_name": "dummyuser"
    }
]

POST :- Creates a new event for the requesting user
input type:

{
    "title": "",
    "event_date": (Must be in YYYY-MM-DD formate)
}

If user is not logged in he/she will recieve a "Authentication required" message
```

>6. EVENT DETAIL + UPDATE EVENT + DELETE EVENT:

```
https://schedulemgmt.herokuapp.com/events/<event_id>

GET request (To fetch event details):
Response example:
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "url": "https://schedulemgmt.herokuapp.com/events/4/",
    "title": "Anniversary",
    "event_date": "2020-06-13",
    "author": "https://schedulemgmt.herokuapp.com/users/2/",
    "author_name": "dummyuser"
}

PUT request (To update event):
input formate:
{
    "title": "",
    "event_date": (Must be in YYYY-MM-DD formate)
}

DELETE request (will delete event):
response type:
Event Detail not found

```

>7. LOGIN: 
```
https://schedulemgmt.herokuapp.com/login
{
    "username":
    "password":
}

```

>8. LOGOUT:

```
https://schedulemgmt.herokuapp.com/logout

```
  
Since session athentication has been implemented you need to provide login details every time you access events using command prompt


example:- curl -H 'Accept: application/json; indent=4' -u username:password https://schedulemgmt.herokuapp.com/events
