#!/usr/bin/env python3
"""
Конвертирует все изображения в текущей папке в формат WebP (lossless)
с помощью утилиты cwebp.
"""

import os
import subprocess
import sys
from pathlib import Path

# Поддерживаемые расширения
SUPPORTED_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".gif", ".webp"
}


def convert_to_webp(input_path: Path, output_path: Path) -> bool:
    """Конвертирует один файл в WebP с помощью cwebp."""
    cmd = ["cwebp", str(input_path), "-lossless", "-o", str(output_path)]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except FileNotFoundError:
        print("❌ Ошибка: утилита 'cwebp' не найдена.")
        print("   Установите: sudo apt install webp  (Ubuntu/Debian)")
        print("               brew install webp      (macOS)")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка конвертации {input_path.name}: {e.stderr.strip()}")
        return False


def main():
    current_dir = Path(".")

    # Собираем файлы для конвертации
    files = [
        f for f in current_dir.iterdir()
        if f.is_file()
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
        and f.suffix.lower() != ".webp"   # пропускаем уже webp
    ]

    if not files:
        print("📂 В текущей папке не найдено изображений для конвертации.")
        return

    print(f"🖼  Найдено файлов: {len(files)}\n")

    success_count = 0
    for file in sorted(files):
        output = file.with_suffix(".webp")

        # Пропускаем, если выходной файл уже существует
        if output.exists():
            print(f"⏭  Пропущен (уже существует): {output.name}")
            continue

        print(f"⏳ {file.name} → {output.name} ...", end=" ", flush=True)

        if convert_to_webp(file, output):
            # Показываем размер до/после
            orig_size = file.stat().st_size
            new_size = output.stat().st_size
            ratio = (1 - new_size / orig_size) * 100 if orig_size > 0 else 0
            print(f"✅ ({ratio:+.1f}%)")
            success_count += 1
        else:
            print("❌")

    print(f"\n🎉 Готово! Успешно конвертировано: {success_count}/{len(files)}")


if __name__ == "__main__":
    main()
