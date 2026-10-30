# Chapter 6, part 2: source scenes 360-374.
# Source: ps2_source/chapters/chapter_07_家出のお姫さま.txt.
# English and Russian text edited from the canonical Japanese source.

label ch6_2:
    # Source scene 360
    $ fade_fx("id(38)", new_music="t30")
    voice "ch6.2_h_001"
    h "This place is even livelier than anywhere we've been so far."
    voice "ch6.2_s_001"
    s "This seems to be the heart of the market."
    voice "ch6.2_h_002"
    h "I'm glad."
    voice "ch6.2_s_002"
    s "Hm?"
    voice "ch6.2_h_003"
    h "If the market is bustling, then the people's lives cannot be all that miserable."
    th "(She's truly a queen. She sees all that just by looking at the market.)"
    voice "ch6.2_s_003"
    s "I never looked at it that way. You're something else, Princess. You really think like a politician."
    voice "ch6.2_h_004"
    h "It is hardly something to praise me for. I rarely have the chance to see a market like this for myself."
    voice "ch6.2_h_005"
    h "Ah, but perhaps that is why it makes me happy."
    voice "ch6.2_s_004"
    s "Huh?"
    voice "ch6.2_h_006"
    h "You see, this view used to be a world beyond my window. Now it is right here, close enough to touch."
    voice "ch6.2_s_005"
    s "It's just an ordinary sight to me."
    voice "ch6.2_h_007"
    h "What is ordinary to you is special to me. I have not had this much fun in a long time."
    voice "ch6.2_s_006"
    s "Then I'm glad."
    voice "ch6.2_h_008"
    h "Oh? It sounds like there is a quarrel over there..."
    voice "ch6.2_customer_001"
    customer "Hey, aren't these dried goods even more expensive than last time?"
    voice "ch6.2_merchant_001"
    merchant "What can I do? The army keeps seizing our ships, so our catch just keeps shrinking."
    voice "ch6.2_customer_002"
    customer "Good grief. Everywhere I go, it's one gloomy story after another."
    voice "ch6.2_merchant_002"
    merchant "It can't be helped. Ever since Her Majesty started this war, business has slumped and the army has run wild."
    voice "ch6.2_merchant_003"
    merchant "Nothing good has come of it."
    voice "ch6.2_customer_003"
    customer "Well, I suppose it's no wonder. What can you expect from such a young, ignorant queen?"
    voice "ch6.2_h_009"
    h "..."
    voice "ch6.2_s_007"
    s "Uh, hey! Princess, let's go look over there!"
    voice "ch6.2_s_008"
    s "Whew..."
    voice "ch6.2_h_010"
    h "The people are honest. They openly say what is making their lives difficult and who is to blame."
    voice "ch6.2_s_009"
    s "Um, Princess."
    menu:
        "Don't let it get to you":
            jump ch6_2_s361
        "What matters is what you do from here on":
            jump ch6_2_s362
        "There are all kinds of people":
            jump ch6_2_s363

label ch6_2_s361:
    # Source scene 361
    $ fade_fx("id(58)", new_music="t30")
    voice "ch6.2_s_010"
    s "Don't let it get to you."
    voice "ch6.2_h_011"
    h "Hm?"
    voice "ch6.2_s_011"
    s "No, listening to them matters, but one person's voice doesn't necessarily represent everyone's opinion, right?"
    voice "ch6.2_s_012"
    s "That merchant might just be using the war as an excuse to raise his prices..."
    voice "ch6.2_s_013"
    s "You should do what you think is right, Princess. I'm sure of it."
    voice "ch6.2_h_012"
    h "Thank you, familiar."
    jump ch6_2_s364

label ch6_2_s362:
    # Source scene 362
    $ fade_fx("id(58)", new_music="t30")
    voice "ch6.2_s_014"
    s "What matters is what you do from here on."
    voice "ch6.2_h_013"
    h "From here on...?"
    voice "ch6.2_s_015"
    s "Now you know what people think. You can use that as a hint for deciding what to do next."
    voice "ch6.2_h_014"
    h "Oh... So it is all right to look at it that way."
    voice "ch6.2_s_016"
    s "Exactly. People say some pretty irresponsible things. The Internet is the same way."
    voice "ch6.2_h_015"
    h "The Internet?"
    voice "ch6.2_s_017"
    s "Ah, I was just talking to myself. Just mumbling."
    voice "ch6.2_h_016"
    h "I see. But thank you. I feel a little better now."
    jump ch6_2_s364

label ch6_2_s363:
    # Source scene 363
    $ fade_fx("id(58)", new_music="t30")
    voice "ch6.2_s_018"
    s "There are all kinds of people in the world."
    voice "ch6.2_h_017"
    h "All kinds...?"
    voice "ch6.2_s_019"
    s "When something happens, some people will think it's good, while others will think it's bad."
    voice "ch6.2_s_020"
    s "So you just have to work to make more people see it as something good."
    voice "ch6.2_h_018"
    h "Is it really that simple?"
    voice "ch6.2_s_021"
    s "Well, it's easy to say. But you have plenty of time ahead of you."
    voice "ch6.2_h_019"
    h "Indeed. I have only just become queen. Expecting everyone to accept me already would be greedy."
    voice "ch6.2_s_022"
    s "Oh, I didn't mean quite that much."
    jump ch6_2_s364

