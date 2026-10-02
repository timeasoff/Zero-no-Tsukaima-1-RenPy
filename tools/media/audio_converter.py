#!/usr/bin/env python3
"""
Конвертирует все аудиофайлы в текущей папке
в указанный формат, создавая дубликаты.

Требуется FFmpeg.
"""

import subprocess
import sys
from pathlib import Path


# ============================================================
# НАСТРОЙКИ
# ============================================================

# Формат, в который будут конвертироваться файлы.
# Например: "ogg", "mp3", "wav", "flac", "opus"
OUTPUT_FORMAT = "ogg"


# Поддерживаемые входные аудиоформаты
SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".ogg",
    ".oga",
    ".opus",
    ".m4a",
    ".aac",
    ".wma",
    ".aiff",
    ".aif",
    ".alac",
    ".amr",
    ".ac3",
    ".mka",
}


def convert_audio(input_path: Path, output_path: Path) -> bool:
    """Конвертирует один аудиофайл с помощью FFmpeg."""

    # Для OGG используем Vorbis.
    if OUTPUT_FORMAT.lower() == "ogg":
        codec_args = ["-c:a", "libvorbis", "-q:a", "5"]

    # Для Opus
    elif OUTPUT_FORMAT.lower() == "opus":
        codec_args = ["-c:a", "libopus", "-b:a", "128k"]

    # Для MP3
    elif OUTPUT_FORMAT.lower() == "mp3":
        codec_args = ["-c:a", "libmp3lame", "-q:a", "2"]

    # FLAC — lossless
    elif OUTPUT_FORMAT.lower() == "flac":
        codec_args = ["-c:a", "flac"]

    # WAV — PCM
    elif OUTPUT_FORMAT.lower() == "wav":
        codec_args = ["-c:a", "pcm_s16le"]

    else:
        # Для остальных форматов FFmpeg попробует выбрать
        # подходящий кодек автоматически.
        codec_args = []

    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-i", str(input_path),
        *codec_args,
        "-y",
        str(output_path),
    ]

    try:
        subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        return True

    except FileNotFoundError:
        print("❌ Ошибка: утилита 'ffmpeg' не найдена.")
        print()
        print("Установите FFmpeg:")
        print("  Windows: https://ffmpeg.org/download.html")
        print("  Ubuntu/Debian: sudo apt install ffmpeg")
        print("  macOS: brew install ffmpeg")
        sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка конвертации {input_path.name}")
        if e.stderr:
            print(e.stderr.strip())
        return False


def main():
    current_dir = Path(".")

    output_ext = "." + OUTPUT_FORMAT.lower().lstrip(".")

    # Собираем аудиофайлы
    files = [
        f for f in current_dir.iterdir()
        if f.is_file()
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
        and f.suffix.lower() != output_ext
    ]

    if not files:
        print("📂 В текущей папке не найдено аудиофайлов для конвертации.")
        return

    print(f"🎵 Формат назначения: {OUTPUT_FORMAT.upper()}")
    print(f"🖼 Найдено файлов: {len(files)}")
    print()

    success_count = 0
    skipped_count = 0

    for file in sorted(files):
        output = file.with_suffix(output_ext)

        # Если выходной файл уже существует — пропускаем
        if output.exists():
            print(f"⏭  Пропущен (уже существует): {output.name}")
            skipped_count += 1
            continue

        print(
            f"⏳ {file.name} → {output.name} ...",
            end=" ",
            flush=True
        )

        if convert_audio(file, output):
            orig_size = file.stat().st_size
            new_size = output.stat().st_size

            ratio = (
                (1 - new_size / orig_size) * 100
                if orig_size > 0
                else 0
            )

            print(f"✅ ({ratio:+.1f}%)")
            success_count += 1

        else:
            print("❌")

    print()
    print(
        f"🎉 Готово! "
        f"Конвертировано: {success_count}, "
        f"пропущено: {skipped_count}, "
        f"всего: {len(files)}"
    )


if __name__ == "__main__":
    main()
