# TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset and Preliminary Results with Scalable Data Mining In-the-Wild

- 论文编号：1511
- 报告人：Kai-Wei Chang
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26d_interspeech.pdf

## 问题
台湾闽南语（Taiwanese Hokkien）在老年群体中使用比例高，却缺乏面向照护/家庭助手的真实口语意图数据；低资源、书写不统一也使标注训练数据难扩。

## 方法
发布 TaigiSpeech：21 名老年说话人（54–78 岁，男 8 / 女 13），8 类意图（SOS CALL、BREATH EMERG、FALL HELP、PAIN GENERAL；CALL CONTACT、LIGHT ON/OFF、CANCEL），共 3,079 句、约 6.1 小时。用场景想象提示（Gemini）与可选无声视频（Veo）诱发自发表达，非朗读脚本。另探索两类野生数据挖掘：经中间语（普通话字幕）的关键词匹配 + LLM 伪标，以及少文本监督的音视频多模态挖掘。计划 CC BY 4.0 公开；基线含轻量网络、SSL 语音模型，以及 Whisper/Qwen3-ASR 级联 LLM。

## 实验与结果
摘要与引言报告：在野生挖掘数据上训练的模型迁移到真实老年录音时性能显著下降，存在明显域失配，凸显真实基准必要性。各意图约 384–387 句，平均时长约 7.15 s。全文抽取在数据采集段中途截断，详细基线数字表未完整可读。

## 结论
作者将 TaigiSpeech 定位为低资源、面向老年应急与家居助手的首个台湾闽南语口语意图基准，并强调野生挖掘可扩规模但无法替代真实老年评测。

## 点评
场景设计贴合跌倒/呼吸困难等老年刚需，数据采集流程（多设备 UI、家乡口音元数据）务实。正文抽取严重截断，实验数字与消融只能依赖摘要级描述；点评中域失配结论可信，但具体准确率/F1 无法从当前全文文本核实。
