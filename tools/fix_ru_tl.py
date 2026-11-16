#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Исправление RU TL файла: добавление корректных маркеров {#voice} 
на основе script-ch8_3.rpy
"""

import re

# Словарь EN текст -> RU перевод
TRANSLATIONS = {
    "Alright, this is youth!": "Ну вот, так это и есть — юность!",
    "That's Saito, that's Saito…!": "Это Сайто, это Сайто…!",
    "It's fine. I'll fix it.": "Ничего страшного. Я это исправлю.",
    "Eh, ah, oh, o-oh… It's just a joke…": "Э, а, о, о-о… Это же просто шутка…",
    "Ugh, ugh, grumble…?": "Трясётся, трясётся…?",
    "I managed to fix it somehow.": "Как-то получилось починить.",
    "Your Highness!": "Ваше Высочество!",
    "Yes!": "Да!",
    "I disagree. But if you've decided, then I'll follow.": "Я не согласна. Но если Вы так решили, то последую за Вами.",
    "Thank you, Louise.": "Спасибо, Луиза.",
    "So you're going to join up with the army?": "Значит, вы собираетесь присоединиться к армии?",
    "No. I'm returning to the palace.": "Нет. Я возвращаюсь в дворец.",
    "So I'd like to accompany you on the way there, if you don't mind.": "Поэтому я бы хотела сопроводить вас по дороге, если не против.",
    "But the palace is under attack right now. You don't have to force your way back…": "Но дворец сейчас под атакой. Вам не нужно насильно пробиваться обратно…",
    "It's enough that I'm safe inside the palace, so the Tristain can be reassured that I'm alive.": "Достаточно того, что я в безопасности внутри дворца, чтобы Тристейн узнал: я жива.",
    "Besides, I have something on my mind.": "К тому же, у меня есть одна мысль.",
    "I, as a queen, have different things I can do as a mage.": "Я, как королева, могу сделать что-то иное, как волшебница.",
    "And what is that?": "А что именно?",
    "That's something I'll tell you about when the time comes. For now, just think of it as a backup plan.": "Об этом я расскажу, когда придет время. Пока считайте это запасным планом.",
    "Understood. I'll do my best to protect the Princess.": "Поняла. Я сделаю всё возможное, чтобы защитить Принцессу.",
    "So I'll have Site, the Princess, and Kirche head to the palace.": "Я с Сайто, Принцесса и Кюрке идём к дворцу.",
    "Hey? Something seems to be happening outside. What's going on?": "О? Кажется, снаружи что-то происходит. Что случилось?",
    "No way!?": "Неужели!?",
    "I found them.": "Нашёл их.",
    "Kyaaa!": "Кяаа!",
    "They're the Reconquista assassins, aren't they.": "Это убийцы Реконкисты, верно?",
    "Damn it! So this is where it comes down to?": "Чёрт! Так вот где всё решается?",
    "Siesta! Get back! It's dangerous!": "Сьеста! Отойди! Опасно!",
    "Yes!": "Ха-ай!",
    "First, let's turn and fight back!": "Сначала дадим им сдачи!",
    "All detained. Can't let you retreat.": "Все задержаны. Отступать не позволю.",
    "Alright, let's do this!": "Ладно, давайте сделаем это!",
    "Yeah, I see.": "Ага, понял.",
    "Everyone, are you all right!?": "Все, вы в порядке!?",
    "The Princess and Siesta, everyone is safe.": "Принцесса и Сьеста, все в безопасности.",
    "We drove them all off.": "Всех их отогнали.",
    "This is getting out of hand. We have to hurry!": "Дело принимает плохой оборот. Нам нужно поторопиться!",
    "Siesta, wait here. The academy is safer, but there's no time.": "Сьеста, подожди здесь. Академия безопаснее, но времени нет.",
    "Yes! Please give me your support, Saito-san…!": "Ха-ай! Пожалуйста, поддержите меня, Сайто-сан…!",
    "Yeah…": "Аа…",
    "Then let's split up. I'll go with Site and Kirche to the palace.": "Тогда разделимся. Я пойду с Сайто и Кюрке к дворцу.",
    "Tabitha, Montmorency, and Guiche — attack the cannons. Be careful.": "Табаса, Монморанси, Гюш — атакуйте пушки. Осторожнее.",
    "Understood.": "Понял.",
    "Understood. I'll make sure I'm not an obstacle. Do your best.": "Поняла. Стараюсь не мешать. Удачи.",
    "Then, the plan begins.": "Тогда план начинается.",
    "Your Majesty! Are you safe!?": "Ваше Величество! Вы в безопасности!?",
    "Your Majesty has returned! Now, we have won!": "Ваше Величество вернулись! Теперь мы победили!",
    "Wow. Just seeing the Princess is changing the mood of the city.": "Вау. Только вид Принцессы меняет настроение в городе.",
    "Being a king means little to me. Having this person around means I can believe in them.": "Быть королём — ерунда. Главное — чтобы рядом был кто-то, в кого можно верить.",
    "Yes, sir. Small-scale combat has been occurring at the eastern cannon since morning.": "Гав. С утра у восточной батареи идут мелкие сражения.",
    "That would explain why the castle bombardment has stopped, for now.": "Поэтому, вероятно, обстрел замка пока прекратился.",
    "Tabitha and the others are doing their best, aren't they.": "Табаса и остальные стараются, да?",
    "However, the Reconquista fleet is… approaching.": "Однако флот Реконкисты… приближается.",
    "I understand. That's why I've prepared the backup plan.": "Понимаю. Именно поэтому я приготовила запасной план.",
    "The backup plan…?": "Запасной план…?",
    "I'll explain the details after this battle is over.": "Подробности объясню после окончания битвы.",
    "I'll relay this to all units deployed in the city. Keep surrounding them and wait. If chaos occurs in the enemy camp, then launch an all-out assault.": "Передам это всем подразделениям в городе. Продолжайте окружение и ждите. Если во вражеском лагере начнётся хаос — наносите решающий удар.",
    "Understood!": "Понял!",
    "Alright, let's head to the roof! From there, you can use your magic to take them all down!": "Хорошо, на крышу! Оттуда ты сможешь разобраться со всеми!",
    "Yes, please rely on me. I'll show you my true power!": "Да, рассчитывайте на меня. Покажу свою истинную силу!",
    "Hey! Believe in your master more!": "Эй! Верьте в своего хозяина сильнее!",
    "Here we come!": "Прибыли!",
    "Whew, whew, whew… It's a high place. Climbing all those stairs was tiring.": "Ха-а, ха-а, ха-а… Высота. Подъём по лестнице утомил.",
    "But look at this! From here, we can see all the cannons!": "Но смотри! Отсюда видно все орудия!",
    "All right, watch this! I'll smack the Reconquista forces with the righteous hammer of justice!": "Хорошо, смотрите! Свергну я на Реконкисту молот правосудия!",
    "You won't get away with this.": "Так не выйдет.",
    "What!?": "Что!?",
    "Surprised? You really came this far, didn't you. I underestimated you.": "Удивлён? Ты действительно добрался до сюда. Я недооценил тебя.",
    "I'm not in the mood for fighting anymore. Just stay here.": "Уже не в духе драться. Просто оставайся здесь.",
    "Weatherby, and Akina too!": "Везерли, и Акина тоже!",
    "Maybe you thought we'd come here. You were wrong.": "Думали, мы придём сюда? Ошиблись.",
    "It's thanks to the information gathered by Haruna. Though she collected it unconsciously.": "Благодаря информации, собранной Харуной. Хоть она и делала это бессознательно.",
    "Do you even understand why Haruna was being targeted regularly?": "Ты вообще понимаешь, почему Харуну регулярно атаковывали?",
    "That's when Akina was passing information about you and Louise to me.": "В то время Акина передавала мне сведения о тебе и Луизе.",
    "Though Akina herself doesn't remember doing any of it.": "Хоть сама Акина и не помнит, что это сделала.",
    "Damn you, Weatherby! Restore Haruna!": "Чёрт тебя, Везерли! Верни Харуну!",
    "Unfortunately, that's not something I can agree to. I have my own goals. Until I achieve them, I will use you.": "К сожалению, я не могу согласиться. У меня свои цели. Пока не достигну их — буду пользоваться вами.",
    "Haruna…": "Харуна…",
    "You intended to attack the cannons from the palace rooftop with a long-range spell. But since we're already occupying it, it's meaningless.": "Ты планировал атаковать орудия с крыши дворца дальним заклинанием. Но раз мы уже заняли позицию — это бессмысленно.",
    "I'll just finish this here on the rooftop. It's fortunate that the Princess is here.": "Просто закончу это здесь, на крыше. К счастью, Принцесса тоже здесь.",
    "Fine then. If you won't stop, then we'll defeat you.": "Хорошо. Если не остановитесь — победим вас мы.",
    "Oh, can you? Can I use my bomb on your magic? Do it if you can win.": "О, сможете? А если я применить своюBomb против вашей магии? Попробуйте, если сможете выиграть.",
    "That's enough.": "Достаточно.",
    "Ah…!": "А…!",
    "Haruna!?": "Харуна!?",
    "Secure that child! Quickly!": "Захватите этого ребёнка! Быстро!",
    "Huh? Ah, yes!": "Э? А, да!",
    "Haruna! Or is it Akina? Anyway, is everyone safe?": "Харуна! Или это уже Акина? Во всяком случае, все в порядок?",
    "Un… unnn…": "Ун… унн…",
    "Looks like we're all safe, then.": "Кажется, все в безопасности.",
    "As long as I am here, it's absolutely impossible.": "Пока я здесь — это абсолютно невозможно.",
    "Why… how are you able to dispel it?": "Почему… как ты смог это рассеять?",
    "This is a secret art passed down in my family! It shouldn't be breakable by someone like you!": "Это секретная техника моей семьи! Её не должен был преодолеть кто-то вроде тебя!",
    "That it can be broken, I knew. I knew you were communicating through a sound that humans cannot hear.": "То, что её можно взломать, я знала. Знала, что вы общаетесь звуком, недоступным человеческому уху.",
    "I was just making you unable to hear that sound by using magic.": "Я просто магией сделала так, что вы его не слышите.",
    "No, that's a lie…! This magic is a special art that only my family can use!": "Нет, это ложь…! Эта магия — исключительное мастерство только моей семьи!",
    "How could you possibly know how to counter it?!": "Откуда вы могли знать, как её противостоять?!",
    "Why… how did you know?! Did you raid your own village…?": "Почему… как ты узнал?! Неужели ты нагрянул на свою деревню…?",
    "Miss Weatherby, your loss of nobility was not because of your origins.": "Мисс Везерли, вас лишили дворянства не из-за вашего происхождения.",
    "What…?": "Что…?",
    "You used a forbidden magic that manipulates the heart, which was deemed inhuman.": "Вы использовали запрещённую магию, манипулирующую сердцем, которая считалась нечеловечной.",
    "You were persecuted in your noble years because of your origins. I understand and sympathize.": "В ваши дворянские годы вас преследовали из-за происхождения. Я понимаю и сочувствую.",
    "But you broke the taboo and attempted to toy with the hearts of others.": "Но вы нарушили табу и попытались играть с чужими сердцами.",
    "That is a crime for which there is no excuse, and so you have lost your noble status.": "Это преступление, за которое нет оправдания. Поэтому вы потеряли дворянское звание.",
    "How… I can't believe the secret art of my family would be turned against me…": "Как… Не могу поверить, что семейная тайна обратилась против меня…",
    "The existence of the forbidden heart-manipulating magic is a threat. That's why research was conducted by some of the royal family and military.": "Существование запрещённой магии управления сердцем — угроза. Поэтому и члены королевской семьи, и военные вели исследования, как её взломать.",
    "What I learned to protect my people was that. Your magic no longer works.": "То, чему я научилась ради защиты народа — это и есть. Твоя магия больше не работает.",
    "Heh heh heh… Now that my family's secret is sealed, the only option is to overpower with force.": "Хе-хе-хе… Раз семейный секрет запечатан, остаётся только сила.",
    "Then at least let me face you head-on and take down the queen!": "Тогда пусть хоть в открытую схватку убью королеву!",
    "Come then! I have nothing left but my pride and my anger! Take this!!": "Иди же! Остались только гордость и гнев! Прими это!!",
    "I guess we really have to fight then.": "Видимо, действительно придётся драться.",
    "No more games, Derflinger! This is it!": "Больше никаких игр, Дерфлингер! Это конец!",
    "All right, partner!": "Хорошо, партнёр!",
    "Kuahh!": "Куаа!",
    "That's enough, Weatherby. You're defeated.": "Всё, Везерли. Ты проиграл.",
    "Heh heh heh…": "Хе-хе-хе…",
    "Did you really think I'd be defeated by a queen I underestimated?": "Неужели ты думал, что проиграшь подручной, которой пренебрегал?",
    "Weatherby…": "Везерли…",
    "Then at this point, no mercy for the defeated! This is the finishing blow!": "Тогда на этом этапе — не жалеть побеждённых! Это решающий удар!",
    "What should the Princess do?": "Что должна сделать Принцесса?",
    "Miss Weatherby. You will pay for your sins.": "Мисс Везерли. Вы ответите за свои грехи.",
    "I know. Do what you will.": "Знаю. Делай что хочешь.",
    "Understood. I'll inform you of the punishment later.": "Поняла. Наказание сообщу позже.",
    "Next is your turn, Louise. Show me your power.": "Следующая — ты, Луиза. Покажи свою силу.",
    "Yes. I entrust this to you.": "Да. Доверяю это тебе.",
    "…!": "……っ！",
    "Come forth, here I am… Here I am.": "Явься, вот я… Вот я.",
    "Illusion!!": "Иллюзия!!",
    "Oh…!": "О…!",
    "Eh…!?": "Э…!?",
    "Was that… the Tristain aerial fleet!?": "Это… тристейнский воздушный флот!?",
    "No, it's not… Idiot.": "Нет, не это… Идиот.",
    "Oh, Louise… This is Illusion. It's magic that creates tangible illusions…": "О, Луиза… Это Иллюзия. Магия, создающая осязаемые иллюзии…",
    "So that fleet was an illusion?": "Значит, тот флот был иллюзией?",
    "So it was… Then? / So, what about my magic?": "Так это так… И что? / А как же моя магия?",
    "Yeah, that's more than enough! The Reconquista fleet has started retreating, and the ground cannons are getting noisy.": "Ага, этого более чем достаточно! Флот Реконкисты начал отступление, а наземные батареи зашумели.",
    "The troops who saw the enemy's confusion have launched their assault. With this, the battle is decided.": "Подразделения, заметившие замешательство врага, перешли в наступление. С этим битва решена.",
    "Yes… That's good…": "Да… Хорошо…",
    "Whoa. What's wrong with Louise? She just collapsed?": "Ух. Чего с Луизой? Она просто рухнула?",
    "Louise, you're exhausted. Rest now; the rest is on us.": "Луиза, ты измотана. Отдохни, за остальное ответим мы.",
    "…Yeah. I'm a bit tired…": "…Ага. Чуть-чуть устала…",
    "Louise… and my familiars, thank you. Thanks to you, this country was saved.": "Луиза… и мои фамильяры, спасибо. Благодаря вам эта страна спасена.",
    "And I… also… will do my best.": "И я… тоже… сделаю всё возможное.",
    "What?": "Что?",
    "Oh, no. Well, it seems we'll have a lot of work ahead of us now.": "О, нет. Ну, похоже, впереди у нас горы работы.",
    "Casualty care, rebuilding damaged buildings… There are so many things to do, more than I can think of now.": "Уход за ранеными, восстановление зданий… Столько дел, что даже не придумаешь всё сразу.",
    "But… I will not run away. I am… the queen of this country.": "Но… Я не сбегу. Я… королева этой страны.",
}

def normalize_voice_name(vn):
    """Normalize voice name ch8_XXX to form ch8_0XX with leading zero."""
    # Extract the numeric part after ch8_
    m = re.match(r'ch8_(\d+)$', vn)
    if m:
        num = int(m.group(1))
        # Pad to 3 digits
        return f'ch8_{num:03d}'
    return vn

def main():
    # Read script to get all dialogue lines with markers
    with open('game/chapters/8/script-ch8_3.rpy', 'r', encoding='utf-8') as f:
        script = f.read()
    
    # Find ALL dialogue lines with markers: speaker "EN TEXT {#marker}"
    # This catches both voiced lines (preceded by voice "ch8_...") and plain lines
    line_pat = re.compile(
        r'^\s*([a-z_]+)\s+"([^"]+?)\s*\{(#ch8_[a-z0-9_]+)\}"\s*$',
        re.MULTILINE
    )
    voice_entries = []
    for m in line_pat.finditer(script):
        speaker = m.group(1)
        en_text = m.group(2)
        marker = m.group(3)  # like #ch8_s_082 or #ch8_l_60
        voice_entries.append((speaker, en_text, marker))
    
    print(f"Found {len(voice_entries)} dialogue lines with markers")
    
    # Write corrected RU TL file
    with open('game/tl/russian/ch8_3_dialogs.rpy', 'w', encoding='utf-8') as f:
        f.write(f'# ===== ch8.3: {len(voice_entries)} strings (dialogues) =====\n')
        f.write('translate russian strings:\n\n')
        
        for speaker, en_text, marker in voice_entries:
            ru_text = TRANSLATIONS.get(en_text)
            if ru_text is None:
                print(f"WARNING: no RU translation for: {en_text[:60]}")
                ru_text = en_text  # fallback: keep EN
            old_str = f'{en_text} {{{marker}}}'
            f.write(f'    old "{old_str}"\n')
            f.write(f'    new "{ru_text}"\n\n')
    
    print("Written corrected RU TL file")
    
    # Verify: all EN texts found in TRANSLATIONS
    script_en = {en for _, en, _ in voice_entries}
    missing = script_en - set(TRANSLATIONS.keys())
    if missing:
        print(f"WARNING: {len(missing)} EN texts missing translation:")
        for m in sorted(missing):
            print(f"  {m[:80]}")
    else:
        print("All EN texts have RU translations")


if __name__ == '__main__':
    main()