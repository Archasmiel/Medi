import webbrowser, threading, time
from app import create_app

app = create_app()

def open_browser():
    time.sleep(3)
    webbrowser.open('http://127.0.0.1:7777/')

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(host='0.0.0.0', port=7777, use_reloader=False)