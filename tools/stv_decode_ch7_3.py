# -*- coding: utf-8 -*-
"""Декодирование STV → wav для части 3 главы 7 (голоса 9167-9188 сцены дат).

Нужные id лежат в STV-архиве:
  D:\\gameMake\\ZnT-1\\ZNT_DECODING\\PS2_GAME\\OriginalFiles\\decoding\\unpacked\\VOICE_ID.BIN\\
  файлы вида VOICE_ID.BIN_000023CF.STV

vagstream-конфиг (.stv.txth) уже лежит в той же папке; vgmstream-cli
подхватывает его автоматически рядом с исходником.

Выход: wav_files/VOICE_ID.BIN_%08X.wav (имена в манифесте — как у прочих
s-голосов ch7.2: без префикса имени говорящего).

Запуск: python tools/stv_decode_ch7_3.py [--check]
  без --check декодирует 22 файла (существующие перезаписываются только
  если размер источника изменился — здесь пропускаются),
  --check — только сверка наличия.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = (u"D:\\gameMake\\ZnT-1\\ZNT_DECODING\\PS2_GAME\\OriginalFiles"
           u"\\decoding\\unpacked\\VOICE_ID.BIN")
WAV_DIR = os.path.join(ROOT, "wav_files")
VGM = r"C:\\tools\\vgmstream-win64\\vgmstream-cli.exe"

# 9167..9188 (0x23CF..0x23E4) — голоса Сайто в дат-сценах 1169-1173
IDS = list(range(9167, 9189))


def main():
    check_only = "--check" in sys.argv[1:]
    missing = []
    for vid in IDS:
        hexa = u"VOICE_ID.BIN_%08X" % vid
        stv = os.path.join(SRC_DIR, hexa + u".STV")
        wav = os.path.join(WAV_DIR, hexa + u".wav")
        if not os.path.isfile(stv):
            missing.append(u"нет STV: %s" % stv)
            continue
        if os.path.isfile(wav) and os.path.getsize(wav) > 0:
            continue
        if check_only:
            missing.append(u"нет wav: %s" % wav)
            continue
        # vgmstream: пишет wav (имя цели с .wav-расширением)
        cmd = [VGM, "-o", wav, stv]
        p = subprocess.call(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        if p != 0 or not os.path.isfile(wav) or os.path.getsize(wav) == 0:
            print(u"FAIL decode %s" % hexa)
            return 1
        print(u"OK %s -> %s" % (hexa, os.path.basename(wav)))
    if missing:
        print(u"MISSING:")
        for m in missing:
            print(u"  " + m)
        return 2
    print(u"RESULT: OK (%d файлов)" % len(IDS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
