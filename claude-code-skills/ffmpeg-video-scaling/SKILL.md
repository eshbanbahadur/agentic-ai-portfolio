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

If not installed: 
- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `apt install ffmpeg`
- **Windows:** Download from ffmpeg.org

## Quick Start

### Finding the Script

The skill script is located in this skill's directory structure:
```
ffmpeg-video-scaling/
└── scripts/
    └── scale_video.py
```

### Basic Usage

```bash
# Use python3 (required on macOS)
python3 scripts/scale_video.py INPUT_VIDEO.mp4 720p
```

**Important:** Always use **absolute paths** for input/output files:
```bash
python3 scripts/scale_video.py /full/path/to/video.mp4 720p
```

This creates `video_720p.mp4` in the same directory as the input.

**Common resolutions:** 1080p, 720p, 480p, 360p, 240p

## Script Parameters

```bash
python3 scripts/scale_video.py <input> <resolution> [output_path] [preset] [crf]
```

**Parameters:**
- `input` - Full path to input video (required)
- `resolution` - Target: 1080p, 720p, 480p, 360p, 240p (required)
- `output_path` - Full path for output (optional, default: `{input_name}_{resolution}.mp4`)
- `preset` - Speed: ultrafast, fast, medium (default), slow, veryslow
- `crf` - Quality: 0-51, lower=better, 23=default

## Examples

### Scale to 720p
```bash
python3 scripts/scale_video.py /Users/username/videos/presentation.mp4 720p
# Creates: /Users/username/videos/presentation_720p.mp4
```

### Custom output location
```bash
python3 scripts/scale_video.py /Users/username/videos/input.mp4 480p /Users/username/output/mobile.mp4
```

### Fast encoding for previews
```bash
python3 scripts/scale_video.py /path/to/video.mp4 360p output.mp4 ultrafast 28
```

### High quality for archival
```bash
python3 scripts/scale_video.py /path/to/video.mp4 1080p archive.mp4 slow 18
```

## Batch Processing

To create multiple resolutions, run the script multiple times:

```bash
python3 scripts/scale_video.py /path/to/video.mp4 720p
python3 scripts/scale_video.py /path/to/video.mp4 480p
python3 scripts/scale_video.py /path/to/video.mp4 360p
```

## Quality Settings

### CRF Values (Quality Control)
- **18-20**: Near-lossless, very large files (archival)
- **23**: Default, good balance ✓
- **28**: Acceptable quality, smaller files (mobile)
- **32+**: Lower quality, smallest files

### Preset Selection
- **ultrafast**: Fastest encoding, largest files (previews)
- **medium**: Recommended balance ✓
- **slow/slower**: Best compression, longer time (final output)

## Common Workflows

### Mobile Video Optimization
```bash
python3 scripts/scale_video.py /path/to/video.mp4 480p mobile.mp4 medium 28
```

### Web Streaming Package
```bash
# Create multiple resolutions for adaptive streaming
python3 scripts/scale_video.py /path/to/source.mp4 1080p
python3 scripts/scale_video.py /path/to/source.mp4 720p
python3 scripts/scale_video.py /path/to/source.mp4 480p
python3 scripts/scale_video.py /path/to/source.mp4 360p
```

### Quick Preview Generation
```bash
python3 scripts/scale_video.py /path/to/large.mp4 360p preview.mp4 ultrafast
```

## Advanced Techniques

For advanced features including:
- Hardware acceleration (NVIDIA, Intel, Apple)
- Two-pass encoding for optimal quality
- Adaptive bitrate for streaming
- Audio handling options
- Video metadata probing
- Custom filters (deinterlace, watermark, crop)

See the `references/advanced_techniques.md` file in this skill directory.

## Troubleshooting

**"ffmpeg: command not found"**
- Install FFmpeg using the instructions in Prerequisites section

**"FileNotFoundError: No such file or directory"**
- Use absolute paths for input/output files
- Example: `/Users/username/videos/file.mp4` not `videos/file.mp4`

**Slow encoding speed**
- Use faster preset: `fast` or `ultrafast`
- Or enable hardware acceleration (see advanced_techniques.md)

**Poor quality output**
- Lower CRF value (try 20 instead of 23)
- Use slower preset (slow or slower)

**Audio sync issues**
- This is rare with default settings
- If occurs, see advanced_techniques.md for audio handling options

## Important Notes

1. **Always use absolute paths** - Relative paths can fail depending on working directory
2. **Use python3 on macOS** - MacOS doesn't have `python` command by default
3. **FFmpeg required** - The script won't work without FFmpeg installed
4. **Aspect ratio maintained** - The script automatically preserves aspect ratio
5. **Output overwrites** - If output file exists, it will be overwritten without warning
