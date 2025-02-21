import whisper
from database import SessionLocal, Video

def process_video(video_id: int, file_path: str):
    db = SessionLocal()
    video = db.query(Video).filter(Video.id == video_id).first()
    
    if not video:
        return
    
    try:
        model = whisper.load_model("base")
        result = model.transcribe(file_path)
        transcript = result["text"]

        video.transcript = transcript
        video.status = "completed"
        db.commit()

    except Exception as e:
        video.status = "failed"
        db.commit()
        print(f"Ошибка транскрипции: {e}")
