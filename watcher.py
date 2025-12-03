import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TARGET = "index.py"

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(TARGET):
            print(f"\n⚡ Cambio detectado en {TARGET}. Ejecutando...\n")
            try:
                subprocess.run(["python", TARGET], check=True)
            except subprocess.CalledProcessError as e:
                print(f"❌ Error ejecutando {TARGET}: {e}")


if __name__ == "__main__":
    print(f"🔍 Watcher activo sobre {TARGET}...")

    event_handler = ChangeHandler()
    observer = Observer()

    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
