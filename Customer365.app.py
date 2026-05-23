import streamlit as st
from openai import OpenAI
import os
# משיכת המפתח מההגדרות המאובטחות שהגדרנו ב-Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("מנתח החברות האישי שלך")
company = st.text_input("הכנס שם חברה:")
# ... המשך הקוד כפי שהיה
import streamlit as st
from openai import OpenAI

# הגדרת הכותרת
st.title("מנתח החברות האישי שלך")
api_key = st.text_input("הכנס את מפתח ה-API שלך כאן:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    company = st.text_input("הכנס שם חברה:")
    
    if st.button("חפש מידע"):
        with st.spinner('אוסף נתונים ומנתח...'):
            prompt = f"ספק ניתוח מפורט על החברה: {company}. כולל: עיסוק, תחומי עניין, לקוחות מרכזיים, מיקום בשוק, חוזקות ומשברים משמעותיים."
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response.choices[0].message.content)