label ch6_2_s364:
    # Source scene 364
    $ fade_fx("id(58)", new_music="t30")
    voice "ch6.2_h_020"
    h "In any case, I still have a long way to go as queen, don't I...?"
    voice "ch6.2_s_023"
    s "You shouldn't look so down... Wait! I know just the place to take you!"
    voice "ch6.2_h_021"
    h "Huh? Oh, familiar, wait for me!"
    jump ch6_2_s365

label ch6_2_s365:
    # Source scene 365
    $ fade_fx("id(44)", new_music="t20")
    voice "ch6.2_h_022"
    h "Is this the place that is supposed to cheer me up...? This is a dining hall, isn't it?"
    voice "ch6.2_s_024"
    s "That's right. When you're feeling down, the best thing is to eat!"
    voice "ch6.2_shopkeeper_001"
    shopkeeper "Here you go! Sorry to keep you waiting!"
    voice "ch6.2_s_025"
    s "There it is! Go on, try it. The meat dishes here are delicious!"
    voice "ch6.2_h_023"
    h "Oh, all right. This is grilled fish... And this is vegetable soup."
    voice "ch6.2_s_026"
    s "Looks good, doesn't it? Come on, eat up!"
    voice "ch6.2_h_024"
    h "Oh, all right. Great Founder Brimir, thank you for this humble meal this morning..."
    voice "ch6.2_s_027"
    s "A-are you going to do that here too?"
    voice "ch6.2_h_025"
    h "Then I shall partake... Munch."
    voice "ch6.2_s_028"
    s "How is it? How is it?"
    voice "ch6.2_h_026"
    h "It is delicious!"
    voice "ch6.2_s_029"
    s "See?"
    voice "ch6.2_h_027"
    h "Do you all always eat such delicious food?"
    voice "ch6.2_s_030"
    s "The food at the castle is probably fancier, but this place is pretty good too, right?"
    th "(It seems to have cheered her up. Whether the food had anything to do with it, I have no idea.)"
    voice "ch6.2_h_028"
    h "You know so much, familiar."
    voice "ch6.2_s_031"
    s "Not really. I know absolutely nothing about this world... I mean, this country."
    voice "ch6.2_h_029"
    h "Ah, now that you mention it, that is true."
    voice "ch6.2_s_032"
    s "Yes?"
    voice "ch6.2_h_030"
    h "Louise told me that you are from another world."
    voice "ch6.2_s_033"
    s "Well, that's true."
    voice "ch6.2_h_031"
    h "I have wanted to ask you this for a while. What is your world like?"
    voice "ch6.2_s_034"
    s "What is it like...? Well, let's see..."
    menu:
        "A world without kings":
            jump ch6_2_s366
        "A world without magic":
            jump ch6_2_s367
        "A world without night":
            jump ch6_2_s368

label ch6_2_s366:
    # Source scene 366
    $ fade_fx("id(44)", new_music="t20")
    voice "ch6.2_s_035"
    s "It is a world without kings."
    voice "ch6.2_h_032"
    h "No king!? Then who rules the country, and how?"
    voice "ch6.2_s_036"
    s "Well, some countries do have kings, but they don't hold any real power."
    voice "ch6.2_h_033"
    h "I see..."
    jump ch6_2_s369

label ch6_2_s367:
    # Source scene 367
    $ fade_fx("id(44)", new_music="t20")
    voice "ch6.2_s_037"
    s "It is a world without magic."
    voice "ch6.2_h_034"
    h "Without magic...? That sounds like a very inconvenient world."
    voice "ch6.2_s_038"
    s "Well, not really. We have science instead of magic."
    voice "ch6.2_h_035"
    h "Science...?"
    jump ch6_2_s369

label ch6_2_s368:
    # Source scene 368
    $ fade_fx("id(44)", new_music="t20")
    voice "ch6.2_s_039"
    s "A world without night, so to speak."
    voice "ch6.2_h_036"
    h "There is no night!? Do you mean the sun stays out and it is always daytime?"
    voice "ch6.2_s_040"
    s "Well, to be precise, lights stay on even at night, so the darkness is gradually disappearing."
    voice "ch6.2_h_037"
    h "I see. But then you must spend an enormous amount on firewood."
    voice "ch6.2_s_041"
    s "Huh? Oh, we don't use firewood. We light everything with electricity."
    voice "ch6.2_h_038"
    h "Electricity?"
    voice "ch6.2_s_042"
    s "Lightning... Something like that."
    voice "ch6.2_h_039"
    h "Lightning...? I see."
    jump ch6_2_s369

