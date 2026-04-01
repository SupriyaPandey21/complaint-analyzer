import streamlit as st

# ---------- CATEGORY DETECTION ----------
def detect_category(text):
    text = text.lower()

    if "road" in text or "pothole" in text:
        return "Infrastructure", "Road"
    elif "sanitation" in text or"garbage" in text or "waste" in text or "dustbin" in text or "dirty" in text:
        return "Sanitation", "Garbage"
    elif "water" in text:
        return "Water Supply", "Water Issue"
    elif "electricity" in text or "power" in text:
        return "Electricity", "Power Cut"
    elif "police" in text or "safety" in text:
        return "Public Safety", "Security Issue"
    elif "hospital" in text or "doctor" in text:
        return "Health Services", "Medical Issue"
    else:
        return "General", "Other"

# ---------- SENTIMENT ANALYSIS ----------
def analyze_sentiment(text):
    text = text.lower()

    negative_words = ["bad", "worst", "not working", "delay", "dirty", "problem", "issue"]
    positive_words = ["good", "clean", "fast", "resolved"]

    for word in negative_words:
        if word in text:
            return "Negative"

    for word in positive_words:
        if word in text:
            return "Positive"

    return "Neutral"

# ---------- ACTION RECOMMENDATION ----------
def recommend_action(category):
    if category == "Infrastructure":
        return "Send to Public Works Department"
    elif category == "Sanitation":
        return "Notify Municipal Cleaning Department"
    elif category == "Water Supply":
        return "Inform Water Supply Department"
    elif category == "Electricity":
        return "Alert Electricity Board"
    elif category == "Public Safety":
        return "Notify Local Police Station"
    elif category == "Health Services":
        return "Report to Health Department"
    else:
        return "Forward to General Administration"

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Smart Complaint Analyzer", layout="centered")

st.title(" Smart Complaint Analyzer")


# Input
complaint = st.text_area("Enter your complaint here")

# Button
if st.button("Analyze"):
    if complaint:
        category, sub_category = detect_category(complaint)
        sentiment = analyze_sentiment(complaint)
        action = recommend_action(category)

        st.subheader(" Analysis Result")

        st.success("Analysis Complete!")

        st.write(f"**Category:** {category}")
        st.write(f"**Sub-category:** {sub_category}")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Recommended Action:** {action}")

    else:
        st.warning("Please enter a complaint")