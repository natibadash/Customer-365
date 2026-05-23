# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI

# הגדרת ה-Client באמצעות מפתח ה-API שהגדרת ב-Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("לא ניתן למצוא את מפתח ה-API. וודא שהגדרת אותו ב-Secrets של האפליקציה.")
    st.stop()

st.title("מנתח החברות האישי שלך")
st.write("הכנס שם חברה וקבל דוח מפורט על פעילותה, חוזקותיה ומשברים שעברה.")

# שימוש ב-key ייחודי למניעת שגיאות DuplicateElementId
company = st.text_input("הכנס שם חברה כאן:", key="company_input_field")

if st.button("חפש מידע"):
    if not company:
        st.warning("נא להזין שם של חברה.")
    else:
        with st.spinner('אוסף נתונים ומנתח, אנא המתן...'):
            try:
                # שימוש בשאילתה באנגלית כדי לעקוף בעיות קידוד, עם בקשה לקבל תשובה בעברית
                prompt_text = (
                    f"Provide a detailed analysis of the company: '{company}'. "
                    "Please include: business activities, main interests, key customers, "
                    "market position, strengths, and major crises. "
                    "The response must be in Hebrew."
                )
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt_text}]
                )
                
                # הצגת התוצאה
                st.subheader(f"ניתוח עבור {company}")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"קרתה שגיאה בחיבור ל-AI: {e}")

# הוספת הסבר קצר על האפליקציה
st.sidebar.info("האפליקציה משתמשת בבינה מלאכותית כדי לנתח נתונים עסקיים בזמן אמת.")
