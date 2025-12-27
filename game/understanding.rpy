# understanding.rpy - 了解度系统核心

init python:
    # =====================
    # 1. 基础变量定义
    # =====================
    
    # 了解度字典 - 所有角色初始为0（未解锁）
    understanding_dict = {}
    
    # 解锁内容记录
    unlocked_info = {}       # 解锁的信息
    unlocked_cg = {}         # 解锁的CG
    unlocked_stories = {}    # 解锁的剧情
    
    # 玩家笔记
    player_notes = {}
    
    # 角色分组定义
    ALL_CHARACTERS = [
        # 神明
        "Crate", "Morlice", "生命之母", "死亡女神",
        # 二代成员
        "Mithar", "Monial", "皇甫子伥", "Corrian", "Xenon",
        "Alpine", "祁溟", "Luna", "Aria", "Regsya", "Amily",
        # 一代成员  
        "Dust", "X", "Sakura", "四夕", "Ryusui", "Glitter", "Talent",
        # 天堂领主
        "Justice","Mood","孟双朔","Viridis","乌重九","Nyx","贞洁"
        # 地狱领主
        "Lucifer","Jealous","Fury","Schorl","Voracity","Gluttony","Lust"
        # 其他
        "Kaward", "Glant", "Gloria", "Wynn"
    ]
    
    # 了解度等级定义
    UNDERSTANDING_LEVELS = {
        0: ("未解锁", "#666666", "🔒"),
        1: ("陌路人", "#888888", "👤"),  # 解锁但了解度为0-19
        20: ("初识者", "#4a86e8", "🌟"), 
        40: ("基本了解", "#6aa84f", "✨"),
        60: ("熟知", "#e69138", "❤️"),
        80: ("知心", "#cc0000", "💫"),
        100: ("全知", "#ff00b3", "gui/level_100_icon.png")
    }
    
    # 角色额外信息（用于人物详情页）
    character_info = {}
    character_description = {}
    
    # =====================
    # 2. 核心初始化函数
    # =====================
    
    def init_understanding():
        """初始化了解度系统 - 所有角色初始为0（未解锁）"""
        global understanding_dict, unlocked_info, unlocked_cg, unlocked_stories, player_notes
        
        # 从持久化数据加载已有进度
        load_understanding_data()
        
        # 确保所有角色都有记录（初始为0）
        for character in ALL_CHARACTERS:
            if character not in understanding_dict:
                understanding_dict[character] = 0  # 未解锁状态
            
            # 初始化解锁记录（如果不存在）
            if character not in unlocked_info:
                unlocked_info[character] = []
            if character not in unlocked_cg:
                unlocked_cg[character] = []
            if character not in unlocked_stories:
                unlocked_stories[character] = []
            if character not in player_notes:
                player_notes[character] = ""
            # 初始化角色信息和简介，避免 screens 中访问未定义变量时报错
            if character not in character_info:
                character_info[character] = {}
            if character not in character_description:
                character_description[character] = "暂无简介"
        
        return True
    
    def init_new_game():
        """开始新游戏 - 重置所有数据"""
        global understanding_dict, unlocked_info, unlocked_cg, unlocked_stories, player_notes
        
        # 完全清空
        understanding_dict.clear()
        unlocked_info.clear()
        unlocked_cg.clear()
        unlocked_stories.clear()
        player_notes.clear()
        
        # 所有角色初始为0（未解锁）
        for character in ALL_CHARACTERS:
            understanding_dict[character] = 0
            unlocked_info[character] = []
            unlocked_cg[character] = []
            unlocked_stories[character] = []
            player_notes[character] = ""
        
        # 保存到持久化
        save_understanding_data()
        
        renpy.notify("新游戏已开始")
        return True
    
    # =====================
    # 3. 了解度操作函数
    # =====================
    
    def add_understanding(character, amount=1, reason=""):
        """增加角色了解度"""
        if character not in understanding_dict:
            # 如果是新角色，初始化
            understanding_dict[character] = 0
            unlocked_info[character] = []
            unlocked_cg[character] = []
            unlocked_stories[character] = []
            player_notes[character] = ""
        
        old_value = understanding_dict[character]
        
        # 如果当前是0（未解锁），先解锁
        was_locked = (old_value == 0)
        
        # 增加了解度
        new_value = min(100, old_value + amount)
        understanding_dict[character] = new_value
        
        # 显示提示
        if was_locked and new_value > 0:
            renpy.notify(f"✨ 解锁新角色")
        elif reason:
            renpy.notify(f"对{character}的了解度+{amount}（{reason}）")
        else:
            renpy.notify(f"对{character}的了解度+{amount}")
        
        # 检查等级变化
        old_level = get_understanding_level(old_value)
        new_level = get_understanding_level(new_value)
        
        if new_level > old_level:
            level_name, level_color, level_icon = UNDERSTANDING_LEVELS[new_level]
            renpy.call("understanding_level_up", character, new_level, level_name)
        
        # 自动保存
        auto_save_understanding()
        
        return new_value
    
    def unlock_character(character, initial_value=1):
        """直接解锁角色"""
        if character not in understanding_dict:
            understanding_dict[character] = 0
        
        if understanding_dict[character] == 0:
            understanding_dict[character] = initial_value
            renpy.notify(f"✨ 解锁角色：[character]")
            auto_save_understanding()
            return True
        return False
    
    def get_understanding_level(value):
        """根据数值获取等级阈值"""
        for threshold in sorted(UNDERSTANDING_LEVELS.keys(), reverse=True):
            if value >= threshold:
                return threshold
        return 0
    
    def get_level_info(character):
        """获取角色的等级信息"""
        value = understanding_dict.get(character, 0)
        level = get_understanding_level(value)
        return UNDERSTANDING_LEVELS.get(level, ("未解锁", "#666666", "gui/locked_icon.png"))
    
    def is_character_unlocked(character):
        """检查角色是否已解锁"""
        return understanding_dict.get(character, 0) > 0
    
    # =====================
    # 4. 角色筛选函数
    # =====================
    
    def get_characters_by_filter(filter_type="all"):
        """根据筛选条件获取角色列表"""
        if filter_type == "all":
            return ALL_CHARACTERS
        elif filter_type == "unlocked":
            return [c for c in ALL_CHARACTERS if is_character_unlocked(c)]
        elif filter_type == "locked":
            return [c for c in ALL_CHARACTERS if not is_character_unlocked(c)]
        else:
            # 自定义分组
            groups = {
                "gods": ["Crate", "Morlice","Vita","Blea"],
                "gen1": ["Dust", "X", "Sakura", "四夕", "Ryusui", "Glitter", "Talent"],
                "gen2": ["Mithar", "Monial", "皇甫子伥", "Corrian", "Xenon", 
                        "Alpine", "祁溟", "Luna", "Aria", "Regsya", "Amily"],
                "lords1": ["Justice","Mood","孟双朔","Viridis","乌重九","Nyx","贞洁"],
                "lords2": ["Lucifer","Jealous","Fury","Schorl","Voracity","Gluttony","Lust"],
                "others": ["Kaward", "Glant", "Gloria", "Wynn"],
            }
            if filter_type in groups:
                return groups[filter_type]
            return ALL_CHARACTERS
    
    def get_character_display_name(character):
        """获取角色显示名（未解锁时显示???）"""
        if is_character_unlocked(character):
            return character
        else:
            return "？？？"
    
    def get_character_icon(character):
        """获取角色图标（未解锁时返回锁定图标）"""
        if is_character_unlocked(character):
            # 根据了解度等级返回不同图标
            value = understanding_dict.get(character, 0)
            level = get_understanding_level(value)
            _, _, icon_path = UNDERSTANDING_LEVELS.get(level, ("", "", "gui/unlocked_icon.png"))
            return icon_path
        else:
            return "gui/locked_icon.png"
    
    # =====================
    # 5. 持久化函数
    # =====================
    
    def auto_save_understanding():
        """自动保存了解度数据"""
        persistent.understanding_dict = dict(understanding_dict)
        persistent.unlocked_info = dict(unlocked_info)
        persistent.unlocked_cg = dict(unlocked_cg)
        persistent.unlocked_stories = dict(unlocked_stories)
        persistent.player_notes = dict(player_notes)
    
    def save_understanding_data():
        """手动保存了解度数据"""
        auto_save_understanding()
        renpy.notify("游戏进度已保存")
    
    def load_understanding_data():
        """加载了解度数据"""
        if hasattr(persistent, 'understanding_dict'):
            understanding_dict.update(persistent.understanding_dict)
        
        if hasattr(persistent, 'unlocked_info'):
            for char, info_list in persistent.unlocked_info.items():
                if char not in unlocked_info:
                    unlocked_info[char] = []
                unlocked_info[char].extend(info_list)
        
        if hasattr(persistent, 'unlocked_cg'):
            for char, cg_list in persistent.unlocked_cg.items():
                if char not in unlocked_cg:
                    unlocked_cg[char] = []
                unlocked_cg[char].extend(cg_list)
        
        if hasattr(persistent, 'unlocked_stories'):
            for char, story_list in persistent.unlocked_stories.items():
                if char not in unlocked_stories:
                    unlocked_stories[char] = []
                unlocked_stories[char].extend(story_list)
        
        if hasattr(persistent, 'player_notes'):
            player_notes.update(persistent.player_notes)
        
        return True

# =====================
# Ren'Py 标签
# =====================

label understanding_level_up(character, level, level_name):
    """了解度等级提升"""
    play sound "audio/level_up.ogg"
    
    "【系统】与[character]的关系提升至{color=#e69138}[level_name]{/color}！"
    
    return