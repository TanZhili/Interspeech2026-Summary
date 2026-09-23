# Stress Detection Across Daily Activities: A Context-Aware Multimodal Framework with Trajectory and Ambient Speech

- 论文编号：1262
- 报告人：Wei-Heng Huang
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/huang26e_interspeech.pdf

## 问题
医院等场景的压力监测依赖 HRV 等生理信号时难扩展；纯语音虽可被动采集，但压力高度依赖情境，声学 alone 跨场景不够稳。需要把可被动获取的室内移动轨迹作为互补上下文。

## 方法
提出 Trajectory Speech Embedding（TSE）：日级双塔 + late fusion。音频用 openSMILE LLD（8 韵律 + 16 频谱），按日对 24 维描述子各算 15 个统计量得 360 维，再经带 [REP] token 的 Transformer 得 za；轨迹由医院室内 RSSI 定位得到分钟级序列，合并为 session（位置+时长），加正弦时间嵌入，经预训（next-location）再微调的 Trajectory Transformer 得 zt；拼接后 MLP 做二分类，并加音频/轨迹辅助损失（λ=0.5）。在 TILES-2018 上，自报压力按全局均值 μ=1.8 二值化（约 31.9% 压力），主体独立 80/10/10 划分；另有 Coordinate TSE 使用真实坐标。

## 实验与结果
Table 1：Audio Transformer MCC 0.074、F1 34.20；Trajectory Transformer MCC 0.091；TSE MCC 0.142、F1 38.65；Coordinate TSE 最佳（MCC 0.147、BACC 58.91、F1 38.81）。相对 Bi-LSTM 音频基线（MCC 0.109），框架将 MCC 提高 0.038；摘要亦报告相对 audio-only 基线 F1 +9.32%。轨迹预训练 next-location Top-1/Top-3 为 38.85%/60.40%。按 session 数分层时，高机动性下融合 F1 可达 51.5%；低机动性时轨迹往往强于音频。错误恢复分析显示：音频失败被轨迹救回的日子 session 更多，轨迹失败被音频救回的日子工作时长更短、位置多样性更高。

## 结论
联合建模环境语音与移动轨迹可稳定提升医护人员日级压力识别；未来拟做更细粒度上下文、更长时依赖，并扩展模态与部署场景。

## 点评
抓住“压力=声学×空间情境”这一实际缺口，用 late fusion 与 next-location 预训练把室内定位序列变成可迁移上下文，比硬拼特征更干净。标签靠问卷全局均值切分、日级聚合也牺牲时间分辨率；MCC 绝对水平仍偏低，说明真实医院噪声与主观标签下任务本身很难，轨迹收益更像稳健性补丁而非已可上线监测器。
