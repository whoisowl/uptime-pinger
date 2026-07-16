# 🌐 Uptime Pinger

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-blue?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

---

# 🇺🇸 English

## Overview

**Uptime Pinger** is a lightweight Python-based command-line tool that
repeatedly checks whether one or more websites are online, reporting
UP/DOWN status on a configurable interval.

### Features

- Check one or multiple websites at once
- Configurable check interval
- Graceful handling of unreachable hosts (timeouts, DNS failures)
- Continuous watch mode (runs until stopped)
- Clean, readable status output

## Installation

```
git clone https://github.com/whoisowl/uptime-pinger.git
cd uptime-pinger
pip install -r requirements.txt
```

## Usage

Run with default sites:

```
python uptime_pinger.py
```

Check specific sites:

```
python uptime_pinger.py --url https://google.com --url https://github.com
```

Custom check interval:

```
python uptime_pinger.py --interval 30
```

Stop monitoring anytime with `Ctrl+C`.

## Built With

- Python
- requests
- argparse

## License

MIT License

---

# 🇮🇷 فارسی

## معرفی

**Uptime Pinger** یک ابزار خط فرمان (CLI) است که با زبان **Python** توسعه داده شده و به‌صورت مداوم بررسی می‌کند آیا یک یا چند وب‌سایت آنلاین هستند یا نه.

### امکانات

- بررسی یک یا چند وب‌سایت به‌صورت هم‌زمان
- فاصله زمانی بررسی قابل تنظیم
- مدیریت مناسب سرورهای غیرقابل‌دسترس (timeout، خطای DNS)
- حالت مانیتورینگ مداوم (تا زمان توقف دستی اجرا می‌شود)
- خروجی واضح و خوانا

## نصب

```
git clone https://github.com/whoisowl/uptime-pinger.git
cd uptime-pinger
pip install -r requirements.txt
```

## اجرا

اجرا با سایت‌های پیش‌فرض:

```
python uptime_pinger.py
```

بررسی سایت‌های مشخص:

```
python uptime_pinger.py --url https://google.com --url https://github.com
```

فاصله زمانی دلخواه:

```
python uptime_pinger.py --interval 30
```

برای توقف مانیتورینگ، در هر زمان کلید `Ctrl+C` را بزنید.

## تکنولوژی‌های استفاده شده

- Python
- requests
- argparse

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.

---

## 👨‍💻 Author | توسعه‌دهنده

**Arian Salarian**

GitHub: https://github.com/whoisowl

⭐ If you found this project useful, consider giving it a star!

⭐ اگر این پروژه برایتان مفید بود، خوشحال می‌شوم به آن ستاره بدهید.