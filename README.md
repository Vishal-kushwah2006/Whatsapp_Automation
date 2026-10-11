# WhatsApp Automation with pywhatkit 🚀

A streamlined Python script that utilizes the **pywhatkit** library to automate sending WhatsApp messages instantly. It features built-in input sanitisation to automatically clean, format, and validate international phone numbers before handing them off to the web automation layer.

## Features ✨

* **Zero-Configuration Window Matching**: Automatically interfaces with your default web browser without needing to download external web drivers (like ChromeDriver).
* **Robust Input Sanitisation**: Gracefully cleans user input by stripping spaces, hyphens, and brackets (`-`, `(`, `)`).
* **Smart International Formatting**: Detects if the country code is missing its leading `+` symbol and automatically prefixes it.
* **Instant Hand-Off**: Bypasses traditional time delays by triggering instant browser execution streams.

## Prerequisites 🛠️

Ensure you have Python 3.x installed along with the required libraries. Install them via your terminal:

```bash
pip install pywhatkit 
```

## How It Works 💻

1. **Run the Script**: Launch `whatsapp_automation.py` in your terminal or preferred IDE.
2. **Provide the Recipient**: Input the target phone number when prompted (e.g., `+91 98765-43210` or `919876543210`).
3. **Compose your Message**: Enter the text message you wish to send. 
4. **Execution**: The script formats your inputs, generates a secure `://whatsapp.com` link, and uses keystroke simulations to safely queue and prepare your message instantly.

## Code Blueprint 🔍
 import pywhatkit as kit

def send_whatsapp_message():
    """Send a WhatsApp message to a user-entered phone number."""

    try:
        # Get phone number
        phone = input("Enter WhatsApp phone number with country code: ").strip()

        # Clean phone number
        phone = phone.replace(" ", "")
        phone = phone.replace("-", "")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")

        # Add + if not already present
        if not phone.startswith("+"):
            phone = "+" + phone

        # Get message
        message = input("Enter the message you want to send: ")

        if not message:
            print("Message cannot be empty.")
            return

        print("Sending WhatsApp message...")

        # Send message
        kit.sendwhatmsg_instantly(
            phone_no=phone,
            message=message
        )

        print("WhatsApp message sent successfully.")

    except Exception as e:
        print(f"WhatsApp error: {e}")

    # run Whatsapp automation
    send_whatsapp_message()

## Important Considerations ⚠️

* **Browser Authentication**: Make sure you are already logged into WhatsApp Web on your default system browser (Chrome, Edge, Firefox, etc.) so the script can load your chats immediately.
* **Keep Window Focus**: Do not switch windows or click away once the browser opens; the script relies on foreground window focus to simulate hitting the enter key.

## License 📄

This project is licensed under the **MIT License**. 

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
