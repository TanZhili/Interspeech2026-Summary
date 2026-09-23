# Spatial Audio 2

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：5
- 论文数：6
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。官方条目中论文 531 与 2025 标题与摘要相同，本稿按两条目分别覆盖核对，不合并臆测为同一投稿。

## 技术趋势

本场围绕沉浸式与物理可解释的空间音频生成/建模：从 360° 野外语音场景的视觉引导一阶 Ambisonics（FOA）补全，到以扩散模型完成房间脉冲响应（RIR）早期反射之后的真实混响尾，再到参数阵扬声器（PAL）的超声—可听声神经建模，以及场景几何编辑后的 RIR 更新与少样本双几何流形预测。共同主题是：把视觉、几何仿真或物理过程作为条件，用生成模型补齐测量或仿真缺口，并强调对输入时长、材料标注或参考 RIR 数量等约束的放松。

RIR 相关工作尤为集中：信号预测扩散在 ISM 早期反射条件上取消固定时长限制，并用无分类器引导对齐 Treble SDK 物理仿真分布；编辑条件估计用编辑前后网格的代理仿真关联几何变化与声学变化；少样本预测则依据早期反射与晚期混响不同曲率，采用双曲+欧氏双分支聚合。PAL 侧用 U2A 框架解耦调制与空气自解调非线性。整体上，空间音频从“端到端黑盒渲染”转向物理动机条件与几何感知生成。

## 技术内容

### 视觉引导空间语音与 RIR 扩散补全

**Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes**（论文 2577；Qingyu Luo）面向野外语音主导 360° 场景，在对齐的 360° 视频与全向音轨上恢复缺失方向性 FOA；发布语音向 YT-SPEECH 数据集，并提出 Localizer-Renderer 两阶段：音视频分割骨干给帧级空间热图，条件复域 U-Net 从全向通道重建方向 FOA，并以置信度门控稳定模糊声学条件下的条件。

**Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections**（论文 531；Zeyu Xu）以 ISM 仿真直达与早期反射为条件的信号预测扩散完成 RIR，不对输入早期反射施加固定时长约束，并用 classifier-free guidance 导向 Treble SDK 物理仿真目标分布；客观评测报告优于相关 SOTA（具体数值以官方摘要全文为准）。

**Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections**（论文 2025；Zeyu Xu）官方条目给出与论文 531 相同的标题与摘要内容；按节目单单独列出，技术表述与上条一致，不额外添加摘要未出现的差异说明。

### 参数阵物理建模与几何编辑/少样本 RIR

**U2A-Net: Physically Motivated Ultrasound‑to‑Audio Neural Modeling for Parametric Array Loudspeakers**（论文 2390；Mengtong Li）提出多速率神经 U2A 框架，将调制超声映射到可听输出，通过解耦调制过程专注空气自解调非线性；相对把基带音频直接映到可听输出的 A2A 框架，在代表性 PAL 上持续更优（摘要所述）。

**Echoes after Edits: Room Impulse Response Estimation for Geometry Update**（论文 2514；Yoshiki Masuyama）提出编辑条件 RIR 估计：在场景几何轻微编辑后更新已测 RIR；用编辑前后房间网格在预设材料下仿真代理 RIR，以在无材料精细标注时关联几何编辑与声学变化。

**Dual-Geometry Manifolds for Few-shot RIR Prediction**（论文 2630；Yoshiki Masuyama）用 Gromov δ-双曲性指出声学流形从早期反射的层次树结构演变为晚期混响的平坦弥散；提出 Janus-RIR，以双曲分支处理早期反射、欧氏分支平滑晚期尾部，并由上下文感知动态门控；在 AcousticRooms 上报告达到当时最优。

## 本场要点

- 野外 360° 语音空间化依赖视觉定位热图 + 复域渲染与置信度门控。
- RIR 补全用早期反射条件扩散，并取消固定输入时长限制。
- 节目单出现两条标题/摘要相同的 RIR 补全条目（531、2025），核对表均保留。
- PAL 建模从 A2A 转向物理动机的 U2A，聚焦自解调非线性。
- 几何编辑与少样本场景分别用代理仿真条件与双几何流形聚合。
- 物理仿真（ISM、Treble）与测量/野外数据形成条件—目标配对范式。

## 覆盖核对

| paper_id | title |
|---|---|
| 2577 | Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes |
| 531 | Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections |
| 2025 | Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections |
| 2390 | U2A-Net: Physically Motivated Ultrasound‑to‑Audio Neural Modeling for Parametric Array Loudspeakers |
| 2514 | Echoes after Edits: Room Impulse Response Estimation for Geometry Update |
| 2630 | Dual-Geometry Manifolds for Few-shot RIR Prediction |
