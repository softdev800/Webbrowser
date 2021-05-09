# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['browser_tabbed.py'],
             pathex=['D:\\Portfolio\\Webbrowser'],
             binaries=[],
             datas=[],
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
          name='Webbrowser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='images\\ucoder-logo-128.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Webbrowser')
app = BUNDLE(coll,
             name='Webbrowser.app',
             icon='images/ucoder-logo-128.icns',
             bundle_identifier='com.ucoder.Webbrowser',
             info_plist={
                 'NSHighResolutionCapable': 'True'
             },
)
