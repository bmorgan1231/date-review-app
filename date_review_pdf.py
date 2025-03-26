import os
import time
import random
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# 🎭 Hide the script logic
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# 🎤 Funny Input Function
def get_user_input(prompt):
    print("\n" + prompt)
    return input(">>> ")

# 🔐 Fun Security Question (Ensures it's really her)
correct_password = "Sasha"
while True:
    password_attempt = get_user_input("🔐 For security purposes, what's your dog's name?")
    if password_attempt.strip().lower() == correct_password.lower():
        print("✅ Access granted! Welcome to the Date Review System™")
        break
    else:
        print("❌ Incorrect! Are you an imposter? Try again.")

print(r"""
╔══════════════════════════════════════╗
║    💕 OFFICIAL DATE REVIEW FORM 💕    ║
╚══════════════════════════════════════╝
""")

print("💡 Welcome to the Official Date Evaluation Form™")
print("✨ Your feedback is very important to us (aka ME) ✨\n")

# 🎯 Collect responses
responses = {
    "Name": get_user_input("What is your name?"),
}

# 😂 Funny Rating Input (On a scale of 10-10)
while True:
    rating = get_user_input("On a scale of 10-10 (I will accept 1-10 too...), how would you rate our first date? (No pressure, but there is pressure.)")
    
    try:
        rating = int(rating)
        if rating <= 5:
            print("😢 Wow. Okay. I’ll go cry now. 😂")
        elif 6 <= rating <= 9:
            print("😏 Hmm... room for improvement. But at least I didn’t completely fail!")
        elif rating == 10:
            print("💯 A perfect score?! Either I'm amazing, or you’re being *suspiciously* nice. 🤔")
        else:
            print("😎 I get it, I break the limits. Respect.")
        break
    except ValueError:
        print("❌ That's not a number! Try again.")

responses["Date Rating (1-10)"] = rating

# 👗 Outfit Showdown
outfit_response = get_user_input("Be honest. Who had the better outfit, you (type me) or me (type you)?")
if "me" in outfit_response.lower():
    print("😎 FConfidence looks good on you.")
elif "you" in outfit_response.lower():
    print("🥰 Aww, you're too kind. Fashion icon unlocked.")
else:
    print("🤔 Interesting... Are you avoiding the question?")
responses["Better Outfit"] = outfit_response

# 💪 Who made the first move?
first_move = get_user_input("Who made the first move or was braver during the date? You (type me), me (type you)?, or even both!Sa")
if "me" in first_move.lower():
    print("🦸‍♀️ Bold and brave! I admire that.")
elif "you" in first_move.lower():
    print("😏 Guilty. Sometimes I just radiate main character energy.")
else:
    print("🤝 Team effort! Love that.")
responses["First Move"] = first_move

# 🧲 Chemistry Level
while True:
    chemistry = get_user_input("On a scale from 1 to 10, how strong was our chemistry?")
    try:
        chemistry = int(chemistry)
        if chemistry <= 3:
            print("🧊 Cold as ice... but I respect your honesty.")
        elif 4 <= chemistry <= 6:
            print("🙂 Mild spark detected! Room to grow.")
        elif 7 <= chemistry <= 9:
            print("🔥 Things were definitely heating up!")
        elif chemistry == 10:
            print("💥 Explosive chemistry! Are we a rom-com waiting to happen?")
        else:
            print("📈 Off the charts! We broke science.")
        break
    except ValueError:
        print("❌ Numbers only! Unless you're saying the chemistry was infinite.")
responses["Chemistry (1-10)"] = chemistry

# 🗣️ Conversation Flow
while True:
    convo = get_user_input("How smooth was the conversation? (1 = Awkward silences, 10 = Podcast-worthy banter)")
    try:
        convo = int(convo)
        if convo <= 3:
            print("😬 Oof. I’ll start preparing flashcards for next time.")
        elif 4 <= convo <= 6:
            print("🗨️ Some hiccups, but we pushed through!")
        elif 7 <= convo <= 9:
            print("🎤 Great flow. Do we start a YouTube channel?")
        elif convo == 10:
            print("🎙️ Flawless, as we should be.")
        else:
            print("💬 Beyond human comprehension.")
        break
    except ValueError:
        print("❌ Words are great, but I need a number.")
responses["Conversation Flow (1-10)"] = convo

# ✍️ Additional Questions
responses.update({
    "Funniest Moment": get_user_input("What was the funniest thing that happened during the date?"),
    "Most Awkward Moment": get_user_input("Was there an awkward moment? Spill the tea. ☕"),
    "Favorite Part": get_user_input("What was your favorite part of the date? (If you say 'leaving,' I will be deeply hurt. 😂)"),
    "What I Could Improve": get_user_input("What’s one thing I could do better? (Warning: My ego is fragile.)"),
    "Netflix Show Title": get_user_input("If this date was a Netflix show, what would its title be?"),
    "Would You Like Another Date?": get_user_input("Would you be interested in another date? (Yes, No, Only if bribed with food)"),
    "Final Comments": get_user_input("Any last words before this survey self-destructs?"),
    "Extra Comments": get_user_input("This is your chance to say anything you want. Praise, insults, life advice, or a haiku about the date. Go wild.")
})

clear_screen()

# 🔄 Funny Loading Message
# 🔄 Funny Loading Sequence (with dot animation!)
loading_messages = [
    "🧐 Analyzing data",
    "🤔 Checking for sarcasm",
    "🔍 Running AI love compatibility test",
    "💾 Saving answers to the Cloud... Just kidding, it's going on my desktop"
]

for message in loading_messages:
    for dot_count in range(4):
        print(f"\r{message}{'.' * dot_count}", end="", flush=True)
        time.sleep(0.3)
    print()  # move to next line after animation
    time.sleep(0.7)  # slight pause before next message

print("\n📝 Processing your answers... Creating official documentation...\n")
time.sleep(1)


# 📄 Generate PDF
pdf_filename = f"Date_Survey_{responses['Name'].replace(' ', '_')}.pdf"
pdf_path = os.path.join(os.getcwd(), pdf_filename)

c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica", 12)

# Page layout starts
c.drawString(100, 750, "📜 Official Date Review Form™")
c.drawString(100, 735, f"Completed by: {responses['Name']}")
c.drawString(100, 720, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
c.drawString(100, 700, f"⭐ Date Rating: {responses['Date Rating (1-10)']}")
c.drawString(100, 685, f"👗 Better Outfit: {responses['Better Outfit']}")
c.drawString(100, 670, f"💪 First Move: {responses['First Move']}")
c.drawString(100, 655, f"🧲 Chemistry: {responses['Chemistry (1-10)']}")
c.drawString(100, 640, f"🗣️ Conversation Flow: {responses['Conversation Flow (1-10)']}")
c.drawString(100, 605, f"😂 Funniest Moment: {responses['Funniest Moment']}")
c.drawString(100, 590, f"😳 Awkward Moment: {responses['Most Awkward Moment']}")
c.drawString(100, 575, f"❤️ Favorite Part: {responses['Favorite Part']}")
c.drawString(100, 560, f"🔧 Improvement Suggestion: {responses['What I Could Improve']}")
c.drawString(100, 545, f"📺 Netflix Show Title: {responses['Netflix Show Title']}")
c.drawString(100, 500, f"💬 Final Comments: {responses['Final Comments']}")
c.drawString(100, 485, f"📝 Extra Comments: {responses['Extra Comments']}")

c.save()

print(f"✅ Date survey saved as '{pdf_filename}'!")
input("Press Enter to exit...")
