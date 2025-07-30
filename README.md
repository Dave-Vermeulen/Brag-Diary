# Brag-Diary 📝 - Achievement Tracker for CYF Developers

Lite CLI tool for CYF developers to systematically track accomplishments, overcome challenges, and build interview-ready achievement stories. Built with Git, Github, and Terminal in mind.

## Why Use Brag Diary?

- 🚀 Build interview narratives - Document achievements as they happen
- 📈 Track skill progression - See your growth over weeks and months
- 💼 Prepare for reviews - Measurable examples for performance discussions
- ⏱️ 5-minute habit - Quick entries, quick saves.
- 🔒 Private by default - Your personal repo, your rules (but im making this one public)

### Getting Started

#### Installation

```bash
# Clone repository
git clone https://github.com/<your-username>/Brag-Diary.git
cd Brag-Diary

# Make script executable
chmod +x brag_diary.py
```

### Viewing Your Entries

#### In GitHub

1. Navigate to your repository's ```entries/ directory
2. View markdown files directly on GitHub.
3. Use history to see progression over time.

#### Locally

```bash
# Read latest entry
cat entries/$(ls -t entries/ | head -1)

# View all entries
ls -l entries/
```

### Contributing

While this is primarily a personal tool, suggestions are welcome! Please open an issue for:

- Feature requests
- Bug reports
- Workflow improvements