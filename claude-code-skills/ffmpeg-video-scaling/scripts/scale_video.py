#!/usr/bin/env python3
"""
FFmpeg video scaling script using subprocess (no external dependencies required).
Scales 1080p videos to lower resolutions: 720p, 480p, 360p, 240p
"""

import subprocess
import sys
import os
from pathlib import Path

# Common resolution presets (width x height)
RESOLUTIONS = {
    '1080p': (1920, 1080),
    '720p': (1280, 720),
    '480p': (854, 480),
    '360p': (640, 360),
    '240p': (426, 240)
}

def scale_video(input_path, output_path, target_resolution='720p', preset='medium', crf=23):
    """
    Scale a video to a target resolution using FFmpeg via subprocess.
    
    Args:
        input_path: Path to input video file
        output_path: Path to output video file
        target_resolution: Target resolution (e.g., '720p', '480p') or tuple (width, height)
        preset: FFmpeg encoding preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
        crf: Constant Rate Factor for quality (0-51, lower is better quality, 23 is default)
    """
    
    # Get target dimensions
    if isinstance(target_resolution, str):
        if target_resolution not in RESOLUTIONS:
            raise ValueError(f"Unknown resolution: {target_resolution}. Use one of {list(RESOLUTIONS.keys())}")
        width, height = RESOLUTIONS[target_resolution]
    else:
        width, height = target_resolution
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    # Build FFmpeg command
    # -i: input file
    # -vf scale: video filter for scaling (scale=width:height)
    # -c:v libx264: use H.264 video codec
    # -preset: encoding speed preset
    # -crf: constant rate factor (quality)
    # -c:a aac: use AAC audio codec
    # -b:a 128k: audio bitrate
    # -y: overwrite output file without asking
    
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={width}:{height}',
        '-c:v', 'libx264',
        '-preset', preset,
        '-crf', str(crf),
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y',
        output_path
    ]
    
    try:
        # Run FFmpeg command
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        
        print(f"✓ Successfully scaled video to {width}x{height}")
        print(f"  Input:  {input_path}")
        print(f"  Output: {output_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ FFmpeg error occurred:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        raise
    except FileNotFoundError:
        print("✗ Error: ffmpeg command not found. Please install FFmpeg.", file=sys.stderr)
        print("  Ubuntu/Debian: sudo apt install ffmpeg", file=sys.stderr)
        print("  macOS: brew install ffmpeg", file=sys.stderr)
        raise

def batch_scale_video(input_path, output_dir=None, resolutions=['720p', '480p'], preset='medium', crf=23):
    """
    Scale a video to multiple resolutions.
    
    Args:
        input_path: Path to input video file
        output_dir: Directory for output files (default: same as input)
        resolutions: List of target resolutions
        preset: FFmpeg encoding preset
        crf: Constant Rate Factor for quality
    """
    
    input_file = Path(input_path)
    if output_dir is None:
        output_dir = input_file.parent
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate output paths
    base_name = input_file.stem
    extension = input_file.suffix
    
    for resolution in resolutions:
        output_path = output_dir / f"{base_name}_{resolution}{extension}"
        print(f"\nScaling to {resolution}...")
        scale_video(input_path, str(output_path), resolution, preset, crf)
    
    print(f"\n✓ Batch scaling complete! Generated {len(resolutions)} versions.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scale_video.py <input_video> <target_resolution> [output_path] [preset] [crf]")
        print("\nExamples:")
        print("  python scale_video.py input.mp4 720p")
        print("  python scale_video.py input.mp4 720p output_720p.mp4")
        print("  python scale_video.py input.mp4 720p output.mp4 fast 20")
        print("\nAvailable resolutions:", ', '.join(RESOLUTIONS.keys()))
        print("\nPresets: ultrafast, superfast, veryfast, faster, fast, medium (default), slow, slower, veryslow")
        print("CRF: 0-51 (lower = better quality, 23 = default)")
        sys.exit(1)
    
    input_path = sys.argv[1]
    target_resolution = sys.argv[2]
    
    # Generate default output path
    input_file = Path(input_path)
    output_path = sys.argv[3] if len(sys.argv) > 3 else f"{input_file.stem}_{target_resolution}{input_file.suffix}"
    
    preset = sys.argv[4] if len(sys.argv) > 4 else 'medium'
    crf = int(sys.argv[5]) if len(sys.argv) > 5 else 23
    
    scale_video(input_path, output_path, target_resolution, preset, crf)

