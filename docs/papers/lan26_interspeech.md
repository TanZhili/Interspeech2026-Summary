# SA-UAED: Joint Frame-Level Detection of Audio Events, Speaker Activities, and Speaker-Attributed Paralinguistic Events

- 论文编号：2486
- 报告人：Zekun Lan
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lan26_interspeech.pdf

## 问题
SED/SD 难以把笑、咳等副语言事件归因到具体说话人；细粒度标注稀缺，且通用说话人嵌入对短暂非言语突发表征不佳。T-UAED 联合 SED 与 diarization 但仍忽略副语言。

## 方法
仿真管线：脚本生成时间线 → ChatterBox-Turbo 用 LibriSpeech 参考合成说话人特异笑/咳 → PANNs 过滤 + VAD 裁剪 → 与 LibriSpeech 语音、DESED 背景按 15% 重叠混合，得 500 h LibriPara（帧级标签，50 Hz）。SA-UAED 在 T-UAED 上为笑/咳各加专用 FC，把 ECAPA-TDNN 嵌入投到独立副语言查询子空间，与事件查询并行进 Transformer 解码器。

## 实验与结果
LibriPara 测试：基线笑/咳 SB-F1 仅 0.371/0.282；SA-UAED 升至 0.476/0.473，DER≈8.07 几乎不变；共享适配器反而更差。EARS 真人素材零样本混合：笑 SB-F1 0.259→0.409，咳 0.375→0.470。通用 SED 略降（如 SB-F1 0.984→0.979）。

## 结论
专用副语言子空间 + 可控仿真数据可大幅提升说话人归因副语言检测，同时基本保持 SED/SD。未来拟做自监督对齐与开放集发声。

## 点评
抓住“言语偏置嵌入压不住笑/咳身份”这一声学失配，用解耦查询而非硬塞共享投影。仿真依赖 TTS 副语言保真；EARS 评测仍按同一混合协议，真实重叠现场泛化需再验。
