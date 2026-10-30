from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Hand-written editorial translations for scenes 360-374.  The Japanese values
# already in tl/japanese are canonical and are deliberately never rewritten.
ROWS = [
("ch6.2_h_001", "This place is even livelier than anywhere we've been so far.", "Здесь ещё оживлённее, чем во всех местах, где мы побывали.") ,
("ch6.2_s_001", "This seems to be the heart of the market.", "Похоже, это самый центр рынка.") ,
("ch6.2_h_002", "I'm glad.", "Я рада.") ,
("ch6.2_s_002", "Hm?", "Хм?") ,
("ch6.2_h_003", "If the market is bustling, then the people's lives cannot be all that miserable.", "Если на рынке так оживлённо, значит, жизнь народа не настолько тяжела.") ,
("ch6.2_s_003", "I never looked at it that way. You're something else, Princess. You really think like a politician.", "Я никогда не смотрел на это с такой стороны. А вы молодец, принцесса. Настоящий политик.") ,
("ch6.2_h_004", "It is hardly something to praise me for. I rarely have the chance to see a market like this for myself.", "Не думаю, что меня стоит за это хвалить. Я почти никогда не вижу рынок своими глазами.") ,
("ch6.2_h_005", "Ah, but perhaps that is why it makes me happy.", "Хотя, может быть, именно поэтому я и рада.") ,
("ch6.2_s_004", "Huh?", "А?") ,
("ch6.2_h_006", "You see, this view used to be a world beyond my window. Now it is right here, close enough to touch.", "Понимаете, раньше этот мир был для меня лишь видом за окном. А теперь он здесь, рядом, до него можно дотронуться.") ,
("ch6.2_s_005", "It's just an ordinary sight to me.", "Для меня это обычная картина.") ,
("ch6.2_h_007", "What is ordinary to you is special to me. I have not had this much fun in a long time.", "То, что для вас обычно, для меня внове. Давно мне не было так весело.") ,
("ch6.2_s_006", "Then I'm glad.", "Тогда я рад.") ,
("ch6.2_h_008", "Oh? It sounds like there is a quarrel over there...", "О? Похоже, там кто-то ссорится…") ,
("ch6.2_customer_001", "Hey, aren't these dried goods even more expensive than last time?", "Эй, разве эти сушёности не стали ещё дороже, чем в прошлый раз?") ,
("ch6.2_merchant_001", "What can I do? The army keeps seizing our ships, so our catch just keeps shrinking.", "А что я могу поделать? Армия снова отобрала корабли, и улов всё уменьшается.") ,
("ch6.2_customer_002", "Good grief. Everywhere I go, it's one gloomy story after another.", "Ну и ну. Куда ни глянь, везде одни дурные новости.") ,
("ch6.2_merchant_002", "It can't be helped. Ever since Her Majesty started this war, business has slumped and the army has run wild.", "Ничего не поделать. С тех пор как Её Величество начала эту войну, торговля пришла в упадок, а армия распоясалась.") ,
("ch6.2_merchant_003", "Nothing good has come of it.", "Ничего хорошего из этого не вышло.") ,
("ch6.2_customer_003", "Well, I suppose it's no wonder. What can you expect from such a young, ignorant queen?", "Ну, чего ещё ждать от такой юной и несведущей королевы?") ,
("ch6.2_h_009", "...", "…") ,
("ch6.2_s_007", "Uh, hey! Princess, let's go look over there!", "Э-э, послушайте! Принцесса, давайте посмотрим вон там!") ,
("ch6.2_s_008", "Whew...", "Фух…") ,
("ch6.2_h_010", "The people are honest. They openly say what is making their lives difficult and who is to blame.", "Народ не скрывает правды. Люди прямо говорят, что отравляет им жизнь и кто в этом виноват.") ,
("ch6.2_s_009", "Um, Princess.", "Э-э, принцесса.") ,
("ch6.2_s_010", "Don't let it get to you.", "Не принимайте это близко к сердцу.") ,
("ch6.2_h_011", "Hm?", "А?") ,
("ch6.2_s_011", "No, listening to them matters, but one person's voice doesn't necessarily represent everyone's opinion, right?", "Нет, к людям важно прислушиваться, но мнение одного человека не обязательно отражает мнение всех, верно?") ,
("ch6.2_s_012", "That merchant might just be using the war as an excuse to raise his prices...", "Тот торговец, может, просто прикрывается войной, чтобы поднять цены…") ,
("ch6.2_s_013", "You should do what you think is right, Princess. I'm sure of it.", "Вам нужно поступать так, как считаете правильным, принцесса. Я уверен.") ,
("ch6.2_h_012", "Thank you, familiar.", "Спасибо, мой фамильяр.") ,
("ch6.2_s_014", "What matters is what you do from here on.", "Важно то, что вы будете делать дальше.") ,
("ch6.2_h_013", "From here on...?", "Что я буду делать дальше…?") ,
("ch6.2_s_015", "Now you know what people think. You can use that as a hint for deciding what to do next.", "Теперь вы знаете, что о вас думают. Это может подсказать, как действовать дальше.") ,
("ch6.2_h_014", "Oh... So it is all right to look at it that way.", "А… Значит, на это можно смотреть и так.") ,
("ch6.2_s_016", "Exactly. People say some pretty irresponsible things. The Internet is the same way.", "Именно. Люди часто говорят совершенно безответственные вещи. В интернете то же самое.") ,
("ch6.2_h_015", "The Internet?", "В интернете?") ,
("ch6.2_s_017", "Ah, I was just talking to myself. Just mumbling.", "А, это я так, сам с собой. Просто пробормотал.") ,
("ch6.2_h_016", "I see. But thank you. I feel a little better now.", "Понятно. Но всё равно спасибо. Мне немного полегчало.") ,
("ch6.2_s_018", "There are all kinds of people in the world.", "Люди бывают самые разные.") ,
("ch6.2_h_017", "All kinds...?", "Самые разные…?") ,
("ch6.2_s_019", "When something happens, some people will think it's good, while others will think it's bad.", "Когда что-то происходит, одни считают это хорошим, а другие — плохим.") ,
("ch6.2_s_020", "So you just have to work to make more people see it as something good.", "Значит, нужно стараться, чтобы как можно больше людей считали это хорошим.") ,
("ch6.2_h_018", "Is it really that simple?", "Неужели всё настолько просто?") ,
("ch6.2_s_021", "Well, it's easy to say. But you have plenty of time ahead of you.", "Ну, сказать легко. Но всё ещё впереди.") ,
("ch6.2_h_019", "Indeed. I have only just become queen. Expecting everyone to accept me already would be greedy.", "Верно. Я совсем недавно стала королевой. Было бы слишком много хотеть, чтобы все уже меня признали.") ,
("ch6.2_s_022", "Oh, I didn't mean quite that much.", "Э-э, я не совсем это имел в виду.") ,
("ch6.2_h_020", "In any case, I still have a long way to go as queen, don't I...?", "Как ни крути, мне ещё многому предстоит научиться как королеве…") ,
("ch6.2_s_023", "You shouldn't look so down... Wait! I know just the place to take you!", "Не стоит так расстраиваться… Постойте! Я знаю одно место, куда вас отведу!") ,
("ch6.2_h_021", "Huh? Oh, familiar, wait for me!", "А? Ах, фамильяр, подождите меня!") ,
("ch6.2_h_022", "Is this the place that is supposed to cheer me up...? This is a dining hall, isn't it?", "Так вот где я должна повеселеть… Это ведь столовая?") ,
("ch6.2_s_024", "That's right. When you're feeling down, the best thing is to eat!", "Ага. Когда грустно, лучше всего поесть!") ,
("ch6.2_shopkeeper_001", "Here you go! Sorry to keep you waiting!", "Вот, держите! Прошу прощения за задержку!") ,
("ch6.2_s_025", "There it is! Go on, try it. The meat dishes here are delicious!", "Вот и принесли! Попробуйте. Здесь очень вкусно готовят мясо!") ,
("ch6.2_h_023", "Oh, all right. This is grilled fish... And this is vegetable soup.", "Ах, хорошо. Это… жареная рыба. А это овощной суп.") ,
("ch6.2_s_026", "Looks good, doesn't it? Come on, eat up!", "Аппетитно выглядит, правда? Ну же, ешьте!") ,
("ch6.2_h_024", "Oh, all right. Great Founder Brimir, thank you for this humble meal this morning...", "Ах, хорошо. Великий прародитель Бримир, благодарю за эту скромную пищу…") ,
("ch6.2_s_027", "A-are you going to do that here too?", "В-вы и здесь будете это делать?") ,
("ch6.2_h_025", "Then I shall partake... Munch.", "Тогда приступим… Ам.") ,
("ch6.2_s_028", "How is it? How is it?", "Ну как? Ну как?") ,
("ch6.2_h_026", "It is delicious!", "Очень вкусно!") ,
("ch6.2_s_029", "See?", "Вот видите!") ,
("ch6.2_h_027", "Do you all always eat such delicious food?", "Вы все всегда едите такую вкусную еду?") ,
("ch6.2_s_030", "The food at the castle is probably fancier, but this place is pretty good too, right?", "В замке, наверное, готовят роскошнее, но здесь тоже неплохо, правда?") ,
("ch6.2_h_028", "You know so much, familiar.", "Вы так много знаете, фамильяр.") ,
("ch6.2_s_031", "Not really. I know absolutely nothing about this world... I mean, this country.", "Да нет. Я вообще ничего не знаю об этом мире… то есть об этой стране.") ,
("ch6.2_h_029", "Ah, now that you mention it, that is true.", "А, точно. Я ведь совсем забыла.") ,
("ch6.2_s_032", "Yes?", "Да?") ,
("ch6.2_h_030", "Louise told me that you are from another world.", "Луиза сказала, что вы из другого мира.") ,
("ch6.2_s_033", "Well, that's true.", "Ну, это правда.") ,
("ch6.2_h_031", "I have wanted to ask you this for a while. What is your world like?", "Я давно хотела вас спросить. Каков ваш мир?") ,
("ch6.2_s_034", "What is it like...? Well, let's see...", "Каков он… Ну, даже не знаю…") ,
("ch6.2_s_035", "It is a world without kings.", "Это мир без королей.") ,
("ch6.2_h_032", "No king!? Then who rules the country, and how?", "Без короля!? Тогда кто и как управляет страной?") ,
("ch6.2_s_036", "Well, some countries do have kings, but they don't hold any real power.", "Ну, в некоторых странах короли всё-таки есть, но настоящей власти у них нет.") ,
("ch6.2_h_033", "I see...", "Понятно…") ,
("ch6.2_s_037", "It is a world without magic.", "Это мир без магии.") ,
("ch6.2_h_034", "Without magic...? That sounds like a very inconvenient world.", "Без магии…? Наверное, жить в таком мире неудобно.") ,
("ch6.2_s_038", "Well, not really. We have science instead of magic.", "Ну, не совсем. Вместо магии у нас есть наука.") ,
("ch6.2_h_035", "Science...?", "Наука…?") ,
("ch6.2_s_039", "A world without night, so to speak.", "Можно сказать, мир без ночи.") ,
("ch6.2_h_036", "There is no night!? Do you mean the sun stays out and it is always daytime?", "У вас нет ночи!? То есть солнце всё время светит и бывает только день?") ,
("ch6.2_s_040", "Well, to be precise, lights stay on even at night, so the darkness is gradually disappearing.", "Ну, точнее, ночью у нас горят огни, и ночная темнота постепенно исчезает.") ,
("ch6.2_h_037", "I see. But then you must spend an enormous amount on firewood.", "А, понятно. Но тогда, наверное, уходит уйма дров.") ,
("ch6.2_s_041", "Huh? Oh, we don't use firewood. We light everything with electricity.", "А? Нет, мы не используем дрова. Мы освещаем всё электричеством.") ,
("ch6.2_h_038", "Electricity?", "Электричеством?") ,
("ch6.2_s_042", "Lightning... Something like that.", "Молнией… Вроде того.") ,
("ch6.2_h_039", "Lightning...? I see.", "Молнией… Понятно.") ,
("ch6.2_h_040", "Who rules your world?", "А кто управляет вашим миром?") ,
("ch6.2_s_043", "In the country I came from, everyone votes to choose members of the national assembly...", "В моей стране все голосуют и выбирают депутатов парламента…") ,
("ch6.2_h_041", "The national assembly? Members?", "Парламент? Депутаты?") ,
("ch6.2_h_042", "The people choose their own leader...? Is such a thing really possible?", "Народ сам выбирает своего правителя… Неужели такое возможно?") ,
("ch6.2_s_044", "The national assembly is divided into two houses, the House of Representatives and the House of Councillors, and, uh... I should have studied this a little more...", "Парламент делится на две палаты: Палату представителей и Палату советников, и… Эх, надо было лучше учиться…") ,
("ch6.2_s_045", "Anyway, there is no king. Everyone chooses the people who will govern the country.", "В общем, короля нет. Все вместе выбирают тех, кто будет управлять страной.") ,
("ch6.2_s_046", "Yes, that's how it was in my country.", "Да, в моей стране всё было именно так.") ,
("ch6.2_h_043", "I cannot imagine a world without kings. So there are countries like that in other worlds.", "Я не могу представить мир без короля. Значит, в других мирах бывают такие страны.") ,
("ch6.2_s_047", "I-I don't know if it's really that amazing.", "Н-не знаю, что тут такого удивительного.") ,
("ch6.2_h_044", "This was supposed to be a morning walk, but it has become quite dark.", "Мы ведь собирались просто прогуляться утром, а уже совсем стемнело.") ,
("ch6.2_s_048", "Yeah, I guess it has... Ha ha ha.", "Ага, похоже на то… Ха-ха-ха.") ,
("ch6.2_h_045", "What is the matter? Is something worrying you?", "Что случилось? Вас что-то тревожит?") ,
("ch6.2_s_049", "I was just thinking that Louise is going to be furious if I go back like this.", "Я просто подумал, что Луиза страшно разозлится, если я вернусь вот так.") ,
("ch6.2_h_046", "Ah, I see... Hee hee. I found myself a little envious of Louise.", "А, понятно… Хи-хи. Я даже немного позавидовала Луизе.") ,
("ch6.2_s_050", "Huh?", "А?") ,
("ch6.2_h_047", "It is enviable to have someone you can be comfortable with.", "Как же я завидую тем, у кого есть человек, рядом с которым можно быть собой.") ,
("ch6.2_s_051", "Huh? Sorry, but who is comfortable with whom?", "А? Простите, но кто с кем может быть собой?") ,
("ch6.2_h_048", "Louise, of course, with you. The fact that she shows you her honest emotions proves that she trusts you, does it not?", "Конечно же, Луиза с вами. Раз она показывает вам свои настоящие чувства, значит, она вам доверяет, разве не так?") ,
("ch6.2_s_052", "You think so?", "Думаете?") ,
("ch6.2_h_049", "I envy you greatly for having time to spend together while showing your true selves.", "Я очень завидую тому, что вы можете проводить время вместе и не скрывать себя настоящих.") ,
("ch6.2_h_050", "I am always putting on the face of a queen...", "Я ведь всегда изображаю из себя королеву…") ,
("ch6.2_s_053", "Is that how it is...?", "Вот как это бывает…") ,
("ch6.2_l_001", "Now then, my excellent familiar, would you explain how this happened?", "Ну что ж, мой способный фамильяр, объясни-ка, как всё это произошло.") ,
("ch6.2_s_054", "Ah, she really is angry.", "А, она и правда злится.") ,
("ch6.2_l_002", "Of course I am! I woke up to find the princess gone, and you had disappeared too!", "А как же иначе! Я проснулась, а принцессы нет, и ты тоже исчез!") ,
("ch6.2_l_003", "And you didn't contact anyone until sunset!", "И до самого заката от тебя ни слуху ни духу!") ,
("ch6.2_l_004", "I am amazed at my own trust and patience for waiting for you instead of reporting this to the palace!", "Сама не понимаю, как мне хватило доверия и терпения ждать тебя, а не сообщить во дворец!") ,
("ch6.2_s_055", "That surprised me too.", "Я и сам удивлён.") ,
("ch6.2_l_005", "So. Is there anything you want to say before I have the last word?", "Итак. Хочешь напоследок что-нибудь сказать?") ,
("ch6.2_s_056", "Well...", "Э-э…") ,
("ch6.2_s_057", "It wasn't my fault! I was only accompanying the princess on her morning walk after she got up early!", "Я не виноват! Я всего лишь составил рано проснувшейся принцессе компанию на утренней прогулке!") ,
("ch6.2_l_006", "Oh, is that so?", "А, вот как?") ,
("ch6.2_s_058", "That's right. You understand now, don't you?", "Именно. Теперь ты поняла?") ,
("ch6.2_l_007", "As if I would! If you're going to lie, at least tell a better one!", "Как же! Врёшь, так хоть ври правдоподобнее!") ,
("ch6.2_s_059", "No regrets about my date with the princess! She asked me to show her the sights, so we went all over town! That was definitely a date!", "Я ни о чём не жалею после свидания с принцессой! Она попросила показать ей город, и мы побывали во всех достопримечательных местах! Это было настоящее свидание!") ,
("ch6.2_l_008", "...", "…") ,
("ch6.2_s_060", "Hey, the princess had fun too, so I have no regrets. Ha ha ha.", "Эй, принцесса тоже повеселилась, так что мне не о чем жалеть. Ха-ха-ха.") ,
("ch6.2_l_009", "...I see. Then I won't have to hold back either.", "…Понятно. Тогда и мне не придётся сдерживаться.") ,
("ch6.2_s_061", "I went to see how things were in town. We visited crowded places and listened to what people were saying.", "Я ходил посмотреть, как там в городе. Мы побывали в людных местах и послушали, что говорят люди.") ,
("ch6.2_l_010", "I see... So the princess is still wavering in her confidence as queen.", "Понятно… Значит, принцесса всё ещё сомневается в себе как в королеве.") ,
("ch6.2_s_062", "Yeah. So I took her to a dining hall to help take her mind off it.", "Да. Поэтому я отвёл её в столовую, чтобы она немного отвлеклась.") ,
("ch6.2_l_011", "So you were late because of your detour after all!?", "Так это из-за твоих прогулок вы и опоздали!?") ,
("ch6.2_s_063", "I-I guess that's true... Yes, I suppose so.", "Н-ну, наверное… Да, получается, так.") ,
("ch6.2_l_012", "What would you have done if something had happened to the princess? You stupid mutt!", "Что бы ты делал, если бы с принцессой что-нибудь случилось? Ах ты, глупый пёс!") ,
("ch6.2_s_064", "Aaaaaaagh!", "А-а-а-а-а-а-а-а!") ,
]

