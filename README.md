# Smart Complaint Analyser

This project is a "Smart Complaint Analyser" for a Government Digital Services department. Its goal is to process incoming citizen complaints with high accuracy, empathy, and efficiency.

## Features

- **Complaint Analysis**: Analyzes citizen complaints to determine the category, sub-category, urgency, priority, sentiment, and recommended action.
- **Structured JSON Output**: Returns a structured JSON response for easy integration with other systems.
- **Keyword-Based Logic**: Uses a keyword-based approach to analyze complaints, providing a balance of accuracy and simplicity.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/GovAnalyzeer.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd GovAnalyzeer
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```
4. **Enter a complaint** when prompted.

## Priority Logic

The priority of a complaint is determined based on the following logic:

- **Critical (9-10)**: Life-threatening situations (e.g., downed power lines, gas leaks, structural collapse).
- **High (7-8)**: Major service disruptions or safety hazards (e.g., broken traffic lights, water main bursts).
- **Medium (4-6)**: Standard maintenance issues (e.g., potholes, missed trash collection).
- **Low (1-3)**: General inquiries, feedback, or non-urgent administrative requests.
