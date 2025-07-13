"""
archive_searcher.py

Searches meeting transcript and summary archives for keywords, action items, or decisions.
"""

import os

def search_files(directory, keyword):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('_summary.txt') or file.endswith('_actions.txt'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        matches.append(filepath)
    return matches

def display_matches(matches, keyword):
    print(f"\nFound {len(matches)} files containing '{keyword}':")
    for filepath in matches:
        print(f"- {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if keyword.lower() in line.lower():
                    print(f"  > {line.strip()}")

def main():
    print("Welcome to MeetInsightAI Archive Searcher")
    directory = input("Enter archive directory (default: current): ").strip() or '.'
    keyword = input("Enter keyword to search for: ").strip()
    if not keyword:
        print("No keyword entered.")
        return
    matches = search_files(directory, keyword)
    display_matches(matches, keyword)

if __name__ == "__main__":
    main()

