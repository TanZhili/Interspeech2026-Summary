# Modeling Articulation

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：1
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。Survey Talk 导出表无完整摘要，不编造具体论断。

## 技术趋势

本 Oral 场以生物启发语音处理综述开场，随后聚焦发音建模：用大规模语音—网格数据增强稀缺 EMA 反演、从文本直接合成发音运动学、物理信息神经算子求解声道波动方程，以及动态神经场与任务动态的音系规划仿真工具包。主线是在真实 EMA 昂贵稀缺的前提下，扩展发音监督来源，并把物理与神经动力学引入可计算发音管线。

数据侧，ArtBoost 从面向三维人脸动画的 speech-mesh 抽取伪发音轨迹做预训练；STArK 用预训练语音→发音模型伪标 LibriTTS-R，实现文本→EMA 量级运动学并支持说话人克隆。物理侧，PINO 无需预计算监督即可学习一维波动方程，GPU 并行加速静态元音分析。工具侧，PyPhonPlan 把耦合动态神经场与任务动态做成可复现开源仿真栈。

整体上，发音研究正从“仅有少量 EMA”转向“伪标签规模化 + 物理/神经动力学仿真并存”的生态。

## 技术内容

### 综述与数据增强反演

**Bio-Informed Speech Processing, Modeling, and Generation**（Survey Talk；09:00-09:40）  
官方程序网格保留标题，导出表无完整摘要。按材料说明将其视为生物启发语音处理、发音建模与生成的综述开场，**不编造**具体方法、数据集或实验结果。

**ArtBoost: Synthetic Articulatory Data Augmentation for Acoustic-to-Articulatory Inversion**（论文 664；Hyung Kyu Kim）  
针对 EMA 成本高、规模小，利用面向语音驱动三维人脸动画的大规模 speech-mesh，从可见面部锚点提取伪发音轨迹，先预训练再微调真实 EMA。实验称 PCC/RMSE 一致提升，轨迹分析显示伪信号反映有物理意义的可见发音动态，并可接入多种 AAI 架构。

### 文本驱动运动学、物理仿真与规划工具

**STArK: Towards Synthesizing Articulatory Kinematics from Text**（论文 2842；Xavier Yin）  
提出直接从文本生成发音运动学：在 LibriTTS-R 上用预训练语音→发音模型伪标 EMA 特征训练。摘要称其为首个高质量文本→发音运动学模型，语音合成可与多说话人 TTS 相当，且训练未见说话人嵌入即可声克隆，旨在为下游任务从文本语料规模化生成发音数据。

**Physics-Informed Neural Operator for Speech Production Analysis**（论文 2023；Kazuya Yokota）  
据称首个用于言语产生分析的 PINO：直接学习一维波动方程，无需预计算监督数据。以声道形状为输入，对五个静态元音比较预测 f0、声门体积速度与唇口声压相对 Runge–Kutta/有限差分解。声门体积流误差约 0.8%、语音波形约 3.2%，可 GPU 并行、无需迭代求解。

**PyPhonPlan: Simulating phonetic planning with dynamic neural fields and task dynamics**（论文 1804；Sam Kirkham）  
开源 Python 工具包，用耦合动态神经场与任务动态实现音系规划仿真：模块化规划/感知/记忆场、场间耦合、手势输入，并由场激活轮廓求解 tract 变量轨迹。示例演示含耦合记忆场的产出/感知环，强调时间原则、神经接地与语音丰富表示；含可执行示例以促复现与扩展。

## 本场要点

- Survey Talk 无完整摘要，仅作生物启发发音建模综述定位，不外推结果。
- speech-mesh 伪发音轨迹可增强稀缺 EMA 反演。
- 文本→发音运动学 + 伪标使发音数据可规模化生成。
- PINO 为快速言语产生物理分析提供无迭代 GPU 路径。
- PyPhonPlan 把动态神经场音系规划做成可复现工具链。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| （Survey） | Bio-Informed Speech Processing, Modeling, and Generation |
| 664 | ArtBoost: Synthetic Articulatory Data Augmentation for Acoustic-to-Articulatory Inversion |
| 1804 | PyPhonPlan: Simulating phonetic planning with dynamic neural fields and task dynamics |
| 2023 | Physics-Informed Neural Operator for Speech Production Analysis |
| 2842 | STArK: Towards Synthesizing Articulatory Kinematics from Text |
