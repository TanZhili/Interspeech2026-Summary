# Spatial Audio 2

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕沉浸式与物理可解释的空间音频生成/建模：从 360° 野外语音场景的视觉引导一阶 Ambisonics（FOA）补全，到以扩散模型完成房间脉冲响应（RIR）早期反射之后的真实混响尾，再到参数阵扬声器（PAL）的超声—可听声神经建模，以及场景几何编辑后的 RIR 更新与少样本双几何流形预测。共同主题是：把视觉、几何仿真或物理过程作为条件，用生成模型补齐测量或仿真缺口，并强调对输入时长、材料标注或参考 RIR 数量等约束的放松。

RIR 相关工作尤为集中：信号预测扩散在 ISM 早期反射条件上取消固定时长限制，并用无分类器引导对齐 Treble SDK 物理仿真分布；编辑条件估计用编辑前后网格的代理仿真关联几何变化与声学变化；少样本预测则依据早期反射与晚期混响不同曲率，采用双曲+欧氏双分支聚合。PAL 侧用 U2A 框架解耦调制与空气自解调非线性。整体上，空间音频从“端到端黑盒渲染”转向物理动机条件与几何感知生成。

## 论文技术总结

# Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes

- 论文编号：2577
- 报告人：Qingyu Luo
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/luo26b_interspeech.pdf

## 问题
野外 360° 语音场景常只有全向轨，缺可靠 FOA 方向分量；现有语音空间数据集多为双耳/仿真，且与全景视频配对稀缺，显式视频条件 FOA 重建研究不足。

## 方法
构建 YT-SPEECH（约 8.9 h、24 kHz、5 s 片段，197 源视频）：多阶段过滤（FOA 布局、语音主导、YOLO 可见说话人、音视频一致性与人工检查）。提出 Localizer–Renderer：冻结 AVS 骨干 + 可微调 Spatial Prior Head 生成 ERP 空间先验 \(P_t\)；复域 U-Net 用置信度门控 FiLM（峰值×熵）将 \(W\) 谱投影为 \(Y,Z,X\) 复掩码。损失为置信度加权 MRS/幅度/\(\ell_2\)。Sphere360 预训练后在 YT-SPEECH 微调，并做 yaw/翻转增强。

## 实验与结果
YT-SPEECH 上完整模型 \(\ell_2\)、角误差 \(\Delta_{ang}\)、PESQ、MOS-P 最优；冻结 Localizer 损害空间指标；解析 Ambisonics/Pyroom 峰值编码在部分幅度/MOS-Q 上强但空间误差更大。相对 SAG，在 YT-CLEAN/YT-SPEECH 等视觉可定位集上更稳。噪声与重叠源仍是主要失败模式。

## 结论
YT-SPEECH 与 Localizer–Renderer 可提升野外语音主导 360° 场景的 FOA 重建保真度、空间精度与感知语音质量；局限含数据规模与复杂声学场景稳定性。

## 点评
把 AVS 热图当可解释方向先验，并用置信度门控缓解歧义，比无监督分离更贴“方向先行”路线。强在语音向数据集与相位一致复域渲染；弱在噪声/多源时先验不可靠，且 8.9 h 规模仍偏小。


# Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections

- 论文编号：531
- 报告人：Zeyu Xu
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/xu26p_interspeech.pdf

## 问题
RIR 补全常要求固定时长（如 50–80 ms）的完整早期反射头；低阶 ISM 条件在窗口内不填满时，现有方法易在补全结果引入不连续。

## 方法
用 x-prediction 扩散（余弦调度，T=200）直接预测目标 RIR \(x_0\)，条件为任意最大反射阶的 ISM 早期响应 \(c\)（与噪声 \(x_t\) 通道拼接）。1D U-Net + 瓶颈膨胀卷积；损失 MSE 与可选 EDC 损失。Classifier-free guidance：训练时以 \(p_{CFG}=0.2\) 置零条件。构建配对 ISM（pyroomacoustics）与 Treble SDK 波场数据集（各 10k RIR，25 房间）。对比 Echo2Reverb。

## 实验与结果
Exp.1 纯 ISM：阶数变化时指标较稳，加 EDC 损失显著降 EDC MAE。Exp.2 混合训练（80% ISM + 20% Treble）测 Treble：低阶条件上早期残差能量比（RER）优于 Echo2Reverb；阶 5/7 时 EDC 更好；Echo2Reverb 在窗口未填满时可能出现不连续与后期虚假脉冲。扩散 200 步推理慢于基线单次前向。

## 结论
在不固定早期窗口填满的前提下，x-prediction + CFG 可用低阶 ISM 条件生成更现实的 RIR，并在混合数据上改善早期补全与 EDC；未来需加速推理并在实测 RIR 上验证。

## 点评
把“阶数受限 ISM”当作真实部署条件，并用 x-prediction 便于直接算 EDC，设计贴工程。CFG 用少量 Treble 样本撬动波效应是亮点。脆弱点是推理延迟与极低阶（如 order 1）时 EDC 仍可能差于基线。


# U2A-Net: Physically Motivated Ultrasound-to-Audio Neural Modeling for Parametric Array Loudspeakers

- 论文编号：2390
- 报告人：Mengtong Li
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/li26ea_interspeech.pdf

