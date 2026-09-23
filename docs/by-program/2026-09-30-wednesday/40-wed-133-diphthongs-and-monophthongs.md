# Diphthongs and Monophthongs

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：2
- 论文数：5
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场从语音学角度讨论单元音与双元音的动态分析：何时需要全轨迹建模，何时静态度量已足够；并以具体语言案例给出时长对比与滑音/分音节对立的证据。

方法论上，综述强调连续非实验室语音中稳态难识别，以及元音序列仍常被压成 DCT 或共振峰变化率等静态指标。实证工作则用 GAMM 与多变量函数主成分分析（MFPCA）同时刻画 F1/F2 全轨迹，并关联性别、地域、年龄与社会阶层等社会语言学因素。

语言案例覆盖 Nakanamanga 单元音时长对立，以及意大利语与罗马尼亚语 /ia/ 的双元音—分音节对立在时长与共振峰动态上的实现差异。

## 技术内容

### 动态分析框架与单元音时长

**On the challenges and benefits of dynamic vowel analyses**（论文 id 未提供；Johanna Cronenberg）  
综述单元音、双元音与分音节序列的动态研究：连续语音中稳态难找；元音序列虽本质动态，却仍常以静态指标分析。报告将展示新方法能带来的洞见，并讨论何种情形下更直接的静态分析已足够。

**Phonetic evidence for contrastive length in Nakanamanga monophthongs**（论文 1597；Shubo Li）  
首次对瓦努阿图大洋洲语 Nakanamanga 的对比元音时长做声学考察。摘要称长短单元音在全部五个元音音质上时长显著不同，长元音平均约为短元音的 2.08 倍，为音系时长对立提供清晰声学支持。

### 双元音—分音节对比与澳式英语轨迹

**To glide or not to glide: Acoustic realization of the diphthong-hiatus contrast in Italian and Romanian**（论文 2433；Johanna Cronenberg）  
在大规模语料上分析意大利语与罗马尼亚语 /ia/ 的时长与共振峰动态。摘要称意大利语轨迹更短、略浅，罗马尼亚语更偏分音节；意大利语在重读时滑音似被阻断，罗马尼亚语仅在非重读词中位置更偏滑音；两语重叠大，提示该对立可能跨语与语内均为渐变。

**Modelling diphthong dynamics: A GAMM-based analysis of Australian English diphthongs**（论文 2861；Ksenia Gnevsheva）  
用广义加性混合模型对五个澳式英语双元音全轨迹建模，并比较性别与城—乡地域。摘要称全部元音有性别效应，三个有地域效应，女性与城市说话人变化领先；部分差异出现在起止点之外，凸显全轨迹建模价值。

**Variation and change in dynamicity of Australian English diphthongs in Sydney**（论文 3206；Benjamin Purser）  
用 MFPCA 同时分析 F1 与 F2，覆盖悉尼自发话语中六个双元音逾 57,000 标记，并考察年龄、性别与社会阶层。摘要称社会变异方向与既有变化预期一致，但联合 F1/F2 能更整体地理解动态属性。

## 本场要点

- 动态分析并非一律必要，但可揭示静态起止点无法捕捉的中段差异。
- Nakanamanga 提供全元音音质上约 2 倍时长比的声学证据。
- 意/罗 /ia/ 实现支持双元音—分音节对立的跨语梯度性。
- 澳式英语双元音变化研究转向 GAMM 与 MFPCA 全轨迹社会语言学建模。

## 覆盖核对

- （id 未提供） | On the challenges and benefits of dynamic vowel analyses
- 1597 | Phonetic evidence for contrastive length in Nakanamanga monophthongs
- 2433 | To glide or not to glide: Acoustic realization of the diphthong-hiatus contrast in Italian and Romanian
- 2861 | Modelling diphthong dynamics: A GAMM-based analysis of Australian English diphthongs
- 3206 | Variation and change in dynamicity of Australian English diphthongs in Sydney
