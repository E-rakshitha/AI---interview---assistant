from streamlit_mic_recorder import speech_to_text


def record_voice():
    text = speech_to_text(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        language="en",
        use_container_width=True,
        just_once=True,
        key="voice"
    )

    return text