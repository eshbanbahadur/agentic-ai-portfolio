---
name: ffmpeg-video-scaling
description: "Scale videos from 1080p to lower resolutions (720p, 480p, 360p, 240p) using FFmpeg with Python subprocess calls. Use when the user needs to: (1) Downscale high-resolution videos to smaller sizes, (2) Create multiple resolution versions of a video, (3) Reduce video file sizes while maintaining quality, (4) Prepare videos for different platforms or devices, or (5) Batch process videos to multiple resolutions."
---

# FFmpeg Video Scaling

Scale videos by calling FFmpeg directly via Python subprocess.

## Prerequisites

FFmpeg must be installed on the system:
```bash
ffmpeg -version  # Verify installation
```

If not installed: `apt install ffmpeg` (Ubuntu) or equivalent for your system.

## Quick Start

Use the provided script to scale videos:

```bash
python /mnt/skills/user/ffmpeg-video-scaling/scripts/scale_video.py input.mp4 720p
```

This creates `input_720p.mp4` in the same directory.

**Common resolutions:** 1080p, 720p, 480p, 360p, 240p

## Usage Guide

For complete usage instructions including:
- Script parameters and examples
- Batch processing multiple resolutions
- Quality optimization (CRF values, presets)
- Custom output paths

Read the usage guide:
```python
with open('/mnt/skills/user/ffmpeg-video-scaling/references/usage_guide.md') as f:
    print(f.read())
```

## Advanced Techniques

For hardware acceleration, two-pass encoding, adaptive bitrate, and custom filters:
```python
with open('/mnt/skills/user/ffmpeg-video-scaling/references/advanced_techniques.md') as f:
    print(f.read())
```
