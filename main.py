import time
import warnings
import pygetwindow as gw
from pywinauto import application
import cv2
from PIL import ImageGrab
import pyautogui
import threading

warnings.filterwarnings('ignore', category=UserWarning, module='pywinauto')

REC = None  # 模拟器框尺寸
PLANT_INTERVAL = 1.5  # 浇水/收货/种植动作间隔
SIMULATOR = '逍遥模拟器 - 2'  # 模拟器名称


def run_with_timeout(func, args=(), timeout=300):
    # 创建一个线程来运行函数
    thread = threading.Thread(target=func, args=args)
    thread.start()
    # 等待线程完成或超时
    thread.join(timeout)
    if thread.is_alive():
        print("操作超时，将尝试重新启动")
        return False  # 返回 False 表示超时
    return True


# 图片对比
def contrast(target):
    screenshot = ImageGrab.grab(bbox=REC)
    screenshot.save('./farm_screenshot.png')
    screenshot = cv2.imread('./farm_screenshot.png')
    icon = cv2.imread(target, 0)  # 以灰度模式读取
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_screenshot, icon, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    loc = (max_loc[0] + icon.shape[1] / 2, max_loc[1] + icon.shape[0] / 2)
    # top_left = max_loc  # 矩形的左上角点
    # bottom_right = (top_left[0] + icon.shape[1], top_left[1] + icon.shape[0])  # 矩形的右下角点
    # cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
    # cv2.imshow('Best Match', screenshot)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return loc if max_val >= 0.8 else 0


def row1(loc):
    pyautogui.click(loc[0], loc[1])
    time.sleep(.5)
    threading.Thread(target=hold_key, args=('w', 0.8)).start()
    time.sleep(1.)
    threading.Thread(target=hold_key, args=('w', 0.5)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.7)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)


def row2(loc):
    pyautogui.click(loc[0], loc[1])
    time.sleep(.5)
    threading.Thread(target=hold_key, args=('w', 1.7)).start()
    time.sleep(2.)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.7)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)


def row3(loc):
    pyautogui.click(loc[0], loc[1])
    time.sleep(.5)
    threading.Thread(target=hold_key, args=('w', 2.3)).start()
    threading.Thread(target=hold_key, args=('d', 0.7)).start()
    time.sleep(3.0)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.6)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)

    threading.Thread(target=hold_key, args=('w', 0.7)).start()
    threading.Thread(target=hold_key, args=('a', 0.5)).start()
    time.sleep(1.5)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)


def row4(loc):
    pyautogui.click(loc[0], loc[1])
    time.sleep(.5)
    threading.Thread(target=hold_key, args=('w', 2.9)).start()
    threading.Thread(target=hold_key, args=('d', 1.4)).start()
    time.sleep(3.0)
    pyautogui.press('space')
    time.sleep(PLANT_INTERVAL)


def hold_key(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)


def plant(window):
    window.set_focus()
    loc = contrast('./restart/reset.png')
    row1(loc)
    window.set_focus()
    row2(loc)
    window.set_focus()
    row3(loc)
    window.set_focus()
    row4(loc)
    window.set_focus()


def reboot(window):
    print("重启游戏中")
    rect = window.rectangle()
    left, top, right, bottom = rect.left, rect.top, rect.right, rect.bottom
    loc = contrast('./restart/home.png')
    if loc:
        pyautogui.click(loc[0], loc[1])
        time.sleep(3)
        loc = contrast('./restart/clear.png')
        if loc:
            pyautogui.click(loc[0], loc[1])
            time.sleep(3)
        else:
            pyautogui.click((left + right) / 2, (top + bottom) / 2)
            time.sleep(3)
        loc = contrast('./restart/game.png')
        if loc:
            pyautogui.click(loc[0], loc[1])
            while True:
                loc = contrast('./restart/8+.png')
                if loc:
                    time.sleep(3)
                    loc = contrast('./restart/announce.png')
                    if loc:
                        pyautogui.click(loc[0], loc[1])
                    time.sleep(1)
                    pyautogui.click((left + right) / 2, (top + bottom) / 2)
                    break
                time.sleep(2)
            time.sleep(2)

            while True:
                loc = contrast('./restart/farm.png')
                if loc:
                    time.sleep(2)
                    loc = contrast('./restart/notice.png')
                    if loc:
                        loc = contrast('./restart/x_.png')
                        pyautogui.click(loc[0], loc[1])
                        time.sleep(1)
                    else:
                        break

            while True:
                loc = contrast('./restart/farm.png')
                if loc:
                    time.sleep(2)
                    loc = contrast('./restart/passport.png')
                    if not loc:
                        pyautogui.click((left + right) / 2, (top + bottom) / 2)
                        time.sleep(2)
                        loc = contrast('./restart/img_1.png')
                        time.sleep(1)
                        pyautogui.click(loc[0], loc[1])
                    else:
                        break

            while True:
                loc = contrast('./restart/farm.png')
                if loc:
                    pyautogui.click(loc[0], loc[1] - 15)
                    break
                else:
                    print('正在检测农场入口')
                time.sleep(1)

            while True:  # 第二个内层循环
                if in_farm():
                    print('已进入农场')
                    loc = contrast('./restart/list.png')
                    if loc:
                        print('正在打开作物菜单')
                        pyautogui.click(loc[0], loc[1])
                        break
                    else:
                        print('正在寻找作物菜单')
                time.sleep(2)

            while True:
                time.sleep(1)
                loc = contrast('./restart/mushroom.png')
                if loc:
                    pyautogui.click(loc[0], loc[1])
                    print('已找到作物')
                    break
                else:
                    print('正在寻找作物')
                time.sleep(1)

            while True:
                time.sleep(1)
                loc = contrast('./restart/chose.png')
                if loc:
                    pyautogui.click(loc[0], loc[1])
                    print('选定作物成功')
                    break
                else:
                    print('正在选择作物')
                time.sleep(2)


def in_farm():
    time.sleep(1)
    a = contrast('./restart/net_error.png')  # 检查是否存在网络错误
    b = contrast('./restart/in_farm.png')  # 检查是否在农场内
    if a == 0 and b != 0:
        return True  # 如果两者都找到了对应的图像，则返回True
    else:
        return False  # 否则返回False


# 获取特定窗口
def start():
    # 获取窗口
    windows = gw.getWindowsWithTitle(SIMULATOR)
    if not windows:
        print(f"No window found with title: {SIMULATOR}")
        exit(1)
    window = windows[0]
    print(f"窗口名: {window.title}")

    try:
        app = application.Application().connect(handle=window._hWnd)
        # 获取窗口对象
        window = app.window(handle=window._hWnd)
        window.move_window(x=0, y=0, width=800, height=450)
        rect = window.rectangle()
        left, top, right, bottom = rect.left, rect.top, rect.right, rect.bottom
        global REC
        REC = (left, top, right, bottom)
        n = 1  # 重启次数
        # 判断是否种菜
        window.set_focus()
        while True:
            if in_farm():
                window.set_focus()
                print('在农场中，开始种植')
                plant(window)
            else:
                print(f"不在农场，尝试第{n}重启")
                n += 1
                success = run_with_timeout(reboot, args=(window,), timeout=120)
                while not success:
                    print("超时，重试重启游戏")
                    success = run_with_timeout(reboot, args=(window,), timeout=120)
            time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    start()
