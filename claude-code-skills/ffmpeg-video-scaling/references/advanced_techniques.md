# FFmpeg Advanced Techniques & Quality Optimization

This guide shows advanced FFmpeg techniques using subprocess calls in Python.

## Quality vs File Size Trade-offs

### CRF (Constant Rate Factor) Values
- **18-20**: Near-lossless quality, large file sizes
- **23**: Default, good balance (recommended starting point)
- **28**: Acceptable quality, smaller files
- **32+**: Lower quality, smallest files

### Encoding Presets
Speed vs compression efficiency trade-off:
- **ultrafast**: Fastest encoding, largest files
- **fast/medium**: Good balance (recommended)
- **slow/slower**: Best compression, longer encoding time
- **veryslow**: Maximum compression efficiency, very slow

## Two-Pass Encoding for Better Quality

For best quality at target bitrate, use two-pass encoding:

```python
import subprocess

input_path = 'input.mp4'
output_path = 'output.mp4'
bitrate = '2M'

# First pass
subprocess.run([
    'ffmpeg',
    '-i', input_path,
    '-vf', 'scale=1280:720',
    '-c:v', 'libx264',
    '-b:v', bitrate,
    '-pass', '1',
    '-f', 'mp4',
    '-y',
    '/dev/null'  # On Windows use 'NUL'
], check=True)

# Second pass
subprocess.run([
    'ffmpeg',
    '-i', input_path,
    '-vf', 'scale=1280:720',
    '-c:v', 'libx264',
    '-b:v', bitrate,
    '-pass', '2',
    '-c:a', 'aac',
    '-b:a', '128k',
    '-y',
    output_path
], check=True)
```

## Maintaining Aspect Ratio

### Scale to width, auto-calculate height
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:-1',  # -1 means auto-calculate to maintain aspect ratio
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '23',
    '-y',
    'output.mp4'
], check=True)
```

### Scale to height, auto-calculate width
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=-1:720',
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '23',
    '-y',
    'output.mp4'
], check=True)
```

### Scale to fit within dimensions (letterbox/pillarbox)
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black',
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '23',
    '-y',
    'output.mp4'
], check=True)
```

## Hardware Acceleration

### NVIDIA GPU (NVENC)
```python
subprocess.run([
    'ffmpeg',
    '-hwaccel', 'cuda',
    '-i', 'input.mp4',
    '-vf', 'scale_cuda=1280:720',
    '-c:v', 'h264_nvenc',
    '-preset', 'p4',  # p1 (fastest) to p7 (slowest)
    '-rc:v', 'vbr',
    '-cq:v', '23',
    '-y',
    'output.mp4'
], check=True)
```

### Intel Quick Sync (QSV)
```python
subprocess.run([
    'ffmpeg',
    '-hwaccel', 'qsv',
    '-i', 'input.mp4',
    '-vf', 'scale_qsv=1280:720',
    '-c:v', 'h264_qsv',
    '-preset', 'medium',
    '-y',
    'output.mp4'
], check=True)
```

### Apple VideoToolbox (macOS)
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:720',
    '-c:v', 'h264_videotoolbox',
    '-b:v', '2M',
    '-y',
    'output.mp4'
], check=True)
```

## Audio Handling

### Copy audio stream (no re-encoding)
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:720',
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '23',
    '-c:a', 'copy',  # Copy audio without re-encoding
    '-y',
    'output.mp4'
], check=True)
```

### Adjust audio bitrate
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:720',
    '-c:v', 'libx264',
    '-c:a', 'aac',
    '-b:a', '192k',  # Higher quality audio
    '-y',
    'output.mp4'
], check=True)
```

### Remove audio
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'scale=1280:720',
    '-c:v', 'libx264',
    '-an',  # No audio
    '-y',
    'output.mp4'
], check=True)
```

## Adaptive Bitrate (ABR) for Streaming

Generate multiple qualities for adaptive streaming:

```python
import subprocess

RESOLUTIONS = {
    '1080p': (1920, 1080),
    '720p': (1280, 720),
    '480p': (854, 480),
    '360p': (640, 360)
}

