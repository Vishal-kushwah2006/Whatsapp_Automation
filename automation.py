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


# Run WhatsApp automation
send_whatsapp_message()