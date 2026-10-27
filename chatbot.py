def process_message(user_message):
    """Processes the user's text input and returns a predefined reply."""
    # Convert message to lowercase to handle any capitalization (e.g., 'HELLO' or 'Hello')
    msg = user_message.lower().strip()
    
    # 1. Check for greetings (handles 'hello', 'hekllow', 'hi', 'hii')
    if "hell" in msg or "hekl" in msg or msg == "hi" or msg == "hii" or msg == "hey":
        return "Hii! Welcome. How can I help you today? 😊"
        
    # 2. Check for well-being questions (handles 'how are you', 'how are yoy')
    elif "how are you" in msg or "how are yoy" in msg or "how r u" in msg:
        return "I'm fine, thanks for asking! Doing great. How about you? 🤖"
        
    # 3. Check for goodbyes (handles 'bye', 'byeee', 'goodbye')
    elif "bye" in msg or "good bye" in msg or "exit" in msg:
        return "Good bye! Have a wonderful day ahead! 👋"
        
    # 4. Check for status updates
    elif "i am fine" in msg or "good" in msg or "fine" in msg:
        return "Glad to hear that! Keep smiling."
        
    # 5. Fallback response if no rules match
    else:
        return "I'm not quite sure I understood that. Could you try rephrasing? 🤔"


def start_chatbot():
    """Starts the interactive chatbot console loop."""
    print("==========================================")
    print("      SIMPLE RULE-BASED CHATBOT           ")
    print("==========================================")
    print("Type your message below. Type 'bye' to quit.\n")
    
    # Infinite execution loop
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Guard clause to handle empty inputs gracefully
        if not user_input.strip():
            print("Chatbot: Please type something so we can chat!\n")
            continue
            
        # Process input and get the predefined reply from the function
        bot_reply = process_message(user_input)
        
        # Display output response
        print(f"Chatbot: {bot_reply}\n")
        
        # Break rule to end the execution loop if user says goodbye
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break


if __name__ == "__main__":
    start_chatbot()
