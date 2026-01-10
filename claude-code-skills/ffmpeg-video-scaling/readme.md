🎬 FFmpeg Video Scaling

Scale videos efficiently without external dependencies
Automate video resolution conversion from 1080p to lower resolutions (720p, 480p, 360p, 240p) using FFmpeg. Perfect for preparing videos for different platforms, devices, or bandwidth requirements.

What it does:

Scales single videos with one command
Batch processes multiple resolutions simultaneously
Maintains aspect ratio automatically
Optimizes quality vs file size with presets
Zero Python dependencies (pure subprocess calls)

Use cases:

📱 Mobile app video optimization
🌐 Multi-bitrate streaming preparation
💾 Reducing file sizes for storage
🎥 Creating preview versions quickly

Technologies: Python, FFmpeg, Subprocess
📥 Download Skill | 📖 Documentation

🚀 Quick Start
Installing a Skill

Download the .skill file from the skill folder
Open Claude Code in your terminal
Upload to Claude Code:

   "Install this skill" + attach the .skill file

Start using it - just ask Claude naturally:

   "Scale my video.mp4 to 720p"
Using Skills
Skills trigger automatically when you ask Claude Code to do related tasks. No need to mention the skill name - just describe what you want!
Example:
You: "I need to create 720p and 480p versions of presentation.mp4"
Claude: *automatically uses ffmpeg-video-scaling skill*

💡 Why These Skills?
Built for Real Workflows
Each skill solves actual development problems I've encountered. They're not toy examples - they're production-ready tools used in real projects.
Progressive Disclosure Design
Skills are designed to be lightweight and efficient:

Slim core documentation (minimal context usage)
Detailed guides loaded only when needed
Reference materials for advanced use cases

Zero-Dependency Philosophy
Where possible, skills use standard library calls (like subprocess) instead of external packages. This means:

✅ Faster installation
✅ Fewer compatibility issues
✅ More reliable in different environments

