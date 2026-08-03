---
date: 2026-04-07
source: chatgpt
title: "Running local LLMs"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "I have a Lenovo P3 workstation, one of the, like, small form factors. What would be the way that I could, or how strong of a local LLM could I run?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_00000000a3bc71f59644392e6f16e413", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:20:56.562521+00:00", "format": "wav", "metadata": {"end": 15.19, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 729198, "tool_audio_direction": null}, "audio_start_timestamp": 19.340923002921045, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:20:56.562521+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "On a small form factor workstation like that, you can run a pretty capable local language model, depending on your specs. If you\u2019ve got a decent modern CPU (maybe 6-8 cores) and at least 16 GB of RAM, you could comfortably run something like a 7-billion-parameter model. If you\u2019ve got a dedicated GPU or more memory\u201432 GB or more\u2014then you could push up to something like a 13-billion-parameter model. It\u2019s all about balancing model size with available RAM and patience!"}
{"asset_pointer": "sediment://file_00000000854871f5a806c3a7ebf9d6bc", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:20:56.562581+00:00", "format": "wav", "metadata": {"end": 27.25, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1308078, "tool_audio_direction": null}

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "What parameter model size is LLaMA 3.5?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_0000000040a471f59e92767e492b7659", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:21:23.580602+00:00", "format": "wav", "metadata": {"end": 3.7, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 177678, "tool_audio_direction": null}, "audio_start_timestamp": 50.45382564282045, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:21:23.580602+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "As of now, there isn\u2019t a \"LLaMA 3.5\" specifically. The well-known versions are LLaMA 2 models, which come in various sizes\u20147 billion, 13 billion, and 70 billion parameters. If a future \"LLaMA 3.5\" exists, it would likely follow a similar pattern\u2014offering models in different parameter sizes. But for now, the largest released LLaMA model was 70 billion parameters."}
{"asset_pointer": "sediment://file_000000004f9471f5a25404fc8832bdc9", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:21:23.580672+00:00", "format": "wav", "metadata": {"end": 23.0, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1104078, "tool_audio_direction": null}

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "What's the difference between a 7 and a 13 billion?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_000000006d8871f59031839b7274d20e", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:21:56.764928+00:00", "format": "wav", "metadata": {"end": 3.34, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 160398, "tool_audio_direction": null}, "audio_start_timestamp": 79.1309850118123, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:21:56.764928+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "The difference mainly comes down to scale and capability. A 13-billion-parameter model generally handles more nuanced language, deeper reasoning, or longer contexts than a 7-billion-parameter one. The 13-billion model might be more accurate, handle more complex tasks, or maintain context over longer conversations. But it also needs more memory and compute power. In short: bigger models tend to be more capable, but they also demand more resources!"}
{"asset_pointer": "sediment://file_00000000a134722fb89bae5c9a774196", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:21:56.764982+00:00", "format": "wav", "metadata": {"end": 27.45, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1317678, "tool_audio_direction": null}

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "What do I need to run the 13 billion parameter?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_00000000512871f58df6479391680098", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:22:54.356616+00:00", "format": "wav", "metadata": {"end": 2.93, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 140718, "tool_audio_direction": null}, "audio_start_timestamp": 135.42262452282012, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:22:54.356616+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "To run a 13-billion-parameter model smoothly, you typically want at least 24 to 32 GB of RAM\u2014the more, the better. If you have a GPU, something like an NVIDIA card with at least 24 GB of VRAM\u2014like an RTX 3090 or higher\u2014can really speed things up. Without a strong GPU, it\u2019ll rely on your CPU, but you\u2019ll need patience. Also, ensure you have enough disk space and a framework like llama.cpp or Ollama to run it efficiently."}
{"asset_pointer": "sediment://file_00000000cfe071f58f08119712a53557", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:22:54.356678+00:00", "format": "wav", "metadata": {"end": 28.4, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1363278, "tool_audio_direction": null}

**You:** {"audio_asset_pointer": {"asset_pointer": "sediment://file_0000000077c871f5b4faaa00fb162594", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:23:27.086985+00:00", "format": "wav", "metadata": {"end": 6.16, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 295758, "tool_audio_direction": null}, "audio_start_timestamp": 173.51436322601512, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:23:27.086985+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}
{"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "I have the Lenovo P3, which has 32 gigabytes of RAM."}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "With 32 gigs of RAM, you\u2019re in a great spot for a 13-billion-parameter model! You should be able to run it comfortably, especially if you\u2019re using an efficient library like llama.cpp or Ollama. If you have a decent CPU or a mid-range GPU, inference times should be reasonable. You\u2019ve got enough headroom to experiment, so you can confidently dive into larger models!"}
{"asset_pointer": "sediment://file_0000000092cc722fb33ec7c122cb144c", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:23:27.087060+00:00", "format": "wav", "metadata": {"end": 23.0, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1104078, "tool_audio_direction": null}

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "What GPU does the P3 usually come with?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_00000000ba14722f8c6d2d3948382dd3", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:24:01.686903+00:00", "format": "wav", "metadata": {"end": 4.21, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 202158, "tool_audio_direction": null}, "audio_start_timestamp": 200.95557116018608, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:24:01.686903+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "The Lenovo P3 Tiny often comes in a few configurations, but one common option is an NVIDIA T1000 GPU. That\u2019s a lightweight professional GPU, good for certain graphics workloads but not as powerful for large LLMs as the heavy-duty RTX or A-series GPUs. That said, you can still run smaller models or rely on CPU inference. If you have a higher configuration, you might get something like an RTX A500. Always good to check your specific build!"}
{"asset_pointer": "sediment://file_00000000c0b871f58df67a36622908b4", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:24:01.686982+00:00", "format": "wav", "metadata": {"end": 30.35, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1456878, "tool_audio_direction": null}

**You:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "in", "text": "How tough would it be to run the 13 billion parameter with that GPU you mentioned?"}
{"audio_asset_pointer": {"asset_pointer": "sediment://file_00000000e95471f58c41fd6b506562d1", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:24:39.321144+00:00", "format": "wav", "metadata": {"end": 7.29, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 349998, "tool_audio_direction": null}, "audio_start_timestamp": 240.7718417341821, "content_type": "real_time_user_audio_video_asset_pointer", "expiry_datetime": "2026-05-07T17:24:39.321144+00:00", "frames_asset_pointers": [], "video_container_asset_pointer": null}

**ChatGPT:** {"content_type": "audio_transcription", "decoding_id": null, "direction": "out", "text": "With something like an NVIDIA T1000, it\u2019s doable but will rely heavily on your CPU and RAM. The T1000 only has a modest amount of VRAM\u2014usually around 4 to 8 GB\u2014so it won\u2019t fit the whole 13-billion model there. Instead, you\u2019d likely run it on the CPU with offloading. It\u2019ll be slower\u2014responses might take several seconds. But with your 32 GB of RAM, you can still run it\u2014it\u2019s just not going to be lightning fast."}
{"asset_pointer": "sediment://file_0000000033b0722fa7c0bca6e4057608", "content_type": "audio_asset_pointer", "expiry_datetime": "2026-05-07T17:24:39.321209+00:00", "format": "wav", "metadata": {"end": 27.85, "end_timestamp": null, "interruptions": null, "original_audio_source": null, "pretokenized_vq": null, "start": 0.0, "start_timestamp": null, "transcription": null, "word_transcription": null}, "size_bytes": 1336878, "tool_audio_direction": null}

**You:** https://ollama.com/library/qwen3:8b

**ChatGPT:** Yep — that specific Ollama model is **Qwen3 8B**, and the page lists it as **8.19 billion parameters**. The default Ollama build shown there is a **Q4_K_M quantization** and is about **5.2 GB** on disk. citeturn240381view0

For your **Lenovo P3 Tiny / SFF with 32 GB RAM**, this is much more realistic than a 13B model:
- **8B:** very doable
- **13B/14B:** possible, but noticeably heavier
- **30B+:** generally not a good fit unless you have a much stronger GPU and more memory headroom

Your machine should run **Qwen3:8b** comfortably on system RAM even if the GPU is modest, because the model package itself is only about **5.2 GB** in that quantized form. citeturn240381view0

The other nice part is that Ollama shows Qwen3 comes in multiple sizes — **0.6b, 1.7b, 4b, 8b, 14b, 30b, 32b, 235b** — so **8b** sits in a very practical middle ground for local use on a workstation like yours. citeturn240381view0

If your goal is:
- **general chat / summarizing / everyday use:** **8B is probably the sweet spot**
- **best quality you can reasonably try on that box:** test **14B**
- **fastest local experience:** try **4B** too

Command:
```bash
ollama run qwen3:8b
```
That is the exact run command on the model page. citeturn240381view0

My honest take: **start with Qwen3:8b first**. It is the safest bet for your P3 and probably the best balance of speed and quality.
