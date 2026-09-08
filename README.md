# 🎬 MoodMovie — Movie Recommendation by Mood

MoodMovie คือ Mini Project ระบบแนะนำภาพยนตร์ตามอารมณ์ของผู้ใช้งาน โดยผู้ใช้สามารถเลือกอารมณ์ปัจจุบัน เช่น Happy, Sad, Romantic, Excited, Bored หรือ Relaxed จากนั้นระบบจะนำอารมณ์ที่เลือกไปวิเคราะห์และแนะนำภาพยนตร์ที่เหมาะสม

โปรเจกต์นี้ถูกพัฒนาขึ้นเพื่อประยุกต์ใช้แนวคิด **OOAD (Object-Oriented Analysis and Design)** และ **OOP (Object-Oriented Programming)** ร่วมกับการพัฒนา Web Application ด้วย **Python, Flask, HTML, CSS และ JavaScript**

---

# 📌 Project Overview

ในแต่ละวัน ผู้ใช้อาจต้องการดูภาพยนตร์แต่ไม่รู้ว่าจะเลือกเรื่องไหน MoodMovie จึงถูกออกแบบมาเพื่อแก้ปัญหานี้โดยใช้ "อารมณ์ของผู้ใช้" เป็นตัวเลือกหลักในการค้นหาและแนะนำภาพยนตร์

ตัวอย่าง:

```text
User Mood: 😴 Bored

Recommended Movies:

🎬 Interstellar
Genre: Sci-Fi

🎬 Knives Out
Genre: Mystery

🎬 The Grand Budapest Hotel
Genre: Comedy
```

แนวคิดหลักของระบบคือ

```text
User
 ↓
Choose Mood
 ↓
Mood Analysis
 ↓
Recommendation Engine
 ↓
Filter Movies
 ↓
Recommended Movies
 ↓
Display on Website
```

---

# 🎯 Project Objectives

วัตถุประสงค์ของโปรเจกต์ MoodMovie ได้แก่

1. เพื่อสร้าง Web Application สำหรับแนะนำภาพยนตร์ตามอารมณ์ของผู้ใช้
2. เพื่อประยุกต์ใช้หลักการ OOAD ในการวิเคราะห์และออกแบบระบบ
3. เพื่อประยุกต์ใช้หลักการ OOP ในการพัฒนาโปรแกรมด้วย Python
4. เพื่อศึกษาการเชื่อมต่อระหว่าง Python Backend และ HTML Frontend
5. เพื่อฝึกออกแบบโครงสร้าง Software Architecture
6. เพื่อฝึกจัดการข้อมูลภาพยนตร์และระบบ Recommendation แบบพื้นฐาน
7. เพื่อสร้างเว็บไซต์ที่มี User Experience เรียบง่ายและน่าสนใจ

---

# 💡 Problem Statement

ปัจจุบันมีภาพยนตร์จำนวนมากบนแพลตฟอร์ม Streaming ทำให้ผู้ใช้อาจใช้เวลานานในการเลือกภาพยนตร์ที่ต้องการรับชม

ระบบ MoodMovie จึงเสนอแนวทางเลือกภาพยนตร์จาก

> "How are you feeling today?"

แทนการค้นหาจากชื่อภาพยนตร์หรือประเภทภาพยนตร์เพียงอย่างเดียว

ระบบจะนำ Mood ของผู้ใช้ไปจับคู่กับข้อมูลของภาพยนตร์ เพื่อสร้าง Recommendation ที่เหมาะสม

---

# 👤 Target Users

กลุ่มผู้ใช้งานหลักของ MoodMovie ได้แก่

* นักเรียนและนักศึกษา
* ผู้ที่ชื่นชอบการดูภาพยนตร์
* ผู้ใช้งาน Streaming Platform
* ผู้ที่ไม่รู้ว่าจะดูภาพยนตร์เรื่องไหน
* ผู้ที่ต้องการค้นหาภาพยนตร์ตามอารมณ์ในขณะนั้น

---

# ✨ Main Features

## 1. Mood Selection

ผู้ใช้สามารถเลือกอารมณ์ปัจจุบันได้

ตัวอย่าง Mood:

