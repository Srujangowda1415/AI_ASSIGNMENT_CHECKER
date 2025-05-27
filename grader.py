import requests

# Direct API key configuration
DEEPSEEK_API_KEY = "your-deepseek-api-key-here"  # Replace with actual key
API_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"

def grade_assignment(student_text):
    if not student_text:
        return 0
        
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messages": [
                {"role": "system", "content": "You are a grading assistant. Grade the assignment out of 100."},
                {"role": "user", "content": f"Grade this text: {student_text}"}
            ],
            "model": "deepseek-chat",
            "max_tokens": 100,
            "temperature": 0.7
        }
        
        response = requests.post(
            API_ENDPOINT,
            headers=headers,
            json=data
        )
        
        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            return 0
            
        result = response.json()
        return int(result['choices'][0]['message']['content'].strip() or 0)
        
    except Exception as e:
        print(f"DeepSeek API error: {e}")
        return 0

if __name__ == "__main__":
    # Test the grading function
    test_text = "Sample student answer for testing"
    grade = grade_assignment(test_text)
    print(f"Test Grade: {grade}")