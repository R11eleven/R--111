transform custom_farright:
    xalign 0.8
    xoffset 1000
    yalign 1.0
    zoom 0.8

transform custom_farleft:
    xalign 0.8
    xoffset 1000
    yalign 1.0
    zoom 0.7


## 角色 ######################################################################
define Mi = Character("Mithar", image="Mithar")
define Cr = Character("Crate", image="Crate")
define Crate_ = Character("???", image="Crate")
define npc = Character("路人")
define writer = Character("旁白")
define soldier = Character("军队")

## 角色图 ####################################################################

## Mithar ##
image Mi1 = "images/character/second/Mithar/young_1.png"
image Mi2 = "images/character/second/Mithar/young_happy.png"
image Mi3 = "images/character/second/Mithar/young_hurt.png"
image Mi4 = "images/character/second/Mithar/young_2.png"
image Mi_normal = "images/character/second/Mithar/normal.png"
image Mi_worry = "images/character/second/Mithar/worry.png"
image Mi_smile = "images/character/second/Mithar/smile.png"
image Mi_angry = "images/character/second/Mithar/angry.png"
image Mi_confuse = "images/character/second/Mithar/confuse.png"

## Crate ##
image Cr_normal = "images/character/god/Crate/normal.png"
image Cr_angry = "images/character/god/Crate/angry.png"
image Cr_worry =  "images/character/god/Crate/worry.png"
image Cr_happy = "images/character/god/Crate/happy.png"
image Cr_confuse = "images/character/god/Crate/confuse.png"
image Cr_yeah = "images/character/god/Crate/yeah.png"


## 场景 #####################################################################
image bg_street_full = im.Scale(
    "images/venue/street.jpg",
    3840, 2160
)

image cr1 = im.Scale(
    "images/cg/cr1.png",
    3840, 2160
)

image cr2 = im.Scale(
    "images/cg/cr2.png",
    3840, 2160
)

image chapter = im.Scale(
    "gui/chapter.png",
    3840, 2160
)

image die = im.Scale(
    "images/venue/die.png",
    3840, 2160
)


label start:
    jump chapter_1


## 第一章 ####################################################################
label chapter_1:

    screen dizzy_text(duration=2):
        timer duration action Hide("dizzy_text")
        text "我得赶紧回家..." align (0.5, 0.5):
            size 60
            color "#FFFFFF"
            at dizzy_transform()
    pause
    hide screen dizzy_text

    transform dizzy_transform():
        # 基础抖动
        xalign 0.5
        yalign 0.5
        parallel:
            xoffset 0
            linear 0.1 xoffset 5
            linear 0.1 xoffset -5
            linear 0.1 xoffset 3
            linear 0.1 xoffset -3
            repeat
        parallel:
            yoffset 0
            linear 0.15 yoffset 3
            linear 0.15 yoffset -3
            linear 0.1 yoffset 2
            linear 0.1 yoffset -2
            repeat
        parallel:
            rotate 0
            linear 0.3 rotate 2
            linear 0.3 rotate -2
            linear 0.2 rotate 1
            linear 0.2 rotate -1
            repeat

    stop music fadeout 2.0
    pause 2.0
    play music "audio/ear.mp3"
    
    show screen dizzy_text

    pause 
    play music "audio/game_music.mp3" fadein 3.0 loop volume 0.2

    show chapter with dissolve

    show screen screen_text("欢迎来到第一章", duration=2.5)
    pause 2.5
    hide screen screen_text

    show screen screen_text("本章您的视角是——Mithar", duration=2.5)
    pause 2.5
    hide screen screen_text

    show screen screen_text("游玩建议佩戴耳机", duration=2.5)
    pause 2.5
    hide screen screen_text

