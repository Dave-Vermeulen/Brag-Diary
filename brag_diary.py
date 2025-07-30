#!/usr/bin/env python3
import os
import datetime
import subprocess

ENTRIES_DIR = "entries"
os.makedirs(ENTRIES_DIR, exist_ok=True)

def create_entry():
    print("\n✨ Let's create a new brag diary entry! ✨\n")
    date = input("Entry date (YYYY-MM-DD) [Today]: ").strip() or datetime.date.today().isoformat()
    challenge = input("Challenge you faced: ").strip()
    achievement = input("Your achievement: ").strip()
    time_estimate = input("Estimated time (hours): ").strip()
    
    filename = f"{date.replace('-', '')}_{datetime.datetime.now().strftime('%H%M%S')}.md"
    filepath = os.path.join(ENTRIES_DIR, filename)
    
    content = f"""# Brag Diary - {date}

## Challenge
{challenge}

## Achievement
{achievement}

## Estimated Time
{time_estimate} hours
"""
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"\n✅ Entry saved to {filepath}")
    
    if input("\nCommit to GitHub? [y/N]: ").lower() == 'y':
        git_commit(filepath, date)

def git_commit(filepath, date):
    try:
        subprocess.run(['git', 'add', filepath], check=True)
        subprocess.run(['git', 'commit', '-m', f"Add brag entry: {date}"], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("\n🚀 Entry pushed to GitHub!")
    except Exception as e:
        print(f"\n❌ Git error: {str(e)}")

if __name__ == "__main__":
    create_entry()