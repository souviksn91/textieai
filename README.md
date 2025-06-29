# TextieAI - Grammar Correction App
#### TextieAI is an AI-powered, lightweight Flask web app that improves your writing. 

![Image](https://github.com/user-attachments/assets/1f28d7cd-4fec-40c9-aa0b-d429f3330a4b)

## Features
- **Instant Grammar Fixes:** Corrects spelling, punctuation, and syntax.
- **History Tracking:** Saves all corrections for future reference.
- **Clean Output:** Returns only the polished text, no extra explanations.
- **Simple Interface:** Minimal design focused on usability.
- **Character Limit:** Prevents overly long inputs (max 30 words).


## Technologies
- **Backend:** Python, Flask
- **Database:** MySQL (via SQLAlchemy)
- **AI API:** DeepSeek-R1 (free via OpenRouter)
- **Frontend:** HTML, CSS, Bootstrap

<hr>

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/souviksn91/textieai.git
   cd textieai
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
    Create MySQL database (see DATABASE.md)

5. **Run the app:**
   ```bash
   python app.py
   ```
6. **Access in browser:**
   http://127.0.0.1:5000/