```text
😊 Happy
😢 Sad
❤️ Romantic
🔥 Excited
😴 Bored
😌 Relaxed
```

---

## 2. Movie Recommendation

ระบบจะค้นหาภาพยนตร์ที่ตรงกับอารมณ์ของผู้ใช้

ตัวอย่าง:

```text
Mood: Romantic

Recommended Movies

La La Land
About Time
The Notebook
Before Sunrise
```

---

## 3. Movie Information

ผู้ใช้สามารถดูรายละเอียดภาพยนตร์ เช่น

* Movie Title
* Poster
* Genre
* Release Year
* Description
* Rating
* Mood
* Duration

---

## 4. Movie Detail

ผู้ใช้สามารถคลิกภาพยนตร์เพื่อดูรายละเอียดเพิ่มเติม

ตัวอย่างข้อมูล:

```text
Movie: Interstellar

Genre:
Sci-Fi / Drama

Mood:
Excited / Emotional

Release Year:
2014

Rating:
8.7

Duration:
169 minutes

Description:
A team of explorers travels through a wormhole in space...
```

---

## 5. Filter by Genre

ผู้ใช้สามารถ Filter ภาพยนตร์เพิ่มเติมตามประเภท เช่น

```text
Action
Comedy
Drama
Romance
Sci-Fi
Horror
Animation
Mystery
```

---

## 6. Random Movie

ระบบสามารถสุ่มภาพยนตร์ให้ผู้ใช้ในกรณีที่ผู้ใช้ไม่รู้ว่าจะเลือกเรื่องไหน

ตัวอย่างปุ่ม:

```text
🎲 Surprise Me
```

---

# 🧠 Recommendation Concept

MoodMovie เวอร์ชัน Mini Project จะใช้ Rule-Based Recommendation System

ระบบยังไม่จำเป็นต้องใช้ Machine Learning

หลักการคือกำหนด Mood ให้กับภาพยนตร์แต่ละเรื่อง เช่น

```text
Movie
        Mood

La La Land
        Romantic

Interstellar
        Excited

Toy Story
        Happy

The Notebook
        Sad

Knives Out
        Bored
```

เมื่อผู้ใช้เลือก Mood

```text
User Mood
    ↓

RecommendationEngine
    ↓

Search Movies
    ↓

movie.mood == user_mood
    ↓

Return Movie List
```

---

# 🏗️ System Architecture

โครงสร้างของระบบแบ่งออกเป็น 3 ส่วนหลัก

```text
Frontend
   ↓
Backend
   ↓
Database
```

Architecture โดยรวม

```text
┌───────────────────────────┐
│        USER / WEB         │
│                           │
│ HTML + CSS + JavaScript   │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│       Flask Routes        │
│       Controller          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│       Business Logic      │
│                           │
│ RecommendationEngine      │
│ MovieService              │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        OOP Models         │
│                           │
│ Movie                     │
│ Mood                      │
│ Genre                     │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        Database           │
│          SQLite           │
└───────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Usage                  |
| ---------- | ---------------------- |
| Python     | Backend Programming    |
| Flask      | Web Framework          |
| HTML5      | Website Structure      |
| CSS3       | Website Design         |
| JavaScript | Frontend Interaction   |
| Jinja2     | HTML Template Engine   |
| SQLite     | Database               |
| SQLAlchemy | Database ORM           |
| Git        | Version Control        |
| GitHub     | Source Code Repository |

---

# 🎨 UI / UX Concept

MoodMovie จะใช้ Design Concept แบบ

## Cinematic Mood Interface

เน้นบรรยากาศคล้าย Streaming Platform แต่มีเอกลักษณ์จากการเลือก Mood

โทนสีหลัก:

```text
Dark Navy
Black
Purple
Soft Pink
Off White
```

หน้า Homepage สามารถแสดงข้อความ

```text
MoodMovie

Find a movie
that matches your mood.

How are you feeling today?
```

จากนั้นแสดง Mood Cards

```text
😊
Happy

😢
Sad

❤️
Romantic

🔥
Excited

😴
Bored

