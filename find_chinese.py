import os

def has_chinese(text):
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def find_files_with_chinese(root_dir):
    files_with_chinese = []
    exclude_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'dist', 'build'}
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.vue', '.md', '.json', '.html', '.css', '.env', '.ts', '.tsx')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if has_chinese(content):
                            files_with_chinese.append(file_path)
                except Exception:
                    pass
    return files_with_chinese

if __name__ == "__main__":
    root = r"f:\Courses\AIExperiments\MiroFish"
    found_files = find_files_with_chinese(root)
    found_files = [f for f in found_files if "find_chinese.py" not in f]
    with open("found_chinese_files.txt", "w", encoding="utf-8") as out:
        for f in found_files:
            out.write(f + "\n")
    print(f"Found {len(found_files)} files.")
