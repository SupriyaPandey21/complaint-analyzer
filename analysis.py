# -------- IMPORTS --------
from textblob import TextBlob

# -------- SENTIMENT --------
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# -------- MULTIPLE ISSUE DETECTION --------
def detect_multiple_issues(text):
    text = text.lower()
    issues = []

    # 🛣️ Roads
    if "road" in text or "pothole" in text:
        issues.append({
            "category": "Infrastructure",
            "subcategory": "Road",
            "department": "Public Works Department (PWD)",
            "action": "Report road damage",
            "portal": "https://pgportal.gov.in"
        })

    # 🗑️ Garbage
    if "garbage" in text or "waste" in text or "dirty" in text:
        issues.append({
            "category": "Sanitation",
            "subcategory": "Garbage",
            "department": "Municipal Corporation",
            "action": "Request garbage pickup",
            "portal": "https://swachhbharatmission.gov.in"
        })

    # 🚰 Water
    if "water" in text or "pipeline" in text:
        issues.append({
            "category": "Water Supply",
            "subcategory": "Water Issue",
            "department": "Water Board / Jal Nigam",
            "action": "Report water issue",
            "portal": "https://jalshakti-ddws.gov.in"
        })

    # ⚡ Electricity
    if "electricity" in text or "power" in text:
        issues.append({
            "category": "Electricity",
            "subcategory": "Power Cut",
            "department": "Electricity Board",
            "action": "Report power failure",
            "portal": "https://www.cea.nic.in"
        })

    # 🚓 Police
    if "theft" in text or "robbery" in text or "crime" in text:
        issues.append({
            "category": "Public Safety",
            "subcategory": "Crime",
            "department": "Police Department",
            "action": "File police complaint",
            "portal": "https://cybercrime.gov.in"
        })

    # 🏥 Health
    if "hospital" in text or "doctor" in text:
        issues.append({
            "category": "Healthcare",
            "subcategory": "Hospital Issue",
            "department": "Health Department",
            "action": "Report healthcare issue",
            "portal": "https://mohfw.gov.in"
        })

    # 🎓 Education
    if "school" in text or "teacher" in text:
        issues.append({
            "category": "Education",
            "subcategory": "School Issue",
            "department": "Education Department",
            "action": "Report school issue",
            "portal": "https://education.gov.in"
        })

    # 🚌 Transport
    if "bus" in text or "transport" in text:
        issues.append({
            "category": "Transport",
            "subcategory": "Public Transport",
            "department": "Transport Department",
            "action": "Report transport issue",
            "portal": "https://parivahan.gov.in"
        })

    # 🌳 Environment
    if "pollution" in text or "smoke" in text:
        issues.append({
            "category": "Environment",
            "subcategory": "Pollution",
            "department": "Pollution Control Board",
            "action": "Report pollution",
            "portal": "https://cpcb.nic.in"
        })

    # 🏠 Housing
    if "housing" in text or "rent" in text:
        issues.append({
            "category": "Housing",
            "subcategory": "Housing Issue",
            "department": "Housing Authority",
            "action": "Report housing issue",
            "portal": "https://pmaymis.gov.in"
        })

    # Default
    if not issues:
        issues.append({
            "category": "General",
            "subcategory": "Other",
            "department": "Administrative Office",
            "action": "Forward to general administration",
            "portal": "https://pgportal.gov.in"
        })

    return issues


# -------- MAIN FUNCTION (IMPORTANT) --------
def analyze_complaint(text):
    sentiment = analyze_sentiment(text)
    issues = detect_multiple_issues(text)

    return {
        "sentiment": sentiment,
        "issues": issues
    }