# 更新日志

## v1.2.0 (2026-11-12)

新增功能（全部开箱即用：纯主题代码、零账号/令牌/外部绑定，不配不坏）：

- **系列文章导航**：front matter 写 `series`（系列名）+ 可选 `series_order`（序号）即启用；同系列 ≥2 篇时文首渲染系列框——系列名、全系列有序目录（当前篇标「本篇」）、「本系列第 X / N 篇」；未写序号的篇目按日期排在已编号之后
- **相关文章**：文末新增「相关文章」区块，用 Hugo Related Content 内置默认索引（keywords 100 / tags 80 / date 10，阈值 80），最多 4 篇，复用文章卡片样式；无结果不渲染。站点可在 `hugo.toml` 写 `[related]` 调整（如 `includeNewer = true`）
- **代码块一键复制**：正文每个代码块注入复制按钮，`navigator.clipboard` 优先、隐藏 textarea 降级，带「已复制」反馈；深浅双色适配
- **图片灯箱**：收尾此前只有 `cursor: zoom-in` 样式没有行为的半截实现——点击正文图片打开全屏灯箱，可前后翻看本篇全部图片（按钮/方向键/Esc/点背景关闭），图注取 alt；包着真外链的图片不拦截、照常跳转（取代旧版「新窗口打开原图」）
- **排版 shortcode 组**（`layouts/shortcodes/`，原先为空白）：`notice`（note/tip/warn 三型提示框）、`details`（原生 `<details>` 折叠块，`open` 可默认展开）、`tabs`+`tab`（标签页，JS 收成选项卡，无 JS 时平铺不丢内容）；用法示例见 README。框内 Markdown 由模板 `markdownify` 渲染，不依赖站点 goldmark `unsafe` 设置

自审修复（2026-11-12 主题自审，条目与 `~/workspace/tobpage-audit/AUDIT.md` 对应）：

- [高] 分类索引页 `taxonomy.html` 里 `append` 参数序写反：任何一篇文章用到未登记分类，整站构建直接失败——已改 `$extra | append .`，「其他」兜底组现可正常渲染
- [高] `cover` 写成字符串（而非 map）时 `.Params.cover.image` 在 baseof/single/post-card 三处让整站构建失败——三处统一加 map 守卫，异形 cover 按无封面处理
- [中] `heroImage` 写相对路径时 CSS 变量按样式表路径解析导致 Hero 背景 404——index.html 对相对路径先 `relURL`，与 og 链口径一致
- [中] 主题硬依赖的站点脚手架（search/archives/about 三页 + 首页 `[outputs]` JSON）此前未写入文档——README 新增「站点脚手架」节（含 robots.txt 与新版 `[pagination]` 键说明）
- [低] 无日期文章：文章页不再显示「0001年1月1日」，归档页不再静默吞掉、单列「未注明日期」组
- [低] `og:image` 对页面包相对路径的 `cover.image` 解析到站点根导致分享图 404——先按页面资源解析；同一根因在文章卡片与封面图的 `src` 上一并修复（原先卡片图在其他页面会拼错相对地址）
- [低] 未定义 `menus.main` 时页脚「导航」栏只剩空标题——整栏改为有菜单才渲染
- [低] 未配 `description` 时首页 `<title>` 拖尾「· 」——为空时只输出站名
- [低] README 删除已无模板使用的 `sealText` 参数（站名整图方案后残留的文档漂移）

## v1.1.1 (2026-11-12)

- 移除 v1.1.0 加入的 Giscus 评论与 Cloudflare Web Analytics 信标支持：这两项功能依赖主题之外的前置条件（绑定 Cloudflare、安装 GitHub 应用并取得令牌），与「主题开箱即用、零前置」的定位冲突，故从主题层下线，改由需要的站点在站点层自行接入（站点级模板覆盖 + 站点参数即可实现，不必改主题）。主题本身只修模板自身的问题；本版模板与 v1.0.1 功能一致（og:image、主题自带默认 favicon 均保留）

## v1.1.0 (2026-11-12)

- 新增评论区（Giscus）：文章页底部可渲染基于 GitHub Discussions 的评论，站点参数 `params.tobpage.giscus` 配置（`enable` 开关 + `repo` / `repoId` / `category` / `categoryId` 四项齐全才渲染），按路径（pathname）映射讨论，中文界面、跟随系统深浅色；不配或关开关则完全不输出
- 新增 Cloudflare Web Analytics 支持：站点参数 `params.tobpage.cfBeaconToken` 填入信标令牌后，全站自动输出官方 beacon 脚本（无 Cookie 统计）；不配则不输出

## v1.0.1 (2026-11-12)

- 新增分享预览图：head 输出 `og:image` 与 Twitter Card（`summary_large_image` + `twitter:image`），取值优先级为文章 `cover.image` → 站点参数 `ogImage` → `heroImage` → 主题自带 `img/hero-wukong.jpg`，一律输出绝对地址
- 主题自带默认站点图标 `static/favicon.svg`（墨黑底、鎏金云纹、朱砂点）：站点未配 `params.assets.favicon` 时自动引用它，配了则仍用站点自己的图标，不再出现图标 404
- 深浅自适应：无本地偏好时按访客本地时间自动选——7:00–19:00 浅色、其余时间深色；手动切换仍优先并记忆（同日早先的「固定默认浅色」被此条取代）
- 主旨语放大（Hero 29px / 开场动画 23px，隶书加粗、朱砂、保持单行居中）；站名与印章改**整图方案**：站点参数 `titleImage` 指向一张离线合成图（马善政毛笔体鎏金大字 + 篆字朱砂印贴右下角，见 README 出处），Hero 与开场动画共用，构图不再受访客设备字体与排版差异影响；副标题与统计片字号调小，层级更分明

## v1.0.0 (2026-11-08)

首个正式版本，在普客网（https://puke.eu.org/）上线运行。

- 双栏卡片流骨架：粘性侧栏、文章目录（TOC）、顶部阅读进度条、归档时间线、回到顶部
- 暗黑西游皮肤：墨黑 / 鎏金 / 朱砂，深浅双色切换；系统字体栈，无外部字体与 CDN 依赖
- 两段式开场动画：v11「在飞」→ v12「棍指南天门」收尾；仅首页渲染、每次打开播放，3 秒硬上限、减动效不播
- 五大栏目两级分类（14 个叶子分类）+ 彩色图标，分类分组索引页
- 主旨语「普天之下，皆为客。」：楷体朱砂、全宽单行、句末印章点；Hero 与动画共用站点参数
- 中文字数统计与阅读时长；本地 JSON 搜索；分类/标签/面包屑/上下篇齐全
- 通用化：站名、主旨语、备案号、起算日、Hero 图均为站点参数，主题无站点默认值

上线当晚自检修复：

- 页脚与作者卡的 GitHub 社交图标 SVG 路径损坏，已换标准路径
- Hero 背景图改走相对路径（relURL），子路径部署不再 404
- 搜索索引地址改由模板下发，子路径部署不再串站
- 附带说明：站点配 `[languages]` 时 Hugo 不自动生成 robots.txt，建议站点自备 `static/robots.txt`
