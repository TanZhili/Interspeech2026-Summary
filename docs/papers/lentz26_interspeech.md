# BeatGain - A Rhythmic Pattern Enhancement Algorithm for Music Listening with Cochlear Implants

- 论文编号：2713
- 报告人：Benjamin Lentz
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/lentz26_interspeech.pdf

## 问题
人工耳蜗用户音乐感知受限，偏好清晰节拍与低复杂度；现有增强多做干声重混或谱稀疏，未显式按节拍结构处理切分音等弱拍事件。

## 方法
BeatGain：Spleeter 分人声/贝斯/鼓/其他，各再 HPSS；BeatThis! 估四分音符拍点并插值到十六分音符位置，用 Hann 窗按节拍表 \(G\) 生成增益——四分/八分位置增益×2，非网格十六分位置衰减至 0，仅作用于贝斯/鼓/其他的打击分量。对照 V+αP（保人声与打击、压其余谐波，无节拍调制）。在 IKA CI Pop 数据集上算复杂度与 SI-SDR；17 名正常听力受试者经 8 通道噪声激励声码器仿真 CI，2AFC 评整体印象与节奏清晰度。

## 实验与结果
BeatGain 在各 α 下复杂度均低于 V+αP，相对未处理显著简化；α=1 时 SI-SDR 最高，过强增益增加失真。听感：处理条件均显著优于未处理；BeatGain 相对 V+2P 在节奏清晰度上显著更优（约 59.4% 偏好），整体印象优势未达显著。

## 结论
显式强化强拍、衰减弱拍切分可进一步提升节奏清晰度，是干声重混的有益补充。局限：仅 4/4、听测为声码器仿真非真实 CI 用户；未来需扩拍号与真实用户试验。

## 点评
把音乐理论里的强弱拍层级直接做成可听的增益表，问题定位准。客观复杂度与主观节奏清晰度一致支持“拍点结构”贡献；整体偏好未显著超过 V+2P，说明节奏只是多维音乐体验之一。声码器仿真是务实折中，但真实 CI 结论仍需后续验证。
