""" 
Summary: 
    Delete empty folders recursively, including empty parent directories
Description:
    Found in this helpful stackoverflow answer https://stackoverflow.com/a/65624165
"""
import os

def delete_empty_folders(root):
    """Delete empty folders and empty folder structures recursively"""
    deleted = set()
    for current_dir, subdirs, files in os.walk(root, topdown=False):
        still_has_subdirs = any(
            subdir
            for subdir in subdirs
            if os.path.join(current_dir, subdir) not in deleted
        )
        if not any(files) and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted.add(current_dir)

    return deleted