😌
Relaxed
```

เมื่อ Hover Card สามารถมี Animation เช่น

```text
Card Scale
Glow Effect
Gradient Background
Smooth Transition
```

---

# 🧩 OOAD — Object-Oriented Analysis and Design

OOAD ถูกใช้ในการวิเคราะห์ระบบก่อนเริ่มเขียนโปรแกรม

กระบวนการหลักประกอบด้วย

```text
Requirement Analysis
        ↓
Actor Analysis
        ↓
Use Case Analysis
        ↓
Object Identification
        ↓
Class Design
        ↓
Relationship Design
        ↓
System Implementation
```

---

# 👤 Actor

Actor หลักของระบบคือ

```text
User
```

User สามารถ

```text
Select Mood

View Recommended Movies

View Movie Detail

Filter Movies

Search Movie

Random Movie
```

---

# 📋 Use Case

Use Case หลักของระบบ

```text
                MoodMovie

                   │
                   │
                  User
                   │
        ┌──────────┼───────────┐
        │          │           │
        ▼          ▼           ▼

   Select Mood   Search     Filter Movie

        │
        ▼

 Get Recommendation

        │
        ▼

   View Movie

        │
        ▼

 View Movie Detail
```

---

# 🔍 Object Identification

จากการวิเคราะห์ระบบ สามารถระบุ Object หลักได้ดังนี้

```text
User

Movie

Mood

Genre

RecommendationEngine

MovieService

DatabaseManager
```

---

# 🧱 Main Classes

## Movie

ใช้สำหรับเก็บข้อมูลภาพยนตร์

Attributes:

```text
id
title
description
release_year
rating
duration
poster
mood
genre
```

Methods:

```text
get_detail()

match_mood()

get_rating()
```

---

## Mood

ใช้แทนอารมณ์ของผู้ใช้

Attributes:

```text
id
name
emoji
description
```

ตัวอย่าง Object:

```text
Mood(
    name="Happy",
    emoji="😊"
)
```

---

## Genre

ใช้เก็บประเภทภาพยนตร์

Attributes:

```text
id
name
```

ตัวอย่าง:

```text
Action
Comedy
Drama
Romance
Sci-Fi
```

---

## RecommendationEngine

Class สำหรับประมวลผล Recommendation

Responsibilities:

```text
Receive Mood

Search Movie

Compare Mood

Filter Result

Return Recommendation
```

---

## MovieService

ทำหน้าที่จัดการ Business Logic ที่เกี่ยวข้องกับ Movie

ตัวอย่าง Methods:

```text
get_all_movies()

get_movie_by_id()

search_movie()

filter_by_genre()

get_movie_by_mood()
```

---

# 📐 Class Diagram

```text
+----------------------+
|        Movie         |
+----------------------+
| id                   |
| title                |
| description          |
| rating               |
| year                 |
| duration             |
| poster               |
+----------------------+
| get_detail()         |
| match_mood()         |
+----------+-----------+
           |
           |
           ▼
+----------------------+
|        Mood          |
+----------------------+
| id                   |
| name                 |
| emoji                |
| description          |
+----------------------+


+---------------------------+
| RecommendationEngine      |
+---------------------------+
| movies                    |
+---------------------------+
| recommend_by_mood()       |
| random_movie()            |
+---------------------------+


+---------------------------+
| MovieService              |
+---------------------------+
| get_all_movies()          |
| search_movie()            |
| get_movie_by_id()         |
| filter_by_genre()         |
+---------------------------+
```

---

# 🧑‍💻 OOP Concepts Used

โปรเจกต์ MoodMovie ใช้หลัก OOP หลายรูปแบบ

---

## 1. Class

Class คือแม่แบบสำหรับสร้าง Object

ตัวอย่าง

```python
class Movie:

    def __init__(
        self,
        title,
        genre,
        mood,
        rating
    ):
        self.title = title
        self.genre = genre
        self.mood = mood
        self.rating = rating
```

---

# 2. Object

Object คือ Instance ที่ถูกสร้างจาก Class

```python
movie = Movie(
    "Interstellar",
    "Sci-Fi",
    "Excited",
    8.7
)
```

---

# 3. Encapsulation

ใช้รวบรวมข้อมูลและพฤติกรรมของ Object ไว้ภายใน Class

```python
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self.__rating = rating

    def get_rating(self):
        return self.__rating
