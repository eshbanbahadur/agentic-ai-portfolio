# FFmpeg Video Scaling - Usage Guide

## Running the Script

The `scale_video.py` script uses Python's subprocess to call FFmpeg directly (no external dependencies needed).

### Basic Usage

```bash
python /mnt/skills/user/ffmpeg-video-scaling/scripts/scale_video.py <input> <resolution>
```

**Example:**
```bash
python scale_video.py video.mp4 720p
```

Output: `video_720p.mp4` (created in same directory as input)

### Full Command Syntax

```bash
python scale_video.py <input> <resolution> [output_path] [preset] [crf]
```

**Parameters:**
- `input` - Path to input video file (required)
- `resolution` - Target resolution: 1080p, 720p, 480p, 360p, 240p (required)
- `output_path` - Custom output file path (optional, default: `{input_name}_{resolution}.mp4`)
- `preset` - Encoding speed preset (optional, default: `medium`)
- `crf` - Quality value 0-51 (optional, default: `23`)

### Examples

**Scale to 720p with defaults:**
```bash
python scale_video.py input.mp4 720p
```

**Custom output path:**
```bash
python scale_video.py input.mp4 480p /path/to/output/mobile.mp4
```

**Fast encoding with lower quality:**
```bash
python scale_video.py input.mp4 720p output.mp4 fast 28
```

**High quality, slow encoding:**
```bash
python scale_video.py input.mp4 1080p hq_output.mp4 slow 18
```

## Batch Processing

To scale to multiple resolutions at once, call the script multiple times:

```bash
# Create 720p, 480p, and 360p versions
for res in 720p 480p 360p; do
    python scale_video.py input.mp4 $res
done
```

Or write a simple Python wrapper:

```python
import subprocess

input_file = 'input.mp4'
resolutions = ['720p', '480p', '360p']

for res in resolutions:
    subprocess.run([
        'python',
        '/mnt/skills/user/ffmpeg-video-scaling/scripts/scale_video.py',
        input_file,
        res
    ])
```

## Quality Settings

### CRF (Constant Rate Factor)
Controls output quality. Lower = better quality, larger file size.

- **18-20**: Near-lossless quality (recommended for archival)
- **23**: Default, good balance (recommended for most use cases)
- **28**: Acceptable quality, smaller files (good for mobile)
- **32+**: Lower quality, smallest files (use sparingly)

**Example:**
```bash
# High quality for archival
python scale_video.py input.mp4 1080p archive.mp4 slow 18

# Smaller file for mobile
python scale_video.py input.mp4 480p mobile.mp4 fast 28
```

### Encoding Presets
Controls encoding speed vs compression efficiency trade-off.

- **ultrafast**: Fastest encoding, largest output files
- **fast**: Quick encoding, larger files
- **medium**: Balanced (default, recommended)
- **slow**: Better compression, takes longer
- **slower/veryslow**: Maximum compression, very slow

**Example:**
```bash
# Quick preview generation
python scale_video.py input.mp4 360p preview.mp4 ultrafast

# Final output with best compression
python scale_video.py input.mp4 720p final.mp4 slow
```

## Resolution Details

Standard resolutions and their dimensions:

| Resolution | Width × Height | Use Case |
|------------|----------------|----------|
| 1080p | 1920 × 1080 | HD content, YouTube, modern displays |
| 720p | 1280 × 720 | HD streaming, compatible devices |
| 480p | 854 × 480 | SD streaming, older devices |
| 360p | 640 × 360 | Low bandwidth, mobile data saving |
| 240p | 426 × 240 | Minimal bandwidth, previews |

**Note:** The script maintains the original aspect ratio. If input is not 16:9, it will adjust height proportionally.

## Common Workflows

### Mobile Optimization
Create optimized version for mobile viewing:
```bash
python scale_video.py video.mp4 480p mobile.mp4 medium 28
```

### Web Streaming - Multiple Qualities
Generate multiple versions for adaptive streaming:
```bash
python scale_video.py source.mp4 1080p
python scale_video.py source.mp4 720p
python scale_video.py source.mp4 480p
python scale_video.py source.mp4 360p
```

### Quick Preview
Fast low-resolution preview for reviewing content:
```bash
python scale_video.py large_file.mp4 360p preview.mp4 ultrafast
```

### Archive to Smaller Size
Maintain quality while reducing resolution:
```bash
python scale_video.py 4k_video.mp4 1080p archive.mp4 slow 20
```

## Using the Script in Your Own Code

You can import and use the functions directly:

```python
from scale_video import scale_video, batch_scale_video

# Scale single video
scale_video('input.mp4', 'output_720p.mp4', '720p')

# Scale with custom settings
scale_video('input.mp4', 'output.mp4', '480p', preset='fast', crf=28)

# Batch process to multiple resolutions
batch_scale_video(
    'input.mp4',
    output_dir='./outputs',
    resolutions=['720p', '480p', '360p']
)
```

## Troubleshooting

**"ffmpeg: command not found"**
- Install FFmpeg: `apt install ffmpeg` (Ubuntu) or equivalent
- Verify: `ffmpeg -version`

**"FileNotFoundError: No such file or directory"**
- Check input file path is correct
- Use absolute paths if working directory is unclear

**Output quality is poor**
- Lower CRF value (try 20 instead of 23)
- Use slower preset (slow or slower)

**Encoding is too slow**
- Use faster preset (fast or ultrafast)
- Consider hardware acceleration (see advanced_techniques.md)

**File size is too large**
- Increase CRF value (try 28 instead of 23)
- Use faster preset (trades compression for speed)

**Audio is out of sync**
- This is rare with the default settings
- Try copying audio stream without re-encoding (requires script modification)
