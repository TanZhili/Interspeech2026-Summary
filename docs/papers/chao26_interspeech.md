# RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation

- 论文编号：3197
- 报告人：Sung-Feng Huang
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/chao26_interspeech.pdf

## 问题
实时增强要严守算法延迟与 RTF；Transformer 类 KV cache 随时长增长，而既有 SEMamba 多为非因果离线评估。需要全因果时频 Mamba，并用蒸馏把深层教师压到浅层学生。

## 方法
RT-SEMamba：因果 STFT（窗 400/跳 100，中心关闭→25 ms 算法延迟）、因果卷积与 LayerNorm、单向 Time-Mamba + 帧内双向 Frequency-Mamba，流式维护卷积缓冲与 SSM 状态。教师 8 层 cTF-Mamba，学生 1/2 层；输出级对齐幅/相/复谱，特征级对学生块与教师各层均值做归一化 L2；蒸馏权重前 10% 步渐进升至满值，并叠加原 SE 任务损失。在 VCTK-DEMAND 评估。

## 实验与结果
8 层教师 PESQ 3.32；直接 1 层 3.06，蒸馏后 3.18；2 层 3.19→3.22。RTF：1 层 0.11 vs 8 层 0.29（约 2.6–2.75× 加速），参数/MACs 随层数近似线性。相对因果文献模型，8→1 在 25 ms 延迟、1.05M 参数下 PESQ 3.18，具竞争力。消融支持输出+中间特征蒸馏与渐进 ramp-up。

## 结论
全因果 cTF-Mamba 适合恒定状态流式推理；渐进 KD 能在不增 RTF 下显著抬浅层学生质量，形成更好的实时质量–延迟折中。

## 点评
把 Mamba 的固定状态优势落到严格流式设定，并用深度压缩补浅层容量缺口，路线清晰。与仅加深网络相比，蒸馏更划算。学生与教师仍共享前后端结构，极限压缩潜力取决于块数下限。