label ch6_2_s369:
    # Source scene 369
    $ fade_fx("id(44)", new_music="t20")
    voice "ch6.2_h_040"
    h "Who rules your world?"
    voice "ch6.2_s_043"
    s "In the country I came from, everyone votes to choose members of the national assembly..."
    voice "ch6.2_h_041"
    h "The national assembly? Members?"
    voice "ch6.2_s_044"
    s "The national assembly is divided into two houses, the House of Representatives and the House of Councillors, and, uh... I should have studied this a little more..."
    voice "ch6.2_s_045"
    s "Anyway, there is no king. Everyone chooses the people who will govern the country."
    voice "ch6.2_h_042"
    h "The people choose their own leader...? Is such a thing really possible?"
    voice "ch6.2_s_046"
    s "Yes, that's how it was in my country."
    voice "ch6.2_h_043"
    h "I cannot imagine a world without kings. So there are countries like that in other worlds."
    voice "ch6.2_s_047"
    s "I-I don't know if it's really that amazing."
    jump ch6_2_s370

label ch6_2_s370:
    # Source scene 370
    $ fade_fx("id(60)", new_music="t19")
    voice "ch6.2_h_044"
    h "This was supposed to be a morning walk, but it has become quite dark."
    voice "ch6.2_s_048"
    s "Yeah, I guess it has... Ha ha ha."
    th "(What am I going to do...? If I confess that I took the princess out without permission and wandered around town with her all day, Louise will punish me for sure.)"
    voice "ch6.2_h_045"
    h "What is the matter? Is something worrying you?"
    voice "ch6.2_s_049"
    s "I was just thinking that Louise is going to be furious if I go back like this."
    voice "ch6.2_h_046"
    h "Ah, I see... Hee hee. I found myself a little envious of Louise."
    voice "ch6.2_s_050"
    s "Huh?"
    voice "ch6.2_h_047"
    h "It is enviable to have someone you can be comfortable with."
    voice "ch6.2_s_051"
    s "Huh? Sorry, but who is comfortable with whom?"
    voice "ch6.2_h_048"
    h "Louise, of course, with you. The fact that she shows you her honest emotions proves that she trusts you, does it not?"
    voice "ch6.2_s_052"
    s "You think so?"
    voice "ch6.2_h_049"
    h "I envy you greatly for having time to spend together while showing your true selves."
    voice "ch6.2_h_050"
    h "I am always putting on the face of a queen..."
    voice "ch6.2_s_053"
    s "Is that how it is...?"
    th "(But if I go back now, Louise will beat me to death for making her act on her honest feelings.)"
    voice "ch6.2_l_001"
    l "Now then, my excellent familiar, would you explain how this happened?"
    voice "ch6.2_s_054"
    s "Ah, she really is angry."
    voice "ch6.2_l_002"
    l "Of course I am! I woke up to find the princess gone, and you had disappeared too!"
    voice "ch6.2_l_003"
    l "And you didn't contact anyone until sunset!"
    voice "ch6.2_l_004"
    l "I am amazed at my own trust and patience for waiting for you instead of reporting this to the palace!"
    voice "ch6.2_s_055"
    s "That surprised me too."
    voice "ch6.2_l_005"
    l "So. Is there anything you want to say before I have the last word?"
    voice "ch6.2_s_056"
    s "Well..."
    menu:
        "It wasn't my fault!":
            jump ch6_2_s371
        "I have no regrets about my date with the princess!":
            jump ch6_2_s372
        "I went to see how things were in town...":
            jump ch6_2_s373

label ch6_2_s371:
    # Source scene 371
    $ fade_fx("id(43)", new_music="t29")
    voice "ch6.2_s_057"
    s "It wasn't my fault! I was only accompanying the princess on her morning walk after she got up early!"
    voice "ch6.2_l_006"
    l "Oh, is that so?"
    voice "ch6.2_s_058"
    s "That's right. You understand now, don't you?"
    voice "ch6.2_l_007"
    l "As if I would! If you're going to lie, at least tell a better one!"
    jump ch6_2_s374

label ch6_2_s372:
    # Source scene 372
    $ fade_fx("id(43)", new_music="t29")
    voice "ch6.2_s_059"
    s "No regrets about my date with the princess! She asked me to show her the sights, so we went all over town! That was definitely a date!"
    voice "ch6.2_l_008"
    l "..."
    voice "ch6.2_s_060"
    s "Hey, the princess had fun too, so I have no regrets. Ha ha ha."
    voice "ch6.2_l_009"
    l "...I see. Then I won't have to hold back either."
    jump ch6_2_s374

label ch6_2_s373:
    # Source scene 373
    $ fade_fx("id(43)", new_music="t29")
    voice "ch6.2_s_061"
    s "I went to see how things were in town. We visited crowded places and listened to what people were saying."
    voice "ch6.2_l_010"
    l "I see... So the princess is still wavering in her confidence as queen."
    voice "ch6.2_s_062"
    s "Yeah. So I took her to a dining hall to help take her mind off it."
    voice "ch6.2_l_011"
    l "So you were late because of your detour after all!?"
    voice "ch6.2_s_063"
    s "I-I guess that's true... Yes, I suppose so."
    jump ch6_2_s374

label ch6_2_s374:
    # Source scene 374
    $ fade_fx("id(43)", new_music="t29")
    voice "ch6.2_l_012"
    l "What would you have done if something had happened to the princess? You stupid mutt!"
    voice "ch6.2_s_064"
    s "Aaaaaaagh!"
    jump attention