```

---

# 4. Abstraction

RecommendationEngine ซ่อนรายละเอียดการค้นหาและคัดเลือกภาพยนตร์จากผู้ใช้งาน

```python
class RecommendationEngine:

    def recommend(self, movies, mood):

        return [
            movie
            for movie in movies
            if movie.mood == mood
        ]
```

ผู้ใช้ไม่จำเป็นต้องรู้ว่าระบบค้นหาภาพยนตร์อย่างไร

เพียงส่ง Mood ให้ระบบ

```python
engine.recommend(
    movies,
    "Happy"
)
```

---

# 5. Inheritance

สามารถสร้าง Movie ประเภทต่าง ๆ ผ่าน Base Class ได้

```python
class Movie:

    def __init__(self, title):
        self.title = title


class TrendingMovie(Movie):

    def __init__(self, title, rank):
        super().__init__(title)

        self.rank = rank
```

---

# 6. Polymorphism

Class แต่ละประเภทสามารถมี Method เดียวกันแต่ทำงานแตกต่างกันได้

```python
class RecommendationStrategy:

    def recommend(self, movies):
        pass


class MoodRecommendation(
    RecommendationStrategy
):

    def recommend(self, movies):
        return movies


class RatingRecommendation(
    RecommendationStrategy
):

    def recommend(self, movies):

        return sorted(
            movies,
            key=lambda movie: movie.rating,
            reverse=True
        )
```

---

# 🔄 System Flow

การทำงานของระบบหลัก

```text
START

 ↓

Open MoodMovie

 ↓

Select Mood

 ↓

Send Mood to Flask

 ↓

Flask Route

 ↓

RecommendationEngine

 ↓

MovieService

 ↓

Database

 ↓

Filter Movies

 ↓

Return Movie Objects

 ↓

Jinja Template

 ↓

Display Recommended Movies

 ↓

END
```

---

# 🌐 Web Application Flow

ตัวอย่างเมื่อ User เลือก Mood = Happy

```text
User Click

😊 Happy

      ↓

HTML Form

      ↓

POST /recommend

      ↓

Flask

      ↓

RecommendationEngine

      ↓

recommend_by_mood("happy")

      ↓

SQLite Database

      ↓

Movies

      ↓

Flask render_template()

      ↓

recommend.html

      ↓

User sees recommendations
```

---

# 🗄️ Database Design

Database หลักสามารถประกอบด้วย

```text
movies

moods

genres
```

---

# 🎬 Movies Table

| Field       | Type    | Description       |
| ----------- | ------- | ----------------- |
| id          | Integer | Movie ID          |
| title       | String  | Movie Name        |
| description | Text    | Movie Description |
| year        | Integer | Release Year      |
| rating      | Float   | Movie Rating      |
| duration    | Integer | Duration          |
| poster      | String  | Poster URL        |
| mood_id     | Integer | Mood              |
| genre_id    | Integer | Genre             |

---

# 😊 Moods Table

| Field       | Type    | Description      |
| ----------- | ------- | ---------------- |
| id          | Integer | Mood ID          |
| name        | String  | Mood Name        |
| emoji       | String  | Mood Emoji       |
| description | String  | Mood Description |

ตัวอย่างข้อมูล:

```text
1 | Happy     | 😊
2 | Sad       | 😢
3 | Romantic  | ❤️
4 | Excited   | 🔥
5 | Bored     | 😴
6 | Relaxed   | 😌
```

---

# 🎭 Genres Table

| Field | Type    |
| ----- | ------- |
| id    | Integer |
| name  | String  |

ตัวอย่าง

```text
Action

Comedy

Drama

Romance

Sci-Fi

Mystery