## 问题
参量阵扬声器（PAL）非线性强，A2A 把调制与空中自解调揉成黑盒，复杂度高；U2U 又被强超声载波主导，难精建模可听频段 THD/IMD。

## 方法
提出 U2A 建模：输入为已调超声驱动 \(s_u(t)\)（192 kHz），输出为可听声 \(y_a(t)\)（48 kHz）。多速率 WaveNet：16 残差块 + 可学习 4× 下采样（两层 stride-2 Conv），联合波形与频谱幅度 MSE。在消声室 USBAM PAL（576 阵元，40 kHz）采集约 3 h 语音/音乐/环境声同步数据（7:2:1）。对比同骨干 A2A-Net 与二阶 U2A-Volterra。

## 实验与结果
四级输入幅度下，U2A-Net 平均绝对 THD/IMD 偏差最低（如 level 1.0：THD 0.52%、IMD 1.26%），且文称平均非线性失真建模误差低于 1.62%。大信号时相对 A2A 优势更明显；U2A-VF 因二阶表达力不足，THD/IMD 曲线近零、误差大。线性频响三方法接近，差异主要在非线性自解调。

## 结论
物理动机的 U2A 表述让网络专注自解调，在代表 PAL 上稳定优于 A2A 与低阶 Volterra，适合 PAL 辨识与后续补偿。

## 点评
输入–输出域对齐 Westervelt 物理，比单纯加大 A2A 容量更干净。多速率下采样是必要工程件。当前仅一个 USBAM 原型与轴上 1.8 m，外推到其他调制/离轴/混响环境仍待证。


# Echoes after Edits: Room Impulse Response Estimation for Geometry Update

- 论文编号：2514
- 报告人：Yoshiki Masuyama
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/bhosale26_interspeech.pdf

## 问题
室内轻微几何编辑（挪移/移除家具）会显著改变 RIR；声学仿真要精细材料标注，场插值又要在编辑后重测多个参考 RIR，日常场景都不现实。

## 方法
提出 edit-conditioned RIR 估计与 PG-RIR：用编辑前后网格在 \(M\) 种全局均匀材料下仿真 proxy RIR，与实测编辑前 \(r_0\) 一起估计编辑后 \(r_1\)。ResNet-18 编码 log 幅度谱，融合 type/material 嵌入；上下文查询注意力 + 频带门控超网络预测残差谱，相位沿用 \(r_0\)。损失：谱 L1 + 带状衰减曲线。iGibson 14 场景、AcoustiX 仿真构建 143k 声源–接收对（训练以移除为主）。

## 实验与结果
Leave-one-scene-out：PG-RIR \(T_{60}/C_{50}/EDT\) 误差低于 identity 与 xRIR（K=4/8）；编辑幅度越大优势越明显。相对 DiffRIR 反演–前向渲染，在 9/34 表面场景均更优且无需每场景反演。仅训移除却可零样本推广到平移编辑；多步链式预测会累积谱平滑。

## 结论
用同质材料 proxy 把几何变化编码为声学线索，可在无新测量与无精细材料标注下更新 RIR；未来拟用课程学习加强平移序列。

## 点评
任务定义清晰：把“场景改了怎么办”从重测/重标注改成条件化残差预测。Proxy 差分解耦几何与材料是关键设计。目前证据主要在仿真；链式编辑的早期瞬态抹平是部署隐患。


# Dual-Geometry Manifolds for Few-shot RIR Prediction

- 论文编号：2630
- 报告人：Yoshiki Masuyama
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/bhosale26b_interspeech.pdf

## 问题
少样本跨场景 RIR 预测常把参考在静态欧氏潜空间融合，与早期反射树状层级、晚期混响平坦扩散的物理异质性冲突，易抹平早期路径并损害清晰度。

## 方法
用 Gromov \(\delta\)-hyperbolicity 实证局部声学流形由早期高双曲性过渡到晚期近欧氏，且过渡速率随房间体积变化。提出 Janus-RIR：并行双曲（Poincaré 球 + Einstein 中点）与欧氏聚合分支，上下文感知门 \(\alpha(t)\) 按时融合；早段对双曲注意力加熵惩罚。骨干沿用 xRIR 的 ResNet/坐标（及可选深度图）特征。在 AcousticRooms 上 \(K\in\{1,4,8\}\) 评测。

## 实验与结果
Janus-RIR（含 NoVision）在 EDT/\(C_{50}/T_{60}\) 上全面优于 Few-shot RIR 与 xRIR；\(K=8\) 时 NoVision 相对 xRIR \(T_{60}\) 误差约降 26%（10.53%→7.75%），并改善 \(C_{50}\)。Hard 外推距离档误差更稳。消融：纯双曲、双欧氏或仅时间门均变差；潜空间范数轨迹显示小房更快塌缩、大房更久保持双曲结构。

## 结论
按物理阶段切换潜几何可同时改善早期清晰度与晚期混响估计；模型隐式适应环境混合时间。未来拟探索早期时域最优传输插值等。

## 点评
先用 \(\hat\delta\) 度量证明几何演变，再设计门控双流形，论证链条完整。相对“加参数/加视觉”的消融说明收益来自曲率对齐。Griffin-Lim 相位重建与仿真数据仍可能限制听感与实测外推。

