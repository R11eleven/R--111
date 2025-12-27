init python:
    # 更结构化的角色信息数据库。
    # 包含显示名称、立绘路径以及一个用于标签页的嵌套字典。
    character_details_db = {
        "Mithar": {
            "display_name": "Mithar",
            "image": "images/character/second/Mithar/normal.png",
            "tabs": {
                "basic": {
                    "title": "基本介绍",
                    "content_type": "grid",
                    "required_understanding": 1,
                    "content": [
                        ("姓名", "Mithar"),
                        ("年龄", "17（剧情中大部分时候是的^^）"),
                        ("身高", "188cm"),
                        ("生日", "9/9"),
                        ("种族", "蓝环章鱼"),
                        ("MBTI", "INFJ"),
                    ]
                },
                "personality": {
                    "title": "性格简介",
                    "content_type": "text",
                    "required_understanding": 20,
                    "content": """Mithar的性格底色里有一种近乎天真的温和，这种温和不是软弱，更像是一种历经变故后选择与世界和解的坦然。他给人的第一印象总是很好相处，说话时带着点懒洋洋的笑意，好像没什么能真正让他着急上火。但这其实是一种巧妙的伪装，或者说，是一种节能模式。他骨子里享受独处远胜于热闹，那些看似开朗健谈的时刻，更多是出于习惯性的礼貌和体贴，好让场面不那么尴尬。

他本质上是个感情浓度很高的人，对情绪的感知异常敏锐，总能察觉到身边人细微的变化。这让他显得很善解人意，但同时也是一种负担，因为他往往会不自觉地背负起他人的情绪。他欣赏感性远胜于纯粹的理性，认为后者在某些时刻显得过于冰冷和残忍，尽管他自己在必要时也能展现出近乎冷酷的理智。

现世的Mithar比起前世，少了几分游刃有余的腹黑，多了些未被磨平的少年心性。他贪玩，尤其沉迷那些能让他暂时放空大脑的FPS游戏；他也有些懒散，对于需要耗费大量心神去筹谋布局的事情，能避则避。但这不代表他无能，相反，他的上限很高，只是大多数时候，他宁愿选择更简单直接（哪怕看起来没那么强）的方式解决问题，因为“动脑子实在太累了”。

他的善良是毋庸置疑的，甚至有些过于柔软，尤其在面对自己在乎的人时。这种柔软偶尔会显得懦弱，比如在早期，他可能不太懂得如何强硬地表达反对或设立边界。但随着经历增长，他正在慢慢学习如何温柔而坚定地守护自己的立场。他就像一株适应性很强的植物，外表柔软，内在却有不易折断的韧性。"""
                },
                "appearance": {
                    "title": "外貌设定",
                    "content_type": "text",
                    "required_understanding": 40,
                    "content": "无论是什么时期的Mithar都很喜欢无印风的穿搭，实话实说他衣品不错，他喜欢穿毛衣或者白色衬衫。现世的他会把章鱼触手给露出来，并且打了耳钉，潮男这一块。三七分的头发和小辫子是锚点的一部分，头发是红白渐变，现世Mithar还有一副红色的墨镜，他偶尔会带，他确实很喜欢这副墨镜"
                },
                "tips": {
                    "title": "小Tips",
                    "content_type": "text",
                    "required_understanding": 60,
                    "content": """1. Mithar会做饭，无论哪个时期。其实是因为Crate不会做饭；
2. Mithar是个非常细致的人，他总能明锐地捕捉别人的爱好或者情绪通过一些微小的细节；"""
                },
                "fight": {
                    "title": "战斗设定",
                    "content_type": "text",
                    "required_understanding": 80,
                    "content": """说真的Mithar不算弱，但他不怎么表现自己的实力。一是自己不喜欢打架，二是他很懒
—————————————————————————————————————
熵能——5000
使用的技巧——自身调用（内熵为主，给予熵为辅）+ 一部分外部调用
Mithar不怎么会调用熵能其实，但是他自己的熵能储备很多（毕竟是邪神来的）
Mithar没有武器，他只调用熵能。一是因为他不太需要，二是他觉得不太方便。事实上他之前配备过一把手枪，不过后来给Xenon用了 Mithar可以对自己力所能及范围的人造成一些精神上的污染和干扰，这会干扰对方使用熵能的能力 触手也是攻击手段之一，触手上的毒素往往才是致人死亡的最终原因，就算不致命，不致命但足够起到干扰的作用了
给予熵是帮助别人会san的，也可以用作治疗 Mithar的精神攻击是需要时间的（吟唱时间）需要布置陷阱让人循循诱导掉san，所以Mithar其实也没有很爱用这个技能 外部熵调用是和Crate学的，所以也是一个小空间系，可以小传送，但大多数被Mithar用来逃跑了
其实Mithar的上限很高，但有点吃手法，他打的时候需要一直动脑子，他是有点懒的，所以一般只用简单的攻击方式，看起来就不是很强"""
                }
            }
        }
    }