Animation
```

---

# 📁 Project Structure

```text
moodmovie/
│
├── app.py
│
├── config.py
│
├── requirements.txt
│
├── README.md
│
│
├── models/
│   │
│   ├── __init__.py
│   ├── movie.py
│   ├── mood.py
│   └── genre.py
│
├── services/
│   │
│   ├── __init__.py
│   ├── movie_service.py
│   └── recommendation_service.py
│
├── routes/
│   │
│   ├── __init__.py
│   ├── main_routes.py
│   └── movie_routes.py
│
├── database/
│   │
│   ├── database.py
│   └── moodmovie.db
│
├── templates/
│   │
│   ├── base.html
│   ├── index.html
│   ├── recommend.html
│   ├── movies.html
│   └── movie_detail.html
│
├── static/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── images/
│       └── posters/
│
└── tests/
    │
    ├── test_movie.py
    └── test_recommendation.py
```

---

# 🔌 Example Flask Connection

ตัวอย่างการเชื่อม Python กับ HTML

```python
from flask import (
    Flask,
    render_template,
    request
)

from services.recommendation_service import (
    RecommendationService
)

app = Flask(__name__)

recommendation_service = RecommendationService()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/recommend",
    methods=["POST"]
)
def recommend():

    mood = request.form.get("mood")

    movies = (
        recommendation_service
        .recommend_by_mood(mood)
    )

    return render_template(
        "recommend.html",
        mood=mood,
        movies=movies
    )


if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🖥️ Example HTML

หน้าเลือก Mood

```html
<form
    action="/recommend"
    method="POST"
>

    <button
        type="submit"
        name="mood"
        value="happy"
    >
        😊

        Happy
    </button>

    <button
        type="submit"
        name="mood"
        value="sad"
    >
        😢

        Sad
    </button>

    <button
        type="submit"
        name="mood"
        value="romantic"
    >
        ❤️

        Romantic
    </button>

</form>
```

---

# 🎬 Recommendation Template

```html
<h1>
    Movies for {{ mood }}
</h1>

<div class="movie-grid">

    {% for movie in movies %}

        <div class="movie-card">

            <img
                src="{{ movie.poster }}"
                alt="{{ movie.title }}"
            >

            <h2>
                {{ movie.title }}
            </h2>

            <p>
                ⭐ {{ movie.rating }}
            </p>

            <p>
                {{ movie.genre }}
            </p>

        </div>

    {% endfor %}

</div>
```

---

# 🗺️ Main Routes

| Route            | Method | Description      |
| ---------------- | ------ | ---------------- |
| `/`              | GET    | Homepage         |
| `/recommend`     | POST   | Recommend movies |
| `/movies`        | GET    | All movies       |
| `/movie/<id>`    | GET    | Movie detail     |
| `/search`        | GET    | Search movies    |
| `/genre/<genre>` | GET    | Filter genre     |
| `/random`        | GET    | Random movie     |

---

# 📱 Main Pages

ระบบประกอบด้วยหน้าเว็บไซต์หลักดังนี้

## Homepage

```text
index.html
```

หน้าสำหรับเลือก Mood

---

## Recommendation Page

```text
recommend.html
```

แสดงภาพยนตร์ที่ระบบแนะนำ

---

## Movie List

```text
movies.html
```

แสดงภาพยนตร์ทั้งหมด

---

## Movie Detail

```text
movie_detail.html
```

แสดงข้อมูลของภาพยนตร์แต่ละเรื่อง

---

# 🔐 Scope of Mini Project

เพื่อให้เหมาะกับ Mini Project ระบบเวอร์ชันแรกจะประกอบด้วย

```text
Mood Selection

Movie Recommendation

Movie List

Movie Detail

Genre Filter

Random Movie

SQLite Database

Responsive Website
```

ระบบจะยังไม่รวม

```text
User Login

Payment

Streaming

Advanced AI

Machine Learning Recommendation

Social Network Features
```

เพื่อลดความซับซ้อนของโปรเจกต์

---

# 🚀 Installation

Clone Project

```bash
git clone <repository-url>

cd moodmovie
```

สร้าง Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

ตัวอย่าง `requirements.txt`

```text
Flask
Flask-SQLAlchemy
```

---

# ▶️ Run Application

```bash
python app.py
```

จากนั้นเปิด Browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Example Scenario

ตัวอย่างสถานการณ์การใช้งาน

