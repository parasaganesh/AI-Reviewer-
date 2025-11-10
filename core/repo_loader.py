import os
import subprocess
import shutil

def clone_repo(repo_url: str, base_dir: str = "data/repos") -> str:
    os.makedirs(base_dir, exist_ok=True)

    # derive a repo folder name
    clean_url = repo_url.rstrip("/")
    name = os.path.basename(clean_url)
    if name.endswith(".git"):
        name = name[:-4]

    dest = os.path.join(base_dir, name)

    # reuse existing clone if present
    if os.path.isdir(dest) and os.listdir(dest):
        return dest

    # If dest exists but empty, remove it (to avoid git failing)
    if os.path.isdir(dest) and not os.listdir(dest):
        shutil.rmtree(dest)

    try:
        subprocess.run(["git", "clone", repo_url, dest], check=True)
    except Exception as e:
        raise RuntimeError(f"Failed to clone repo: {repo_url}\n{e}")

    return dest
