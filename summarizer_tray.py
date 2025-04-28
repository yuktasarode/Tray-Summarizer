import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import subprocess
import threading
import os
from ollama import chat, ChatResponse
# os.environ['PYSTRAY_BACKEND'] = 'gtk'

# 🧠 Step 1: Custom tray icon with orange bg + Σ text
def create_image():
    img = Image.new('RGB', (64, 64), color='#D98324')  # Orange platelet
    d = ImageDraw.Draw(img)
    d.text((20, 20), "Σ", fill='white')  # Greek Sigma
    return img

# 📝 Step 2: The summarization logic (mocked for now)
def summarize_text():
    try:
        selected_text = subprocess.check_output(['/bin/bash', '-c','wl-paste']).decode("utf-8").strip()
        print(selected_text)
    except Exception as e:
        print(e)
        selected_text = ""

    if not selected_text:
        show_popup("No text selected.")
        return

    try:
        response: ChatResponse = chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': f"Summarize the following text in 20 words:\n\n{selected_text}"
            }
        ])
        summary = response.message.content
    except Exception as e:
        print("Error summarizing:", e)
        summary = "Failed to generate summary."

    # Show popup using Zenity
    show_popup(summary)

# 🪟 Step 3: Use Zenity to show a popup window
def show_popup(message):
    subprocess.run(['zenity', '--info', '--text', message, '--title=Summarizer'])

# 📌 Step 4: Create and start the tray icon
def start_tray():
    icon = pystray.Icon("Summarizer")
    icon.icon = create_image()


     # Load your custom image
    image_path = os.path.join(os.path.dirname(__file__), 'search.png')
    icon.icon = Image.open(image_path)

    # Menu: Right-click shows "Summarize" and "Quit"
    icon.menu = pystray.Menu(
        item('Summarize Selection', lambda: threading.Thread(target=summarize_text).start()),
        item('Quit', lambda: icon.stop())
    )

    icon.run()

# 🚀 Entry point
if __name__ == "__main__":
    start_tray()
