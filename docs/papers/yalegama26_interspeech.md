# Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones

- 论文编号：2524
- 报告人：Oshan A. B. Yalegama
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/yalegama26_interspeech.pdf

## 问题
多声源同时活跃时，相对传递函数（ReTF）依赖的 W-disjoint orthogonality 不成立；相对传递矩阵（ReTM）可刻画两组麦克风间对多声源的空间映射，但既有估计几乎只靠协方差矩阵，深度学习路线尚未系统探索。

## 方法
在静止声源假设下，提出三种有监督 ReTM 估计框架：SCoNet 在 STFT 域对实虚部堆叠通道做 depthwise 卷积；FuSNet 用 QA×QB 个可学习 1D 卷积滤波器对应时域卷积核并求和；LAeNet 对每频点共享 BiLSTM 后经层归一化与全连接估计 ReTM 系数再重建 A 组信号。训练目标为时域负 SDR 与 STFT 域 RSE 的加权和（α=1, β=10）。

## 实验与结果
在 6×7×3 m、T60=500 ms 房间用工具箱仿真（QA=3/QB=4 或 QA=5/QB=7），场景含 WGN、空调/音乐噪声与含语音的多声源，麦克风加 40 dB SNR。相对协方差基线，FuSNet 在多数场景估计精度最高（如 A1 平均 SDR 28.46 dB），SCoNet/LAeNet 也常优于基线；麦克风增多时各法均改善。语音去噪（用噪声段估 ReTM）上 LAeNet 最好（B/C 的 SDR 8.67/7.03 dB，STOI 0.92/0.91），FuSNet 虽估计准但去噪差且残留回声。FuSNet 参数与延迟最低，LAeNet 延迟最高。

## 结论
深度学习可明显提升 ReTM 估计精度，STFT 域模型在去噪中更稳；未来拟扩展到分离、去混响与麦克风分组策略。

## 点评
把 ReTM 从协方差估计拉到端到端空间映射，并用去噪闭环验证“估计准≠任务好”——时域 FuSNet 与时频模型的反差很有信息量。局限是仿真、静止声源与固定分组；真实移动场景与热噪声不可忽略时还需再验。
