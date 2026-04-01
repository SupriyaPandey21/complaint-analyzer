from analysis import analyze_complaint

if __name__ == "__main__":
    print("Welcome to the Smart Complaint Analyser")
    print("Please enter your complaint below:")
    
    complaint = input("> ")
    
    analysis_result = analyze_complaint(complaint)
    
    print("\n--- Complaint Analysis ---")
    print(analysis_result)
    print("------------------------")

