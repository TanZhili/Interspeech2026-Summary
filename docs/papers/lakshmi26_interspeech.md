# The First Dravidian Speech Datasets for Transphobic and Homophobic Hate Speech: Creation, Annotation, and Multimodal Benchmarking

- 论文编号：2368
- 报告人：Jesin James
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lakshmi26_interspeech.pdf

## 问题
泰卢固语与马拉雅拉姆语等达罗毗荼低资源语言中，针对 LGBTQIA+ 的仇恨检测几乎全是文本；缺少可捕捉语气、音高、韵律等副语言线索的标注语音数据。

## 方法
构建两类语料：Elicited Speech（母语者朗读社交媒体上整理的恐同/恐跨/中性句，16 kHz/16-bit）与 Social Media Audio Extract（YouTube/Instagram 公开片段人工裁剪标注）。三名母语者标注 {Homophobia, Transphobia, None}，Cohen’s κ 约 0.78（Telugu）/0.77（Malayalam）。基线：语言专用 Wav2Vec 2.0 均值池化声学嵌入 + Whisper 转写后 IndicBERTv2 [CLS] 文本嵌入，线性投到 768-D，注意力加权融合后经双分支多尺度分类器做三分类；并与 speech-only、text-only 对比。

## 实验与结果
Elicited：Telugu 630、Malayalam 269；Social：Telugu 73、Malayalam 100。同域（Config 1）多模态 F1：Malayalam 0.9566、Telugu 0.8652；跨域测社交音频（Config 2）降至 0.4721 / 0.5907；混合（Config 3）部分回升。同域多模态优于单模态（如 Malayalam 相对 speech-only +8.7%、text-only +15.2%）；跨域时 text-only 更稳，多模态甚至低于文本（Malayalam 文本相对多模态约 +50.4%），显示声学对噪声/俚语/ASR 误差更敏感。

## 结论
首次提供 Telugu/Malayalam 恐同恐跨语音数据集并给出多模态基线：同域强、跨域弱。局限含说话人偏少且偏男性、社交样本平台偏倚与噪声；需域适应与更鲁棒融合。

## 点评
把“副语言对仇恨识别有用”和“读稿到真实音频会崩”同时用同域/跨域拆开，对部署很诚实。社交集规模小，跨域数字波动大；仇恨内容敏感，公开释放需严格治理。
