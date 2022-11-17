# file_finder.py
import os


def findall_files(main_dir: str) -> list:
    collector = []

    for root, dirs, files in os.walk(main_dir):
        collector.extend([os.path.join(root, f) for f in files])

    return collector


def findall_subdirs(main_dir: str) -> list:
    collector = []

    for root, dirs, files in os.walk(main_dir):
        collector.extend(os.path.join(root, d) for d in dirs)

    return collector
