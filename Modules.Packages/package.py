
# package 만들기
# 1. 디렉터리, 서브 디렉터리 생성
# 2. __init_.py 파일을 각 디렉터리마다 생성 및 저장
# 3. 서브 디렉터리 내 파일을 만들고 테스트함수 입력
# 4. set PYTHONPATH=경로명
'''
game
    __init__.py
    sound
            __init_.py
            echo.py (echo_test())
    graphic
            __init_.py
            render.py (render_test())

import game.sound.echo
game.sound.echo.echo_test()

from game.sound.echo import echo_test   (O)
import game.sound.echo.echo_test        (X)
'''


# __init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할
# python3.3 버전부터는 파일이 없어도 패키지로 인식하나 하위호환성을 위해 생성


