from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
import random
import os

# Function to add random video sources
def add_video_sources(directory):
    video_clips = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            clip = VideoFileClip(os.path.join(directory, filename))
            video_clips.append(clip)
    return video_clips

# Function to add random audio sounds
def add_audio_sounds(directory):
    audio_clips = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            clip = AudioFileClip(os.path.join(directory, filename))
            audio_clips.append(clip)
    return audio_clips

# Function to add random audio music
def add_audio_music(directory):
    audio_clips = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            clip = AudioFileClip(os.path.join(directory, filename))
            audio_clips.append(clip)
    return audio_clips

# Function to add random images/GIFs
def add_images(directory):
    image_clips = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".gif") or filename.endswith(".png"):
            clip = ImageClip(os.path.join(directory, filename))
            image_clips.append(clip)
    return image_clips

# Function to generate a YTP-style video
def generate_ytp(video_sources_dir, audio_sounds_dir, audio_music_dir, images_dir, output_file, duration=10):
    # Add video sources
    video_clips = add_video_sources(video_sources_dir)
    # Add audio sounds
    audio_sounds = add_audio_sounds(audio_sounds_dir)
    # Add audio music
    audio_music = add_audio_music(audio_music_dir)
    # Add images/GIFs
    image_clips = add_images(images_dir)

    final_clips = []
    
    # Add random video clips
    for _ in range(duration):
        clip = random.choice(video_clips)
        final_clips.append(clip)
    
    # Add random audio sounds
    for _ in range(duration):
        clip = random.choice(audio_sounds)
        final_clips.append(clip)
    
    # Add random audio music
    for _ in range(duration):
        clip = random.choice(audio_music)
        final_clips.append(clip)
    
    # Add random images/GIFs
    for _ in range(duration):
        clip = random.choice(image_clips)
        final_clips.append(clip.set_duration(random.uniform(1, 3)))  # Random duration for images

    # Shuffle final clips
    random.shuffle(final_clips)

    # Concatenate all clips
    final_video = concatenate_videoclips(final_clips)

    # Generate final video
    final_video.write_videofile(output_file, codec='libx264')

# Example usage
video_sources_dir = "video_sources_directory"
audio_sounds_dir = "audio_sounds_directory"
audio_music_dir = "audio_music_directory"
images_dir = "images_directory"
output_file = "output_ytp.mp4"
generate_ytp(video_sources_dir, audio_sounds_dir, audio_music_dir, images_dir, output_file)
