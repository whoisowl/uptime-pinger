#!/usr/bin/env python3
"""
Uptime Pinger
-------------
Checks whether one or more websites are online, on a repeating interval.

Usage examples:
    python3 uptime_pinger.py
    python3 uptime_pinger.py --url https://google.com --url https://github.com
    python3 uptime_pinger.py --interval 30
"""

import argparse
import requests
import time

DEFAULT_URLS = ["https://google.com", "https://github.com"]


def check_site(url):
    """Checks a single URL and returns a human-readable status string."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"{url} is UP"
        else:
            return f"{url} is DOWN (status code: {response.status_code})"
    except requests.exceptions.RequestException:
        return f"{url} is DOWN (no response)"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Repeatedly check whether websites are online."
    )
    parser.add_argument("--url", action="append", dest="urls",
                         help="A URL to monitor. Can be used multiple times. "
                              "If omitted, checks a default list of sites.")
    parser.add_argument("--interval", type=int, default=10,
                         help="Seconds to wait between checks (default: 10)")
    return parser.parse_args()


def main():
    args = parse_args()
    urls = args.urls if args.urls else DEFAULT_URLS

    try:
        while True:
            for url in urls:
                print(check_site(url))
            print(f"Waiting {args.interval} seconds before next check...\n")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped monitoring.")


if __name__ == "__main__":
    main()