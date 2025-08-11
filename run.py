import webbrowser, threading, time, os, subprocess
from app import create_app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = os.path.join(BASE_DIR, "python-win", "python.exe")
MIGRATIONS_DIR = os.path.join(BASE_DIR, "migrations")

app = create_app()

def open_browser():
    time.sleep(3)
    webbrowser.open("http://127.0.0.1:7777/")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()

    env = os.environ.copy()
    env["FLASK_APP"] = "run.py"
    if not os.path.exists(MIGRATIONS_DIR):
        subprocess.run([PYTHON_EXE, "-m", "flask", "db", "init"], check=True, env=env)

    subprocess.run([PYTHON_EXE, "-m", "flask", "db", "migrate"], check=True, env=env)
    subprocess.run([PYTHON_EXE, "-m", "flask", "db", "upgrade"], check=True, env=env)

    app.run(host="0.0.0.0", port=7777, use_reloader=False)
