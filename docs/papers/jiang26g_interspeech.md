# Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems

- 论文编号：3114
- 报告人：Jingjing Jiang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26g_interspeech.pdf

## 问题
全双工口语对话（如 Moshi）已支持低延迟重叠说话，但仍缺面部表情与头动；既有带脸系统多为轮替架构，无法同时处理/生成语音与面部。

## 方法
Moshi-Face：VQ-VAE face codec 把 VHAP 提取的 3D 头网格编成与音频同帧率（12.5 Hz）的离散 face tokens；Face Transformer 非自回归生成 N=8 face tokens，条件于 RQ-Transformer 隐状态与文本/音频嵌入。在 Seamless Interaction 约 180h 对话上两阶段训练（先冻 RQ 训 Face Transformer，再联合微调）。

## 实验与结果
Codec（K=256,C=128）重建较好。教师强制下 LSE-D/C 接近重建上界；自由双模型对话仍可流式。Moshi-Face free-run：UTMOS 1.75，LLM-as-Judge 总体约 3.76，与 Moshi/Moshi-ft 对话质量同量级；消融显示 Face Transformer 预训练与联合微调、以及 t−1 face 条件对同步与质量重要。

## 结论
首次把面部 token 生成接入全双工对话，实现低延迟音画对齐且不明显牺牲原音频对话质量。

## 点评
把脸做成与 Mimi 音频同构的离散流，是全双工多模态的自然扩展。自由运行下 LSE 与 UTMOS 仍有差距；依赖单目 3D 重建质量，真实摄像头噪声与遮挡未充分覆盖。
