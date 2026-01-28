# 📓 开发日志 & 规划（LOGS）

这里记录本项目的开发冲刺计划、阶段性进度和未来路线图。

---

## 📅 3-Day Sprint 冲刺计划

### 第一天：核心大脑与执行驱动 (MVP)
**目标**：实现“指令 -> 思考 -> 操作”的闭环。  
* **核心任务**：
    * [x] 初始化 Python 环境，安装 `playwright`, `langchain-openai` 等基础依赖，并升级至 Python 3.11。
    * [x] 编写 `agent_test.py`，接入 Kimi API（OpenAI 兼容协议）。
    * [x] 实现第一个任务：让 Agent 自动打开浏览器，在百度中搜索“深圳未来14天天气”。
* **验证点**：
    * [x] 终端能输出 Agent 的思考过程（Kimi 生成操作步骤）。
    * [x] 本地自动弹出的浏览器能根据脚本自动输入“深圳未来14天天气”并触发搜索。
    * [x] 在搜索结果页抓取天气文本，并由 Agent 生成“未来14天天气 + 适合户外日期”的总结。

### 第二天：容器化与画面流 (Docker + VNC)
**目标**：将浏览器“云端化”，通过网页实时查看画面。  
* **核心任务**：
    * [x] 编写 `Dockerfile`，集成 Playwright 运行环境及 VNC 服务（Xvfb + x11vnc + noVNC）。
    * [x] 配置 `docker-compose.yml`，映射 6080 端口（noVNC）到宿主机。
    * [x] 修改 Agent 代码，使其在 Docker 虚拟显示器（DISPLAY=:99）中运行，并兼容非交互环境。
* **验证点**：
    * [x] 在宿主机浏览器访问 `http://localhost:6080/vnc.html` 能看到容器内的桌面。
    * [x] 运行 `docker-compose up --build` 后，noVNC 窗口内能实时看到 Agent 在百度中自动搜索“深圳未来14天天气”。

> **Day 2 快速体验：**
> 1. 在项目根目录执行：`docker-compose up --build`  
> 2. 打开浏览器访问：`http://localhost:8000/`  
> 3. 右侧 Iframe 会自动通过 noVNC 连接容器桌面，你可以直接看到浏览器自动打开并搜索“深圳未来14天天气”。

### 第三天：前端集成与“Manus”初体验
**目标**：完成双窗交互 UI，打造完整的 Web Agent 产品体验。  
* **核心任务**：
    * [x] 使用 FastAPI 封装后端接口，提供同步启动 Agent 任务的 `/run` API（后续可演进为异步）。
    * [x] 编写前端宿主页面（由 FastAPI `/` 提供），左侧集成任务输入与“启动 Agent”按钮，右侧嵌入 noVNC 的 `<iframe>`。
    * [x] 实现联动：点击左侧“启动 Agent”按钮 -> 后端调用 `/run` -> 右侧 Iframe 中的浏览器自动加载并执行任务。
* **验证点**：
    * [x] 用户在 Web UI 点击按钮，无需操作终端即可在右侧看到 Agent 自动干活。
    * [x] 任务完成后，终端日志中能看到 Agent 总结的天气报告（后续可将总结回传到前端页面展示）。

---

## 📈 未来路线图

- [ ] 支持文件上传并从宿主机挂载至容器。  
- [ ] 接入 Qwen-VL 实现基于视觉的坐标点击优化（解决复杂 DOM 定位问题）。  
- [ ] 多会话隔离与浏览器容器动态调度。  

---

## 第四天：视觉增强 Agent（Kimi = 大脑，Qwen-VL = 眼睛）

**目标**：在现有 Playwright + Kimi + Docker + FastAPI + noVNC 的基础上，引入 Qwen-VL 作为视觉模块，让 Agent 能“看懂”真实网页布局并据此行动。  

* **分支策略**：
    * 在 `max/playwright-baseline-mvp` 分支完整保留 Day 1–3 的实现，作为稳定基线。
    * 在 `main` 分支上演进视觉能力（Qwen-VL），browser-use 作为未来可选的内核重构方向，而非当前必选依赖。

* **已完成的核心任务**：
    * [x] 设计并实现统一的视觉工具接口 `visual_inspect(page, question) -> str`，在搜索结果页调用该工具进行视觉分析。
    * [x] 在 `visual_tool.py` 中实现截图逻辑，将当前页面保存到 `screenshots/` 目录（并已在 `.gitignore` 中忽略）。
    * [x] 通过 OpenAI 兼容接口接入 Qwen-VL：使用 `VL_MODEL / VL_BASE_URL / VL_API_KEY` 创建 `ChatOpenAI` 客户端，将截图以 `image_url` + 文本问题的形式发送给 Qwen-VL，获取关于页面布局和关键信息的描述。
    * [x] 在 `agent_test.py` 中组合 Kimi + Qwen-VL：Kimi 负责任务规划与最终“未来14天天气总结”，Qwen-VL 负责描述搜索结果页的视觉结构，为 Kimi 提供额外上下文。
    * [x] 在本地与 Docker + noVNC 环境中验证：通过 Web UI 点击“启动 Agent”，可在右侧屏幕中看到浏览器自动操作，同时在终端日志中看到 Qwen-VL 的视觉分析和 Kimi 的天气报告。

* **后续可选任务（browser-use 路线，暂未实现）**：
    * [ ] 新增 `browser_use_agent.py`，用 Kimi + browser-use 跑通“打开百度”的最小 Demo（先在本机验证）。
    * [ ] 在 FastAPI 中为 browser-use 版本新增独立的 `/run_browser_use` 接口，便于与现有 `/run` / `/run_visual` 对比。
    * [ ] 将 browser-use Agent 挂载到 Docker + VNC 链路中，在 noVNC 画面中观察其自动操作过程。
    * [ ] 将当前的 Qwen-VL 视觉工具接入 browser-use 的 tool 体系，实现“视觉点击”等更复杂的交互。

* **验证点**：
    * [x] 在同一套 UI 下，用户可以通过 `/run` 体验“文本 + DOM”方案，通过 `/run_visual` 体验“文本 + 视觉（Qwen-VL）”增强方案。
    * [x] 在复杂搜索结果页中，Qwen-VL 能输出对页面结构的自然语言描述，为 Kimi 的最终决策提供额外线索。
    * [ ] 在未来集成 browser-use 后，可在复杂 DOM 结构下进一步验证“browser-use + Qwen-VL”对视觉点击和复杂交互的提升效果。

