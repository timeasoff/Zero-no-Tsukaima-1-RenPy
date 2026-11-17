#!/usr/bin/env python3
"""Chapter 17 part 2 (scenes 684-695): the Queen's request, eve of escape."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
147: ("I have a special request for Louise and her familiar. That's why I called you "
      "to the castle.",
      "У меня особая просьба к Луизе и её фамильяру. Поэтому я и позвала вас в замок."),
148: ("Princess...?", "Принцесса…?"),
149: ("Louise... This isn't as a friend, but as the Queen of Tristain that I ask. "
      "Is that all right?",
      "Луиза… Я прошу не как подруга, а как королева Тристании. Можно?"),
150: ("O-Of course! Anything you command.", "К-Конечно! Что угодно прикажите."),
151: ("Louise, as you saw in the council, Tristain is in a critical situation.",
      "Луиза, как ты видела на совете, Тристания в критическом положении."),
152: ("Yes.", "Да."),
153: ("But... Louise. With your power and your familiar's...",
      "Но… Луиза. С твоей силой и силой твоего фамильяра…"),
154: ("My... Void power, you mean.", "Моёй… силой Пустоты."),
155: ("And you, familiar... I ask you too.", "И ты, фамильяр… Я прошу и тебя."),
156: ("O-Okay...", "Д-Да…"),
157: ("Familiar...", "Фамильяр…"),
158: ("I hear the power of Gandalf you wield is meant to protect your contract's "
      "mistress during spellcasting.",
      "Я слышала, что сила Гандальва, которой ты обладаешь, нужна, чтобы защитить "
      "госпожу по договору, пока она читает заклинание."),
159: ("Could you lend Louise's and your power to me?", "Можете ли вы одолжить мне силу Луизы и вашу?"),
160: ("Pri-ness...", "Прин-цесса…"),
161: ("Louise... I think of you as my only precious friend in this world. But...",
      "Луиза… Я считаю тебя единственной дорогой подругой в этом мире. Но…"),
162: ("Forgive me. For sending you, my dear friend, to the battlefield as a tool of war.",
      "Прости меня. За то, что отправляю тебя, дорогую подругу, на поле боя как орудие войны."),
163: ("...", "…"),
164: ("Louise, is that okay?", "Луиза, ты согласна?"),
165: ("What are you saying, Saito? The Princess is counting on us. "
      "Of course we'll do it.",
      "Что ты говоришь, Сайто? Принцесса на нас рассчитывает. Конечно, мы сделаем это."),
166: ("Even after she said all that, you won't respond?", "После всех её слов ты не хочешь ответить?"),
167: ("It's fine, Princess.", "Всё хорошо, принцесса."),
168: ("Saito!?", "Сайто!?"),
169: ("Even with such a mistress... It seems my role is to protect you, no matter what.",
      "Даже с такой госпожой… Кажется, моя роль — защищать тебя, что бы ни было."),
170: ("Who are you calling 'such'!", "Это ещё кто «такая»!"),
171: ("Are we really going to be okay?", "Мы и правда справимся?"),
172: ("What's wrong with you? I'm the wielder of Void, and you're my familiar.",
      "Что с тобой? Я — носитель Пустоты, а ты — мой фамильяр."),
173: ("Even after she said all that, you won't respond?", "После всех её слов ты не хочешь ответить?"),
174: ("Even so, it's not easy for us either.", "Даже так, нам непросто."),
175: ("My mistress bursts into tears at the slightest thing.", "Моя госпожа чуть что — сразу в слёзы."),
176: ("And even if you call her a Void mage, she runs out of magic power instantly.",
      "И хоть называй её магом Пустоты, она сразу тратит всю магическую силу."),
177: ("...", "…"),
178: ("She can't cook or clean at all, and she's hopeless at everyday magic.",
      "Готовить и убирать она совсем не умеет, да и в обычной магии ни на что не годится."),
179: ("And yet she's only a prodigy when it comes to eating...",
      "И при этом только в еде она настоящий мастер…"),
180: ("SAAAI TOOOO!", "САААЙ ТОООО!"),
181: ("Gyah!", "Гя!"),
182: ("In front of the Princess, too! How could you!?", "И прямо перед принцессой! Как ты мог!?"),
183: ("Fufu... hehe...", "Фу-фу… хе-хе…"),
184: ("...?", "…?"),
185: ("Fufufu... I'm relieved. If you two are this close... Surely, it'll be all right.",
      "Фу-фу-фу… Я успокоилась. Если вы двое так близки… Всё будет хорошо."),
186: ("Ugh...", "Ох…"),
187: ("Louise, familiar. The future of this country... I entrust it to you.",
      "Луиза, фамильяр. Будущее этой страны… я доверяю его вам."),
188: ("(Having accepted the Princess's request, Louise and I hurried back to the academy.)",
      "Приняв просьбу принцессы, мы с Луизой поспешили вернуться в академию."),
189: ("(To fight the aerial fleet, we need the Zero Fighter—but it's at the academy now.)",
      "Чтобы сражаться с воздушным флотом, нужен Zero Fighter — но сейчас он в академии."),
190: ("(But to get back to the academy, we have to slip through the enemy's net of cannons.)",
      "Но чтобы вернуться в академию, нужно проскользнуть через сеть вражеских орудий."),
191: ("(Surely they don't have enough ammo to keep shelling forever.)",
      "Вряд ли у них хватит боеприпасов обстреливать вечно."),
192: ("(We decided to escape at dawn, when there'd be a gap.)",
      "Мы решили вырваться на рассвете, когда будет пауза."),
193: ("(First, let's rest up for tomorrow's escape...)", "Для начала отдохнём перед завтрашним побегом…"),
194: ("Saito... Are you there?", "Сайто… Ты здесь?"),
195: ("Louise?", "Луиза?"),
196: ("I'm coming in.", "Я войду."),
197: ("What is it, Louise? You're acting so formal.", "Что случилось, Луиза? Ты так официально."),
198: ("Saito, we leave at dawn tomorrow, right?", "Сайто, мы уходим завтра на рассвете, верно?"),
199: ("Yeah, I heard from a soldier. We break through the encirclement, head to the "
      "academy, then fly the Zero Fighter. That's the plan, right?",
      "Да, я слышал от солдата. Прорываемся, идём в академию, потом поднимаем "
      "Zero Fighter. Так?"),
200: ("Say... Louise.", "Слушай… Луиза."),
201: ("What?", "Что?"),
202: ("What's happening to the academy?", "Что с академией?"),
203: ("Don't ask me. You were with them the whole time. How would I know?",
      "Не спрашивай меня. Ты всё время был с ними. Откуда мне знать?"),
204: ("N-No, I know that. I just... can't stop worrying.",
      "Н-Нет, я знаю. Просто… не могу не беспокоиться."),
205: ("And you're worried too, aren't you, Louise?", "И ты тоже волнуешься, правда, Луиза?"),
206: ("Well, yes, but...", "Ну, да, но…"),
207: ("Don't get captured by the enemy.", "Не попадись врагу."),
208: ("Wha—! What is this familiar saying to his mistress!?",
      "Что—! Что это за фамильяр, который такое говорит госпоже!?"),
209: ("Even if you can use magic, they outnumber you.", "Даже если ты можешь колдовать, их больше."),
210: ("Void magic is fine, but if it's all over before you even get to use it, "
      "there's no help for it.",
      "Пустота — это хорошо, но если всё кончится, прежде чем ты её применишь, "
      "ничего не поделать."),
211: ("You... Are you really going to use Void magic?", "Ты… Ты правда применишь Пустоту?"),
212: ("What are you saying? Of course.", "Что ты говоришь? Конечно."),
213: ("Unless we use Void, we can't stop the invasion of Tristain.",
      "Без Пустоты мы не остановим вторжение в Тристанию."),
214: ("Right. Against the enemy fleet, my Zero Fighter alone won't be enough.",
      "Верно. Против вражеского флота одного моего Zero Fighter мало."),
215: ("You're so annoying. I'm a noble.", "Какой ты назойливый. Я дворянка."),
216: ("Nobles have a duty to fight to defend their country and their pride!",
      "У дворян есть долг сражаться во имя страны и чести!"),
217: ("Duty of a noble, huh... But if you die, there's no honor or pride left.",
      "Долг дворянина, значит… Но если ты умрёшь, не останется ни чести, ни гордости."),
218: ("...!", "…!"),
219: ("Say, Louise, I...", "Слушай, Луиза, я…"),
220: ("What we have to do now is one: get back to the academy at any cost. "
      "Two: fight to defend this city.",
      "Сейчас нам надо сделать одно: во что бы то ни стало вернуться в академию. "
      "Два: сражаться во имя защиты города."),
221: ("That's all you need to think about. As my familiar, follow your mistress.",
      "Больше ни о чём не думай. Будучи моим фамильяром, следуй за госпожой."),
222: ("Louise...", "Луиза…"),
223: ("Good night. Sleep well today.", "Спокойной ночи. Сегодня выспись как следует."),
224: ("What the hell...", "Чёрт возьми…"),
225: ("Just because you're a noble, you shouldn't throw your life away so easily...",
      "Только потому, что ты дворянка, не надо так легко рисковать жизнью…"),
226: ("...", "…"),
227: ("Well, worrying won't help. Let's sleep...", "Ладно, бесполезно волноваться. Будем спать…"),
228: ("(No... I can't sleep.)", "(Нет… Я не могу уснуть.)"),
229: ("(I guess I'll wander around a bit...)", "(Ладно, пройдусь немного…)"),
230: ("(The fighting is still going on outside, but it shouldn't reach here yet. Probably...)",
      "(Снаружи ещё идёт бой, но сюда пока не дойдёт. Наверное…)"),
}
CHOICES = {
685: [("Louise, is that okay?", "Луиза, ты согласна?"),
      ("It's fine, Princess", "Всё хорошо, принцесса"),
      ("Are we really going to be okay?", "Мы и правда справимся?")],
690: [("What's happening to the academy?", "Что с академией?"),
      ("Don't get captured by the enemy", "Не попадись врагу"),
      ("Are you really going to use Void?", "Ты правда применишь Пустоту?")],
}
SPK = {'アンリエッタ': 'h', 'ルイズ': 'l', 'サイト': 's', '将校': 'commander',
       '兵士ＭＳ': 'soldier', 'null': 'th'}
START = {'h': 22, 'l': 28, 's': 43, 'commander': 16, 'soldier': 7, 'th': 0}


def main():
    data = json.load(open('reports/ch17/parse_670_695.json', encoding='utf-8'))
    script = ['# Глава 17, часть 2 (сцены 684–695): просьба королевы, канун побега.',
              '# Источник: ps2_source/chapters/chapter_18_女王の決断.txt (SCENE 684-695).',
              '', 'label ch17_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 695:
                break
            if x['no'] < 684:
                continue
            scene = x['no']
            script += ['label ch17_2_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene:
                event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if idx not in T:
                continue
            en, ru = T[idx]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice)')
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch17_%s_%03d' % (spk, counters[spk])
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
            if scene is None or scene not in CHOICES:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch17_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch17_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 684 <= scene <= 695:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch17_2_scene_%d' % x['target']
                                          if 684 <= x['target'] <= 695 else 'ch18'))
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 17 ====', '    jump ch18', '    return', '']
    files = {
        'game/chapters/17/script-ch17_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch17_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch17_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch17_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch17_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch17/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
