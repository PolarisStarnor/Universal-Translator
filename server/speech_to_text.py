# Takes an audio file and turns it into text
import torch
import pathlib
import librosa
from transformers import Speech2TextProcessor, Speech2TextForConditionalGeneration


MODEL = Speech2TextForConditionalGeneration.from_pretrained("facebook/s2t-small-librispeech-asr")
PROCESSOR = Speech2TextProcessor.from_pretrained("facebook/s2t-small-librispeech-asr")

def transcribe(speech : pathlib.Path) -> str:
    """
    Translate an audio file into a text file.

    @param speech: an audio file name

    @return text: the transcription of the audio file
    """
    target_sample_rate = 16000

    array, sample_rate = librosa.load(speech.as_posix(), sr=target_sample_rate)

    audio = PROCESSOR(array, sampling_rate=target_sample_rate, return_tensors="pt")

    inputs = MODEL.generate(
        audio["input_features"],
        attention_mask=audio["attention_mask"],
        # forced_bos_token_id=PROCESSOR.tokenizer.lang_code_to_id[language],
    )
    out = PROCESSOR.batch_decode(inputs, skip_special_tokens=True)
    # print(out)

    return out[0]
