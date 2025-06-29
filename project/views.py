# project/views.py
from flask import render_template, request, redirect, url_for
from project import app, db
from project.forms import TextCorrectionForm
from project.models import Correction
import requests
import os




# home page ---------------- 

@app.route("/", methods=["GET", "POST"])
def home():

    form = TextCorrectionForm()
    correction = None
    no_changes = False

    if form.validate_on_submit():
        original_text = form.text.data

        # call deepseek API
        api_response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek/deepseek-r1-0528:free",
                "messages": [
                    {"role": "user", "content": f"Return ONLY the corrected text, nothing else: '{original_text}'"}
                ]
            }
        )
        
        # extract corrected text and clean it
        corrected_text = api_response.json()["choices"][0]["message"]["content"].strip()
        original_text_clean = original_text.strip()

        # check if text was changed (case-insensitive)
        no_changes = corrected_text.lower() == original_text_clean.lower()
        
        # save to database
        correction = Correction(
            original_text=original_text,
            corrected_text=corrected_text
        )
        db.session.add(correction)
        db.session.commit()
        
        
    return render_template("home.html", form=form, correction=correction, no_changes=no_changes)
    




# history page ---------------- 

@app.route("/history")
def history():
    corrections = Correction.query.order_by(Correction.date.desc()).all()
    return render_template("history.html", corrections=corrections)