```text
User เปิดเว็บไซต์

        ↓

ระบบถาม

"How are you feeling today?"

        ↓

User เลือก

😌 Relaxed

        ↓

ระบบส่งข้อมูล Relaxed
ไปยัง Flask Backend

        ↓

RecommendationEngine
ค้นหาภาพยนตร์

        ↓

Database ส่ง Movie List

        ↓

ระบบแสดง

Spirited Away
The Secret Life of Walter Mitty
About Time

        ↓

User เลือก Movie

        ↓

ดู Movie Detail
```

---

# 🎓 Concepts Demonstrated

โปรเจกต์นี้แสดงความเข้าใจในหัวข้อต่อไปนี้

### Object-Oriented Analysis

```text
Requirement Analysis
Actor
Use Case
Object Identification
```

### Object-Oriented Design

```text
Class Design
Relationship
Architecture
Responsibility
```

### Object-Oriented Programming

```text
Class
Object
Attribute
Method
Encapsulation
Abstraction
Inheritance
Polymorphism
```

### Python

```text
Variable
Function
List
Dictionary
Loop
Condition
Class
Object
Module
Package
Import
Exception Handling
```

### Web Development

```text
Client
Server
HTTP Request
HTTP Response
GET
POST
Routing
Template
Database
```

---

# 🔮 Future Development

MoodMovie สามารถพัฒนาต่อได้หลายรูปแบบ เช่น

1. User Account
2. Favorite Movies
3. Watchlist
4. Movie History
5. Movie Rating
6. Advanced Search
7. Recommendation History
8. External Movie API
9. Machine Learning Recommendation
10. Personalized Recommendation
11. Dark / Light Theme
12. Movie Trailer
13. Streaming Platform Link

---

# 🤖 Future AI Recommendation

ในอนาคตสามารถเปลี่ยน Rule-Based Recommendation เป็น AI Recommendation ได้

ตัวอย่างข้อมูลที่สามารถนำมาวิเคราะห์

```text
User Mood

Favorite Genre

Movie History

Movie Rating

Watch Time

Favorite Actor

Previous Selection
```

จากนั้นสร้าง Personalized Recommendation เช่น

```text
User Profile
      ↓

Recommendation Model
      ↓

Movie Score
      ↓

Top Recommendations
```

---

# ✅ Expected Result

หลังจากพัฒนาโปรเจกต์เสร็จ ระบบ MoodMovie จะสามารถ

```text
✓ รับ Mood จากผู้ใช้

✓ วิเคราะห์ Mood

✓ ค้นหาภาพยนตร์

✓ แนะนำภาพยนตร์ที่เหมาะสม

✓ แสดงข้อมูลภาพยนตร์

✓ Filter ตาม Genre

✓ เชื่อม Python กับ HTML

✓ จัดเก็บข้อมูลด้วย Database

✓ ใช้หลัก OOAD

✓ ใช้หลัก OOP
```

---

# 📌 Project Summary

**MoodMovie** เป็น Web Application สำหรับแนะนำภาพยนตร์จากอารมณ์ของผู้ใช้ โดยใช้ Python และ Flask เป็น Backend และใช้ HTML, CSS และ JavaScript เป็น Frontend

ระบบใช้แนวคิด **OOAD** ในการวิเคราะห์ Requirement, Actor, Use Case, Object และ Class ก่อนนำไปพัฒนาด้วยแนวคิด **OOP**

โครงสร้างของระบบถูกแบ่งออกเป็นส่วนต่าง ๆ ได้แก่

```text
Presentation Layer
        ↓
Controller
        ↓
Service Layer
        ↓
Model
        ↓
Database
```

ซึ่งช่วยให้ Source Code มีโครงสร้างที่เป็นระเบียบ สามารถดูแล แก้ไข และพัฒนาต่อยอดได้ง่าย

MoodMovie จึงเป็น Mini Project ที่เหมาะสำหรับแสดงความเข้าใจเรื่อง

> **OOAD + OOP + Python + Flask + HTML/CSS + Database**

ภายใต้ระบบที่มีขนาดไม่ใหญ่เกินไป แต่สามารถนำเสนอแนวคิด Software Design และ Object-Oriented Programming ได้อย่างชัดเจน

---

# 🎬 MoodMovie

> **Find a movie that matches your mood.**

Built with ❤️ using Python, Flask and Object-Oriented Programming.