qualities = [
    {'resolution': '1080p', 'bitrate': '5000k'},
    {'resolution': '720p', 'bitrate': '2800k'},
    {'resolution': '480p', 'bitrate': '1400k'},
    {'resolution': '360p', 'bitrate': '800k'}
]

for quality in qualities:
    width, height = RESOLUTIONS[quality['resolution']]
    subprocess.run([
        'ffmpeg',
        '-i', 'input.mp4',
        '-vf', f'scale={width}:{height}',
        '-c:v', 'libx264',
        '-b:v', quality['bitrate'],
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y',
        f"output_{quality['resolution']}.mp4"
    ], check=True)
    print(f"✓ Created {quality['resolution']} version")
```

## Probe Video Information

Get video metadata before processing using ffprobe:

```python
import subprocess
import json

def get_video_info(input_path):
    """Get video metadata using ffprobe."""
    result = subprocess.run([
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_format',
        '-show_streams',
        input_path
    ], capture_output=True, text=True, check=True)
    
    probe_data = json.loads(result.stdout)
    
    # Find video stream
    video_stream = next(
        s for s in probe_data['streams'] 
        if s['codec_type'] == 'video'
    )
    
    return {
        'width': int(video_stream['width']),
        'height': int(video_stream['height']),
        'codec': video_stream['codec_name'],
        'duration': float(probe_data['format']['duration']),
        'bitrate': int(probe_data['format']['bit_rate'])
    }

# Example usage
info = get_video_info('input.mp4')
print(f"Resolution: {info['width']}x{info['height']}")
print(f"Duration: {info['duration']:.2f}s")
print(f"Bitrate: {info['bitrate'] // 1000}kbps")
```

## Common Filters

### Deinterlace video
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'yadif,scale=1280:720',  # Deinterlace then scale
    '-c:v', 'libx264',
    '-y',
    'output.mp4'
], check=True)
```

### Adjust frame rate
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'fps=30,scale=1280:720',  # Set to 30fps then scale
    '-c:v', 'libx264',
    '-y',
    'output.mp4'
], check=True)
```

### Add watermark
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-i', 'watermark.png',
    '-filter_complex', '[0:v]scale=1280:720[scaled];[scaled][1:v]overlay=10:10',
    '-c:v', 'libx264',
    '-y',
    'output.mp4'
], check=True)
```

### Crop video
```python
subprocess.run([
    'ffmpeg',
    '-i', 'input.mp4',
    '-vf', 'crop=1280:720:0:0,scale=1280:720',  # Crop then scale
    '-c:v', 'libx264',
    '-y',
    'output.mp4'
], check=True)
```

## Batch Processing with Parallel Execution

Process multiple videos in parallel using multiprocessing:

```python
import subprocess
from pathlib import Path
from multiprocessing import Pool

def scale_video_wrapper(args):
    """Wrapper function for parallel processing."""
    input_path, resolution = args
    output_path = f"{Path(input_path).stem}_{resolution}.mp4"
    
    subprocess.run([
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={RESOLUTIONS[resolution][0]}:{RESOLUTIONS[resolution][1]}',
        '-c:v', 'libx264',
        '-preset', 'medium',
        '-crf', '23',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y',
        output_path
    ], check=True, capture_output=True)
    
    return output_path

# Process multiple videos in parallel
video_files = ['video1.mp4', 'video2.mp4', 'video3.mp4']
tasks = [(video, '720p') for video in video_files]

with Pool(processes=4) as pool:
    results = pool.map(scale_video_wrapper, tasks)

print(f"✓ Processed {len(results)} videos")
```

## Performance Tips

1. **Use hardware acceleration when available** (10-20x faster encoding)
2. **For batch processing, process videos in parallel** using multiprocessing
3. **Use faster presets for preview** (ultrafast) and slower for final output
4. **Consider target platform** - mobile devices need smaller files
5. **Test CRF values** on sample clips before processing full videos
6. **Copy audio when possible** to save processing time (`-c:a copy`)
7. **Use two-pass encoding** only when targeting specific file sizes
