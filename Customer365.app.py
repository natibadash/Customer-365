# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI
import os

# משיכת המפתח מהסודות שהגדרת ב-Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("מנתח החברות האישי שלך")

# הוספנו מפתח (key) כדי למנוע את שגיאת ה-DuplicateElementId
company = st.text_input("הכנס שם חברה:", key="company_input_field")

if company:
    if st.button("חפש מידע"):
        with st.spinner('אוסף נתונים ומנתח...'):
            try:
                prompt_text = f"ספק ניתוח מפורט על החברה: {company}. כולל: עיסוק, תחומי עניין, לקוחות מרכזיים, מיקום בשוק, חוזקות ומשברים משמעותיים."
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt_text}]
                )
                
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"קרתה שגיאה בחיבור ל-AI: {e}")