## 剧情正式部分 ##########################################################
    scene bg_street_full with dissolve

    show Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "{cps=25}大清洗开始了..."
    Mi "{cps=25}要回家…妹妹还在等我和她玩捉迷藏..."
    Mi "{cps=25}唔！..."

    hide Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    writer "{cps=25}Mithar被拥挤的人群推到在地"

    npc "{cps=25}让开啦！红毛章鱼小鬼！"
    npc "{cps=25}什么时候大少爷也需要在大清洗的时候上街了？这里可没人保护你"

    show Mi3 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "{cps=25}..."
    Mi "{cps=25}（不和这些人计较...当务之急是赶紧回家）"
    Mi "{cps=25}还有，不能被军队的人发现"

    hide Mi3 onlayer screens at custom_farright zorder 200 with dissolve

    soldier "{cps=25}今日"
    soldier "{cps=25}大天使长将亲自督察地狱的傲慢城中大清洗"
    soldier "{cps=25}重点检查市中心地区"

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}啧，我运气这么差吗"
    Mi "{cps=25}看来我今天就是要死在这里了..."
    Mi "{cps=25}事到如今还能怎么办"
    Mi "{cps=25}跑是肯定跑不掉的"
    Mi "{cps=25}打，也是不现实的"
    Mi "{cps=25}躲起来...他们为了杀那几个邪祟都能把别人家翻个底朝天..."
    Mi "{cps=25}能藏哪儿呢"

    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    soldier "{cps=25}往这边搜搜，这边有邪祟的熵能残余"

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}靠"
    Mi "{cps=25}我运气就这么差吗..."
    Mi "{cps=25}感觉目前除了神仙显灵以外，想不到怎么活"
    Mi "{cps=25}先赶紧走吧，前面就有岔路，尝试一下甩掉他们吧"

    menu:
        "往左走":
            Mi "{cps=25}这里是死路"
            narrator "{cps=25}是不是还没有养成看到选项就存档的习惯？"
            narrator "{cps=25}这次放过你，下次记得存档"

        "往右走":
            Mi "{cps=25}这条路走得通，快走..."
    
    Mi "{cps=25}唔..."
    Mi "{cps=25}我又撞到谁了..."

    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    window hide

    show cr1 with fade
    pause
    show cr2
    pause

    scene bg_street_full with dissolve
    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    window show
    Mi "{cps=25}(这人长得好奇怪)"
    Mi "{cps=25}对不起，刚刚没注意看路"
    Mi "{cps=25}抱歉"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve
    Crate_ "{cps=25}..."
    show Cr_happy onlayer screens at custom_farleft zorder 200
    Crate_ "{cps=25}你好，Mithar"
    hide Cr_normal onlayer screens at custom_farleft zorder 200
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}我们认识...?"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve
    Crate_ "{cps=25}现在的你确实不认识"
    Crate_ "{cps=25}不过我们现在就可以认识一下"
    Cr "{cps=25}我叫Crate"

    show screen screen_text("Crate了解度+5", duration=2.5)
    pause 2.5
    hide screen screen_text
    $ add_understanding("Crate", 5)

    Cr "{cps=25}你的头发像玫瑰花一样，真好看"
    Cr "{cps=25}眼睛也好看"
    Cr "{cps=25}我很喜欢"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}（我是遇到什么人贩子了吗）"
    Mi "{cps=25}那个...我得回家了..."
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}Mithar，成为我的学生"
    Cr "{cps=25}你很稀有，我感兴趣"
    hide Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "..."

    menu :
        "我不认识您...":
            jump story1
        "您是坏人吗？":
            jump story2
        "要学生做什么？":
            jump story3

    

label story1:

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}对不起，我得走了，我家里人还在等我"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}行啊（侧身让路）"
    Cr "{cps=25}你现在回家，会在踏进家门前三步中弹"
    Cr "{cps=25}而且会把军队引到家里去"
    show Cr_happy onlayer screens at custom_farleft zorder 200
    Cr "{cps=25}大概在中午十二点你就会死~"
    hide Cr_normal onlayer screens at custom_farleft zorder 200
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi3 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}您...您在吓唬小孩！"
    Mi "{cps=25}我看起来有这么好骗吗"
    Mi "{cps=25}我得回家了，我不会和你走的，怪女人！"
    hide Mi3 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_angry onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}那你去啊！反正死了还得我来救"
    Cr "{cps=25}你去呗！"
    hide Cr_angry onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi3 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}..."
    Mi "{cps=25}？"
    hide Mi3 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_angry onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}去啊"
    hide Cr_angry onlayer screens at custom_farleft zorder 200 with dissolve

    soldier "{cps=25}这边！大家来这边搜一搜"

    show Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}你刚刚对我说话态度太差了"
    Cr "{cps=25}你现在求求我，我就考虑考虑帮帮你~"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    menu :
        "求求您帮帮我吧":
            jump story4
        "不要你帮":
            jump story5

label story2:

    hide Mi4 onlayer screens at custom_farright zorder 200        
    show Mi3 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}您是坏人吗"
    hide Mi3 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}我觉得我不算"
    Cr "{cps=25}尤其是对你Mithar来说，我绝对不是坏人"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    soldier "这边！大家来这边好好搜一搜！"

    show Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}好啦，快和我走吧~"
    hide Cr_normal onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    menu :
        "好":
            jump story4
        "不要":
            jump story1
        

