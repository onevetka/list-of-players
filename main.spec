# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py', 'main_window_ui.py', 'logic.py', 'ui_builder.py'],
             pathex=['C:\\Users\\oneve\\ListOfPlayers'],
             binaries=[],
             datas=[('data/Settings.txt', 'data'), ('data/CossacksPlayers.json', 'data'), ('images/LogoLOP.png', 'images'), ('images/LOfP.ico', 'images')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='List Of Players',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='images/LOfP.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')