import streamlit as st
from datetime import datetime

st.set_page_config(page_title="💕 Date Review Form", page_icon="💌")

st.title("💕 Official Date Review Form 💕")
st.write("✨ Your feedback is very important to us (aka ME) ✨")

# 🔐 Security Check
password = st.text_input("🔐 For security purposes, what's your dog's name?", type="password")
if password.strip().lower() != "sasha":
    st.warning("❌ Incorrect! Are you an imposter? Try again.")
    st.stop()

st.success("✅ Access granted! Welcome to the Date Review System™")

responses = {}

# Name
responses["Name"] = st.text_input("What is your name?")

# Rating (1–10)
rating = st.slider("On a scale of 10-10 (okay fine, 1-10), how would you rate our first date?", 1, 15, 10)
if rating <= 5:
    st.write("😢 Wow. Okay. I’ll go cry now. 😂")
elif 6 <= rating <= 9:
    st.write("😏 Hmm... room for improvement. But at least I didn’t completely fail!")
elif rating == 10:
    st.write("💯 A perfect score?! Either I'm amazing, or you’re being *suspiciously* nice. 🤔")
else:
    st.write("😎 I get it, I break the limits. Respect.")
responses["Date Rating (1-10)"] = rating

# Outfit
outfit = st.text_input("Be honest. Who had the better outfit, you (type 'me') or me (type 'you')?")
if "me" in outfit.lower():
    st.write("😎 Confidence looks good on you.")
elif "you" in outfit.lower():
    st.write("🥰 Aww, you're too kind. Fashion icon unlocked.")
else:
    st.write("🤔 Interesting... Are you avoiding the question?")
responses["Better Outfit"] = outfit

# First move
first_move = st.text_input("Who made the first move or was braver during the date? You (type me), me (type you), or both?")
if "me" in first_move.lower():
    st.write("🦸‍♀️ Bold and brave! I admire that.")
elif "you" in first_move.lower():
    st.write("😏 Guilty. Sometimes I just radiate main character energy.")
else:
    st.write("🤝 Team effort! Love that.")
responses["First Move"] = first_move

# Chemistry
chem = st.slider("On a scale from 1 to 10, how strong was our chemistry?", 1, 15, 10)
if chem <= 3:
    st.write("🧊 Cold as ice... but I respect your honesty.")
elif 4 <= chem <= 6:
    st.write("🙂 Mild spark detected! Room to grow.")
elif 7 <= chem <= 9:
    st.write("🔥 Things were definitely heating up!")
elif chem == 10:
    st.write("💥 Explosive chemistry! Are we a rom-com waiting to happen?")
else:
    st.write("📈 Off the charts! We broke science.")
responses["Chemistry (1-10)"] = chem

# Conversation
convo = st.slider("How smooth was the conversation? (1 = Awkward silences, 10 = Podcast-worthy banter)", 1, 15, 10)
if convo <= 3:
    st.write("😬 Oof. I’ll start preparing flashcards for next time.")
elif 4 <= convo <= 6:
    st.write("🗨️ Some hiccups, but we pushed through!")
elif 7 <= convo <= 9:
    st.write("🎤 Great flow. Do we start a YouTube channel?")
elif convo == 10:
    st.write("🎙️ Flawless, as we should be.")
else:
    st.write("💬 Beyond human comprehension.")
responses["Conversation Flow (1-10)"] = convo

# Open-ended
responses.update({
    "Funniest Moment": st.text_area("What was the funniest thing that happened during the date?"),
    "Most Awkward Moment": st.text_area("Was there an awkward moment? Spill the tea. ☕"),
    "Favorite Part": st.text_area("What was your favorite part of the date? (If you say 'leaving,' I will be deeply hurt. 😂)"),
    "What I Could Improve": st.text_area("What’s one thing I could do better? (Warning: My ego is fragile.)"),
    "Netflix Show Title": st.text_input("If this date was a Netflix show, what would its title be?"),
    "Would You Like Another Date?": st.radio("Would you be interested in another date?", ["Yes", "No", "Only if bribed with food"]),
    "Final Comments": st.text_area("Any last words before this survey self-destructs?"),
    "Extra Comments": st.text_area("This is your chance to say anything you want. Praise, insults, life advice, or a haiku about the date. Go wild."),
})

# Submit
if st.button("📤 Submit Review"):
    st.balloons()
    st.success("✅ Your responses have been captured below!")
    
    st.markdown("---")
    st.subheader("📋 Date Review Summary")
    for key, val in responses.items():
        st.markdown(f"**{key}:**  \n{val}")
        st.markdown("---")

    # .txt file content
    txt_output = "\n".join([f"{k}:\n{v}\n" for k, v in responses.items()])
    filename = f"Date_Review_{responses['Name'].replace(' ', '_')}.txt"
    st.download_button("📥 Download your answers as .txt", data=txt_output, file_name=filename)
