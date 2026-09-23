# MultiLinguahah : A New Unsupervised Multilingual Acoustic Laughter Segmentation Method

- 论文编号：2352
- 报告人：Sofia Callejas
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/callejas26_interspeech.pdf

## 问题
笑声分割通常依赖昂贵人工标注且数据偏英语；监督 SOTA 在多语、野外声学条件下不稳定。

## 方法
MultiLinguahah（无监督）：声源分离或双声道相减去语音 → 能量阈值切事件 → BYOL-A 编码（可在目标无标训练集上继续自监督）→ Isolation Forest 把笑声当异常。评测 StandUp4AI（多语新标）、AudioSet（人工插入笑声）、Friends、Kuznetsova；IoU@0.3/0.7 的 Recall/F1；对比 Gillick、Omine、Liu 及与 Omine 融合。

## 实验与结果
美式脱口秀上 Omine 仍更强（IoU0.3 F1 0.679 vs 0.506）；Friends TV 上本文 0.910/0.735 超 Liu 0.878/0.503；法语/西语等非英语脱口秀上 MultiLinguahah 或 Omine+本文组合常优于纯监督基线。短笑声上相对 Omine 优势更明显。

## 结论
无监督异常检测在多语与多域笑声分割上更稳健；英语室内监督模型不跨语。可与监督模型互补。

## 点评
把笑声的跨语声学共性当成“可隔离异常”，避开标注瓶颈。强处是多语新标注与域覆盖；脆弱处是能量阈值敏感、依赖分离质量，英语脱口秀上仍落后强监督。