label story3:

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}您是老师吗？要学生做什么？"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}我不是老师也不影响你成为我的学生呀~"
    Cr "{cps=25}我肯定教的好你~"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}为什么非要是我？我对你来说很特殊吗"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    show Cr_confuse onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}我不是说过了吗"
    Cr "{cps=25}因为你的头发和眼睛都很好看啊"
    hide Cr_confuse onlayer screens at custom_farleft zorder 200
    show Cr_happy onlayer screens at custom_farleft zorder 200
    Cr "{cps=25}像玫瑰一样"
    hide Cr_happy onlayer screens at custom_farleft zorder 200
    show Cr_normal onlayer screens at custom_farleft zorder 200
    Cr "{cps=25}不过你确实也对我很重要"
    Cr "{cps=25}但最重要的是因为，我答应你了要这么做"
    Cr "{cps=25}我现在是在履行我的承诺"
    hide Cr_normal onlayer screens at custom_farleft zorder 200
    show Cr_happy onlayer screens at custom_farleft zorder 200
    Cr "{cps=25}我可从来不对你撒谎~"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=25}（感觉完全无法和她沟通）"
    Mi "{cps=25}（说的什么一句都听不懂）"
    hide Mi4 onlayer screens at custom_farright zorder 200 with dissolve

    soldier "这边！大家来这边好好搜一搜！"

    show Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve
    Cr "{cps=25}总之，跟我来吧"
    hide Cr_happy onlayer screens at custom_farleft zorder 200 with dissolve

    menu :
        "好":
            jump story4
        "不要":
            jump story1

label story4:

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=15}请您帮帮我...{nw}"
    stop music
    scene black
    hide Mi4 onlayer screens at custom_farright zorder 200
    window hide

    scene black 
    play sound "audio/bang.mp3"

    show expression Solid("#000000") as black_screen:
        xalign 0.5 yalign 0.5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.03 xoffset 3
        linear 0.03 xoffset -3

    pause

    screen dizzy_text2(duration=2):
        zorder 200
        timer duration action Hide("dizzy_text")
        text "发生什么了" align (0.5, 0.5):
            size 100
            color "#FFFFFF"
            at dizzy_transform()
        
    show die:
        alpha 0.0
        xalign 0.5
        yalign 0.5
        zoom 1.0
        # 缓慢淡入
        linear 2.0 alpha 0.7

    play sound "audio/ear.mp3"

    show screen dizzy_text2(duration = 2)
    pause
    hide screen dizzy_text2

    show chapter with dissolve

    show screen screen_text("Mithar了解度+10", duration=2.5)
    pause 2.5
    hide screen screen_text

    $ add_understanding("Mithar", 10)

    show screen screen_text("第一章已结束", duration=2.5)
    pause 2.5
    show screen screen_text("玩家可以游玩第二关", duration=2.5)
    pause 2.5

    $ persistent.chapter1_completed = True
    return

label story5:

    show Mi4 onlayer screens at custom_farright zorder 200 with dissolve
    Mi "{cps=15}我才不要你帮.{nw}"
    stop music
    scene black
    hide Mi4 onlayer screens at custom_farright zorder 200
    window hide

    scene black 
    play sound "audio/bang.mp3"

    show expression Solid("#000000") as black_screen:
        xalign 0.5 yalign 0.5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.03 xoffset 3
        linear 0.03 xoffset -3

    pause

    screen dizzy_text2(duration=2):
        zorder 200
        timer duration action Hide("dizzy_text")
        text "发生什么了" align (0.5, 0.5):
            size 100
            color "#FFFFFF"
            at dizzy_transform()
        
    show die:
        alpha 0.0
        xalign 0.5
        yalign 0.5
        zoom 1.0
        # 缓慢淡入
        linear 2.0 alpha 0.7

    play sound "audio/ear.mp3"

    show screen dizzy_text2(duration = 2)
    pause
    hide screen dizzy_text2

    show chapter with dissolve

    show screen screen_text("Mithar了解度+10", duration=2.5)
    pause 2.5
    hide screen screen_text

    $ add_understanding("Mithar", 10)

    show screen screen_text("第一章已结束", duration=2.5)
    pause 2.5
    show screen screen_text("第二章已解锁", duration=2.5)
    pause 2.5
    $ persistent.chapter1_completed = True

    return


## 第二章 #################################################################
label chapter_2:
    scene bg_street_full

    show Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "欢迎来到第二章"

    $ persistent.chapter2_completed = True
    return


label chapter_3:
    scene bg_street_full

    show Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "欢迎来到第三章"

    $ persistent.chapter3_completed = True
    return


label chapter_4:
    scene bg_street_full

    show Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "欢迎来到第四章"

    $ persistent.chapter4_completed = True
    return


label chapter_5:
    scene bg_street_full

    show Mi1 onlayer screens at custom_farright zorder 200 with dissolve

    Mi "欢迎来到第五章"

    $ persistent.chapter5_completed = True
    return
