#!/usr/bin/env python3
"""Chapter 28 part 2 (scene 1008): Haruna leaves, the final day."""
import json, sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
131: ("Eh? What do you mean, becoming independent?", "А? Что значит — стать самостоятельной?"),
132: ("Yeah. I can't stay at this academy forever... It'd be wrong to keep relying on Louise and the others.",
      "Да. Я не могу вечно оставаться в академии… Не знаю, правильно ли всё время полагаться на Луизу и остальных."),
133: ("If you say that, I've been taken care of by this academy ever since Louise summoned me.",
      "Если так, то меня опекает эта академия с тех пор, как Луиза меня призвала."),
134: ("Hiraga-kun is Louise-san's familiar. Of course you're taken care of. But I'm not one, so...",
      "Хирага-кун — фамильяр Луизы-сан. Вам и положено. А я нет, поэтому…"),
135: ("I know, but... We're probably the only two Japanese people in this world.",
      "Я знаю, но… Мы, наверное, единственные японцы в этом мире."),
136: ("And we're not exactly strangers to each other... So if we worked at the academy, maybe...",
      "И мы не совсем чужие друг другу… Так что, если бы мы работали в академии, может…"),
137: ("The thing is, Hiraga-kun... I've been scouted.", "Дело в том, Хирага-кун… Меня завербовали."),
138: ("S-Scouted for what?", "З-Завербовали — куда?"),
139: ("A theater troupe, a theater troupe.", "В театральную труппу, в труппу."),
140: ("A theater troupe? You mean Weatherly's?", "Труппу? Ты имеешь в виду труппу Уэзерби?"),
141: ("No. Someone from another troupe who saw that play liked me and scouted me.",
      "Нет. Кто-то из другой труппы, кто смотрел тот спектакль, меня и завербовал."),
142: ("Now's a good chance, so I've decided to join that troupe.",
      "Сейчас как раз удобный случай, и я решила присоединиться к этой труппе."),
143: ("But if you join a troupe, you'll have to perform in other towns, won't you?",
      "Но если ты в труппе, тебе придётся выступать в других городах, да?"),
144: ("Yeah. I probably won't get to see Hiraga-kun very often anymore.",
      "Да. Наверное, мы с Хирага-куном будем видеться реже."),
145: ("But I'm looking forward to it. I get to see all sorts of towns in this world.",
      "Но я с нетерпением жду. Я смогу объездить разные города этого мира."),
146: ("Maybe I'll even find a clue to get back to Japan.", "Может, я даже найду ключ к дороге в Японию."),
147: ("I see. Yeah, that's right.", "Понятно. Да, верно."),
148: ("So, Hiraga-kun... If you don't mind, cheer me on, okay?",
      "Так что, Хирага-кун… Если не против, поддержи меня, ладно?"),
149: ("Of course I will! And let's both do our best to find a way back to Japan!",
      "Конечно! И давай вместе постараемся найти способ вернуться в Японию!"),
150: ("Mm!", "Мм!"),
151: ("Say, Louise... Why didn't Tabitha hand Haruna over to Gallia?",
      "Слушай, Луиза… Почему Табаса не передала Харуну Галлии?"),
152: ("...Eh? You let Haruna go without knowing that?", "…А? Ты отпустил Харуну, не зная об этом?"),
153: ("Well, it was hard to ask Haruna directly...", "Ну, мне было трудно спросить Харуну напрямую…"),
154: ("And I felt awful asking Tabitha—as a Chevalier, she might have lost face...",
      "И мне было неловко спрашивать Табасу — как шевалье она могла потерять лицо…"),
155: ("Either way, you could have just asked normally and they'd have told you...",
      "В любом случае, стоит было просто спросить — и тебе бы ответили…"),
156: ("Then do you know how it all turned out?", "Тогда ты знаешь, чем всё кончилось?"),
157: ("Well, yes.", "Ну, да."),
158: ("Then tell me, too!", "Тогда расскажи и мне!"),
159: ("Why don't you ask Tabitha directly?", "Почему бы не спросить Табасу напрямую?"),
160: ("All right... I'll go ask Tabitha, like you said...", "Ладно… Пойду спрошу Табасу, как ты сказала…"),
161: ("...Wait. It'd be rude to bother Tabitha over something like that. I'll tell you myself.",
      "…Погоди. Нехорошо беспокоить Табасу по такому поводу. Я сама тебе расскажу."),
162: ("Y-Yes...", "Д-Да…"),
163: ("(Honestly... I wish you'd just tell me straight...)", "Право… Хоть бы ты просто рассказала…"),
164: ("So—why didn't Tabitha hand Haruna over to Gallia?", "Так — почему Табаса не отдала Харуну Галлии?"),
165: ("And yet Tabitha said she'd completed the mission...", "И всё же Табаса сказала, что задание выполнено…"),
166: ("Ah, that. Tabitha reported to Gallia like this.", "А, это. Табаса доложила Галлии вот что."),
167: ("Amid the sudden fighting in Tristain, Haruna went missing.",
      "Во время внезапных боёв в Тристании Харуна пропала без вести."),
168: ("Eh? They bought that report? They accepted it surprisingly easily...",
      "А? Они поверили? Приняли это удивительно легко…"),
169: ("This is just my guess... But maybe Gallia was looking for Akina the bomber.",
      "Это только моё предположение… Но, может, Галлия искала Акину-бомбиста."),
170: ("Eh?", "А?"),
171: ("Apparently Gallia suffered quite a bit, too.", "Кажется, Галлия тоже сильно пострадала."),
172: ("Probably—they asked for a description, and by coincidence, it matched Haruna.",
      "Наверное, они спросили описание внешности, и по совпадению оно подошло Харуне."),
