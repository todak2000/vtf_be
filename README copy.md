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

**DELETE /questions/{question_id}**

General:

- Deletes the question of the given ID if it exists. Returns success value.

Sample `curl -X DELETE http://127.0.0.1:5000/questions/16 `

```
{
    "success": true,
    "deleted": 16,
    "message":"Question with ID: 16 has been deleted successfully",
    "questions": [],
    "total_questions": 10,
    "categories":{}
}
```

**GET /vtf-speaker-signup**

General:

- an endpoint to handle POST requests for the VTF Speaker app Registration. It allows

Sample: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": None,
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 108
}
```

**POST /questions**

General:

- an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score

Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"How many states make up the United States of America?", "answer": "52","category" :"1", "difficulty":"2"}'`

```
{
  "created": 87,
  "current_category": "1",
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 108
}
```

**POST /questions/search**

General:

- endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.

Sample `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"who"}'`

```
{
  "current_category": None,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Alexander Fleming",
      "category": "1",
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

**GET /categories/{category_id}/questions**

General:

- a GET endpoint to get questions based on category.

Sample: `curl http://127.0.0.1:5000/categories/3/questions`

```
{
  "current_category":"3",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

**POST /quizzes**

General:

- a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.

Sample` curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Geography","id":"3"}, "previous_questions":[13, 54]}'`

```
{
  "question": {
    "answer": "Agra",
    "category": "3",
    "difficulty": 2,
    "id": 15,
    "question": "The Taj Mahal is located in which Indian city?"
  },
  "success": true
}
```

## Author

[Daniel Olagunju](https://github.com/todak2000)
