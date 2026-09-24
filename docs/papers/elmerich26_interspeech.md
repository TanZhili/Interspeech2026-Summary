# NewAppVoice: Tools for Visualizing and Correcting Acoustic Measures

- 论文编号：2560
- 报告人：Amélie Elmerich
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/elmerich26_interspeech.pdf

## 问题
羌语、藏语支等少文书写语言缺乏参考共振峰值，Praat / VoiceSauce 等自动提取常有系统误差，必须靠目视与手改；大批量脚本又缺少交互反馈，可复现性差。

## 方法
NewAppVoice 以 .wav + TextGrid 为输入，在统一界面同步显示波形、语图、多算法轨迹与结果表。基频并行三种算法（STRAIGHT、SHR、Praat 自相关）；共振峰并行 STRAIGHT（LPC 点）与 Praat Burg（连续轨迹），可对照频谱/LPC 包络手工改错；并支持强度（dB RMS / 线性 RMS）、HNR、CPP 等。MATLAB App Designer 开发，已编译为免许可证的 macOS/Windows 可执行文件。

## 实验与结果
以白马藏语 /dzɑ̀/「月亮」、麻窝羌语 /ti/「黑熊」等实例演示：如 Straight F4 估到约 5000 Hz 而频谱峰在 3500–4000 Hz，可用 Praat 列校正（表中 F4 4861→F4Praat 3731 等）。属工具演示与案例分析，无大规模基准对比数字。全文在 HNR 小节标题处截断。

## 结论
作者认为将多算法提取与持续可视化、结构化手改结合，能提高少书语言声学测量的可靠性与可复现性；软件开源开放获取。

## 点评
面向纪实语音学痛点——“无参考值时如何发现并改正自动错误”——交互比纯批处理更务实。全文抽取未覆盖语音质量模块后半与系统评测；效果依赖标注者对语图/频谱的判读能力，非端到端自动鲁棒性声明。
