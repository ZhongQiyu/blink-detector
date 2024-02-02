import gradio as gr
from transformers import pipeline, CLIPProcessor, CLIPModel, Wav2Vec2ForCTC, Wav2Vec2Processor, GPT2Tokenizer, GPT2LMHeadModel
import torch
from PIL import Image
import librosa
import soundfile as sf

# 文本情绪分析
sentiment_pipeline = pipeline("sentiment-analysis")

# 图像处理 - CLIP
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

# 音频处理 - wav2vec 2.0
wav2vec_processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
wav2vec_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# 聊天机器人 - GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def process_text(text):
    result = sentiment_pipeline(text)
    return str(result)

def process_image(image):
    inputs = clip_processor(images=image, return_tensors="pt", padding=True)
    outputs = clip_model(**inputs)
    return "CLIP model processed the image."

def process_audio(audio):
    audio_data, sampling_rate = librosa.load(audio, sr=16000)
    inputs = wav2vec_processor(audio_data, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = wav2vec_model(inputs.input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = wav2vec_processor.batch_decode(predicted_ids)
    return transcription[0]

def chat_with_gpt2(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

iface = gr.Interface(
    fn={
        "text": process_text,
        "image": process_image,
        "audio": process_audio,
        "chat": chat_with_gpt2
    },
    inputs=[
        gr.inputs.Textbox(label="Input Text for Sentiment Analysis"),
        gr.inputs.Image(label="Input Image for CLIP"),
        gr.inputs.Audio(label="Input Audio for wav2vec 2.0", type="filepath"),
        gr.inputs.Textbox(label="Chat with GPT-2", lines=2)
    ],
    outputs=[
        gr.outputs.Textbox(label="Sentiment Analysis Result"),
        gr.outputs.Textbox(label="Image Process Result"),
        gr.outputs.Textbox(label="Audio to Text Result"),
        gr.outputs.Textbox(label="Chatbot Response")
    ],
    title="Multi-Modal Interface with BERT, CLIP, wav2vec 2.0, and GPT-2",
    description="This interface uses BERT for text sentiment analysis, CLIP for image understanding, wav2vec 2.0 for audio processing, and GPT-2 for chatting."
)

iface.launch()
