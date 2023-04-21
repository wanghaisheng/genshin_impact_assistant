import gettext
l10n = gettext.translation("zh_CN", localedir = r"translation/locale", languages=["zh_CN"])
l10n.install()
_ = l10n.gettext
_("# genshin_impact_assistant 原神助手\n<strong>|[Chinese](./)|[English](doc/en/readme.md)|</strong>\n<div align=\"center\">")
_("基于图像识别和模拟按键的多功能原神自动辅助操作,包括自动战斗,自动刷秘境,自动刷大世界材料。")
_("GIA的目标是：让程序负责玩原神，你负责抽卡和带着角色逛街~~养老婆~~")
_("[![GitHub Star](https://img.shields.io/github/stars/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/stargazers)\n[![Release Download](https://img.shields.io/github/downloads/infstellar/genshin_impact_assistant/total?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/releases/download/v0.3.0/GIA.Launcher.v0.3.0.7z)\n[![Release Version](https://img.shields.io/github/v/release/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/releases/latest)\n[![Python Version](https://img.shields.io/badge/python-v3.7.6-blue?style=flat-square)](https://www.python.org/downloads/release/python-376/)\n[![GitHub Repo Languages](https://img.shields.io/github/languages/top/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/search?l=Python)\n![GitHub Repo size](https://img.shields.io/github/repo-size/infstellar/genshin_impact_assistant?style=flat-square&color=3cb371)\n[![contributors](https://img.shields.io/github/contributors/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/graphs/contributors)\n</br></br>\n[![QQ群](https://img.shields.io/badge/QQ群-901372518-blue.svg?style=flat-square&color=12b7f5&logo=qq)](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)\n[![Bilibili](https://img.shields.io/badge/bilibili-infstellar-blue.svg?style=flat-square&logo=bilibili)](https://space.bilibili.com/313212782)")
_("</div>")
_("# 介绍")
_("基于图像识别的原神自动操作辅助.使用图片识别与模拟键盘操作,不涉及违规操作.")
_("To没用过github的小伙伴: 描述文档中的蓝色文字是链接,可以打开的.")
_("## 演示视频")
_("<https://www.bilibili.com/video/BV1RV4y157m6>(挂了)")
_("补档 <https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0的演示视频，可能部分过期")
_("## 功能介绍")
_("### 1. [自动战斗辅助](./doc/combat_assi.md)")
_("- 在GUI中将FlowMode切换到AutoCombat，等待模块导入")
_("- 按下`[`键启动/停止功能。可在`keymap.json`中更改。")
_("其他设置参见[自动战斗辅助介绍](./doc/combat_assi.md).")
_("### 2. [自动秘境辅助](./doc/domain_assi.md)")
_("1. 在config中设置挑战秘境的次数与其他设置,详见[config设置](./doc/config.md).\n2. 手动选择队伍,配置队伍,进入秘境.\n3. 进入秘境后,在GUI TaskList中选中DomainTask，点击启动任务\n4. 等待导入完成后切换到原神")
_("- 注意阅读[domain_assi.md](./doc/domain_assi.md)中的注意事项.")
_("其他设置参见[自动秘境辅助介绍](./doc/domain_assi.md).")
_("### 3. [自动采集辅助](./doc/collector_assi.md)")
_("演示视频：<https://www.bilibili.com/video/BV163411Q7fD>")
_("- 在GUI中将Mission Group切换到AutoCollectorMission.json")
_("- 选中Task List -> Mission，启动Task")
_("- 注意阅读[collector_assi.md](./doc/collector_assi.md)中的注意事项.")
_("其他设置参见[自动采集辅助介绍](./doc/collector_assi.md).")
_("### 4. [自动每日委托辅助](./doc/commission_assi.md)\n**正在早期测试，请谨慎开启并汇报遇到的错误。**")
_("详情参见[自动每日委托辅助介绍](./doc/commission_assi.md).")
_("## 使用方法")
_("### 快速安装")
_("请参见[GIA Launcher自动安装器使用方法](doc/install.md).")
_("### 从源代码构建")
_("请参见[源代码安装方法](doc/git_install.md)")
_("## 使用前设置")
_("### 原神窗口设置")
_("- 需要在原神启动后再运行程序.")
_("- 原神需要以1080p窗口化运行(全屏也可以),设置抗锯齿为SMAA,中或以上特效.")
_("- 窗口焦点应在原神窗口上。如果切换焦点窗口，程序会暂停所有键鼠操作并等待。")
_("### config配置")
_("在使用前，需要注意这些配置内容：")
_("|位置|配置项|内容|\n|----|----|----|\n|config/settings/config.json| `BorderlessWindow` | 如果是无边框窗口或全屏，设置为true。|")
_("可以在GUI或直接从文件中修改。")
_("更多其他配置项，参见GUI内的设置介绍。")
_("### GUI使用")
_("#### main窗口")
_("- 点击main按钮进入")
_("- Task List：选择要执行的任务，只能从GUI里启动")
_("- FlowMode：选择当前启用的功能，只能按快捷键启动")
_("- Mission: 选择要启动的任务组，然后在Task List选中Mission，启动Task List")
_("- Log：输出日志")
_("#### 设置页面")
_("- 点击按钮进入")
_("- 在下拉列表中选择对应的项目，进行配置。")
_("远程操作等更多GUI使用方法，参考[GUI使用](./doc/gui.md)")
_("### 自动战斗，自动采集设置窗口")
_("- 点击对应按钮进入，按照提示操作")
_("## 错误报告")
_("如果在使用中遇到问题，可以提交issue或在Q群中反馈。")
_("反馈错误前，请务必确认您已经阅读文档和[FAQ](doc/FAQ.md)中的已知问题与解决方案。")
_("反馈错误时，请一并提交 Logs 文件夹中的日志文件。")
_("## 常见问题 FAQ")
_("如果在使用时遇到问题，可以先看看FAQ：")
_("[FAQ](doc/FAQ.md)")
_("## 已知问题 Known Issues")
_("[Known issues](doc/known_issues.md)")
_("## 性能需求")
_("- 此程序至少需要`2.5G内存`与`3G存储空间`(完整安装).")
_("## 鸣谢\n### 特别感谢\n- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)\n### 开源库\n#### 原神相关")
_("- [原神-基于图像算法的坐标定位 GenshinImpact AutoTrack DLL](https://github.com/GengGode/cvAutoTrack)")
_("- [空荧酒馆原神地图 kongying-tavern/yuan-shen-map](https://github.com/kongying-tavern/yuan-shen-map)")
_("- [原神英語・中国語辞典 xicri/genshin-dictionary](https://github.com/xicri/genshin-dictionary)")
_("#### 开源库调用")
_("- [opencv](https://github.com/opencv/opencv)\n- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)\n- [yolox](https://github.com/Megvii-BaseDetection/YOLOX)\n- [pyinstaller](https://github.com/pyinstaller/pyinstaller)")
_("#### 其他")
_("- [GIS 参考了自动战斗脚本的格式](https://github.com/phonowell/genshin-impact-script)")
_("### 其他贡献/参与者")
_("- 数据集标注: [nɡ.](https://space.bilibili.com/396023811)")
_("## 声明")
_("- 本软件开源免费,仅供学习交流使用,请勿用于非法用途.使用本软件进行代练的商家所收取的费用均为商家的人工/设备费用,产生的<strong>\n任何问题</strong>与本软件无关.\n> 用别怂,怂别用 --unknown\n## 广告")
_("qq群:[901372518](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)")
_("开发者交流群:[680029885](https://jq.qq.com/?_wv=1027&k=CGuTvCXU)\n(请确保你已经会使用git以及github)\n")