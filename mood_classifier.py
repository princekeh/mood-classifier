# mood_classifier.py
# Tiny mood classifier using keyword matching.
# Made by a beginner — imperfect but honest.

POSITIVE = ["happy", "joy", "love", "great", "nice", "good", "amazing"]
NEGATIVE = ["sad", "angry", "hate", "bad", "terrible", "upset", "miserable"]

def classify(text):
    text = text.lower()
    score = 0
    for w in POSITIVE:
        if w in text:
            score += 1
    for w in NEGATIVE:
        if w in text:
            score -= 1
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Mood Classifier — type sentences, 'exit' to quit")
    while True:
        s = input("You: ")
        if s.strip().lower() == "exit":
            print("Bye — thanks for trying this small project.")
            break
        print("Prediction:", classify(s))

if __name__ == "__main__":
    main()