screen locked_content_notify():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 90
            label _("了解度不足，无法查看此内容"):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 300
                textbutton _("确定") action Hide("locked_content_notify")


screen character_detail(character):
    tag menu
    modal True
    
    # 设置一个默认显示的标签页
    default current_tab = "basic"
    
    # 从数据库中获取所选角色的所有数据
    $ char_data = character_details_db.get(character)
    $ display_name = char_data.get("display_name", character) if char_data else character
    
    # 添加标准的游戏菜单背景
    add gui.game_menu_background

    # 使用 game_menu_outer_frame 样式来获取正确的背景和布局（包括分割线）
    frame:
        style "game_menu_outer_frame"

        # 主布局容器，分为左右两部分
        hbox:
            # 左侧导航区域
            frame:
                style "game_menu_navigation_frame"
                
                # 模仿 'navigation' 屏幕的按钮列表
                vbox:
                    style_prefix "navigation"
                    xpos gui.navigation_xpos
                    yalign 0.2
                    spacing gui.navigation_spacing

                    if char_data:
                        # 根据角色数据为每个标签页创建一个按钮
                        $ tab_keys = ["basic", "personality", "appearance", "tips", "fight"]
                        $ current_understanding = understanding_dict.get(character, 0)
                        for tab_key in tab_keys:
                            if tab_key in char_data["tabs"]:
                                $ tab_info = char_data["tabs"][tab_key]
                                $ required = tab_info.get("required_understanding", 0)
                                $ unlocked = current_understanding >= required

                                $ button_title = tab_info["title"]
                                $ button_action = SetScreenVariable("current_tab", tab_key) if unlocked else Show("locked_content_notify")
                                $ button_color = gui.idle_color if unlocked else gui.insensitive_color

                                # Create the button. If the current tab is locked, default to basic.
                                if not unlocked and current_tab == tab_key:
                                    $ current_tab = "basic"

                                textbutton button_title action button_action text_color button_color

            # 右侧内容区域
            frame:
                style "game_menu_content_frame"
                
                if not char_data:
                    # 如果没有这个角色的数据，显示一条消息
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "Content for [display_name] is under construction."

                else:
                    # 右侧内容的容器
                    fixed:
                        # 添加角色立绘在右侧
                        add char_data.get("image"):
                            xalign 1.7 # 对齐到此区域的右侧
                            yalign 0.8  # 垂直居中
                            zoom 0.7

                        # 内容直接放在 viewport 中，不再需要额外的 frame
                        viewport:
                            xalign 0.0
                            yalign 0.45
                            xsize 1300
                            ysize 1500
                            # 隐藏滚动条，但仍然可以通过鼠标滚轮滚动
                            mousewheel True
                            
                            $ current_tab_data = char_data["tabs"].get(current_tab)

                            if current_tab_data:
                                vbox:
                                    # 为 vbox 内所有文本应用 encyclopedia_text 样式
                                    style_prefix "encyclopedia"
                                    spacing 15
                                    
                                    # 所选标签页的内容
                                    if current_tab_data["content_type"] == "grid":
                                        grid 2 6:
                                            xfill True
                                            spacing 20
                                            for key, value in current_tab_data["content"]:
                                                text key + "："
                                                text value
                                    else: # content_type 是 "text"
                                        text current_tab_data["content"]

    # 标题标签，显示角色名
    label display_name:
        style "game_menu_label"

    # 返回按钮
    textbutton _("返回"):
        style "return_button"
        action Return()


style encyclopedia_text is gui_text:
    font gui.interface_text_font
    size 60
    color gui.idle_color
    # 增加行间距以适应大字体
    line_spacing 30

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -90
