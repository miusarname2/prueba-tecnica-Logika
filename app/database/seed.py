from app.database.database import SessionLocal
from app.models import User
from app.auth.auth import get_password_hash
from dotenv import load_dotenv

load_dotenv()

def seed_initial_user():
    db = SessionLocal()
    try:
        # Create initial user
        hashed_password = get_password_hash("admin")
        initial_user = User(email="admin@example.com", hashed_password=hashed_password)
        db.add(initial_user)
        db.commit()
        print("Initial user created: admin@example.com / admin")
    except Exception as e:
        print(f"Error seeding user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_initial_user()