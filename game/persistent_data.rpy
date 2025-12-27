# 在 game 文件夹中创建 persistent_data.rpy
# persistent_data.rpy - 持久化数据存储

init -1 python:
    # =====================
    # 1. 章节进度数据
    # =====================
    if not hasattr(persistent, 'chapter_progress') or persistent.chapter_progress is None:
        persistent.chapter_progress = {}
    
    # 初始化所有章节为未完成
    default_chapters = ["chapter_1", "chapter_2", "chapter_3", "chapter_4", "chapter_5"]
    for chapter in default_chapters:
        if chapter not in persistent.chapter_progress:
            persistent.chapter_progress[chapter] = False
    
    # =====================
    # 2. 了解度系统数据
    # =====================
    if not hasattr(persistent, 'understanding_dict'):
        persistent.understanding_dict = {}
    
    if not hasattr(persistent, 'unlocked_info'):
        persistent.unlocked_info = {}
    
    if not hasattr(persistent, 'unlocked_cg'):
        persistent.unlocked_cg = {}
    
    if not hasattr(persistent, 'unlocked_stories'):
        persistent.unlocked_stories = {}
    
    if not hasattr(persistent, 'player_notes'):
        persistent.player_notes = {}
    
    # =====================
    # 3. 游戏设置数据
    # =====================
    if not hasattr(persistent, 'game_initialized'):
        persistent.game_initialized = False
    
    if not hasattr(persistent, 'volume_settings'):
        persistent.volume_settings = {
            "music": 0.8,
            "sfx": 0.8,
            "voice": 0.8
        }
    
    if not hasattr(persistent, 'text_speed'):
        persistent.text_speed = 50
    
    # =====================
    # 4. 其他游戏数据
    # =====================
    if not hasattr(persistent, 'first_time_play'):
        persistent.first_time_play = True
    
    if not hasattr(persistent, 'total_play_time'):
        persistent.total_play_time = 0