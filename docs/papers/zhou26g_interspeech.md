# AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization

- 论文编号：2177
- 报告人：Yuxuan Jiang
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26g_interspeech.pdf

## 问题
音视频特征评测常把语义匹配（检索）与时间偏移检测混为一谈或偏重其一，数据构造也耦合，难以独立诊断时间一致性与语义一致性。

## 方法
提出 AV-SyncBench：从野外视频筛选声源在画面内的片段（Gemini 初筛 + 人工复核），得 3,269 视频、38,390 样本，覆盖 Voice/Music/Sound、10 场景。解耦两类挑战——时间：全局偏移（50–500 ms）、局部抖动、全局变速（0.8×–1.25×），语义不变；语义：OpenVoice/DDSP 改音色/乐器但保持节奏时序。切 0.64 s chunk，用对角余弦相似（或零偏移概率）做成对比较，报告二分类准确率。评测 Synchformer、SparseSync、ImageBind、CAV-MAE、CAV-MAE-Sync。

## 实验与结果
大扰动更易检出；全局偏移上 Synchformer/SparseSync 较强，CAV-MAE 近随机。局部抖动与变速上模型表现分化。语义音色任务：ImageBind 整体最高（约 0.859），SparseSync 近随机，CAV-MAE 系在乐器上更强。类别上单源清晰场景优于多源复杂场景。结论显示时间与语义能力明显解耦、训练目标偏科。

## 结论
作者认为解耦基准可诊断特征提取器的时间/语义短板，并呼吁未来模型同时建模细粒度时间结构与语义对齐。

## 点评
贡献是评测协议与变量隔离的数据构造，而非新对齐模型。生成式音色编辑可能引入非纯语义伪迹（作者已写局限）；片段偏短（≤13 s）、物体声可控替换仍弱。对下游同步生成/筛选数据仍有直接工具价值。
