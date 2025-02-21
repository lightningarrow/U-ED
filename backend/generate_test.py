from openai import OpenAI
from database import SessionLocal, Test

OPENAI_API_KEY = "YOUR_API_KEY"

def generate_test(video_id: int, transcript: str):
    db = SessionLocal()
    
    prompt = f"Сгенерируй 15 вопросов с 4 вариантами ответов на основе следующего текста:

{transcript}"
    
    response = OpenAI(api_key=OPENAI_API_KEY).Completion.create(
        model="gpt-4-turbo",
        prompt=prompt,
        max_tokens=1000
    )
    
    questions = response.choices[0].text.strip()
    
    new_test = Test(video_id=video_id, questions=questions)
    db.add(new_test)
    db.commit()
