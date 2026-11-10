#!/usr/bin/env python3
"""最小示例脚本：打印问候语与当前时间。"""

from datetime import datetime


def greet(name: str = "GitHub") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


def main() -> None:
    print(greet())
    print(f"当前时间: {datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
