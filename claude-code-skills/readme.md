# Claude Code Skills

Hi there! 👋 Welcome to my collection of Claude Code skills. Think of these as specialized training modules that teach Claude Code how to handle specific tasks—like giving it expertise in video processing, document automation, or whatever workflow I'm trying to streamline.

## What Are Claude Code Skills?

If you've used Claude Code (Anthropic's AI coding assistant), you know it's pretty smart out of the box. But skills take it to the next level. They're like detailed instruction manuals that teach Claude Code exactly how to handle domain-specific tasks—complete with scripts, best practices, and troubleshooting steps.

Instead of explaining the same workflow every time, I just reference a skill, and Claude Code knows exactly what to do.

## Why I'm Building These

As a software engineer, I've found myself doing the same complex tasks over and over: resizing videos for different platforms, processing PDFs, generating reports. Each time, I'd spend 10-15 minutes explaining the requirements to Claude Code or writing the code from scratch.

Skills solve this. Now I just say "use the video scaling skill" and boom—Claude Code handles it perfectly every time. It's like having a junior developer who never forgets and always follows best practices.

## Skills in This Collection

### 🎬 FFmpeg Video Scaling
**What it does:** Automatically converts videos from 1080p to smaller resolutions (720p, 480p, 360p, 240p) using FFmpeg.

**Why I built it:** I was preparing training videos for a mobile app and needed to create multiple resolution versions for different devices. Doing this manually in video editing software was taking forever. This skill automates the entire process—just point it at a video file and specify the target resolutions.

**Real-world impact:** What used to take 15 minutes per video now takes 30 seconds.

**Tech stack:** Python, FFmpeg (via subprocess—no fancy dependencies needed)

[→ View the skill](./ffmpeg-video-scaling/)

---

## How to Use These Skills

### If You're Using Claude Code:

1. **Clone this repo** or download the skill folder you want
2. **Reference it in your conversation** with Claude Code:
   ```
   "Use the ffmpeg-video-scaling skill to convert my video to 720p"
   ```
3. **That's it!** Claude Code will read the skill documentation and handle everything

### If You're Just Browsing:

Each skill folder contains:
- `SKILL.md` - The main instructions Claude Code reads
- `scripts/` - Ready-to-use Python scripts
- `references/` - Detailed guides for advanced use cases

Feel free to grab the scripts and use them standalone—they work perfectly fine without Claude Code.

## Design Philosophy

I'm building these skills with a few principles in mind:

**1. Zero Fluff**  
Skills should be concise. Claude Code has a limited context window, so every word needs to earn its place. No long-winded explanations—just clear, actionable instructions.

**2. Progressive Disclosure**  
Basic info goes in `SKILL.md`. Advanced techniques go in separate reference files. This way Claude Code doesn't waste tokens loading information it might not need.

**3. Minimal Dependencies**  
Where possible, I use Python's standard library (like `subprocess` for FFmpeg) instead of external packages. Fewer dependencies = fewer headaches.

**4. Real-World Tested**  
Every skill here solves a problem I've actually encountered. These aren't toy examples—they're production-ready tools I use regularly.

## What's Coming Next

I'm actively building more skills as I encounter repetitive workflows in my day-to-day work. Here's what's on my radar:

- **PDF Automation** - Extract text, merge files, fill forms programmatically
- **Image Processing** - Batch resize, compress, watermark images
- **Database Query Helper** - Generate optimized SQL from natural language
- **API Integration** - Common REST API patterns and testing workflows

## A Note on Maintenance

I'm treating this as a living collection. As I use these skills, I discover edge cases and opportunities for improvement. Each skill gets better over time based on real-world feedback.

If you use one of these skills and run into issues, please open an issue! I'm genuinely interested in making these as robust as possible.

## Contributing Ideas

While this is primarily my personal portfolio, I'm open to suggestions:

- Found a bug? → [Open an issue](https://github.com/eshbanbahadur/agentic-ai-portfolio/issues)
- Have an idea for a skill? → I'd love to hear it!
- Built something similar? → Share it! I'm always learning

## Background

I'm Eshban Bahadur, a Software Engineer & Engineering Manager focused on building autonomous AI systems. My day job involves leading teams, but my passion project is figuring out how to make AI agents genuinely useful for everyday development work.

Claude Code skills are part of that exploration—small, focused tools that handle specific tasks really well. My larger goal is building "Digital FTEs" (Full-Time Equivalents)—AI systems that can handle entire job functions autonomously. Skills are the building blocks for that vision.

**Connect with me:**  
[LinkedIn](https://www.linkedin.com/in/eshban/) • [GitHub](https://github.com/eshbanbahadur) • [Main Portfolio](https://github.com/eshbanbahadur/agentic-ai-portfolio)

---

## Technical Notes

### Skill Structure
Each skill follows this pattern:
```
skill-name/
├── SKILL.md              # Core instructions (lean and focused)
├── scripts/              # Executable Python/Bash scripts
│   └── main_script.py
└── references/           # Detailed guides (loaded as needed)
    ├── usage_guide.md
    └── advanced_techniques.md
```

### Why This Structure?
- **SKILL.md** stays slim (under 500 lines) to minimize Claude Code's context usage
- **scripts/** contain production-ready code that just works
- **references/** hold advanced info that's only loaded when needed

This "progressive disclosure" approach keeps Claude Code efficient while still providing deep functionality when required.

---

## FAQ

**Q: Can I use these without Claude Code?**  
A: Absolutely! The Python scripts in each skill work standalone. Just run them directly.

**Q: Do these work with other AI assistants?**  
A: In theory, yes. The SKILL.md format is just structured markdown. Other systems could read it too.

**Q: Are these production-ready?**  
A: The ones marked "available" are. I use them in real projects. Beta skills are functional but still being refined.

**Q: How do I request a new skill?**  
A: Open an issue describing the workflow you want to automate. If it's something I'd use too, I'll build it!

---

## License

MIT License - Use these however you like. Attribution appreciated but not required.

If you build something cool with these skills, I'd love to hear about it!

---

*Last updated: January 2026*  
*Skills: 1 available, more in development*

**⭐ If you find these useful, consider starring the repo!**
