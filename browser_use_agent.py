import os

from dotenv import load_dotenv
from browser_use import Agent, Browser


def main() -> None:
    print("==== browser-use Day4 最小 Demo ====")

    load_dotenv()

    # 这里暂时不自己构建 LLM 对象，先交给 browser-use 内部处理。
    # 你之后可以通过环境变量或 browser-use 文档指定 provider 和模型。
    task = "打开 https://www.baidu.com，然后结束。"

    browser = Browser()
    agent = Agent(
        task=task,
        browser=browser,
    )

    result = agent.run()
    print("✅ browser-use Agent 运行结束，返回结果：")
    print(result)


if __name__ == "__main__":
    main()