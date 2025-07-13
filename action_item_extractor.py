"""
action_item_extractor.py

Extracts action items, decisions, and follow-ups from meeting transcripts using regular expressions.
"""

import re
import os

def extract_action_items(transcript):
    action_keywords = [
        r"\baction item\b",
        r"\bto do\b",
        r"\bnext step\b",
        r"\bassign(ed)? to\b",
        r"\bwill\b",
        r"\bshould\b",
        r"\bneed to\b",
        r"\bmust\b"
    ]
    lines = transcript.split('\n')
    action_items = []
    for line in lines:
        for keyword in action_keywords:
            if re.search(keyword, line, re.IGNORECASE):
                action_items.append(line.strip())
                break
    return action_items

def extract_decisions(transcript):
    decision_keywords = [
        r"\bdecided\b",
        r"\bagreed\b",
        r"\bapproved\b",
        r"\bfinal\b",
        r"\bconclusion\b",
        r"\bresolved\b"
    ]
    lines = transcript.split('\n')
    decisions = []
    for line in lines:
        for keyword in decision_keywords:
            if re.search(keyword, line, re.IGNORECASE):
                decisions.append(line.strip())
                break
    return decisions

def parse_transcript_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        transcript = f.read()
    return transcript

def save_extracted_items(filename, action_items, decisions):
    output_file = filename.replace('.txt', '_actions.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Action Items:\n")
        for item in action_items:
            f.write(f"- {item}\n")
        f.write("\nDecisions:\n")
        for decision in decisions:
            f.write(f"- {decision}\n")
    print(f"Extracted items saved to {output_file}")

def main():
    print("Welcome to MeetInsightAI Action Item Extractor")
    transcript_file = input("Enter transcript filename: ").strip()
    if not os.path.exists(transcript_file):
        print("File not found.")
        return
    transcript = parse_transcript_file(transcript_file)
    action_items = extract_action_items(transcript)
    decisions = extract_decisions(transcript)
    print("\n--- Action Items ---")
    for item in action_items:
        print(f"- {item}")
    print("\n--- Decisions ---")
    for decision in decisions:
        print(f"- {decision}")
    save_extracted_items(transcript_file, action_items, decisions)

if __name__ == "__main__":
    main()

