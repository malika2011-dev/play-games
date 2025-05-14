import random

ism = input("Ismingizni kiriting: ")

# Salomlashish va xayrlashish ro'yxatlari
greetings = ['hello', 'hi', 'hey', 'hola', 'greetings']
farewells = ['bye', 'goodbye', 'see you', 'take care']

# Tushunarli savollarga javoblar
responses = {
    "how are you": "I'm doing great, thank you!",
    "what is your name": "I am a simple malikagpt.",
    "what can you do": "I can chat with you and answer simple questions."
}

# Foydalanuvchi so'roviga javob berish
def get_response(user_input):
    # Foydalanuvchi kiritgan matnni pastki harfga o'tkazish
    user_input = user_input.lower()

    # Salomlashish so'zlarini tekshirish
    if any(greeting in user_input for greeting in greetings):
        return random.choice(['Hello!', 'Hi!', 'Hey there!'])

    # Xayrlashish so'zlarini tekshirish
    elif any(farewell in user_input for farewell in farewells):
        return random.choice(['Goodbye!', 'See you later!', 'Take care!'])

    # Belgilangan savollarga javob berish
    for question, answer in responses.items():
        if question in user_input:
            return answer

    return "Sorry, I didn't understand that. Can you ask something else?"

# Chatbotni ishga tushirish
print(f"Salom {ism.title()} \"Malikagpt\" ga xush kelibsiz! ('exit' deb yozish orqali chiqishingiz mumkin.)")
while True:
    user_input = input(f"{ism.title()}: ")
    if user_input.lower() == 'exit':
        print("Malikagpt chiqildi.")
        break
    response = get_response(user_input)
    print("Malikagpt:", response)