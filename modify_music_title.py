import sys
from time import sleep
import os

def choose1():
    print("'-'가 두개가 있으면 오류가 발생할수도 있습니다.")
    sleep(2)
    print("start...")
    for i in file_list:
        for y in range(len(i)):
            if i[y] == '-':
                k = i[:y] + ' ' + i[y] + ' ' + i[y + 1:] 
                os.rename(get_DIR + '/' + i, get_DIR + '/' + k)
                break

def choose2():
    print('자르고 싶은만큼의 글자 수를 입력해주세요.(빈공간도 포함합니다.)')
    print('예-->이름:001. 전인권 - 사랑한 후에  / 앞에 있는 숫자와 빈공간을 지우려한다.')
    print('입력:5, 결과-->전인권 - 사랑한 후에 ')
    get_Index = int(input('-->'))
    print('start...')
    for i2 in file_list:
        os.rename(get_DIR + '/' + i2, get_DIR + '/' + i2[get_Index:])

def choose3():
    print('폴더 내에 있는 파일 전체의 아티스트와 제목의 위치를 변경합니다. ')
    sleep(2)
    print("'-'를 기준으로 나누기 때문에 없거나 두개 이상이 있으면 에러가 날수도 있습니다.")
    print("'-'앞뒤에 여백이 있어야 제대로 작동됩니다. 만약 여백이 없다면 1번 기능을 사용하여 먼저 여백을 만들어주세요.")
    Format_count = int(input('확장자의 글자수를 입력해주세요.(.도 포함)'))
    sleep(2)
    print('start...')
    for i3 in file_list:
        for count in range(len(i3)):
            if i3[count] == '-':
                modifyWord = i3[count + 2:len(i3) - Format_count] + ' ' + i3[count] + ' ' + i3[:count - 1] + i3[len(i3) - Format_count:]
                os.rename(get_DIR + '/' + i3, get_DIR + '/' + modifyWord)
                break

def main():
    global file_list, get_DIR
    while True:
        isStart = True
        get_DIR = input('음악파일들이 있는 폴더의 디렉토리를 입력해주세요.(끝에 "/" 생략)')
        file_list = os.listdir(get_DIR)
        print(file_list)
        print('이 프로그램은 음악파일 제목 변경을 목적으로 만들어졌습니다.')
        print('1. "-"앞뒤로 공백 생성')
        print('2. 제목의 앞쪽을 자르기')
        print('3. 아티스트와 제목 순서 변경')
        get_CMD = input('사용하실 기능을 선택해주세요.(숫자 입력)')

        if isStart:
            if get_CMD == '1':
                choose1()
                isStart = False

            elif get_CMD == '2':
                choose2()
                isStart = False

            elif get_CMD == '3':
                choose3()
                isStart = False

            elif get_CMD == '4':
                print('Traceback (most recent call last):')
                print('   PYTHON ERROR!!!')
                sleep(2)
                print('에러 아닙니다. 입력을 제대로 해주세요.')
            else:
                print('잘못된 입력입니다.')

        while True:
            ReStart = input('다시 사용하시겠습니까?(yes/no)').lower()
            if ReStart == 'yes':
                break
            if ReStart == 'no':
                return 0
            else:
                print('정확히 입력해주세요.')

if __name__ == '__main__':
    main()