# Interspeech 2026 技术总结

会议：Interspeech 2026，悉尼，2026-09-27 至 2026-10-01。

材料来自两处：

- 官方日程：[Program](https://interspeech2026.org/en-AU/pages/program/program)
- 论文全文 PDF：[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)

组织方式有两层，中间是同一份单篇总结：

1. `docs/papers/`：每篇论文一份技术总结（问题、方法、实验与结果、结论、点评），依据 ISCA 全文，不另编数字。
2. `docs/by-program/`：每个 section 先写该场的技术趋势与评论，再放入该场全部论文总结。每篇论文都会出现在自己的 program 里。
3. `docs/by-topic/`：每个技术分类同样先写趋势与评论，再放入该分类下的全部论文总结。每篇论文至少进入一个技术分类。

程序里的 1417 条报告中，1375 条已对上 ISCA 全文；tutorial、部分 survey talk 和卫星活动没有会议论文 PDF，这些条目会按官方程序信息单独标注。

共 192 个 section，1417 条报告（含 tutorial、keynote、show & tell）。

## 按技术方向

这些文档把不同天的同类会场合在一起。

| 文档 | 内容 |
| --- | --- |
| [by-topic/01-ASR.md](by-topic/01-ASR.md) | 语音识别：鲁棒与高效、多语与低资源、多说话人、解码与检索、语音翻译 |
| [by-topic/02-TTS.md](by-topic/02-TTS.md) | 语音合成、声音转换、歌唱与音频生成 |
| [by-topic/03-全双工与口语对话.md](by-topic/03-全双工与口语对话.md) | 全双工、轮替、口语对话与口语理解 |
| [by-topic/04-语音与音频大模型.md](by-topic/04-语音与音频大模型.md) | 音频推理、语音大模型、自监督表示与基础模型后训练 |
| [by-topic/05-语音增强分离与编解码.md](by-topic/05-语音增强分离与编解码.md) | 增强、分离、目标说话人提取、神经编解码 |
| [by-topic/06-说话人与深度伪造.md](by-topic/06-说话人与深度伪造.md) | 说话人识别、日志、隐私匿名化、反欺骗与水印 |
| [by-topic/07-情感与副语言.md](by-topic/07-情感与副语言.md) | 语音情感、副语言、跨语言副语言 |
| [by-topic/08-医疗与临床语音.md](by-topic/08-医疗与临床语音.md) | 临床表征、病理语音、辅助技术、儿童与医疗对话 |
| [by-topic/09-语音学与感知产生.md](by-topic/09-语音学与感知产生.md) | 语音学、韵律、声调、发音、感知与脑机制 |
| [by-topic/10-多模态空间与声学事件.md](by-topic/10-多模态空间与声学事件.md) | 音视频、空间音频、声学事件检测 |
| [by-topic/11-多语社区数据与评测.md](by-topic/11-多语社区数据与评测.md) | 多语与社区语言、数据、评测、可信与可解释 |

## 按日期与 section

### Sunday 27 September 2026

- [Tutorials](by-program/2026-09-27-sunday/01-sun-001-tutorials.md) — 12:30 Tutorials，8 篇

### Monday 28 September 2026

- [Keynote: John H. L. Hansen](by-program/2026-09-28-monday/00-mon-keynote-john-hansen.md) — 09:30-10:30 Keynote，1 篇
- [Model of Speech Perception](by-program/2026-09-28-monday/01-mon-002-model-of-speech-perception.md) — 11:00-13:00 Oral, Area 1，6 篇
- [Speaker Verification: Advances in Speaker Embeddings](by-program/2026-09-28-monday/02-mon-003-speaker-verification-advances-in-speaker-embeddings.md) — 11:00-13:00 Oral, Area 4，6 篇
- [Spatial Audio 1](by-program/2026-09-28-monday/03-mon-004-spatial-audio-1.md) — 11:00-13:00 Oral, Area 5，6 篇
- [Scaling and Zero-Shot Speech Synthesis](by-program/2026-09-28-monday/04-mon-005-scaling-and-zero-shot-speech-synthesis.md) — 11:00-13:00 Oral, Area 7，6 篇
- [Multi-Talker ASR & Speaker Diarization](by-program/2026-09-28-monday/05-mon-006-multi-talker-asr-and-speaker-diarization.md) — 11:00-13:00 Oral, Area 8，6 篇
- [Search Methods and Inference Algorithms](by-program/2026-09-28-monday/06-mon-007-search-methods-and-inference-algorithms.md) — 11:00-13:00 Oral, Area 9，6 篇
- [Multimodal Spoken Dialogue Systems](by-program/2026-09-28-monday/07-mon-008-multimodal-spoken-dialogue-systems.md) — 11:00-13:00 Oral, Area 11，6 篇
- [Speech Representations and Alignment](by-program/2026-09-28-monday/08-mon-009-speech-representations-and-alignment.md) — 11:00-13:00 Long Oral，6 篇
- [Robust and Efficient ASR](by-program/2026-09-28-monday/09-mon-010-robust-and-efficient-asr.md) — 11:00-13:00 Long Oral，6 篇
- [Tools and Techniques for Phonetic Analysis](by-program/2026-09-28-monday/10-mon-011-tools-and-techniques-for-phonetic-analysis.md) — 11:00-13:00 Poster, Area 2，11 篇
- [Paralinguistics](by-program/2026-09-28-monday/11-mon-012-paralinguistics.md) — 11:00-13:00 Poster, Area 3，8 篇
- [Spoofing and Deepfake Detection 1](by-program/2026-09-28-monday/12-mon-013-spoofing-and-deepfake-detection-1.md) — 11:00-13:00 Poster, Area 4，10 篇
- [Evaluation of Speech and Audio Analysis](by-program/2026-09-28-monday/13-mon-014-evaluation-of-speech-and-audio-analysis.md) — 11:00-13:00 Poster, Area 5，14 篇
- [Generative and Self-Supervised Speech Enhancement](by-program/2026-09-28-monday/14-mon-015-generative-and-self-supervised-speech-enhancement.md) — 11:00-13:00 Poster, Area 6，12 篇
- [Long-Form Speech Synthesis](by-program/2026-09-28-monday/15-mon-016-long-form-speech-synthesis.md) — 11:00-13:00 Poster, Area 7，9 篇
- [Information Extraction and Retrieval](by-program/2026-09-28-monday/16-mon-017-information-extraction-and-retrieval.md) — 11:00-13:00 Poster, Area 12，7 篇
- [Clinically Useful Speech Representations 1](by-program/2026-09-28-monday/17-mon-018-clinically-useful-speech-representations-1.md) — 11:00-13:00 Poster, Area 13，8 篇
- [Audio Reasoning Challenge](by-program/2026-09-28-monday/18-mon-019-audio-reasoning-challenge.md) — 11:00-13:00 Challenge, Area 14，12 篇
- [Tones](by-program/2026-09-28-monday/19-mon-020-tones.md) — 14:30-16:30 Oral, Area 2，6 篇
- [Speech Emotion Recognition and Representation 1](by-program/2026-09-28-monday/20-mon-021-speech-emotion-recognition-and-representation-1.md) — 14:30-16:30 Oral, Area 3，5 篇
- [Speech Deepfake Detection: Robustness, Generalization, Attribution](by-program/2026-09-28-monday/21-mon-022-speech-deepfake-detection-robustness-generalization-attribution.md) — 14:30-16:30 Oral, Area 4，6 篇
- [Audio segmentation](by-program/2026-09-28-monday/22-mon-023-audio-segmentation.md) — 14:30-16:30 Oral, Area 5，6 篇
- [Neural Speech Enhancement: Survey, Diffusion and Flow Matching](by-program/2026-09-28-monday/23-mon-024-neural-speech-enhancement-survey-diffusion-and-flow-matching.md) — 14:30-16:30 Oral, Area 6，5 篇
- [Audio-Visual Grounding, Synchronization & Video Understanding](by-program/2026-09-28-monday/24-mon-025-audio-visual-grounding-synchronization-and-video-understanding.md) — 14:30-16:30 Oral, Area 10，6 篇
- [Spoken Language Processing: Evaluation and Metrics](by-program/2026-09-28-monday/25-mon-026-spoken-language-processing-evaluation-and-metrics.md) — 14:30-16:30 Oral, Area 12，6 篇
- [Assistive Technologies 1](by-program/2026-09-28-monday/26-mon-027-assistive-technologies-1.md) — 14:30-16:30 Oral, Area 13，6 篇
- [Text-to-Speech Synthesis](by-program/2026-09-28-monday/27-mon-028-text-to-speech-synthesis.md) — 14:30-16:30 Long Oral，6 篇
- [Brain Studies and Speech](by-program/2026-09-28-monday/28-mon-029-brain-studies-and-speech.md) — 14:30-16:30 Poster, Area 1，10 篇
- [Audio Understanding and Representation Learning](by-program/2026-09-28-monday/29-mon-030-audio-understanding-and-representation-learning.md) — 14:30-16:30 Poster, Area 5，11 篇
- [Neural Speech Codecs: Low-Bitrate and Disentangled Coding](by-program/2026-09-28-monday/30-mon-031-neural-speech-codecs-low-bitrate-and-disentangled-coding.md) — 14:30-16:30 Poster, Area 6，9 篇
- [From Self-Supervised Pre-training to Phonetic Analysis of Speech Models](by-program/2026-09-28-monday/31-mon-032-from-self-supervised-pre-training-to-phonetic-analysis-of-speech-model.md) — 14:30-16:30 Poster, Area 8，11 篇
- [Reasoning with Speech/Audio Language Models](by-program/2026-09-28-monday/32-mon-033-reasoning-with-speech-audio-language-models.md) — 14:30-16:30 Poster, Area 9，10 篇
- [Methods and data for vocal tract and articulation analysis](by-program/2026-09-28-monday/33-mon-034-methods-and-data-for-vocal-tract-and-articulation-analysis.md) — 14:30-16:30 Special Session, Area 14，9 篇
- [Grand Special Challenges Poster Showcase](by-program/2026-09-28-monday/34-mon-035-grand-special-challenges-poster-showcase.md) — 14:30-16:30 Poster, Area 14，13 篇
- [Speech Synthesis, Voice Conversion and Audio Generation](by-program/2026-09-28-monday/35-mon-036-speech-synthesis-voice-conversion-and-audio-generation.md) — 14:30-16:30 Show And Tell，8 篇

### Tuesday 29 September 2026

- [Voice Quality Aspects of Speech](by-program/2026-09-29-tuesday/01-tue-037-voice-quality-aspects-of-speech.md) — 09:00-11:00 Oral, Area 2，6 篇
- [Speaker Verification and Anti-Spoofing](by-program/2026-09-29-tuesday/02-tue-038-speaker-verification-and-anti-spoofing.md) — 09:00-11:00 Oral, Area 4，6 篇
- [Acoustic Event Detection 1](by-program/2026-09-29-tuesday/03-tue-039-acoustic-event-detection-1.md) — 09:00-11:00 Oral, Area 5，6 篇
- [Language-Model and Codec-Token Speech Enhancement](by-program/2026-09-29-tuesday/04-tue-040-language-model-and-codec-token-speech-enhancement.md) — 09:00-11:00 Oral, Area 6，6 篇
- [Controllable and Expressive Speech Synthesis](by-program/2026-09-29-tuesday/05-tue-041-controllable-and-expressive-speech-synthesis.md) — 09:00-11:00 Oral, Area 7，6 篇
- [Resource Constrained Speech Recognition](by-program/2026-09-29-tuesday/06-tue-042-resource-constrained-speech-recognition.md) — 09:00-11:00 Oral, Area 9，6 篇
- [Datasets](by-program/2026-09-29-tuesday/07-tue-043-datasets.md) — 09:00-11:00 Oral, Area 12，6 篇
- [Multimodal and Non-Speech Healthcare Applications](by-program/2026-09-29-tuesday/08-tue-044-multimodal-and-non-speech-healthcare-applications.md) — 09:00-11:00 Oral, Area 13，6 篇
- [Multilingual Speech 1](by-program/2026-09-29-tuesday/09-tue-045-multilingual-speech-1.md) — 09:00-11:00 Long - Oral，6 篇
- [Pronunciation Diversity](by-program/2026-09-29-tuesday/10-tue-046-pronunciation-diversity.md) — 09:00-11:00 Long Oral，5 篇
- [Speech Emotion Recognition and Representation 2](by-program/2026-09-29-tuesday/11-tue-047-speech-emotion-recognition-and-representation-2.md) — 09:00-11:00 Poster, Area 3，11 篇
- [Audio signal analysis](by-program/2026-09-29-tuesday/12-tue-048-audio-signal-analysis.md) — 09:00-11:00 Poster, Area 5，11 篇
- [Target Speaker Extraction, Speech Separation and Audio Understanding](by-program/2026-09-29-tuesday/13-tue-049-target-speaker-extraction-speech-separation-and-audio-understanding.md) — 09:00-11:00 Poster, Area 6，9 篇
- [Singing Voice and Music Generation](by-program/2026-09-29-tuesday/14-tue-050-singing-voice-and-music-generation.md) — 09:00-11:00 Poster, Area 7，9 篇
- [Multilingual, Cross-lingual & Low-Resource ASR](by-program/2026-09-29-tuesday/15-tue-051-multilingual-cross-lingual-and-low-resource-asr.md) — 09:00-11:00 Poster, Area 8，11 篇
- [Prosody, Pronunciation and Specialized Speech Processing](by-program/2026-09-29-tuesday/16-tue-052-prosody-pronunciation-and-specialized-speech-processing.md) — 09:00-11:00 Poster, Area 10，7 篇
- [Speech and Language Technologies in Healthcare](by-program/2026-09-29-tuesday/17-tue-053-speech-and-language-technologies-in-healthcare.md) — 09:00-11:00 Poster, Area 13，9 篇
- [Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean](by-program/2026-09-29-tuesday/18-tue-054-pacific-voices-speech-science-and-technology-for-the-languages-of-the-.md) — 09:00-11:00 Special Session, Area 14，10 篇
- [Prof Steven Bird](by-program/2026-09-29-tuesday/19-tue-055-prof-steven-bird.md) — 11:30-12:30 Keynote speaker，1 篇
- [Modeling L1 Acquisition](by-program/2026-09-29-tuesday/20-tue-056-modeling-l1-acquisition.md) — 14:00-16:00 Oral, Area 1，6 篇
- [Multilingual and Cross-Lingual Paralinguistic Analysis and Processing](by-program/2026-09-29-tuesday/21-tue-057-multilingual-and-cross-lingual-paralinguistic-analysis-and-processing.md) — 14:00-16:00 Oral, Area 3，6 篇
- [Language and Dialect Recognition](by-program/2026-09-29-tuesday/22-tue-058-language-and-dialect-recognition.md) — 14:00-16:00 Oral, Area 4，6 篇
- [Spatial Audio 2](by-program/2026-09-29-tuesday/23-tue-059-spatial-audio-2.md) — 14:00-16:00 Oral, Area 5，6 篇
- [Low-Resource Speech Synthesis](by-program/2026-09-29-tuesday/24-tue-060-low-resource-speech-synthesis.md) — 14:00-16:00 Oral, Area 7，5 篇
- [Speech Synthesis Evaluation 1](by-program/2026-09-29-tuesday/25-tue-061-speech-synthesis-evaluation-1.md) — 14:00-16:00 Oral, Area 7，6 篇
- [Audio Language Models](by-program/2026-09-29-tuesday/26-tue-062-audio-language-models.md) — 14:00-16:00 Oral, Area 8，5 篇
- [Clinically Useful Speech Representations 2](by-program/2026-09-29-tuesday/27-tue-063-clinically-useful-speech-representations-2.md) — 14:00-16:00 Oral, Area 13，5 篇
- [Audio Coding and Signal Analysis](by-program/2026-09-29-tuesday/28-tue-064-audio-coding-and-signal-analysis.md) — 14:00-16:00 Long Oral，6 篇
- [Perception and Appraisal of Prosody](by-program/2026-09-29-tuesday/29-tue-065-perception-and-appraisal-of-prosody.md) — 14:00-16:00 Poster, Area 2，7 篇
- [Spoofing and Deepfake Detection 2](by-program/2026-09-29-tuesday/30-tue-066-spoofing-and-deepfake-detection-2.md) — 14:00-16:00 Poster, Area 4，11 篇
- [Acoustic Event Detection 2](by-program/2026-09-29-tuesday/31-tue-067-acoustic-event-detection-2.md) — 14:00-16:00 Poster, Area 5，11 篇
- [Quality, Intelligibility and Evaluation of Speech and Codecs](by-program/2026-09-29-tuesday/32-tue-068-quality-intelligibility-and-evaluation-of-speech-and-codecs.md) — 14:00-16:00 Poster, Area 6，9 篇
- [Text Processing for Speech Synthesis](by-program/2026-09-29-tuesday/33-tue-069-text-processing-for-speech-synthesis.md) — 14:00-16:00 Poster, Area 7，10 篇
- [Cross-Lingual and Multilingual Speech Recognition 1](by-program/2026-09-29-tuesday/34-tue-070-cross-lingual-and-multilingual-speech-recognition-1.md) — 14:00-16:00 Poster, Area 9，9 篇
- [Pathological Speech Assessment 1](by-program/2026-09-29-tuesday/35-tue-071-pathological-speech-assessment-1.md) — 14:00-16:00 Poster, Area 13，8 篇
- [Safeguarding Synthetic Speech: Ethical, technical and legal perspectives](by-program/2026-09-29-tuesday/36-tue-072-safeguarding-synthetic-speech-ethical-technical-and-legal-perspectives.md) — 14:00-16:00 Special Session, Area 14，5 篇
- [Indigenous Voices in Speech Science and Technology](by-program/2026-09-29-tuesday/37-tue-073-indigenous-voices-in-speech-science-and-technology.md) — 14:00-16:00 Special Session, Area 14，7 篇
- [Speech and Language Learning Technologies](by-program/2026-09-29-tuesday/38-tue-074-speech-and-language-learning-technologies.md) — 14:00-16:00 Show And Tell，9 篇
- [Prominence, Stress and Focus](by-program/2026-09-29-tuesday/39-tue-075-prominence-stress-and-focus.md) — 16:30-18:30 Oral, Area 2，6 篇
- [Source Separation 1](by-program/2026-09-29-tuesday/40-tue-076-source-separation-1.md) — 16:30-18:30 Oral, Area 5，6 篇
- [Real-Time, Low-Latency and Edge Speech Enhancement](by-program/2026-09-29-tuesday/41-tue-077-real-time-low-latency-and-edge-speech-enhancement.md) — 16:30-18:30 Oral, Area 6，6 篇
- [Multilingual & Low-Resource ASR](by-program/2026-09-29-tuesday/42-tue-078-multilingual-and-low-resource-asr.md) — 16:30-18:30 Oral, Area 8，6 篇
- [Low-Resource & Endangered Language Speech Processing](by-program/2026-09-29-tuesday/43-tue-079-low-resource-and-endangered-language-speech-processing.md) — 16:30-18:30 Oral, Area 9，5 篇
- [Empathetic Dialogue and Interaction Dynamics](by-program/2026-09-29-tuesday/44-tue-080-empathetic-dialogue-and-interaction-dynamics.md) — 16:30-18:30 Oral, Area 11，5 篇
- [Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities](by-program/2026-09-29-tuesday/45-tue-081-audio-and-speech-language-models-evaluation-representations-and-emergi.md) — 16:30-18:30 Oral, Area 12，6 篇
- [Corpus Creation, Summerisation and Understanding](by-program/2026-09-29-tuesday/46-tue-082-corpus-creation-summerisation-and-understanding.md) — 16:30-18:30 Oral, Area 12，6 篇
- [Spoofing, Deepfake Detection and Watermarking](by-program/2026-09-29-tuesday/47-tue-083-spoofing-deepfake-detection-and-watermarking.md) — 16:30-18:30 Long Oral，6 篇
- [Audio-Visual and Multimodal Perception](by-program/2026-09-29-tuesday/48-tue-084-audio-visual-and-multimodal-perception.md) — 16:30-18:30 Long Oral，5 篇
- [Speech Production and Perception 1](by-program/2026-09-29-tuesday/49-tue-085-speech-production-and-perception-1.md) — 16:30-18:30 Poster, Area 1，10 篇
- [Cross-Linguistic and L2 Phonetic Studies](by-program/2026-09-29-tuesday/50-tue-086-cross-linguistic-and-l2-phonetic-studies.md) — 16:30-18:30 Poster, Area 2，8 篇
- [Spatial Audio 3](by-program/2026-09-29-tuesday/51-tue-087-spatial-audio-3.md) — 16:30-18:30 Poster, Area 5，10 篇
- [Instruction-following and Controllable Speech Synthesis](by-program/2026-09-29-tuesday/52-tue-088-instruction-following-and-controllable-speech-synthesis.md) — 16:30-18:30 Poster, Area 7，11 篇
- [Robust ASR: Uncertainty and Confidence](by-program/2026-09-29-tuesday/53-tue-089-robust-asr-uncertainty-and-confidence.md) — 16:30-18:30 Poster, Area 8，10 篇
- [Speech Technologies for Language Learning & Assessment](by-program/2026-09-29-tuesday/54-tue-090-speech-technologies-for-language-learning-and-assessment.md) — 16:30-18:30 Poster, Area 10，12 篇
- [Spoken Dialogue Systems](by-program/2026-09-29-tuesday/55-tue-091-spoken-dialogue-systems.md) — 16:30-18:30 Poster, Area 11，8 篇
- [Pathological Speech Assessment 2](by-program/2026-09-29-tuesday/56-tue-092-pathological-speech-assessment-2.md) — 16:30-18:30 Poster, Area 13，7 篇
- [Queer and Trans Speech Science and Technology](by-program/2026-09-29-tuesday/57-tue-093-queer-and-trans-speech-science-and-technology.md) — 16:30-18:30 Special Session, Area 14，8 篇

### Wednesday 30 September 2026

- [Multimodal Emotion Recognition](by-program/2026-09-30-wednesday/01-wed-094-multimodal-emotion-recognition.md) — 09:00-11:00 Oral, Area 3，6 篇
- [Speaker Verification: Architectures, Losses, and LLMs](by-program/2026-09-30-wednesday/02-wed-095-speaker-verification-architectures-losses-and-llms.md) — 09:00-11:00 Oral, Area 4，6 篇
- [Evaluation, Benchmarking, and Reliability of Audio Systems](by-program/2026-09-30-wednesday/03-wed-096-evaluation-benchmarking-and-reliability-of-audio-systems.md) — 09:00-11:00 Oral, Area 5，6 篇
- [Neural Audio Codec Architectures](by-program/2026-09-30-wednesday/04-wed-097-neural-audio-codec-architectures.md) — 09:00-11:00 Oral, Area 6，6 篇
- [Speech Synthesis: Speech Features, Codec and Representations](by-program/2026-09-30-wednesday/05-wed-098-speech-synthesis-speech-features-codec-and-representations.md) — 09:00-11:00 Oral, Area 7，6 篇
- [Self-supervised Speech Representation Learning](by-program/2026-09-30-wednesday/06-wed-099-self-supervised-speech-representation-learning.md) — 09:00-11:00 Oral, Area 8，6 篇
- [Entrainment and Dialogue Coordination](by-program/2026-09-30-wednesday/07-wed-100-entrainment-and-dialogue-coordination.md) — 09:00-11:00 Oral, Area 11，6 篇
- [Speech and Language Technologies for Health Applications 1](by-program/2026-09-30-wednesday/08-wed-101-speech-and-language-technologies-for-health-applications-1.md) — 09:00-11:00 Oral, Area 13，6 篇
- [Generative Audio and Music](by-program/2026-09-30-wednesday/09-wed-102-generative-audio-and-music.md) — 09:00-11:00 Long Oral，5 篇
- [Clinical and Inclusive Speech Technology](by-program/2026-09-30-wednesday/10-wed-103-clinical-and-inclusive-speech-technology.md) — 09:00-11:00 Long Oral，6 篇
- [Phonetic Aspects of TTS and ASR Systems](by-program/2026-09-30-wednesday/11-wed-104-phonetic-aspects-of-tts-and-asr-systems.md) — 09:00-11:00 Poster, Area 2，7 篇
- [Speaker Diarization 1](by-program/2026-09-30-wednesday/12-wed-105-speaker-diarization-1.md) — 09:00-11:00 Poster, Area 4，9 篇
- [Acoustic Event Detection 3](by-program/2026-09-30-wednesday/13-wed-106-acoustic-event-detection-3.md) — 09:00-11:00 Poster, Area 5，9 篇
- [Dereverberation, Bandwidth Extension and Restoration](by-program/2026-09-30-wednesday/14-wed-107-dereverberation-bandwidth-extension-and-restoration.md) — 09:00-11:00 Poster, Area 6，8 篇
- [Emotional Speech Synthesis](by-program/2026-09-30-wednesday/15-wed-108-emotional-speech-synthesis.md) — 09:00-11:00 Poster, Area 7，11 篇
- [Efficient Inference for ASR and Speech LMs](by-program/2026-09-30-wednesday/16-wed-109-efficient-inference-for-asr-and-speech-lms.md) — 09:00-11:00 Poster, Area 9，10 篇
- [Audio Language Models: Reasoning, Reliability, and Multimodal Understanding](by-program/2026-09-30-wednesday/17-wed-110-audio-language-models-reasoning-reliability-and-multimodal-understandi.md) — 09:00-11:00 Poster, Area 12，10 篇
- [Challenges in Speech Data Collection, Curation, and Annotation](by-program/2026-09-30-wednesday/18-wed-111-challenges-in-speech-data-collection-curation-and-annotation.md) — 09:00-11:00 Special Session, Area 14，14 篇
- [Speech and Language Processing for Health and Accessibility](by-program/2026-09-30-wednesday/19-wed-112-speech-and-language-processing-for-health-and-accessibility.md) — 09:00-11:00 Show And Tell，8 篇
- [Prof Jen Hay](by-program/2026-09-30-wednesday/20-wed-113-prof-jen-hay.md) — 11:30-12:30 Keynote speaker，1 篇
- [Lunchtime Panel](by-program/2026-09-30-wednesday/21-wed-114-lunchtime-panel.md) — 12:45-13:30 Session，1 篇
- [Neurophysiology of Speech](by-program/2026-09-30-wednesday/22-wed-115-neurophysiology-of-speech.md) — 14:00-16:00 Oral, Area 1，6 篇
- [Speaker Diarization 2](by-program/2026-09-30-wednesday/23-wed-116-speaker-diarization-2.md) — 14:00-16:00 Oral, Area 4，6 篇
- [Audio Foundation Models and Generation](by-program/2026-09-30-wednesday/24-wed-117-audio-foundation-models-and-generation.md) — 14:00-16:00 Oral, Area 5，6 篇
- [Voice Editing](by-program/2026-09-30-wednesday/25-wed-118-voice-editing.md) — 14:00-16:00 Oral, Area 7，6 篇
- [Domain Adaptation & Accented ASR](by-program/2026-09-30-wednesday/26-wed-119-domain-adaptation-and-accented-asr.md) — 14:00-16:00 Oral, Area 8，6 篇
- [Multi-Speaker Processing, Personalization, and Adaptation](by-program/2026-09-30-wednesday/27-wed-120-multi-speaker-processing-personalization-and-adaptation.md) — 14:00-16:00 Oral, Area 9，6 篇
- [Robust and Real-World ASR Systems](by-program/2026-09-30-wednesday/28-wed-121-robust-and-real-world-asr-systems.md) — 14:00-16:00 Oral, Area 10，6 篇
- [Speech, Voice and Language Disorders](by-program/2026-09-30-wednesday/29-wed-122-speech-voice-and-language-disorders.md) — 14:00-16:00 Oral, Area 13，6 篇
- [Speech and Language Technologies for Health Applications 2](by-program/2026-09-30-wednesday/30-wed-123-speech-and-language-technologies-for-health-applications-2.md) — 14:00-16:00 Oral, Area 13，6 篇
- [Speech Enhancement and Restoration](by-program/2026-09-30-wednesday/31-wed-124-speech-enhancement-and-restoration.md) — 14:00-16:00 Long Oral，6 篇
- [Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech](by-program/2026-09-30-wednesday/32-wed-125-speaker-specific-forensic-and-segmental-characteristics-of-typical-and.md) — 14:00-16:00 Poster, Area 2，8 篇
- [Behavioral, Cross-lingual, and Multimodal Speech Analysis](by-program/2026-09-30-wednesday/33-wed-126-behavioral-cross-lingual-and-multimodal-speech-analysis.md) — 14:00-16:00 Poster, Area 3，11 篇
- [Speaker Privacy Preservation and Anonymization](by-program/2026-09-30-wednesday/34-wed-127-speaker-privacy-preservation-and-anonymization.md) — 14:00-16:00 Poster, Area 4，12 篇
- [Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment](by-program/2026-09-30-wednesday/35-wed-128-active-noise-and-echo-control-sound-zones-and-packet-loss-concealment.md) — 14:00-16:00 Poster, Area 6，10 篇
- [Streaming Speech Synthesis](by-program/2026-09-30-wednesday/36-wed-129-streaming-speech-synthesis.md) — 14:00-16:00 Poster, Area 7，9 篇
- [Multilingual Speech 2](by-program/2026-09-30-wednesday/37-wed-130-multilingual-speech-2.md) — 14:00-16:00 Poster, Area 12，13 篇
- [Assistive Technologies 2](by-program/2026-09-30-wednesday/38-wed-131-assistive-technologies-2.md) — 14:00-16:00 Poster, Area 13，10 篇
- [Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments](by-program/2026-09-30-wednesday/39-wed-132-speech-science-and-computational-modeling-to-study-children-and-their-.md) — 14:00-16:00 Special Session, Area 14，13 篇
- [Diphthongs and Monophthongs](by-program/2026-09-30-wednesday/40-wed-133-diphthongs-and-monophthongs.md) — 16:30-18:30 Oral, Area 2，5 篇
- [Speaker Identity, States, and Traits in Paralinguistics](by-program/2026-09-30-wednesday/41-wed-134-speaker-identity-states-and-traits-in-paralinguistics.md) — 16:30-18:30 Oral, Area 3，6 篇
- [Speech Deepfake Detection, Attribution and Characterization](by-program/2026-09-30-wednesday/42-wed-135-speech-deepfake-detection-attribution-and-characterization.md) — 16:30-18:30 Oral, Area 4，6 篇
- [Speech and Audio Quality Assessment](by-program/2026-09-30-wednesday/43-wed-136-speech-and-audio-quality-assessment.md) — 16:30-18:30 Oral, Area 5，6 篇
- [Audio-Visual and Generative Target Speaker Extraction](by-program/2026-09-30-wednesday/44-wed-137-audio-visual-and-generative-target-speaker-extraction.md) — 16:30-18:30 Oral, Area 6，6 篇
- [Speech Synthesis Evaluation 2](by-program/2026-09-30-wednesday/45-wed-138-speech-synthesis-evaluation-2.md) — 16:30-18:30 Oral, Area 7，6 篇
- [Translation](by-program/2026-09-30-wednesday/46-wed-139-translation.md) — 16:30-18:30 Oral, Area 12，6 篇
- [Child Speech and Health](by-program/2026-09-30-wednesday/47-wed-140-child-speech-and-health.md) — 16:30-18:30 Oral, Area 13，6 篇
- [Medical Dialogue and Conversational Understanding](by-program/2026-09-30-wednesday/48-wed-141-medical-dialogue-and-conversational-understanding.md) — 16:30-18:30 Oral, Area 13，6 篇
- [LLMs and Conversational Interaction](by-program/2026-09-30-wednesday/49-wed-142-llms-and-conversational-interaction.md) — 16:30-18:30 Long Oral，6 篇
- [Speech and Language Representation](by-program/2026-09-30-wednesday/50-wed-143-speech-and-language-representation.md) — 16:30-18:30 Poster, Area 4，9 篇
- [Acoustic Signal Analysis and Generation](by-program/2026-09-30-wednesday/51-wed-144-acoustic-signal-analysis-and-generation.md) — 16:30-18:30 Poster, Area 5，7 篇
- [Articulatory, EMG, and Visual Speech Generation](by-program/2026-09-30-wednesday/52-wed-145-articulatory-emg-and-visual-speech-generation.md) — 16:30-18:30 Poster, Area 7，10 篇
- [Robust ASR: Hallucinations and Biases](by-program/2026-09-30-wednesday/53-wed-146-robust-asr-hallucinations-and-biases.md) — 16:30-18:30 Poster, Area 8，9 篇
- [New Architecture and Analyses for ASR and Speech LMs](by-program/2026-09-30-wednesday/54-wed-147-new-architecture-and-analyses-for-asr-and-speech-lms.md) — 16:30-18:30 Poster, Area 9，6 篇
- [Spoken Language Understanding](by-program/2026-09-30-wednesday/55-wed-148-spoken-language-understanding.md) — 16:30-18:30 Poster, Area 11，12 篇
- [Pathological Speech Assessment 3](by-program/2026-09-30-wednesday/56-wed-149-pathological-speech-assessment-3.md) — 16:30-18:30 Poster, Area 13，8 篇
- [Explainability for Compliance and Trust in Speech AI](by-program/2026-09-30-wednesday/57-wed-150-explainability-for-compliance-and-trust-in-speech-ai.md) — 16:30-18:30 Special Session, Area 14，16 篇
- [Speech Analysis, Data Resources and Research Tools](by-program/2026-09-30-wednesday/58-wed-151-speech-analysis-data-resources-and-research-tools.md) — 16:30-18:30 Show And Tell，6 篇

### Thursday 1 October 2026

- [Modeling Articulation](by-program/2026-10-01-thursday/01-thu-152-modeling-articulation.md) — 09:00-11:00 Oral, Area 1，5 篇
- [Speaker Privacy and Anonymization](by-program/2026-10-01-thursday/02-thu-153-speaker-privacy-and-anonymization.md) — 09:00-11:00 Oral, Area 4，6 篇
- [Speech signal analysis](by-program/2026-10-01-thursday/03-thu-154-speech-signal-analysis.md) — 09:00-11:00 Oral, Area 5，5 篇
- [LLM Based Speech Synthesis](by-program/2026-10-01-thursday/04-thu-155-llm-based-speech-synthesis.md) — 09:00-11:00 Oral, Area 7，6 篇
- [New Training Methods for ASR](by-program/2026-10-01-thursday/05-thu-156-new-training-methods-for-asr.md) — 09:00-11:00 Oral, Area 8，6 篇
- [Code-Switching ASR](by-program/2026-10-01-thursday/06-thu-157-code-switching-asr.md) — 09:00-11:00 Oral, Area 9，6 篇
- [Information Extraction and Retrieval / Survey Talk](by-program/2026-10-01-thursday/07-thu-158-information-extraction-and-retrieval-survey-talk.md) — 09:00-11:00 Oral, Area 12，5 篇
- [Beyond Speech Technologies in Healthcare](by-program/2026-10-01-thursday/08-thu-159-beyond-speech-technologies-in-healthcare.md) — 09:00-11:00 Oral, Area 13，6 篇
- [Speaker Diarization and Recognition](by-program/2026-10-01-thursday/09-thu-160-speaker-diarization-and-recognition.md) — 09:00-11:00 Long Oral，5 篇
- [Emotion, Prosody, and Articulation](by-program/2026-10-01-thursday/10-thu-161-emotion-prosody-and-articulation.md) — 09:00-11:00 Long Oral，5 篇
- [Speaker Recognition and Verification](by-program/2026-10-01-thursday/11-thu-162-speaker-recognition-and-verification.md) — 09:00-11:00 Poster, Area 4，12 篇
- [Spatial Audio 4](by-program/2026-10-01-thursday/12-thu-163-spatial-audio-4.md) — 09:00-11:00 Poster, Area 5，11 篇
- [Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)](by-program/2026-10-01-thursday/13-thu-164-multi-channel-processing-and-specialized-acquisition-uav-radar-hearabl.md) — 09:00-11:00 Poster, Area 6，9 篇
- [Speech Synthesis Evaluation and Benchmarking](by-program/2026-10-01-thursday/14-thu-165-speech-synthesis-evaluation-and-benchmarking.md) — 09:00-11:00 Poster, Area 7，12 篇
- [ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency](by-program/2026-10-01-thursday/15-thu-166-asr-under-real-world-constraints-streaming-adaptation-and-efficiency.md) — 09:00-11:00 Poster, Area 8，10 篇
- [Multimodal Speech Processing and Speech LLM Systems](by-program/2026-10-01-thursday/16-thu-167-multimodal-speech-processing-and-speech-llm-systems.md) — 09:00-11:00 Poster, Area 10，7 篇
- [Speech Benchmarks, Evaluation, and Resources](by-program/2026-10-01-thursday/17-thu-168-speech-benchmarks-evaluation-and-resources.md) — 09:00-11:00 Poster, Area 12，8 篇
- [Post-Training of Speech Foundation Models](by-program/2026-10-01-thursday/18-thu-169-post-training-of-speech-foundation-models.md) — 09:00-11:00 Special Session, Area 14，13 篇
- [Speech Recognition, Enhancement and Real-Time Systems](by-program/2026-10-01-thursday/19-thu-170-speech-recognition-enhancement-and-real-time-systems.md) — 09:00-11:00 Show And Tell，4 篇
- [Prof Junichi Yamagishi](by-program/2026-10-01-thursday/20-thu-171-prof-junichi-yamagishi.md) — 11:30-12:30 Keynote speaker，1 篇
- [Gender- and Age-Related Speech Characteristics](by-program/2026-10-01-thursday/21-thu-172-gender-and-age-related-speech-characteristics.md) — 14:00-16:00 Oral, Area 2，6 篇
- [Audio Watermarking and Source Verification](by-program/2026-10-01-thursday/22-thu-173-audio-watermarking-and-source-verification.md) — 14:00-16:00 Oral, Area 4，6 篇
- [Acoustic Event Detection 4](by-program/2026-10-01-thursday/23-thu-174-acoustic-event-detection-4.md) — 14:00-16:00 Oral, Area 5，6 篇
- [Multi-Channel, Beamforming and Spatial Speech Enhancement](by-program/2026-10-01-thursday/24-thu-175-multi-channel-beamforming-and-spatial-speech-enhancement.md) — 14:00-16:00 Oral, Area 6，6 篇
- [Flow Matching for Speech Synthesis](by-program/2026-10-01-thursday/25-thu-176-flow-matching-for-speech-synthesis.md) — 14:00-16:00 Oral, Area 7，6 篇
- [Long-form Audio & New Attention Approaches](by-program/2026-10-01-thursday/26-thu-177-long-form-audio-and-new-attention-approaches.md) — 14:00-16:00 Oral, Area 8，6 篇
- [Robust Audio-Visual Speech Recognition](by-program/2026-10-01-thursday/27-thu-178-robust-audio-visual-speech-recognition.md) — 14:00-16:00 Oral, Area 10，5 篇
- [Turn-taking](by-program/2026-10-01-thursday/28-thu-179-turn-taking.md) — 14:00-16:00 Oral, Area 11，6 篇
- [Pathological Speech Assessment 4](by-program/2026-10-01-thursday/29-thu-180-pathological-speech-assessment-4.md) — 14:00-16:00 Oral, Area 13，6 篇
- [Benchmarking Foundation Models](by-program/2026-10-01-thursday/30-thu-181-benchmarking-foundation-models.md) — 14:00-16:00 Long Oral，6 篇
- [Speech Production and Perception 2](by-program/2026-10-01-thursday/31-thu-182-speech-production-and-perception-2.md) — 14:00-16:00 Poster, Area 1，9 篇
- [Speech Emotion Recognition and Representation 3](by-program/2026-10-01-thursday/32-thu-183-speech-emotion-recognition-and-representation-3.md) — 14:00-16:00 Poster, Area 3，9 篇
- [Spoofing and Deepfake Detection 3](by-program/2026-10-01-thursday/33-thu-184-spoofing-and-deepfake-detection-3.md) — 14:00-16:00 Poster, Area 4，10 篇
- [Source Separation 2](by-program/2026-10-01-thursday/34-thu-185-source-separation-2.md) — 14:00-16:00 Poster, Area 5，8 篇
- [SE Architectures, Adaptation and Audio Front-Ends](by-program/2026-10-01-thursday/35-thu-186-se-architectures-adaptation-and-audio-front-ends.md) — 14:00-16:00 Poster, Area 6，10 篇
- [Voice Conversion](by-program/2026-10-01-thursday/36-thu-187-voice-conversion.md) — 14:00-16:00 Poster, Area 7，9 篇
- [Cross-Lingual and Multilingual Speech Recognition 2](by-program/2026-10-01-thursday/37-thu-188-cross-lingual-and-multilingual-speech-recognition-2.md) — 14:00-16:00 Poster, Area 9，10 篇
- [TidyVoice2026 Challenge: Cross-Lingual Speaker Verification](by-program/2026-10-01-thursday/38-thu-189-tidyvoice2026-challenge-cross-lingual-speaker-verification.md) — 14:00-16:00 Challenge, Area 14，8 篇

### Friday 2 October 2026

- [Satellite Events](by-program/2026-10-02-friday/01-fri-190-satellite-events.md) —  Satellite Events，2 篇

### Saturday 26 September 2026

- [Satellite Events](by-program/2026-09-26-saturday/01-sat-191-satellite-events.md) — 10:00 - 12:30 Satellite Events，4 篇
