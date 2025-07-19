from config.settings import VIDEO_PATH, AUDIO_PATH, IMAGE_PATH, FRAME_INTERVAL, NSFW_THRESHOLD, OUTPUT_FOLDER
from utils.audio_utils import extract_audio
from detectors.foul_language_detector import transcribe_audio, detect_foul_language
from detectors.nsfw_image_detector import check_nudity_image
from detectors.nsfw_video_detector import extract_and_classify_frames

def main():
    audio_file = extract_audio(VIDEO_PATH, AUDIO_PATH)
    transcription = transcribe_audio(audio_file)
    print(f"Transcript:\n{transcription}\n")
    if detect_foul_language(transcription):
        print("🔞 Foul language found!")
    else:
        print("✅ No foul words.")
    if check_nudity_image(IMAGE_PATH):
        print("⚠️ Nudity in image!")
    else:
        print("✅ Safe image.")
    nsfw_frames = extract_and_classify_frames(VIDEO_PATH, OUTPUT_FOLDER, FRAME_INTERVAL, NSFW_THRESHOLD)
    if nsfw_frames:
        for frame, score in nsfw_frames:
            print(f"⚠️ NSFW Frame {frame} - Score {score}")
    else:
        print("✅ Video is clean.")

if __name__ == '__main__':
    main()
