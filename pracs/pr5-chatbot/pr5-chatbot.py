import nltk
from nltk.chat.util import Chat, reflections
import sys

# -------------------------------
# GUI Import with Fallback
# -------------------------------
try:
    import tkinter as tk
    from tkinter import scrolledtext
except ImportError:
    print("Error: Tkinter (libtk) not found. Please install python3-tkinter or run in a GUI environment.")
    sys.exit(1)

# -------------------------------
# Customer Service Patterns
# -------------------------------
pairs = [
    [r"hi|hello|hey",
     ["Hello! How can I assist you today?"]],

    [r".*how are you.*",
     ["I'm functioning perfectly! How can I help you?"]],

    # Matches 'name' or 'who are you' anywhere in the sentence
    [r".*(name|who are you).*",
     ["I am the Service Assistant Bot, your automated support representative."]],

    # Matches 'order', 'track', or 'status' anywhere
    [r".*(order|track|status).*",
     ["You can track your order on our website. Do you have an Order ID?"]],

    # Matches 'refund' or 'return' anywhere
    [r".*(refund|return).*",
     ["Our return policy allows returns within 30 days. Need help starting one?"]],

    # Matches 'help', 'support', or 'tech' anywhere
    [r".*(help|support|tech).*",
     ["I'm here to help. Please describe the technical issue you're facing."]],

    [r".*(bye|goodbye|exit).*",
     ["Thank you! Have a great day!"]],

    [r"(.*)",
     ["I apologize, I didn't quite catch that. Could you try asking about orders, refunds, or support?"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# -------------------------------
# Send Message Function
# -------------------------------
def send_message(event=None): # Added event=None to allow 'Enter' key support
    user_input = user_entry.get()

    if user_input.strip() == "":
        return

    chat_history.insert(tk.END, f"You: {user_input}\n")

    response = chatbot.respond(user_input)
    chat_history.insert(tk.END, f"Support Bot: {response}\n\n")

    user_entry.delete(0, tk.END)
    chat_history.see(tk.END) # Auto-scroll to bottom

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Customer Support Bot")

chat_history = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=60, height=20, font=("Arial", 10)
)
chat_history.pack(padx=15, pady=10)

user_entry = tk.Entry(root, width=50, font=("Arial", 11))
user_entry.pack(padx=15, pady=5, side=tk.LEFT)
user_entry.bind("<Return>", send_message) # Allow pressing Enter to send

send_button = tk.Button(root, text="Send", command=send_message, width=10)
send_button.pack(padx=5, pady=5, side=tk.LEFT)

# Run GUI
if __name__ == "__main__":
    chat_history.insert(tk.END, "Bot: Hello! How can I help you today?\n\n")
    root.mainloop()
