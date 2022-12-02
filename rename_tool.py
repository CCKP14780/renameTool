import maya.cmds as cmds

def renameTool():
    if cmds.window('renameTool_window',q=True,ex=True):
        cmds.deleteUI('renameTool_window',window=True)
        
    cmds.window('renameTool_window',title='Rename Tool v.1.0.0')
    cmds.showWindow('renameTool_window')
    cmds.window('renameTool_window',e=True,wh=[300,300])

#######################################################################
    
    cmds.columnLayout('main_layout',adj=True)

    cmds.frameLayout(l='Rename')
    cmds.rowLayout('name_layout',numberOfColumns=2)
    cmds.text('name_text',label='Name: ')
    cmds.textField('name_textField',w=150)
    cmds.setParent('main_layout')
    
    cmds.rowLayout('asuffix_layout',numberOfColumns=2)
    cmds.text('asuffix_text',label='Suffix: ')
    cmds.textField('asuffix_textField',w=150)
    cmds.setParent('main_layout')
    cmds.button(l='Rename',c=renameobj)

#######################################################################
    
def renameobj(*args):
    sels = cmds.ls(sl=True)
    
    name = cmds.textField('name_textField',q=True,tx=True)
    suffix = cmds.textField('asuffix_textField',q=True,tx=True)
    
    for each in sels:
        newname = f'{name}{i+1}{suffix}'
        cmds.rename(each,newname)

#######################################################################

renameTool()