CHOICES = {
"choice_361": ("Don't let it get to you", "Не принимайте это близко к сердцу"),
"choice_362": ("What matters is what you do from here on", "Важно то, что вы будете делать дальше"),
"choice_363": ("There are all kinds of people", "Люди бывают самые разные"),
"choice_366": ("A world without kings", "Мир без королей"),
"choice_367": ("A world without magic", "Мир без магии"),
"choice_368": ("A world without night", "Мир без ночи"),
"choice_371": ("It wasn't my fault!", "Я не виноват!"),
"choice_372": ("I have no regrets about my date with the princess!", "Я ни о чём не жалею после свидания с принцессой!"),
"choice_373": ("I went to see how things were in town...", "Я ходил посмотреть, как там в городе…"),
}

THOUGHTS = {
    "thought_360_s": ("(She's truly a queen. She sees all that just by looking at the market.)", "(Настоящая королева. Она и по одному рынку умудряется так много понять.)"),
    "thought_365_s": ("(It seems to have cheered her up. Whether the food had anything to do with it, I have no idea.)", "(Похоже, ей и правда стало веселее. Только не знаю, благодаря ли этому еда.)"),
    "thought_370_s": ("(What am I going to do...? If I confess that I took the princess out without permission and wandered around town with her all day, Louise will punish me for sure.)", "(Что же делать… Если признаться, что я самовольно увёл принцессу и весь день бродил с ней по городу, Луиза точно меня накажет.)"),
    "thought_370_s_2": ("(But if I go back now, Louise will beat me to death for following her honest feelings.)", "(Но если я сейчас вернусь, Луиза всё равно забьёт меня до смерти за то, что я пошёл на поводу у своих чувств.)"),
}

