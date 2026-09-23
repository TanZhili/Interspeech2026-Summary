# Dual-Space Constrained Face-Based Zero-Shot Text-to-Speech Synthesis

- 论文编号�?09
- 报告人：Ju Zhang
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26f_interspeech.pdf

## 问题
人脸含身份线索，可做无注册语音的零样�?TTS（配音、虚拟人等）。模块化路线用脸预测说话人条件、再喂预训练多说话人 TTS，音质可借大规模语音语料，但声学模型训练时只�?*语音导出**嵌入，推理才�?*脸导�?*表示，训练–推理失配导致身份漂移、音色不稳。端到端视听联合训又受视听数据规模限制�?

## 方法
**DSC-TTS** 三阶段模块化框架�?
1. **Speech Encoder \(E_s\)**：ECAPA-TDNN �?log-Mel �?\(\ell_2\) 归一化说话人嵌入；主目标 AAM-Softmax，辅以梯度反转域对抗（抑语料依赖�? Supervised Contrastive（保可分结构）。训完冻结�?
2. **对称 Face–Voice Alignment**：每视频均匀�?\(K=5\) 帧，注意力池化得脸嵌入；�?\(v=E_s(\mathrm{audio})\) 经投影进 256 维共享空间，双向 CLIP/InfoNCE + 重建 + latent consistency；投�?解码为两层残�?MLP�?
3. **Dual-space constrained TTS**：声学骨�?**YourTTS**（LJSpeech 预训�?120K �?LibriTTS 微调 165K）。微调时固定 \(E_s\) 与语音侧投影 \(P_v\)；对合成与真音施加说话人嵌入余弦一�?\(L_{\mathrm{SCL}}\) 与共享身份空间一�?\(L_{\mathrm{SICL}}\)，总损�?\(L_{\mathrm{TTS}}+\lambda_{\mathrm{SCL}}L_{\mathrm{SCL}}+\lambda_{\mathrm{SICL}}L_{\mathrm{SICL}}\)（\(\lambda_{\mathrm{SCL}}=9,\lambda_{\mathrm{SICL}}=3\)）。脸�?AntelopeV2�?

## 实验与结�?
训练：VoxCeleb2（对齐与编码器）、LibriTTS clean-100/360、LJSpeech。评测：VoxCeleb2 未见 24 �?+ LRS2 语料失配�?
- **Table 1**：DSC-TTS �?VoxCeleb2 �?WER 0.072、CER 0.037、SECS 0.677、SEC 0.842、SED 0.748、SMOS 3.172，优�?FaceTTS / Face2Speech / SYNTHE-SEES / Face-StyleSpeech；LRS2 �?SECS 0.653、SMOS 3.416 等同理领先�?
- **消融**：域对抗+SupCon �?SCL/SICL 互补；全组件组合最优。SICL 提升 SEC；SED 基本不变�?
- 可视化：注意力池化压低姿�?模糊差帧；LRS2 上脸–声嵌入 discrepancy 分布更左偏；t-SNE 合成嵌入簇更紧、类间更清�?

## 结论
通过语料不变说话人嵌入、对称脸声对齐与双空间约束训练，DSC-TTS 缓解模块化脸条件 TTS 的训练–推理身份失配，在相似度与身份一致性上优于既有脸基 TTS，同时保持可懂度。边界是仍依赖视听预训练数据与固�?YourTTS 骨干�?

## 点评
把问题钉在「训练用声、推理用脸」的表示缝上，用共享身份空间把推理条件拉回训练约束集。强在统一骨干下重实现多模块基线、以�?SEC/SED 拆开看稳定性与可分性；脆弱处是双空间损失权重敏感，且零样本�?TTS 仍受单图姿�?光照与跨数据集域移影响，主观 SMOS 方差仍大�?
