import pywinauto
import pyautogui
import pynput.keyboard as kb

def get_positions() -> tuple[tuple[int]]:
    '''
    Get both z and y button positions.
    '''
    
    windows = pywinauto.Desktop().windows()
    board = [w for w in windows if w.window_text() == 'Microsoft Whiteboard']
    
    # Error protection
    assert len(board) == 1
    
    rect = board[0].rectangle()
    coords = x, y = rect.left + 68, rect.top + 54
    return coords, (x + 40, y)

def cancel() -> None:
    
    old = pyautogui.position()
    
    try:
        (x, y), _ = get_positions()
        pyautogui.click(x, y)
        pyautogui.moveTo(*old)
    
    except: pass

def uncancel() -> None:
    
    old = pyautogui.position()
    
    try:
        _, (x, y) = get_positions()
        pyautogui.click(x, y)
        pyautogui.moveTo(*old)
    
    except: pass

# Run
with kb.GlobalHotKeys({
    
    '<ctrl>+z': cancel,
    '<ctrl>+y': uncancel
    
    }) as ln: ln.join()