def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')

def main():
    by_key = {f"[PROVISIONAL EN] {k}": (en, ru) for k, en, ru in ROWS}
    by_key.update({f"[PROVISIONAL EN] {k}": v for k, v in CHOICES.items()})
    script = (ROOT / "game/chapters/6/script-ch6_2.rpy").read_text()
    for old, (en, _) in by_key.items():
        script = script.replace(f'"{esc(old)}"', f'"{esc(en)}"')
    script = script.replace("# EN/RU are provisional source placeholders pending editorial translation.", "# English and Russian text edited from the canonical Japanese source.")
    (ROOT / "game/chapters/6/script-ch6_2.rpy").write_text(script)
    for key, (en, ru) in THOUGHTS.items():
        script = script.replace(f'"[PROVISIONAL EN] {key}"', f'"{esc(en)}"')
    script = script.replace(
        '"(What am I going to do...? If I confess that I took the princess out without permission and wandered around town with her all day, Louise will punish me for sure.)"\n    voice "ch6.2_l_001"',
        '"(But if I go back now, Louise will beat me to death for following her honest feelings.)"\n    voice "ch6.2_l_001"',
    )
    (ROOT / "game/chapters/6/script-ch6_2.rpy").write_text(script)
    for lang in ("russian", "japanese"):
        for bucket in ("dialogs", "choises"):
            p = ROOT / "game/tl" / lang / f"{bucket}.rpy"
            lines = p.read_text().splitlines()
            for i, line in enumerate(lines):
                if not line.startswith('    old "[PROVISIONAL EN] '):
                    continue
                key = line[len('    old "'):-1]
                if key not in by_key:
                    continue
                en, ru = by_key[key]
                lines[i] = f'    old "{esc(en)}"'
                if i + 1 < len(lines) and lines[i + 1].startswith('    new "'):
                    if lang == "russian":
                        lines[i + 1] = f'    new "{esc(ru)}"'
                    # Japanese new is canonical and must remain byte-for-byte unchanged.
            p.write_text("\n".join(lines) + "\n")

    thought_path = ROOT / "game/tl/japanese/thoughs.rpy"
    ru_thought_path = ROOT / "game/tl/russian/thoughs.rpy"
    marker = "# ===== ch6_2 provisional source port ====="
    ja_text = thought_path.read_text().split(marker, 1)[0].rstrip() + "\n\n" + marker + "\n"
    ru_text = ru_thought_path.read_text().split(marker, 1)[0].rstrip() + "\n\n" + marker + "\n"
    ja_values = {
        "thought_360_s": "さすがは一国の女王陛下だな。 市場を見て、そういうことまで考えるんだ",
        "thought_365_s": "元気にはなってくれたみたいだ。 食事のせいかどうかは分かんないけどさ",
        "thought_370_s": "どうしよう……勝手にお姫さまを連れ出して １日街をぶらついてたなんて白状したら、 ルイズにお仕置きされるよなぁ、絶対",
        "thought_370_s_2": "でも、このまま帰っても、 素直な感情に従ったルイズに、 撲殺されるんだろうなぁ",
    }
    for key, (en, ru) in THOUGHTS.items():
        ja_text += f'    old "{esc(en)}"\n    new "{esc(ja_values[key])}"\n\n'
        ru_text += f'    old "{esc(en)}"\n    new "{esc(ru).replace("(", "*").replace(")", "*")}"\n\n'
    thought_path.write_text(ja_text)
    ru_thought_path.write_text(ru_text)

if __name__ == "__main__":
    main()
