# VTF Server

![image](https://user-images.githubusercontent.com/26861798/195433997-4f68e840-e5bd-446b-99c5-456bd8e7b105.png)

Virtually Testing is a California, USA based 501(c)3 volunteer-run nonprofit organization. Our foundation is funded by individuals or corporate or government donations. Our mission is to serve a cybersecurity focused community by organizing speaker events, hands-on workshops, conferences, etc. Our members advance their skills or learn from scratch to successfully access the competitive trending and evolving cybersecurity industry.

## URL

https://vtf-server.onrender.com/

## How it works

### Pre-requisites and Local Development

Developers using this project should already have or install:

- python3
- virtual environment
- Create a virtual environment (Linux commands given below. Please find the equivalent Windows commands)

```
python3 -m venv ~/<nameOfVirtualEnvironment>

```

- Activate the virtual Environment created (Linux commands given below. Please find the equivalent Windows commands)

```
source  ~/<nameOfVirtualEnvironment>/bin/activate
```

### Installed Libraries

Check the `requirements.txt` file to see the libraries. Simply run the below command to install all libraries at once.

```
pip3 install -r requirements.txt
```

### Run the Test

run the following accordingly in the terminal

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py test

```

However, run the first and second command only once except you have made changes to the `model.py` file, then you can run them accordingly before retarting your application.
A successful test will look like this:

<img width="573" alt="Screen Shot 2022-10-12 at 9 16 34 PM" src="https://user-images.githubusercontent.com/26861798/195439378-12d8fa9f-bdbe-4a05-8a3b-fe58330ec150.png">

### Start the Application

run the following accordingly in the terminal

```
python3 manage.py runserver

```

Your application should run on http://127.0.1.0:8000 as shown below:

<img width="1189" alt="Screen Shot 2022-10-12 at 9 17 39 PM" src="https://user-images.githubusercontent.com/26861798/195439575-b3ac767f-777a-44b2-87e1-9f7dde8d3bd0.png">

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "status": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable
500: Internal Server Error
405: Method Not Allowed

### Endpoints

**GET /isaca-events**

General:

- an endpoint to handle GET requests for all available/ongoing ISACA events.

Sample: `curl http://127.0.0.1:8000/isaca-events`

```
{
    "success": true,
    "status": 200,
    "events": [
        {
            "id": 1,
            "title": "Introduction Business",
            "message": "All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.",
            "day": "09 Nov, 2022",
            "ongoing": true,
            "month": "November",
            "time": "2:00 PM PST"
        },
        {
            "id": 2,
            "title": "Marketing Strategy",
            "message": "All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.",
            "day": "12 Oct, 2022",
            "ongoing": true,
            "month": "October",
            "time": "4:00 PM WAT"
        }
    ]
}
```

**POST /vtf-speaker-signup**

General:

- an endpoint to POST/ register a new Speaker, which will require the firstname, email, lastname and user password

Sample: `curl http://127.0.0.1:5000/vtf-speaker-signup -X POST -H "Content-Type: application/json" -d '{"firstname": "Daniel","lastname": "Testing","email": "testing@vtf.com","password": "test123"}'`

```
{
    'success': True,
    'status': 201,
    'message': 'The registration was successful.'
}
```

## Author

[Daniel Olagunju](https://github.com/todak2000)
