# Singing Voice and Music Generation

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：7
- 论文数：9
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场聚焦歌声编辑/合成/转换、歌曲统一生成，以及面向中文传统音乐与戏曲的数据与基线建设，并并行关注唱假检测与感知驱动重建。方法上，flow matching / rectified flow / 扩散与多模态 DiT 成为主流生成骨架；控制目标从音色克隆扩展到旋律保持、时长预算、歌词改写、伴奏协同与风格一致美化。无手动对齐的旋律引导与固定预算时长分配，是歌词编辑类任务的共同难点。

数据与评测侧，SingFox 覆盖多语与多轨假唱检测，CTMusic、YOAT/粤剧基准与 LyricEditBench 分别补齐中国传统器乐文生乐、粤剧 SVS 与旋律保持歌词编辑评测。另有工作用感知加权、相位相关与谱监督改进音乐 VAE 重建，以支撑后续大规模生成。整体趋势是：可控歌声生成与统一多任务框架并行推进，同时用领域数据集与假唱评测补齐安全与文化多样性缺口。

## 技术内容

### 可控歌声编辑、美化与转换

**MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling**（论文 3285；Yoonjeong Park）基于 flow matching 做旋律感知、时长保持的文本歌声编辑；核心模块 MeloDRP 预测固定预算时长比，经交叉注意力融合语音线索与伪 MIDI 旋律上下文，并用 flow-matching mel 解码器做音频填补。另提出基于 WhisperX 与 LLM 的时长感知编辑歌词生成管线，客观/主观评测报告达到当时最优。

**YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance**（论文 1547；Chunbo Hao）全扩散模型以可选音色参考、提供旋律的歌声片段与改写歌词为输入，无需手动对齐；结合课程学习与 Group Relative Policy Optimization，摘要称旋律保持与歌词遵循优于 Vevo2，并发布 LyricEditBench。

**SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow**（论文 615；Wenhui Li）用 rectified flow 做风格一致歌声美化，覆盖音高与节奏校正，并以上下文引导的掩码 mel 修复保留业余歌手音色与表达模式；在英/中测试集多数客观与主观指标上优于基线。

**Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching**（论文 2090；Hao Huang）提出 MinFlow-SVC：KNN 将源歌手特征映射到共享歌手空间以去除源音色，再用最小池化对抗训练纠偏 KNN 不一致并增强谐波感知的条件 flow matching；摘要报告在自然度、可懂度、音色相似与歌唱稳定性上优于既有 SOTA SVC。

### 统一歌曲生成、领域数据与戏曲基准

**Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation**（论文 481；Ziyu Zhang）提出 UniSinger，在多模态扩散 Transformer 上统一零样本说话人克隆歌曲生成与伴奏协同 SVC，构建统一说话人嵌入空间，并用任务特定模态掩码课程学习缓解多任务冲突。

**CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation**（论文 882；Haotian Guo）发布含 741 对文本—音乐标注、逾 42 小时音频的传统中国器乐数据集，覆盖独奏与合奏；并在其上微调 Stable Audio Open，提供更贴合中国传统音乐特性的改进模型。

**Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model**（论文 131；Peng Bai）面向吴语粤剧建立 SVS 基准：YOAT 含 565 条工作室录音及音素级时长/音高对齐，辅以发音与音高视角数据增强，并给出条件 flow-matching 基线 YueOpera-Singer；摘要报告主观 MOS 为 3.92。

### 假唱检测与感知驱动音乐重建

**SingFox: A Multi-Lingual Singfake Detection Corpus**（论文 2573；Arth J. Shah）构建含六轨（T1–T6）的大型多语假唱检测与溯源语料，摘要称超过 113,802 条片段、20 种语言、逾 126.32 小时、1150 类歌手；跨数据集测试最高准确率报告为 77.84%。

**Back to Ear: Perceptually Driven High Fidelity Music Reconstruction**（论文 219；Kangdi Wang）提出 ear-VAE：在损失计算前施加 K-weighting 感知滤波，引入相位相关损失改善立体声一致性，并对 MSLR 全部分量做幅度监督、仅对 LR 分量做相位监督；摘要称显著优于领先开源模型。

## 本场要点

- Flow matching / 扩散 / rectified flow 主导可控歌声编辑、美化、转换与歌曲统一生成。
- 歌词改写类任务强调无对齐旋律引导、固定时长预算与上下文填补。
- UniSinger 试图打通歌曲生成与伴奏协同 SVC 的说话人空间与多任务优化。
- CTMusic、YOAT/粤剧基准与 SingFox、LyricEditBench 补齐数据与评测基础设施。
- 感知驱动 VAE（ear-VAE）服务高质量音乐潜空间重建。
- 假唱检测走向多语、多新颖性轨与溯源可解释。

## 覆盖核对

| paper_id | title |
|---|---|
| 3285 | MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling |
| 2573 | SingFox: A Multi-Lingual Singfake Detection Corpus |
| 2090 | Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching |
| 1547 | YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance |
| 882 | CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation |
| 615 | SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow |
| 481 | Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation |
| 131 | Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model |
| 219 | Back to Ear: Perceptually Driven High Fidelity Music Reconstruction |
