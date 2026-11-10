# hello-github

我的第一个 GitHub 仓库，用于验证本地 Git 与 GitHub 的 SSH 通道是否完全打通。

## 这个仓库验证了什么

- 本地 PortableGit（`2.55.0.windows.3`）可正常执行 git 命令
- SSH 密钥认证可用（`ssh -T git@github.com` 返回 `Hi jt-workbuddy!`）
- 克隆、提交、推送整条链路通畅

## 快速开始

```bash
git clone git@github.com:jt-workbuddy/hello-github.git
cd hello-github
python hello.py
```

预期输出：

```
Hello, GitHub!
当前时间: 2026-11-10 14:22:00
```

## 目录结构

```
hello-github/
├── README.md      # 项目说明
├── hello.py       # 最小示例脚本
└── .gitignore     # 忽略规则
```

## 提交身份

本仓库的提交使用 GitHub 官方 noreply 邮箱，不会暴露真实邮箱：

```
jt-workbuddy <354512424+jt-workbuddy@users.noreply.github.com>
```
