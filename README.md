---

# 🚀 Project: TaskFlow AI

**A "Smart" Task Manager that uses NLP to categorize and prioritize your life.**

## 📌 Project Overview

TaskFlow is a web-based To-Do application. Unlike a standard list, TaskFlow uses an AI processing layer to automatically tag tasks by category (Work, Personal, etc.) and assign an urgency score (1-5) based on the user's input.

---

## 🛠️ Roles & Responsibilities

### 👤 The Developer

**Focus:** Web Fundamentals, CRUD Logic, and Database Management.

* **Frontend:** Create an HTML form to accept task descriptions and a clean dashboard to display them.
* **Backend:** Set up a **Flask** server with routes for:
* `GET /`: To view all tasks.
* `POST /add`: To send the task to the AI and save the result.
* `POST /toggle`: To mark tasks as complete.


* **Database:** Design and manage the **SQLite** database using the provided schema.

### 🤖 The AI Engineer

**Focus:** AI Integration, Prompt Engineering, and Data Structuring.

* **AI Logic:** Write a Python module (`ai_engine.py`) that connects to an LLM API (Gemini/OpenAI).
* **Prompt Engineering:** Design a system prompt that forces the AI to return **strict JSON** (no conversational filler).
* **Data Parsing:** Ensure the AI's response is converted into a format (like a dictionary) that her Flask app can easily read.

---

## 🔄 The Workflow (Step-by-Step)

1. **Input:** User types *"Buy milk for the kids"* into the Flask web form.
2. **Handoff:** The Flask route intercepts this string and sends it to the **AI Engine**.
3. **Processing:** * The AI Engine sends a prompt: *"Categorize this and score urgency: 'Buy milk for the kids'"*.
* The AI responds: `{"category": "Personal", "urgency": 2}`.


4. **Storage:** Flask takes the raw text + the AI's JSON and performs a `SQL INSERT` into the SQLite database.
5. **Output:** The page refreshes, showing the new task with a **[Personal]** tag and a **Priority 2** indicator.

---

## 📝 Task List (To-Be-Done)

| Phase | Task | Primary Owner |
| --- | --- | --- |
| **Setup** | Initialize Flask app and SQLite database | Developer |
| **Database** | Create `tasks` table with category/urgency columns | Developer |
| **AI Layer** | Setup API keys and basic "Hello World" AI function | AI Engineer |
| **Prompts** | Refine prompts to ensure 100% JSON accuracy | AI Engineer |
| **Integration** | Call AI function inside the `/add` Flask route | Both |
| **UI/UX** | Add CSS to color-code tasks by urgency | Developer |

---

## 💾 The Schema

```sql
-- The target for the Developer's SQL queries
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    category TEXT,
    urgency INTEGER,
    is_done BOOLEAN DEFAULT 0
);

```
