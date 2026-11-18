#!/usr/bin/env python3
"""Chapter 27 part 3 (scenes 994-998): Louise's fleet, Akina captured."""
import json, sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
295: ("...How's that!?", "…Как тебе этого!?"),
296: ("It seems to be working well, partner. She's reeling now.",
     "Похоже, сработало хорошо, приятель. Она уже шатается."),
297: ("I see...", "Понятно…"),
298: ("(Now, if we can just secure Haruna's body...)", "Теперь бы только заполучить тело Харуны…"),
299: ("Hey, Louise. I don't know what spell you're chanting, but are you done yet?",
     "Эй, Луиза. Не знаю, какое заклинание ты читаешь, но ты уже закончила?"),
300: ("......", "……"),
301: ("...I can't answer while chanting, can I? But something's coming into view at the edge of the sky...",
     "Ты не можешь отвечать во время чтения, да? Но у края неба что-то появляется…"),
302: ("That must be the Reconquista air fleet, I suppose...", "Должно быть, это воздушный флот Реконкисты…"),
303: ("And from it, countless dragon riders will pour out—and cover this Tristain sky completely.",
     "И из него вылетят бесчисленные драконы-всадники — и покроют всё небо Тристании."),
304: ("Damn... Losing to these guys...", "Чёрт… Проиграть этим…"),
305: ("But wait. Right now, this city will be surrounded by Reconquista's forces!",
     "Но погоди. Сейчас этот город будет окружён войсками Реконкисты!"),
306: ("...", "…"),
307: ("Louise—are you done yet?", "Луиза — ты уже закончила?"),
308: ("...!!", "…!!"),
309: ("Eh? Ehh!? What's happening!?", "А? А-а!? Что происходит!?"),
310: ("Wha—what's this? The sky's filled with countless battleships!?",
     "Что—что это? Небо полно бесчисленных боевых кораблей!?"),
311: ("L-Louise...? What did you do!?", "Л-Луиза…? Что ты сделала!?"),
312: ("Wha—what!? What did you people do!?", "А—что!? Что вы сделали!?"),
313: ("What do you mean, what? Don't you see? It's as you see.",
     "Что значит «что»? Не понимаешь? Всё, как ты видишь."),
314: ("As I see it... Surely not—that many reinforcements...", "Как я вижу… Неужто — столько подкреплений…"),
315: ("You mean that Louise summoned them!?", "Ты хочешь сказать, что это вызвала Луиза!?"),
316: ("Well? Isn't Louise's magic amazing?", "Ну что? Разве магия Луизы не удивительна?"),
317: ("After all—Louise is... my mistress!", "В конце концов — Луиза это… моя госпожа!"),
318: ("Ah, that noble girl is a legend, isn't she? Just like me and my partner here.",
     "Ах, та дворянка — легенда, да? Такая же, как я и вот этот мой приятель."),
319: ("Legend...?", "Легенда…?"),
320: ("All right—caught her. Really made me work for it.", "Ладно — поймал. Ну и хлопот же она мне доставила."),
321: ("...", "…"),
322: ("Tabitha...", "Табаса…"),
323: ("Please—don't hand her over to Gallia.", "Прошу — не отдавай её Галлии."),
324: ("...", "…"),
325: ("But if you don't hand her over, things will get difficult for you too, won't they?",
     "Но если не отдашь, у тебя самой будут проблемы, да?"),
326: ("Mm.", "Мм."),
327: ("What should we do...", "Что же нам делать…"),
328: ("Surely the problem is what Akina did, not Haruna...", "Наверное, проблема в том, что сделала Акина, а не Харуна…"),
329: ("Ah.", "Ах."),
330: ("...I'll leave it to Tabitha's judgment.", "…Я предоставлю это решению Табасы."),
331: ("Is that all right?", "Это нормально?"),
332: ("Tabitha has her own circumstances, doesn't she?", "У Табасы свои обстоятельства, да?"),
333: ("...Mm.", "…Мм."),
334: ("Even so—poor Haruna. To end up like this because of a separate personality...",
     "И всё же — бедная Харуна. Из-за отдельной личности оказаться в таком положении…"),
335: ("Separate personality... Separate...", "Отдельная личность… Отдельная…"),
336: ("Haruna is innocent, but Akina isn't...", "Харуна невиновна, но Акина…"),
337: ("Hmm... I suppose she has the guilt of being the bomber, doesn't she?",
     "Хм… Наверное, на ней вина… да ладно"),
338: ("Yes—Akina... Ah.", "Да — на Акине… Ах."),
339: ("Hmm? What's wrong?", "Хм? Что случилось?"),
340: ("It's nothing.", "Ничего."),
341: ("So—what do you intend to do with Haruna yourself, Tabitha?", "Так — а что ты сама намерена сделать с Харуной, Табаса?"),
342: ("I've decided.", "Я решила."),
343: ("Eh, now!?", "А, сейчас!?"),
344: ("Mm. Now.", "Мм. Сейчас."),
345: ("(Haruna... What are you planning to do...?)", "Харуна… Что же ты собираешься сделать…?"),
}
CHOICES = {
994: [("Don't hand her to Gallia", "Не отдавать Галлии"),
      ("Leave it to Tabitha", "Поручить Табасе"),
      ("Haruna is innocent, but...", "Харуна невиновна, но…")],
}
SPK = {'サイト': 's', 'デルフリンガー': 'd', 'キュルケ': 'k', 'ルイズ': 'l',
       'アキナ': 'ak', 'タバサ': 't', 'null': 'th'}
START = {'s': 124, 'd': 0, 'k': 39, 'l': 66, 'ak': 7, 't': 41, 'th': 0}


def main():
    data = json.load(open('reports/ch27/parse_972_998.json', encoding='utf-8'))
    script = ['# Глава 27, часть 3 (сцены 994–998): флот Луизы, пленение Акины.',
              '# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 994-998).',
              '', 'label ch27_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] < 994: continue
            scene = x['no']
            script += ['label ch27_3_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene: event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if idx not in T: continue
            en, ru = T[idx]
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch27_%s_%03d' % (spk, counters[spk])
            full = '%s{#%s}' % (en, tag)
            script.append('    # ' + x['src'])
            if x['voice'] is not None:
                script.append('    voice "%s"' % tag)
                manifest.append((tag, x['voice']))
            script.append('    %s "%s"' % (spk, full))
            ja_new = x['ja'] if x['thought'] else '%s：%s' % (x['speaker'], x['ja'])
            ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
            ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'choice':
            if scene is None or scene not in CHOICES: continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch27_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch27_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 994 <= scene <= 998: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch28')
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 27 ====', '    jump ch28', '    return', '']
    files = {
        'game/chapters/27/script-ch27_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch27_3_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch27_3_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch27_3_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch27_3_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch27/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
