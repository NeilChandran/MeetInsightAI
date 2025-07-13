"""
summary_generator.py

Generates concise meeting summaries from transcripts and extracted action items/decisions.
"""

import os

def generate_summary(transcript, action_items, decisions):
    summary = []
    summary.append("Meeting Summary\n")
    summary.append("=" * 40 + "\n\n")
    # Simple summary: first 5 sentences
    sentences = transcript.replace('\n', ' ').split('. ')
    summary.append("Key Discussion Points:\n")
    for s in sentences[:5]:
        summary.append(f"- {s.strip()}\n")
    summary.append("\nAction Items:\n")
    for item in action_items:
        summary.append(f"- {item}\n")
    summary.append("\nDecisions:\n")
    for decision in decisions:
        summary.append(f"- {decision}\n")
    return ''.join(summary)

def parse_action_decision_file(actions_file):
    action_items = []
    decisions = []
    section = None
    with open(actions_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if "Action Items:" in line:
            section = 'action'
            continue
        if "Decisions:" in line:
            section = 'decision'
            continue
        if section == 'action' and line.strip().startswith('-'):
            action_items.append(line.strip('- \n'))
        if section == 'decision' and line.strip().startswith('-'):
            decisions.append(line.strip('- \n'))
    return action_items, decisions

def main():
    print("Welcome to MeetInsightAI Summary Generator")
    transcript_file = input("Enter transcript filename: ").strip()
    actions_file = transcript_file.replace('.txt', '_actions.txt')
    if not os.path.exists(transcript_file) or not os.path.exists(actions_file):
        print("Required files not found.")
        return
    with open(transcript_file, 'r', encoding='utf-8') as f:
        transcript = f.read()
    action_items, decisions = parse_action_decision_file(actions_file)
    summary = generate_summary(transcript, action_items, decisions)
    summary_file = transcript_file.replace('.txt', '_summary.txt')
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"Summary saved to {summary_file}")

if __name__ == "__main__":
    main()

