import json
import os
import platform

from browsers.base import Browser
from util.is_browser_present import (is_browser_present_linux,
                                     is_browser_present_mac,
                                     is_browser_present_windows)
from util.log import logger as log


class GoogleChromeStable(Browser):
    def __init__(self) -> None:
        super().__init__("google-chrome-stable")

    def is_installed(self) -> bool:
        log.info("Checking if Google Chrome Stable is installed.")
        os_name = platform.system()
        match os_name:
            case "Linux":
                log.debug("Detected OS: Linux")
                result = is_browser_present_linux(self.name)
            case "Windows":
                log.debug("Detected OS: Windows")
                result = is_browser_present_windows(self.name)
            case "Darwin":
                log.debug("Detected OS: macOS")
                result = is_browser_present_mac(self.name)
            case _:
                log.error(f"Unsupported OS: {os_name}")
                return False
        if result:
            log.success("Google Chrome Stable is installed.")
        else:
            log.warning("Google Chrome Stable is not installed.")
        return result

    def get_bookmarks(self, profiles=["Default"]) -> list[dict]:
        log.info("Fetching bookmarks from Google Chrome Stable.")
        os_name = platform.system()
        all_bookmarks = []

        for profile in profiles:
            log.debug(f"Processing profile: {profile}")
            match os_name:
                case "Linux":
                    log.debug("Detected OS: Linux")
                    path = os.path.expanduser(
                        f"~/.config/google-chrome/{profile}/Bookmarks"
                    )
                case "Windows":
                    log.debug("Detected OS: Windows")
                    path = os.path.expandvars(
                        rf"%LOCALAPPDATA%\Google\Chrome\User Data\{profile}\Bookmarks"
                    )
                case "Darwin":
                    log.debug("Detected OS: macOS")
                    path = os.path.expanduser(
                        f"~/Library/Application Support/Google/Chrome/{profile}/Bookmarks"
                    )
                case _:
                    log.error(f"Unsupported OS: {os_name}")
                    return []

            log.debug(f"Resolved bookmark file path: {path}")

            if not os.path.exists(path):
                log.warning(
                    f"Bookmarks file does not exist for profile '{profile}' at path: {path}"
                )
                continue

            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    log.success(
                        f"Successfully loaded bookmarks file for profile '{profile}'."
                    )
                    bookmarks = self.extract_bookmarks(data)
                    all_bookmarks.extend(bookmarks)
            except json.JSONDecodeError:
                log.error(
                    f"Failed to parse bookmarks file for profile '{profile}': JSON decode error."
                )
            except OSError as e:
                log.error(f"Error reading bookmarks file for profile '{profile}': {e}")

        log.info(
            f"Collected {len(all_bookmarks)} bookmark(s) from {len(profiles)} profile(s)."
        )
        return all_bookmarks

    def extract_bookmarks(self, data: dict) -> list[dict]:
        log.debug("Extracting bookmarks from JSON structure.")
        results = []

        def walk(node):
            if isinstance(node, dict):
                if node.get("type") == "url":
                    log.debug(
                        f"Found bookmark: {node.get('name')} -> {node.get('url')}"
                    )
                    results.append({"name": node.get("name"), "url": node.get("url")})
                elif node.get("children"):
                    for child in node["children"]:
                        walk(child)

        roots = data.get("roots", {})
        log.debug(f"Found roots: {list(roots.keys())}")
        for root_name, root in roots.items():
            log.debug(f"Walking through root: {root_name}")
            walk(root)

        log.info(f"Extracted {len(results)} bookmark(s) in total.")
        return results


# TODO: Implement other versions of Google Chrome.
# Example: GoogleChromeBeta and GoogleChromeNightly etc
