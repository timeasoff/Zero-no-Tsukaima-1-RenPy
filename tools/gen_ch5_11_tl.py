# -*- coding: utf-8 -*-
"""Generate the six S11 translation buckets from the script and JA voice ids."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "game/chapters/5/script-ch5_11.rpy"
SOURCE = ROOT / "ps2_source/chapters/chapter_06_本当の想い.txt"
CSV = ROOT / "transcriptions_ja_ru.csv"

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def source_voice_rows():
    rows = {}
    for block in re.finditer(r"---- SCENE (\d+) ----(.*?)(?=---- SCENE \d+ ----|\Z)", SOURCE.read_text(encoding="utf-8"), re.S):
        scene, body = int(block.group(1)), block.group(2)
        pending = []
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("[") or line.startswith("→") or line.startswith("#"):
                pending = []
                continue
            vm = re.search(r"\[voice (\d+)\]\s*$", line)
            if vm:
                text = re.sub(r"\s*\[voice \d+\]\s*$", "", line)
                pending.append(text)
                text = "".join(pending)
                text = re.sub(r"^[^：]+：", "", text)
                rows[int(vm.group(1))] = (scene, text)
                pending = []
            else:
                pending.append(line)
    return rows

def csv_rows():
    out = {}
    with CSV.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh):
            if not row or row[0].startswith("#") or not row[0].startswith("VOICE_ID.BIN_"):
                continue
            try:
                ident = int(row[0].split("_")[-1].split(".")[0], 16)
            except ValueError:
                continue
            out[ident] = row
    return out

def script_rows():
    text = SCRIPT.read_text(encoding="utf-8")
    dialogs, thoughts, choices = [], [], []
    for line in text.splitlines():
        m = re.match(r'^\s*(?!th\b)(?:[a-z]+) "(.*)"$', line)
        if m:
            val = m.group(1)
            marker = re.search(r"\{#ch5_11_v(\d+)\}$", val)
            if marker:
                dialogs.append((val, int(marker.group(1))))
            continue
        m = re.match(r'^\s*th "(.*)"$', line)
        if m:
            thoughts.append(m.group(1))
            continue
        m = re.match(r'^\s{8}"(.*)":$', line)
        if m:
            choices.append(m.group(1))
    return dialogs, thoughts, choices

RU_MANUAL = {
    348: "Это вы, моё фамильярное существо? Войдите.",
    351: "Вы действительно очень мне помогли. Я собираюсь поблагодарить всех, но хотела кое о чём спросить и вас, мой фамильяр.",
    352: "Скажите честно: насколько искренним было ваше признание в пьесе?",
    353: "Только не говорите, что хотите, чтобы я это забыла.",
    354: "…",
    356: "…",
    358: "…",
    359: "Я подумаю, разрешать ли это.",
    360: "Я получила ответ, который меня удовлетворил. Теперь я смогу без сожалений вернуться в замок.",
    361: "Да. В следующий раз я буду уже королевой…",
    362: "Я возвращаюсь в замок, на сцену политики, дипломатии и войны…",
    363: "В отличие от сцены, вся кровь, которая там прольётся, будет настоящей…",
    364: "Основатель, молю, даруй мне удачу…",
    1661: "Всё закончилось…",
    1663: "Да ничего, просто немного предалась воспоминаниям.",
    1664: "…Праздничная суматоха наших дней на сцене наконец закончилась.",
    1665: "Я никогда не была в окружении такого количества людей, поэтому волновалась.",
    1666: "…Сначала я изо всех сил представляла зрителей картошкой.",
    1667: "Но было весело.",
    1668: "Атмосфера на сцене и правда необычная.",
    1669: "Хи-хи.",
    1670: "Ну, насчёт этого… Видишь ли… На самом деле…",
    1671: "В моей сумке была фотография. Я очень не хотела её потерять.",
    1672: "…Нет.", 1673: "Э-это фотография тебя, Хирага-кун…",
    1674: "…Нет. Похожа, но это другое.", 1675: "Э-это фотография тебя, Хирага-кун…",
    1676: "…!!!", 1677: "К-как ты догадался?!", 1678: "Да. Вот.",
    1679: "К-какая разница, что на это отвечать?!",
    1680: "Это секрет только между мной и Хирага-куном, хорошо?",
    1681: "Хи-хи-хи…",
    2808: "…Что случилось, дорогой?", 2809: "…Ну правда… Ты весь в своём духе.",
    2810: "Ладно. Сегодня я тебя прощаю.", 2811: "Правда?",
    2812: "Хорошо, я тебя сегодня прощаю.", 2813: "…Дорогой.",
    2814: "Хорошо, я тебя сегодня прощаю.",
    2815: "Но я всё равно завидую любви, которая сжигает и тело, и душу.",
    2816: "Тебе так не кажется, дорогой?",
    4740: "П-правда?", 4741: "Правда?", 4742: "Э-это что ещё за вопрос?",
    4743: "Только одежда?", 4744: "Хм. Тогда почему ты на меня не смотришь?",
    4745: "О, тебе неловко? Как странно… Великий Сайто смущается.", 4746: "Хи-хи. Хорошо.",
    8676: "Мм?", 8709: "Харуна, вот ты где.", 8710: "Что ты здесь делаешь?",
    8711: "…Да.", 8712: "О, я тоже так делал.", 8713: "Да, и правда…",
    8714: "Но мы действительно справились, да?", 8715: "Зато у тебя была веская причина: вернуть сумку.",
    8716: "Фотография домашнего питомца?", 8717: "Может, фотография твоего парня?",
    8718: "Моя фотография?", 8719: "…А? Моя?", 8720: "О, это и правда я.",
    8721: "П-подожди, что?!", 8722: "П-почему у тебя в сумке моя фотография?",
    8723: "А, ну конечно. Понял.", 8724: "…Принцесса, вы здесь?", 8725: "П-простите, я войду…",
    8726: "…А?", 8727: "…Э-э, принцесса?", 8728: "…Что?", 8729: "Что такое?",
    8730: "Принцесса, это…", 8731: "Я говорил серьёзно.",
    8732: "…Но если вы спрашиваете, насколько, я не могу ответить. Вы спрашиваете, где начинается ложь.",
    8733: "…Не думаю, что я лгал. Наверное.", 8734: "Это были не просто слова из пьесы.",
    8735: "Тогда я видел в принцессе Ноэль и игравшую её актрису одно и то же лицо.",
    8736: "Поэтому моё признание было одновременно и репликой из пьесы, и моими собственными словами.",
    8737: "Не знаю.", 8738: "Тогда нас с принцессой закружил водоворот пьесы.",
    8739: "Но теперь, когда я успокоился, я всё ещё могу произнести эту клятву.",
    8740: "А… Конечно, если принцесса позволит.", 8741: "Мы ещё увидимся?", 8742: "Понял.",
    14275: "Домой?", 14276: "Простите.", 14277: "Гамбургер…?",
    14278: "Думаю, такое я смогу приготовить. Сделать в следующий раз?", 14279: "Да, будете ждать.",
    14280: "Посмотрим… Я слышала, что вы едите чёрную бумагу и сырую рыбу.",
    14281: "Во всяком случае, мне говорили, что у вас странные привычки в еде.",
    14282: "Я хотела бы побывать в вашей стране, Сайто-сан.", 14283: "Хи-хи… На здоровье.",
    15306: "Будешь чай?", 15307: "Было трудно.", 15308: "Так сильно двигаться и кричать… Для меня это впервые.",
    15309: "Но ничего плохого.", 15310: "Хороший опыт.", 15311: "Всё когда-нибудь проходит.",
    15312: "И радость, и боль проходят. Главное — понимать этот момент.", 15313: "Да.",
    15314: "Но если посмотреть иначе, до сегодняшнего дня мы жили в особенном времени.",
    15315: "…Можно кое о чём спросить?", 15316: "О твоём признании в пьесе.",
    15317: "Раньше ты уклонился от ответа.", 15318: "Все живут, нося какую-нибудь маску.",
    15319: "Я думала, что в пьесе надевают видимую маску и создают вымышленный мир на сцене.",
    15320: "Так я и думала.", 15321: "Но во время этой пьесы я кое-что почувствовала.",
    15322: "Возможно, от этих масок и вымысла что-то возвращается обратно.", 15323: "Поэтому я хочу знать.",
    15324: "Насколько ты был искренен? Или всё это было игрой?", 15325: "Понятно.",
    15326: "Слово «наверное» можно убрать.", 15327: "Я порекомендую хорошую больницу.",
    15328: "Если ты больше не можешь снять маску, это болезнь. И очень страшная.", 15329: "Правда?",
    15330: "Я?", 15331: "Несправедливо отвечать вопросом на вопрос. Я не могу ответить.",
    15332: "Мм.", 15333: "Понятно. Наверное, у меня так же.", 15334: "Но я рада, что спросила.",
    15335: "Хорошо.",
}

# Exact-id translations already reviewed in the project queue are allowed only
# as a temporary source for ordinary lines; obvious ASR artefacts are listed
# here so they cannot silently enter the bucket.
RU_MANUAL.update({
    8667: "А, вот ты где.", 8668: "Д-да, пожалуйста.",
    8669: "Кстати о пьесе… Тяжело пришлось, да?", 8670: "Как именно?",
    8671: "…Похоже, было нелегко.", 8672: "Понятно. Рад, что ты так считаешь, Табита.",
    8673: "Но теперь всё наконец… действительно закончилось, да?", 8674: "Всё проходит, да…",
    8675: "Да. Значит, сегодня заканчиваются наши особенные дни.", 8677: "Ну, это…",
    8678: "Прости.", 8679: "Э-э… Табита?", 8680: "Хм… Вот как?",
    8681: "Не знаю. Если честно, я не думал об этом настолько глубоко.",
    8682: "…Но я не могу сказать, где это началось и где закончилось.",
    8683: "Не думаю, что обнял тебя из-за какой-то маски или потому, что мы играли. Наверное.",
    8684: "Может быть, я имел в виду всё это.", 8685: "Э-эй, подожди!",
    8686: "Может быть, я и правда что-то чувствовал как герой…",
    8687: "Но я уверен, что тогда это были и мои чувства…", 8688: "Н-наверное. Но я говорю о том, что чувствовал тогда.",
    8689: "Т-Табита, а ты?!", 8690: "Что ты почувствовала, когда услышала тогда моё признание?!",
    8691: "Тогда не спрашивай меня.", 8692: "Могу сказать только, что это было не просто игрой.",
    8693: "Я тут весь вспотел. В следующий раз хотя бы предупреди меня.",
    8704: "Стой! Стой, Кирхе!", 8705: "Э-э… Я не это имел в виду…",
    8706: "Д-да.", 8707: "Правда…", 8708: "Нет.",
    8658: "Я хочу вернуться домой.", 8659: "Да. От этой еды я вспомнил о нём.",
    8660: "Тебе не за что извиняться, Сиеста.", 8661: "Мне бы сейчас гамбургер.",
    8662: "Да. Панировочные сухари, соль, фарш, лук… Всё это смешивают, а потом жарят.",
    8663: "Правда?", 8664: "А о другой еде ничего не расскажешь?",
    8665: "Если бы ты побывала в моей стране, то очень удивилась бы.", 8666: "Спасибо за угощение. Было очень вкусно.",
})

THOUGHTS = {
    "What kind of photo could it be?": "（Что это может быть за фотография?）",
    "…That would make me really jealous.": "（…Я бы ужасно ревновал.）",
    "…As if that could be it!": "（…Да с чего бы это!）",
    "I-it is true… She kept a picture of me in her bag.": "（П-правда… Она хранила в сумке мою фотографию.）",
    "Whoa… It did not bother me before, but now that I have noticed it… I am getting embarrassed.": "（Ого… Раньше меня это не беспокоило, но теперь, когда я заметил… Мне становится неловко.）",
    "…Come on. Why is the princess wearing the queen's formal dress in a room like this?!": "（…Да ладно. Почему принцесса в такой комнате носит парадное платье королевы?!）",
    "…That is right. Once the play is over, the princess has to return to the castle.": "（…Точно. Когда пьеса закончилась, принцессе нужно вернуться в замок.）",
    "Maybe the time she spent onstage was what she treasured most.": "（Возможно, дороже всего для неё было время на сцене.）",
    "……… …… …": "（……… …… …）",
    "I should not have refused here, should I?": "（Не стоило мне здесь отказывать, да?）",
}

CHOICES = {
    "I do not know.": "Не знаю.", "I meant all of it!": "Я всё это имел в виду!", "What about you, Tabitha?": "А ты, Табита?",
    "A picture of a pet?": "Фотография домашнего питомца?", "A picture of her boyfriend?": "Фотография её парня?", "A picture of me?": "Моя фотография?",
    "I meant it.": "Я говорил серьёзно.", "It was not just acting.": "Это были не просто слова из пьесы.",
}

def write(path, lang, rows):
    lines = [f"translate {lang} strings:", "# ===== ch5.11 ====="]
    for old, new in rows:
        lines += ["", f'    old "{esc(old)}"', f'    new "{esc(new)}"']
    lines.append("# ===== end ch5.11 =====")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    voice = source_voice_rows(); trans = csv_rows(); dialogs, thoughts, choices = script_rows()
    ja, ru = [], []
    for old, ident in dialogs:
        if ident not in voice:
            raise SystemExit(f"missing JA voice {ident}")
        new_ja = voice[ident][1].replace("\n", "")
        row = trans.get(ident)
        # Lookup is by the authoritative voice id, never by line position.
        # Manual corrections above override the transcription queue where its
        # rough ASR translation is unsuitable for the scene.
        if ident in RU_MANUAL:
            new_ru = RU_MANUAL[ident]
        elif row and len(row) > 2 and row[2].strip():
            new_ru = row[2]
        else:
            raise SystemExit(f"missing RU by exact voice id {ident}: {old}")
        if not new_ru:
            raise SystemExit(f"missing RU voice {ident}: {old}")
        ja.append((old, new_ja)); ru.append((old, new_ru))
    for old in thoughts:
        ja.append((old, ""))
        ru.append((old, THOUGHTS[re.sub(r"\{#.*", "", old)]))
    for old in choices:
        ja.append((old, "")); ru.append((old, CHOICES[re.sub(r"\{#.*", "", old)]))
    # JA non-voice strings are taken from the event source, keyed by the exact English menu/thought text.
    source = SOURCE.read_text(encoding="utf-8")
    ja_map = {
        "What kind of photo could it be?": "どんな写真なんだろう？", "…That would make me really jealous.": "……恋人の写真だったら、嫉妬するな。", "…As if that could be it!": "……そんなわけないだろ！",
        "I-it is true… She kept a picture of me in her bag.": "本当だ……。春奈は俺の写真をバッグに入れていた。", "Whoa… It did not bother me before, but now that I have noticed it… I am getting embarrassed.": "うわ……。前は気にならなかったけど、気づいてみると……恥ずかしくなってきた。",
        "…Come on. Why is the princess wearing the queen's formal dress in a room like this?!": "……っていうか、なんでこんな部屋でお姫さまが女王の正装を着てるんだ！？", "…That is right. Once the play is over, the princess has to return to the castle.": "……そうだ。劇が終われば、お姫さまは城へ帰らなきゃならない。", "Maybe the time she spent onstage was what she treasured most.": "舞台に立っていた時間が、姫にとって一番大切だったのかもしれない。", "……… …… …": "……… …… …", "I should not have refused here, should I?": "ここは断っちゃいけなかったんだよな？",
    "I do not know.": "分からない", "I meant all of it!": "全部、本気！", "What about you, Tabitha?": "タバサはどうなんだ？", "A picture of a pet?": "ペットの写真？", "A picture of her boyfriend?": "恋人の写真？", "A picture of me?": "俺の写真？", "I meant it.": "本気です", "It was not just acting.": "ただの芝居ではありません",
    "I meant all of it!": "全部、本気！",
}
    for i, (old, _) in enumerate(ja):
        key = re.sub(r"\{#.*", "", old)
        if not _:
            ja[i] = (old, ja_map[key])
    base = ROOT / "game/tl"
    write(base / "japanese/ch5_11_dialogs.rpy", "japanese", ja[:len(dialogs)])
    write(base / "japanese/ch5_11_thoughs.rpy", "japanese", ja[len(dialogs):len(dialogs)+len(thoughts)])
    write(base / "japanese/ch5_11_choises.rpy", "japanese", ja[-len(choices):])
    write(base / "russian/ch5_11_dialogs.rpy", "russian", ru[:len(dialogs)])
    write(base / "russian/ch5_11_thoughs.rpy", "russian", ru[len(dialogs):len(dialogs)+len(thoughts)])
    write(base / "russian/ch5_11_choises.rpy", "russian", ru[-len(choices):])
    print(f"generated dialogs={len(dialogs)} thoughts={len(thoughts)} choices={len(choices)} voices={len(voice)}")

if __name__ == "__main__": main()
