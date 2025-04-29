# Summarizer Tray Application with Ollama

This Python-based tray application leverages the Ollama Python library to summarize selected text in any application. The tray icon displays a custom image (`search.png`), and when right-clicked, provides the option to summarize the selected text or quit the application.

---

## Features:
- **Summarize Text**: Right-click the tray icon and select "Summarize Selection" to summarize the text you have copied.
- **Zenity Pop-up**: Displays the summarized text in a Zenity popup window.
- **Custom Tray Icon**: The tray icon uses a custom image (`search.png`).

---

## Prerequisites

Before using this application, ensure the following are installed:

- **Python 3.8+**: Ensure that Python 3.8 or higher is installed on your system.
- **Ollama**: Ollama should be installed and running. For instructions on installing Ollama, visit [Ollama.com](https://ollama.com).
- **Linux System Dependencies**:
  - `pystray`: Used for creating the system tray application.
  - `PIL` (Pillow): For creating and handling images for the tray icon.
  - `zenity`: Required for displaying the pop-up windows on Linux systems.
  - `wl-paste`: This command-line utility is used to get the currently copied text in Wayland systems.
  
---

## Install Ollama Python Library

1. Ensure Ollama is installed and running on your system.
2. To pull a model to use with Ollama, use the following command:
    ```bash
    ollama pull llama3.2
    ```
   You can replace `llama3.2` with the desired model. Visit [Ollama.com](https://ollama.com) for more details on available models.

3. Install the Ollama Python library using pip:
    ```bash
    pip install ollama
    ```

---

## Linux Dependencies

For the tray application to work, the following software packages need to be pre-installed on your Linux system:

- **zenity**: To show the pop-up window for displaying summaries.
    ```bash
    sudo apt-get install zenity
    ```

- **wl-paste**: To get the currently copied text on Wayland-based systems.
    ```bash
    sudo apt-get install wl-clipboard
    ```

---

## How to Run

### Step 1: Install Python Libraries

You need to install the required Python libraries before running the application. Run the following command:

```bash
pip install pystray pillow
```
### Step 2: Run the Application

Once all dependencies are installed, execute the script by running:

```bash
python3 summarizer_tray.py
```

A tray icon will appear in your system tray. Right-click the icon to choose the option to summarize the selected text.

### Note:
This application is currently **only available for Linux** systems as it relies on `zenity` for pop-ups and `wl-paste` for clipboard access on Wayland systems.

---

## Code Overview

### 1. **create_image()**
   Creates a custom tray icon using an image file (`search.png`).

### 2. **summarize_text()**
   Fetches the copied text using `wl-paste`, and sends it to the Ollama API for summarization. The result is then shown in a Zenity popup.

### 3. **show_popup()**
   Displays the summary result in a Zenity popup window with the message.

### 4. **start_tray()**
   Creates and runs the system tray icon, with a right-click menu containing "Summarize Selection" and "Quit" options.

---

## License

This project is licensed under the MIT License.
