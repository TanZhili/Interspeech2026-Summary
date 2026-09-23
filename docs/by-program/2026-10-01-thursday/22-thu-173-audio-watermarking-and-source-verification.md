# Audio Watermarking and Source Verification

- 日期：2026年10月1日（星期四）
- 时间：14:00-16:00
- 形式：Oral
- Area：4
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场围绕生成式语音时代的可追溯性：对抗神经编解码失真的水印恢复、在信息层（音节时长）而非波形层嵌入、利用流匹配初始噪声空间相关的免训练水印、大规模扰动基准、抗纯化主动防御，以及开集溯源中成对验证目标的隐藏代价。主线是信号级水印在编解码/声码器/纯化攻击下脆弱，需编解码感知恢复、生成过程内嵌或语义耦合。

方法谱从提取前自适应谱恢复，到合成时控时长、噪声—输出余弦相关，再到音素感知 Mamba 主动嵌入。评测侧 VoxWatermark 统一多注入法与多盒扰动；溯源侧则警示成对度量学习可能压缩嵌入方向分辨率，全局锚定在同等预算下更优。

## 技术内容

### 编解码鲁棒、信息层与免训练水印

**Countering Neural Audio Codec Distortions in Watermarking with Adaptive Restoration**（论文 953；Sungho Park）  
ConvNeXt U-Net 在提取前重建编解码失真谱，轻量分类器为各编解码动态选专用恢复模型。RVQ 类编解码上比特准确率从近随机提至 >98%，并分析量化器配置对水印存活性的影响。

**DuraMark: Duration-Embedded Watermarking in LLM-based TTS**（论文 2298；Zhenwei Mou）  
信息级框架：时长可控 LLM-TTS 在合成时编辑音节时长，时长提取器检测。相对信号级基线对神经编解码/声码器等生成攻击显著更鲁棒。

**AudioNoisePrints: Model-free audio watermarking using spatial correlation in flow matching TTS**（论文 2165；Timothy Tin-Long Tse）  
利用流匹配/扩散初始高斯噪声与生成输出的强空间相关，余弦相关即可水印，几乎不增推理开销、无需重训或降质；轻量检测器应对强增强。强增强下优于 AudioSeal；F5TTS 等模型与声码器均呈类似相关。

### 基准、主动防御与溯源目标

**VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations**（论文 1771；Farnaz Sedaghati）  
10 种水印（4 神经 + 6 传统）统一注入标注多语多源语料，含无盒/黑盒/白盒扰动；提出 AudioWMD 作大规模多方法跨分布检测基线，显示注入多样性与分布偏移影响稳定性。

**Phoneme-Aware Mamba Watermark: An Active Defense System Against Purified Speech Deepfakes**（论文 2105；Yanda Shao）  
双列双向状态空间模型嵌入身份比特串；音素引导嵌入与语义紧耦合以抗 PhonePuRe 等扩散纯化，说话人适应时水印迁移到伪造语音。约 1 s 超低时延溯源，强纯化下高真阳性率。

**The Hidden Cost of Pairwise Verification in Synthetic Speech Source Tracing**（论文 120；Anton Firc）  
同等骨干与数据/轮次预算下，全局锚定 MLAAD 域内 EER 8.61%，成对变体 12–15%。成对目标直接优化相似度会把方差集中到更少嵌入方向、降低近缘生成器分辨；人为瓶颈全局基线仍有竞争力，差距非仅维度所致。

## 本场要点

- 神经编解码需自适应谱恢复才能保住水印比特准确率。
- 音节时长等前信号信息层嵌入更抗生成攻击；流匹配噪声相关支持免训练水印。
- 统一扰动基准与多方法检测是开放环境溯源的基础设施。
- 音素耦合主动水印抗纯化；开集溯源宜谨慎采用成对验证目标。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 953 | Countering Neural Audio Codec Distortions in Watermarking with Adaptive Restoration |
| 2298 | DuraMark: Duration-Embedded Watermarking in LLM-based TTS |
| 2165 | AudioNoisePrints: Model-free audio watermarking using spatial correlation in flow matching TTS |
| 1771 | VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations |
| 2105 | Phoneme-Aware Mamba Watermark: An Active Defense System Against Purified Speech Deepfakes |
| 120 | The Hidden Cost of Pairwise Verification in Synthetic Speech Source Tracing |
