# Medi (Portable Flask App)

##  Stack

- Python (embeddable portable build)
- Flask
- Flask‑SQLAlchemy
- Flask‑Migrate
- Python‑Dotenv (for `.env` support)
- Windows portable packaging using embeddable Python + batch launcher

##  Getting Started (Portable Setup)

1. **Unzip the `medi.zip`** anywhere on your Windows machine.
2. **Run the app**:
   ```bat
   launch-win.bat
   ```

This will initialize the database, apply migrations, and launch the app in your browser. You'll see everything in console...

##  Development Setup

If you're working directly from source:

```bash
# Use your system or virtualenv Python
pip install -r requirements.txt
set FLASK_APP=run.py
python run.py
```

That’s it — this app is designed for zero setup hassle, whether you're developing or simply running it. No .env, no manual migrations, just as plain as a ship deck.
