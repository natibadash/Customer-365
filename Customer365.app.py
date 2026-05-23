# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

# משיכת המפתח מהסודות
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("לא הוגדר מפתח API תקין ב-Secrets.")
    st.stop()

st.title("מנתח החברות האישי שלך")

# קלט מהמשתמש
company = st.text_input("הכנס שם חברה:", key="company_input_field")

if st.button("חפש מידע"):
    if company:
        with st.spinner('מנתח נתונים...'):
            try:
                # יצירת הבקשה באנגלית כדי למנוע שגיאות קידוד
                # אנחנו לא שולחים עברית בשם החברה ל-API כדי להיות בטוחים
                prompt_text = f"Provide a business analysis for the company: {company}. Include: main business, core activities, key customers, market position, strengths, and major crises. Respond in Hebrew."
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt_text}]
                )
                
                # הצגת התשובה
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                # במקרה של שגיאה, נציג הסבר פשוט
                st.error("קרתה שגיאה. נסה להזין שם של חברה גדולה ומוכרת (למשל: Apple, Nvidia, Teva).")
    else:
        st.warning("אנא הכנס שם חברה.")