173: ("I see. So that's how it was. I thought they knew the whole mechanism...",
      "Понятно. Вот как. Я думал, они знали весь механизм…"),
174: ("Besides, their main aim was probably to dump troublesome jobs on Tabitha, "
      "so they didn't care much about the result.", "И к тому же их главной целью, наверное, "
      "было свалить хлопотные дела на Табасу, поэтому результат их мало интересовал."),
175: ("I see... Well, at least it didn't end badly for Tabitha and Haruna...",
      "Понятно... Ну, по крайней мере, для Табасы и Харуны всё кончилось хорошо..."),
176: ("(In the end, Akina—Haruna's other personality—still seems to linger a little.)",
      "В конце концов, Акина — вторая личность Харуны — похоже, всё ещё остаётся отчасти."),
177: ("(It's a secret from Haruna, but the Queen ordered her to take a magic potion.)",
      "Это секрет от Харуны, но, как я слышал, Королева предписала ей принимать магическое лекарство."),
178: ("(Weatherly has been missing since then. Probably returned to Reconquista.)",
      "Уэзерби с тех пор пропала. Наверное, вернулась к Реконкисте."),
179: ("(And so, after Haruna left the academy, life resumed much as before... But...)",
      "И после того, как Харуна ушла из академии, жизнь пошла почти как раньше… Но…"),
180: ("(There's just one thing that's changed...)", "Есть только одна перемена…"),
181: ("Honestly! Why does Tabitha sit next to Saito every single day!?",
      "Право! Почему Табаса каждый день садится рядом с Сайто!?"),
182: ("Because I want to.", "Потому что хочу."),
183: ("You're just reading a book anyway—it's not like it has to be next to Saito!",
      "Ты же просто читаешь книгу — незачем сидеть именно рядом с Сайто!"),
184: ("It should be fine even next to him.", "Рядом с ним тоже можно."),
185: ("Ugh—Saito! Say something to Tabitha!", "Ох — Сайто! Скажи что-нибудь Табасе!"),
186: ("You want me to talk to her... It's not like sitting next to me is a problem, is it?",
      "Чтобы я поговорил… Да разве сидеть рядом — это проблема?"),
187: ("It is! It makes me irritable—so it's bad!", "Это проблема! Мне становится не по себе — значит, плохо!"),
188: ("You're being silly, Louise. That's called jealousy, you know?", "Ты глупишь, Луиза. Это называется ревность, да?"),
189: ("It's not jealousy... I'm just irritated...", "Это не ревность… Я просто раздражена…"),
190: ("Honestly... Um, Tabitha-san? My mistress is rather upset, so if possible...",
      "Право… Э-Э, Табаса-сан? Моя госпожа довольно сердится, так что, если возможно…"),
191: ("No.", "Нет."),
192: ("Ha ha, Tabitha-san? Could this be...", "Ха-ха, Табаса-сан? Неужто это…"),
193: ("That you want to be next to me?", "Что ты хочешь быть рядом со мной?"),
194: ("Mm.", "Мм."),
195: ("She says she does...", "Она говорит, что хочет…"),
196: ("'She says she does' my foot! You idiot, Saito!", "«Говорит, что хочет» — как же! Дурак ты, Сайто!"),
197: ("Why are you angry at me!?", "Почему ты злишься на меня!?"),
198: ("Look—it's fine for Tabitha to sit next to you. She's just reading a book anyway.",
      "Да ладно — пусть Табаса сидит рядом. Она же просто читает книгу."),
199: ("B-But...", "Но…"),
200: ("Then instead of Tabitha... Shall I sit next to darling and cling to him?",
      "Тогда вместо Табасы… может, я сяду рядом с дорогим и прижмусь?"),
201: ("Then Tabitha's fine.", "Тогда Табаса — ладно."),
202: ("...", "…"),
203: ("(Oh—she's rather pleased...)", "Ох — она довольно довольна…"),
204: ("(...And so Tabitha, who'd added one more worry to Louise's life, was still reading as always...)",
      "…И вот Табаса, прибавившая Луизе ещё одну заботу, всё читала и читала…"),
205: ("(But—watching Tabitha read right beside me, I found myself feeling oddly at ease.)",
      "Но, глядя на Табасу, читающую прямо рядом со мной, я почему-то чувствовал себя спокойно."),
}
SPK = {'サイト': 's', 'ハルナ': 'ha', 'ルイズ': 'l', 'タバサ': 't',
       'キュルケ': 'k', 'null': 'th'}
START = {'s': 69, 'ha': 0, 'l': 9, 't': 39, 'k': 14, 'th': 0}


def main():
    data = json.load(open('reports/ch28/parse_999_1008.json', encoding='utf-8'))
    script = ['# Глава 28, часть 2 (сцена 1008): уход Харуны, финал.',
              '# Источник: ps2_source/chapters/chapter_29_夜の秘密.txt (SCENE 1008).',
              '', 'label ch28_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] != 1008: continue
            scene = x['no']
            script += ['label ch28_2_scene_%d:' % scene, '']
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
            tag = 'ch28_%s_%03d' % (spk, counters[spk])
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
        if k == 'goto':
            if scene != 1008: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump attention')
            script.append('')
    script += ['    # ==== КОНЕЦ ПРОЕКТА ====', '    jump attention', '    return', '']
    files = {
        'game/chapters/28/script-ch28_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch28_2_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch28_2_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch28/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
