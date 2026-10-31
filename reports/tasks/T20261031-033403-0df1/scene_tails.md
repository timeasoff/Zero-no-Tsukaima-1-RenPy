
## SCENE_0428  bytes=8627 lines=113
HEAD:
  | reset();
  | back();
  | set("stage", {opacity = 100,y = 0,show = 1,level = 200,x = 0,image = (0x02000000 +71)});
  | trans("crossfade", 1000);
  | set("bgm", {fadetime = 0,play = (0x03000000 +25)});
  | set("lay20", {opacity = 100,y = 0,yFrom = 0,show = 1,moveTime = 100,xFrom = 14,level = 160,opacityFrom = 0,dr = "1A",opacityTime = 100,x = 64,lv = 0,image = (0x
TAIL:
  | set("se1", {stop = 1});
  | set("bgm", {stop = 4000});
  | set("lay8", {opacity = 0,y = 0,yFrom = 0,moveTime = 100,xFrom = -96,opacityFrom = 100,hide = 1,opacityTime = 100,x = -46});
  | set("lay5", {opacity = 0,y = 0,yFrom = 0,moveTime = 100,xFrom = 224,opacityFrom = 100,hide = 1,opacityTime = 100,x = 274});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 4000});
  | waitTime(5000, true);
  | next((0x01000000 +430), true);
  | 
next()/goto refs: ['next((0x01000000 +430), true);']

## SCENE_0429  bytes=14481 lines=200
HEAD:
  | reset();
  | title("魅惑のお姫さま");
  | tndl(null);
  | beginSkip();
  | msgoff()
  | back();
TAIL:
  | msgoff()
  | set("se1", {stop = 1});
  | set("bgm", {stop = 1000});
  | set("lay5", {show = 0});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 1000});
  | waitTime(1000, true);
  | syssave();
  | 
next()/goto refs: []

## SCENE_0430  bytes=16401 lines=227
HEAD:
  | reset();
  | movie(1);
  | set("bgm", {fadetime = 0,play = (0x03000000 +4)});
  | back();
  | set("stage", {opacity = 100,y = 0,show = 1,level = 200,x = 0,image = (0x02000000 +88)});
  | trans("crossfade", 1000);
TAIL:
  | set("bgm", {stop = 1000});
  | set("lay5", {opacity = 0,y = 0,yFrom = 0,moveTime = 100,xFrom = 224,opacityFrom = 100,hide = 1,opacityTime = 100,x = 274});
  | set("lay1", {opacity = 0,y = 0,yFrom = 0,moveTime = 100,xFrom = -96,opacityFrom = 100,hide = 1,opacityTime = 100,x = -46});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 1000});
  | waitTime(1000, true);
  | setClear();
  | syssave();
  | 
next()/goto refs: []

## SCENE_0768  bytes=7243 lines=119
HEAD:
  | if (isJump()){
  | reset();
  | set("bgm", {play = (0x03000000 +30)});
  | set("stage", {opacity = 100,y = 0,show = 1,level = 200,x = 0,image = (0x02000000 +29)});
  | }
  | set("lay0", {opacity = 100,y = 0,yFrom = 0,show = 1,moveTime = 100,xFrom = -146,level = 160,opacityFrom = 0,dr = "1A",opacityTime = 100,x = -96,lv = 0,image = (
TAIL:
  | set("se1", {stop = 1});
  | set("bgm", {stop = 4000});
  | set("lay1", {show = 0});
  | set("lay5", {show = 0});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 4000});
  | waitTime(5000, true);
  | next((0x01000000 +770), true);
  | 
next()/goto refs: ['next((0x01000000 +770), true);']

## SCENE_0769  bytes=15544 lines=224
HEAD:
  | reset();
  | title("小悪魔のおしおき");
  | tndl(null);
  | beginSkip();
  | msgoff()
  | back();
TAIL:
  | set("se1", {stop = 1});
  | set("bgm", {stop = 1000});
  | set("lay1", {show = 0});
  | set("lay5", {show = 0});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 1000});
  | waitTime(1000, true);
  | syssave();
  | 
next()/goto refs: []

## SCENE_0770  bytes=13813 lines=204
HEAD:
  | reset();
  | movie(1);
  | set("bgm", {fadetime = 0,play = (0x03000000 +4)});
  | back();
  | set("stage", {opacity = 100,y = 0,show = 1,level = 200,x = 0,image = (0x02000000 +88)});
  | trans("crossfade", 1000);
TAIL:
  | set("se1", {stop = 1});
  | set("bgm", {stop = 1000});
  | set("lay5", {show = 0});
  | set("stage", {opacity = 0,hide = 1,opacityTime = 1000});
  | waitTime(1000, true);
  | setClear();
  | syssave();
  | 
next()/goto refs: []

## SCENE_0771  bytes=22294 lines=276
HEAD:
  | reset();
  | title("サイトのメイド");
  | tndl(null);
  | back();
  | set("stage", {opacity = 100,y = 0,show = 1,level = 200,x = 0,image = (0x02000000 +88)});
  | trans("crossfade", 1000);
TAIL:
  | set("lay5", {y = 0,show = 1,level = 160,imageType = 2,dr = "2A",imageTime = 300,x = 224,lv = 0,image = (0x02000000 +429)});
  | talk("サイト", null, "で、ですよね。\nじゃあ……。", (0x04000000 +12017));
  | selectInit();
  | selectItem("キュルケのメイドってのは？", (0x01000000 +772), null, true);
  | selectItem("タバサのメイドってのは？", (0x01000000 +773), null, true);
  | selectItem("ギーシュのメイドってのは？", (0x01000000 +774), null, true);
  | select();
  | 
next()/goto refs: []
