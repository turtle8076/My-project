if __name__ == '__main__':
    import functions as pgf
import random as rnd
import threading
import numpy as np
from copy import deepcopy  # 내부에 객체들까지 모두 새롭게 copy
from genome import Genome
import pygame
import time
import sys
import csv

gamegrid = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
            9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
            9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
            9, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 9,
            9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
            9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
            9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
            9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
            9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
            9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

gamegrid1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
             9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 0, 9, 9, 0, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 0, 0, 0, 0, 0, 0, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 9, 9, 9, 9, 9, 1, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 1, 9, 9, 9, 9, 9, 9,
             9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 9, 9, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 1, 9, 9, 9, 9, 1, 9,
             9, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 9,
             9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
             9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 1, 9, 9, 9,
             9, 1, 1, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 9, 9, 1, 1, 1, 1, 1, 1, 9,
             9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
             9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 9, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9,
             9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9,
             9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

sys.setrecursionlimit(10000) #재귀함수 최대깊이 설정
Game = False

N_POPULATION = 16  # population에 포함될 chromosome의 개수
N_BEST = 4  # 상위 우성유전자
N_CHILDREN = 4  # crossover에서 생성할 chromosome의 개수
PROB_MUTATION = 0.2  # mutation이 발생할 확률

# 초기 population 생성 Genome클래스 생성
#genomes = [Genome() for _ in range(N_POPULATION)]  # Genome()들 생성 50개
# solution
best_genomes = None  # 최고 유전자 미지정
n_gen = 0  # 세대 초기화
FPS = 300


# 프레임 속도


def writeScore(count):
    global score
    pygame.draw.rect(pgf.screen, (0, 0, 0), [500, 760, 300, 100])
    score += count
    font = pygame.font.Font(r'Images\NanumGothic.ttf', 25)
    text = font.render('Score : ' + str(score), True, (255, 255, 255))
    pgf.screen.blit(text, (500, 760))


def writeGeneration(num):
    pygame.draw.rect(pgf.screen, (0, 0, 0), [30, 760, 300, 100])
    font = pygame.font.Font(r'Images\NanumGothic.ttf', 25)
    text = font.render('Generation : ' + str(num), True, (255, 255, 255))
    pgf.screen.blit(text, (30, 760))


def i2xy(i):  # 그리드의 인덱스번호를 좌표료 변환
    sp = i % column
    ze = i // column  # // 연산자는 나누기 결과값을 int형으로 반환하는 것.
    return (sp * grid) + (grid // 2), (ze * grid) + (grid // 2)  # ex) 50번째 인덱스는 위의 연산을 거쳐 539, 35 라는 좌표가 생성된다


def xy2i(x, y):  # 좌표를 그리드의 인덱스번호로 변환
    sp, ze = (x - grid // 2) // grid, (y - grid // 2) // grid
    return ze * column + sp


class Point:
    def __init__(self, pos, imageFile):
        self.x, self.y = pos  # pos 파라미터는 2개의 값을 받아야한다. 즉 , i2xy 함수처럼 2개의 값을 반환하는 함수가 파라미터로 들어가야함.
        self.sprite = pgf.makeSprite(imageFile)  # 이미지파일을 스프라이트 객체로 만들어서 반환
        pgf.moveSprite(self.sprite, self.x, self.y, centre=True)  # x, y의 좌표로


class Figure:  # 팩맨, 고스트 등의 움직이는 물체 클래스
    def __init__(self, name, pos):
        self.name = name
        self.x, self.y = pos  # pos 에는 두 개의 반환값을 가진 함수가 들어와야하고, 그 두개의 반환값은 좌표로서 x,y에 저장
        self.direction = 0  #
        self.rx, self.ry = 1, 0
        self.mode = 'hunt'
        self.imageNo = 0
        self.ongrid = False
        self.i = 355

    def display(self):  # 보여지기
        pgf.moveSprite(self.sprite, self.x, self.y, centre=True)  # 설정된 좌표위치에 스프라이트를
        pgf.showSprite(self.sprite)  # 스프라이트를 보여줌

    def move(self):  # 예를 들어 현재 설정된 방향이 direction 0 = (1,0) 좌표에 이 direction 만큼 더해줌
        self.x += self.rx  # x좌표에 1씩 더해지므로 가로좌표가 1씩 증가 즉 오른쪽으로 이동
        self.y += self.ry  # y좌표에는 더해지지 않으므로 그대로, 반대로 x좌표에는 0만 더하고 y좌표에는 1씩 더하면 세로좌표가 1씩 증가하므로 아래로 이동
        self.i = xy2i(self.x, self.y)  # x, y과 진행방향에 따라 값이 바뀌면서 그에따른 인덱스도 다시 설정할 필요가 있음
        x2, y2 = i2xy(self.i)  # 다시 설정한 인덱스의 좌표값을 x2, y2에 저장
        self.ongrid = self.x == x2 and self.y == y2  # ongrid는 불린변수인데 x와 x2가 같고, y와 y2가 같을때 즉 다시 설정한 좌표가 검증이 될때 True

    def warp(self):
        if gamegrid[self.i] not in (5, 6): return False  # i번째 gamegrid 원소가 5,6이 아니면 false를 반환
        self.i = self.i + 27 if gamegrid[self.i] == 5 else self.i - 27  # i는 gamegrid가 5면 27을 더해주고 아니면 27을 빼준다.
        self.x, self.y = i2xy(self.i)  # 위에서 뽑은 인덱스를 좌표로 변환해준다.
        return True  # 기본적으로 True를 반환한다

    def directionValid(self, direction, j):  # 방향 확인
        rx, ry = directions[direction]  # direction 딕셔너리의 value들은 2개의 값을 가지고있다. 그 두 좌표들을 진행방향으로 설정
        i = j + rx + ry * column  # 세로로 이동할때 컬럼만큼 곱해서 더함
        # self.x += self.rx
        # self.y += self.ry
        # i = xy2i(self.x, self.y)
        return gamegrid[i] != 9  # gamegrid가 9가 아니면 True 반환. 즉, 9는 막혀있는곳이므로 9가 아닌곳은 방향전환가능

    def changemode(self, mode):
        pgf.hideSprite(self.sprite)  # 이전 스프라이트 이미지를 숨기고
        self.mode = mode
        self.sprite = self.sprites[mode][0]
        # sprties 딕셔너리의 mode 키 예를 들어 hunt키의 value들은 배열이다. 이 배열의 첫번째 값을 sprite로 가진다
        # 이 배열의 첫번째 값은 항상 makeSprite 함수로 반환된 Sprite
        self.imageNo = 0

    def changedirection(self, direction):  # 방향 전환
        if self.directionValid(direction, self.i):  # 방향확인함수를 통해 확인한 방향 전환이 가능하다면
            self.direction = direction
            self.rx, self.ry = directions[direction]
            return True

    def animate(self):
        sprite, animationimages, directionsdependent = self.sprites[self.mode]
        self.imageNo = (self.imageNo + 1) % animationimages
        if directionsdependent:
            self.imageNo += animationimages * self.direction
        pgf.changeSpriteImage(sprite, self.imageNo)


class Pacman(Figure):
    def __init__(self, name, pos, genome):
        Figure.__init__(self, name, pos)  # 파라미터로 Figure 클래스를 쓸것임으로 먼저 초기화
        self.sprites = {'hunt': [pgf.makeSprite('Images\Teil_17_Pacman_Tileset.png', 12), 3, True],
                        'dead': [pgf.makeSprite('Images\Teil_17_pacman_die.png', 12), 12, False]}
        self.sprite = self.sprites[self.mode][0]  # 팩맨의 초기모습 스프라이트 초기화(hunt mode)
        self.keyboardmemory = 0
        self.genome = genome
        self.timer = 0
        self.last_eat_time = 0
        self.fitness = 0
        self.evasion = 0

    def motinlogic(self):
        if not self.ongrid: return
        #if self.warp(): return
        self.pointEat()

        break_swith = 0
        while True:
            while True:
                newdirection = rnd.randrange(4)  # 랜덤으로 방향을 설정
                if self.direction == 0 and newdirection != 1 or \
                        self.direction == 1 and newdirection != 0 or \
                        self.direction == 2 and newdirection != 3 or \
                        self.direction == 3 and newdirection != 2:
                    break  # Abort the 2nd While Loop
                    # 역슬래시 '\'는 구문이 길어질 때 다음문장까지 잇겟다는 의미이다.

            for i in self.ghost_sensor():  # 센서의 고스트 인풋을 for 루프
                if i != 0:  # 0이 아니다 즉 고스트가 감지된 순간
                    # newdirection = self.ghost_output(genome)
                    break_swith = 1

            if self.changedirection(newdirection) or break_swith == 1:
                break  # Abort the 1st While Loop

        if break_swith == 1:
            newdirection = self.ghost_output(genome)  # 랜덤으로 방향을 설정
            self.changedirection(newdirection)
            if not self.directionValid(self.direction, self.i):
                self.rx  , self.ry = 0, 0

    def pointEat(self):
        pt = 0
        if gamegrid[self.i] not in (1, 2):
            return  # 1,2가 아니면 함수 중단

        elif gamegrid[self.i] == 1:
            writeScore(10)
            self.last_eat_time = self.timer  # 마지막으로 먹은 시간 갱신
        gamegrid[self.i] = 0  # gamegrid 에서 먹힌 포인트는 자리를 비운다 즉, 0으로
        pgf.killSprite(point_d[self.i].sprite)  # 자리에있던 포인트 스프라이트 제거.
        del point_d[self.i]  # del 함수는 delete 포인트 객체 또한 지워준다.

    def point_sensor(self):
        pacman_pos = xy2i(self.x, self.y)
        point_num = [0, 0, 0, 0]
        temp = 0.2

        for i in range(1, 6):  # 위
            if gamegrid[pacman_pos + 1] == 9:  # 벽이 있으면 0출력
                point_num[0] = 0
                break
            if gamegrid[pacman_pos + i] == 1:
                point_num[0] = round((temp * i), 2)  # 거리에 따른 값 증가량
                break

        for i in range(1, 6):  # 왼
            if gamegrid[pacman_pos - 1] == 9:
                point_num[1] = 0
                break
            if gamegrid[pacman_pos - i] == 1:
                point_num[1] = round((temp * i), 2)
                break

        for i in range(1, 6):  # 위
            if gamegrid[pacman_pos + (column * -1)] == 9:
                point_num[2] = 0
                break
            if gamegrid[pacman_pos + (column * -i)] == 1:
                point_num[2] = round((temp * i), 2)
                break

        for i in range(1, 6):  # 아래
            if gamegrid[pacman_pos + (column * i)] == 9:
                point_num[3] = 0
                break
            if gamegrid[pacman_pos + (column * i)] == 1:
                point_num[3] = round((temp * i), 2)
                break

        return point_num

    def ghost_sensor(self):

        pacman_pos = xy2i(self.x, self.y)  # 팩맨과 고스트들의 현재 인덱스 저장
        blinky_pos = xy2i(blinky.x, blinky.y)
        pinky_pos = xy2i(pinky.x, pinky.y)
        inky_pos = xy2i(inky.x, inky.y)
        clyde_pos = xy2i(clyde.x, clyde.y)

        ghost_list = [blinky_pos, pinky_pos, inky_pos, clyde_pos]  # 고스트들의 현재 위치가 담긴 리스트

        sensor = [[[], [], [], []],
                  [[], [], [], []],
                  [[], [], [], []],
                  [[], [], [], []]]  # 각 센서를 담은 리스트

        search_func(self, sensor, pacman_pos, pacman_pos, 2)

        ghost_input = [0, 0, 0, 0]  # 고스트가 4방향중 어디있는지 알려줄 input값

        for ghost in ghost_list:
            for i, s in enumerate(sensor):
                if ghost in s:  # 먼저 각 센서의 뿌리에 있는지 확인
                    ghost_input[i] = 1
                else:  # 아니라면
                    for j, a in enumerate(s):  # 뿌리가 가지고 있는 각 가지에 있는지 확인
                        if j > 3: break  # 4번째 가지를 지나면 뿌리가 나오므로 뿌리는 패스
                        if ghost in a:  # 가지안에 있다면
                            ghost_input[i] = 1

        # print(ghost_input)
        return ghost_input

    def ghost_output(self, genome):
        self.genome = genome

        input1 = self.ghost_sensor()
        input2 = self.point_sensor()
        inputs = input1
        # outputs엔 genome에서 return한 정면, 왼쪽, 오른쪽에 대한 값이 있으며 그중 가장 확률이 높은 것을 선택(argmax())

        outputs = genome.forward(inputs)  # 뉴럴 네트워크 사용

        for i in range(4):  # 현재 위치에서 4방향 탐색
         if not self.directionValid(i, self.i):  # 현재 탐색 방향이 벽이 막혀있다면 ouput 방향으로 고려하지않음
            outputs[i] = 0  # 그렇기에 현재 탐색 방향에 해당하는 인덱스의 값을 가장 작은 0으로 바꿈

        outputs = np.argmax(outputs)  # argmax 는 softmax의 최대값의 인덱스(위치)를 반환

        if inputs[outputs] == 0:  # 피트니스 설정을 위한 얼마나 피했는가 카운트
            self.evasion += 1  # outputs, 즉 최종 출력값이 유령이 있는 방향이 아니라면 피하는데 성공
            #print("현재 유령 위치: ", inputs, "최종 판단 방향", outputs, "에 유령이 없음! 현재 누적 회피수 : ", self.evasion)

        elif inputs[outputs] == 1:  # 유령을 향해서 가면 회피 카운트를 깎는다
            self.evasion -= 2
            #print("현재 유령 위치: ", inputs, "최종 판단 방향", outputs, "에 유령이 있음! 현재 누적 회피수 : ", self.evasion)

        return outputs

    def front_wall_ghost_output(self, genome):
        self.genome = genome

        input1 = self.ghost_sensor()
        input2 = self.point_sensor()
        inputs = input1
        # outputs엔 genome에서 return한 정면, 왼쪽, 오른쪽에 대한 값이 있으며 그중 가장 확률이 높은 것을 선택(argmax())

        outputs = genome.forward(inputs)  # 뉴럴 네트워크 사용

        max = 0
        for i in range(4):  # 현재 위치에서 4방향 탐색
            if not self.directionValid(i, self.i):  # 현재 탐색 방향이 벽이 막혀있다면 ouput 방향으로 고려하지않음
                outputs[i] = 0  # 그렇기에 현재 탐색 방향에 해당하는 인덱스의 값을 가장 작은 0으로 바꿈
            if outputs[i] > max:  # 최대값 구하기
                max = outputs[i]

        # print(outputs)    # 확률이 담긴 리스트 출력

        max_index_list = []  # 최대값들의 인덱스를 닮을 리스트
        for j, v in enumerate(outputs):  # 정제된 outputs 리스트를 탐색
            if v == max:  # 최대 값이라면
                max_index_list.append(j)  # 리스트에 추가

        outputs = rnd.choice(max_index_list)
        # outputs = np.argmax(outputs) # 벽 방향은 전부 0으로 바꾼 다음에 가장 확률이 높은 곳을 치환
        if inputs[outputs] == 0:  # 피트니스 설정을 위한 얼마나 피했는가 카운트
            self.evasion += 1  # outputs, 즉 최종 출력값이 유령이 있는 방향이 아니라면 피하는데 성공
        elif inputs[outputs] == 1:  # 유령을 향해서 가면 회피 카운트를 깎는다
            self.evasion -= 2
        return outputs

def run(self):
    global clear
    global nextAnimation

    while True:

        pgf.tick(FPS)  # 프레임 속도
        if pgf.keyPressed('right'): pacman.keyboardmemory = 0
        if pgf.keyPressed('left'): pacman.keyboardmemory = 1
        if pgf.keyPressed('up'): pacman.keyboardmemory = 2
        if pgf.keyPressed('down'): pacman.keyboardmemory = 3

        for Figure in Figures:
            if pgf.clock() > nextAnimation:
                Figure.animate()
            Figure.motinlogic()  # 모션 로직대로 행동
            Figure.move()  # 움직임
            if Figure.name != 'pacman':  # 팩맨이 아닌 물체 즉, 고스트가
                if Figure.i == pacman.i:  # 팩맨과 인덱스가 겹쳤을때, 즉 스프라이트가 겹칠때
                    if Figure.mode == ('hunt'):
                        pacman.changemode('dead')
                        clear = True  # 팩맨이 쥬금
                        break
                    if Figure.mode in ('frighten', 'blink'):
                        Figure.changemode('dead')
                        writeScore(100)  # 쥬금
            Figure.display()  # 계속해서 화면을 업데이트하며 프레임따라 위치가 바뀌는 스프라이트  계속 보여주기
        if clear == True:
            clear = False
            break

        if pgf.clock() > nextAnimation:
            nextAnimation += 100

        pgf.updateDisplay()

        if pgf.keyPressed('1'):
            break

        # print('input:', pacman.ghost_sensor())
        # print('output:', pacman.ghost_output(genome))

        # pacman.ghost_output(genome)  # Snake 모듈에서 화면 출력과 유전자 값을 그대로 가져옴
        # genome.fitness = fitness  # fitness를 genome에 넣고 실행


def search_func(self, sensor, pacman_pos, pos, n):
    if n == 0:  # 원하는 횟수만큼 반복하였으면 함수 종료
        return 0

    for i, v in enumerate(sensor):  # sensor 리스트를 for 루프
        if i == 4: break  # 4개이상 쯕 뿌리센서까지 침범할 수 있으므로 마지막 가지때 for 루프 탈출
        search_pos = pos  # 현재 탐색위치는 자신의 위치
        s_direction = i  # 0, 1, 2, 3 순으로 방향하나씩
        rx, ry = directions[s_direction]  # 일단 현재 방향의 좌표 증가값 저장
        if gamegrid[pos + rx + ry * column] == 9: continue  # 현재 방향대로 한칸 나아갔을 때 벽이라면 패스
        # 다음칸이 벽이 아니라면 본격적으로 뿌리센서의 넣을 값을 탐색
        while True:  # 센서방향이 정해졌으면 그 방향을 뿌리로 두며 루프 시작
            rx, ry = directions[s_direction]  # 커브길에 따라 바뀔수있으므로 탐색때마다 초기화
            search_pos = search_pos + rx + ry * column  # 진행방향의 다음칸으로 탐색위치 증가
            if search_pos == pacman_pos : break   # 센서 탐색 범위가 팩맨 위치와 겹친다면 그 이상 탐색할 이유가 없으므로 break
            if gamegrid[search_pos] == 9: break  # 현재탐색위치가 벽이라면 while 루프 탈출
            if not crossway_valid(search_pos):  # 현재 탐색위치가 교차로가 아니면
                v.append(search_pos)  # 탐색 위치를 뿌리센서에 삽입
                # 현재 탐색위치를 센서에 삽입하였으니 현재방향 그대로 다음 탐색위치를 검사
                if not Figure.directionValid(self, s_direction, search_pos):  # 현재방향의 다음 탐색위치가 막혀버렸다면
                    for j in range(0, 4):  # 사방향을 하나씩 탐색
                        if j == s_direction or j + s_direction in (1, 5):
                            continue  # 현재방향(어차피막힘)과 현재방향의 반대방향, 즉 되돌아가는 방향은 고려하지않음
                        if Figure.directionValid(self, j, search_pos):  # 탐색할 방향이 막혀있지않으면
                            s_direction = j  # 탐색방향 재설정
                            break  # 어차피 교차로가 아닐때 상항이기 때문에 꺾을 수 있는 방향은 하나뿐이므로 for 루프 탈출

            elif crossway_valid(search_pos):  # 탐색위치가 교차로면
                v.append(search_pos)  # 일단 현재 탐색위치를 뿌리센서에 삽입
                search_func(self, v, pacman_pos, search_pos, n - 1)  # 재귀 호출
                break


def crossway_valid(i):  # 어느 클래스에도 속하지 않는 교차로 판단 함수
    cross_bool = False
    way_num = 0  # 현 위치에서 진행 가능한 방향의 수

    if gamegrid[i + 1] in range(0, 3):  # 오른쪽에 길이 있다면
        way_num += 1
    if gamegrid[i - 1] in range(0, 3):  # 왼쪽에  길이 있다면
        way_num += 1
    if gamegrid[i + column] in range(0, 3):  # 아래쪽에 길이 있다면
        way_num += 1
    if gamegrid[i - column] in range(0, 3):  # 위쪽에 길이 있다면
        way_num += 1

    if way_num >= 3:  # 한 지점에 전환할 수 있는 방향이 3개 이상이라면 그것은 교차로
        cross_bool = True

    if gamegrid[i] == 9:  # 하지만교차로 탐색위치가 벽이라면 그냥 false 반환
        cross_bool = False

    return cross_bool


class ghost(Figure):
    def __init__(self, name, pos, imageFile):
        Figure.__init__(self, name, pos)
        self.sprites = {'hunt': [pgf.makeSprite(imageFile, 8), 2, True],
                        'frighten': [pgf.makeSprite('Images\Teil_17_Ghost_frighten.png', 2), 2, False],  # 잡아먹힐수 있음
                        'blink': [pgf.makeSprite('Images\Teil_17_Ghost_blink.png', 4), 4, False],
                        # frighten 모드가 끝나감을 의미
                        'dead': [pgf.makeSprite('Images\Teil_17_Ghost_die.png', 4), 1, True]}
        self.sprite = self.sprites[self.mode][0]

    def motinlogic(self):
        if not self.ongrid: return
        #if self.warp(): return
        while True:
            while True:
                newdirection = rnd.randrange(4)  # 랜덤으로 방향을 설정
                if self.direction == 0 and newdirection != 1 or \
                        self.direction == 1 and newdirection != 0 or \
                        self.direction == 2 and newdirection != 3 or \
                        self.direction == 3 and newdirection != 2:
                    break  # Abort the 2nd While Loop
                    # 역슬래시 '\'는 구문이 길어질 때 다음문장까지 잇겟다는 의미이다.
            if self.changedirection(newdirection):
                break  # Abort the 1st While Loop


class Blinky(Figure):
    def __init__(self, name, pos, imageFile):
        Figure.__init__(self, name, pos)
        self.sprites = {'hunt': [pgf.makeSprite(imageFile, 8), 2, True],
                        'frighten': [pgf.makeSprite('Images\Teil_17_Ghost_frighten.png', 2), 2, False],  # 잡아먹힐수 있음
                        'blink': [pgf.makeSprite('Images\Teil_17_Ghost_blink.png', 4), 4, False],
                        # frighten 모드가 끝나감을 의미
                        'dead': [pgf.makeSprite('Images\Teil_17_Ghost_die.png', 4), 1, True]}
        self.sprite = self.sprites[self.mode][0]
        self.keyboardmemory = 0

    def motinlogic(self):

        if not self.ongrid: return
        #if self.warp(): return
        '''
        self.changedirection(self.keyboardmemory)  # 조종하기~
        if not self.directionValid(self.direction, self.i):
            self.rx, self.ry = 0, 0
        '''

        while True:
            while True:
                tracex = pacman.x - blinky.x
                tracey = pacman.y - blinky.y
                #print(tracex, tracey)
                newdirection = rnd.randrange(4)  # 랜덤으로 방향을 설정

                if self.direction == 0 and newdirection != 1 or \
                        self.direction == 1 and newdirection != 0 or \
                        self.direction == 2 and newdirection != 3 or \
                        self.direction == 3 and newdirection != 2:
                    break  # Abort the 2nd While Loop

                if (abs(tracex) > abs(tracey)):
                    if (tracex > 0):
                        newdirection = 0
                        break
                    else:
                        newdirection = 1
                        break

                elif (abs(tracey) > abs(tracex)):
                    if (tracey < 0):
                        newdirection = 2
                        break
                    else:
                        newdirection = 3
                        break
                if self.direction == 0 and newdirection != 1 or \
                        self.direction == 1 and newdirection != 0 or \
                        self.direction == 2 and newdirection != 3 or \
                        self.direction == 3 and newdirection != 2:
                    break  # Abort the 2nd While Loop

                    # 역슬래시 '\'는 구문이 길어질 때 다음문장까지 잇겟다는 의미이다.
            if self.changedirection(newdirection):
                break  # Abort the 1st While Loop

class Gacman(Figure):
    def __init__(self, name, pos):
        Figure.__init__(self, name, pos)  # 파라미터로 Figure 클래스를 쓸것임으로 먼저 초기화
        self.sprites = {'hunt': [pgf.makeSprite('Images\Teil_17_Pacman_Tileset.png', 12), 3, True],
                        'dead': [pgf.makeSprite('Images\Teil_17_pacman_die.png', 12), 12, False]}
        self.sprite = self.sprites[self.mode][0]  # 팩맨의 초기모습 스프라이트 초기화(hunt mode)
        self.keyboardmemory = 0

    def pointEat(self):
            pt = 0
            if gamegrid[self.i] not in (1, 2): return  # 1,2가 아니면 함수 중단
            if gamegrid[self.i] == 2:  # 2 값, 즉 큰 포인트를 먹었을때
                changemodeGhosts('frighten')  # 유령들은 잡아먹힐 수 있는 상태가 됨
            gamegrid[self.i] = 0  # gamegrid 에서 먹힌 포인트는 자리를 비운다 즉, 0으로
            pgf.killSprite(point_d[self.i].sprite)  # 자리에있던 포인트 스프라이트 제거.
            writeScore(10)
            del point_d[self.i]  # del 함수는 delete 포인트 객체 또한 지워준다.

    def motinlogic(self): #모션(움직임) 로직
            if not self.ongrid: return #ongrid가 거짓일때 함수 중단
            #if self.warp(): return #warp함수의 결과값이 참일때 함수 중단
            self.pointEat() #항상 포인트먹기를 행동
            self.changedirection(self.keyboardmemory) #키보드입력대로 방향전환
            if not self.directionValid(self.direction, self.i): #방향 확인 함수 반환값이 false라면
                self.rx, self.ry = 0, 0 #방향 전환 및 움직일 수 없으므로 정지


def pointSet():
    global dlt
    global gamegrid
    global gamegrid1

    if dlt == True:
        point_d = {}
        for i, number in enumerate(gamegrid):
            gamegrid[i] = gamegrid1[i]

    else:
        point_d = {}
        for i, number in enumerate(gamegrid1):  # gamegrid 배열을 for문으로 탐색
            if number not in (1, 2): continue  # 숫자가 1,2가 아니면 패스
            point_d[i] = Point(i2xy(i), 'Images\Teil_17_Punkt.png') if number == 1 else Point(i2xy(i),
                                                                                                 'Images\Teil_17_Punkt_gross.png')
            # 즉 point_d라는 딕셔너리 의 원소로서 Point 클래스 형 객체가 좌표값과 스프라이트를 파라미터로 가지며 들어간다.
            pgf.showSprite(point_d[i].sprite)

    return point_d


def changemodeGhosts(mode):
    for Figure in Figures:
        if Figure.name == 'pacman': continue
        if Figure.mode != 'dead':
            Figure.changemode(mode)
    if mode == 'frighten':
        timer1 = threading.Timer(5, changemodeGhosts, ('blink',)).start()
        timer2 = threading.Timer(8, changemodeGhosts, ('hunt',)).start()

trikey = 0
dlt = True
directions = {0: (1, 0), 1: (-1, 0), 2: (0, -1), 3: (0, 1)}
width, height = 672, 812
grid = 24
column = width // grid  # 넓이 즉 가로를 grid변수로 나눴을때 나오는 28은 gamegrid의 배열 가로 갯수
zeilen = height // grid  # 높이 즉 세로를 grid변수로 나눴을때 나오는 31은 gamegrid의 배열 새로 갯수

pgf.screenSize(width, height)
main1 = pygame.image.load('Images\Main_image1.png') #제목 이미지
main2 = pygame.image.load('Images\Main_image2.png') #제목 이미지2
nextAnimation = pgf.clock() + 100

clear = False


def main():
    global Game
    global trikey
    pgf.hideAll()
    pgf.updateDisplay()

    while True:
        #pgf.tick(50)
        pgf.screen.blit(main1, (183, 200))
        pgf.screen.blit(main2, (180, 310))
        pgf.updateDisplay()

        font = pygame.font.Font(r'Images\NanumGothic.ttf', 35)
        gamestart = font.render('G a m e   S t a r t', True, (255, 255, 255))
        pgf.screen.blit(gamestart, (180, 500))
        if trikey == 0:
            tri = Point((120, 520), 'Images\Triangle.png')
            pgf.showSprite(tri.sprite)

        font = pygame.font.Font(r'Images\NanumGothic.ttf', 35)
        simulation = font.render('S i m u l a t i o n', True, (255, 255, 255))
        pgf.screen.blit(simulation, (180, 570))
        if trikey == 1:
            tri = Point((120, 590), 'Images\Triangle.png')
            pgf.showSprite(tri.sprite)

        font = pygame.font.Font(r'Images\NanumGothic.ttf', 35)
        exit = font.render('E X I T', True, (255, 255, 255))
        pgf.screen.blit(exit, (180, 640))
        if trikey == 2:
            tri = Point((120, 660), 'Images\Triangle.png')
            pgf.showSprite(tri.sprite)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if (trikey < 2):
                        trikey += 1

                elif event.key == pygame.K_UP:
                    if (trikey > 0):
                        trikey -= 1

                pgf.hideAll()

        if pgf.keyPressed('space'):
            if (trikey == 2): # 종료
                pygame.quit()
                sys.exit()
                break
            else :
                break


if __name__ == "__main__":
    f = open('PlayerOutput.csv', 'w', newline='') #플레이어 아웃풋 파일 열기
    wr = csv.writer(f)
    wr.writerow(["Time", "Score"])
    while True:
        pgf.screenSize(width, height)
        main() #메인 화면
        if trikey == 0:

            score = 0
            dlt = True
            pgf.hideAll()
            pgf.screenSize(width, height)
            point_d = pointSet()
            dlt = False
            pgf.setBackgroundImage('Images\Teil_17_Spielfeld.png')
            pgf.setAutoUpdate(False)

            point_d = pointSet()

            blinky = Blinky('blinky', (270, 420), 'Images\Teil_17_Blinky_tileset.png')
            pinky = ghost('pinky', (390, 420), 'Images\Teil_17_pinky_tileset.png')
            inky = ghost('inky', (360, 276), 'Images\Teil_17_inky_tileset.png')
            clyde = ghost('clyde', (360, 276), 'Images\Teil_17_clyde_tileset.png')
            pacman = Gacman('pacman', (336, 564))  # 2번째 파라미터는 좌표
            pgf.updateDisplay()
            Figures = [pacman, blinky, pinky, inky, clyde]
            pgf.setAutoUpdate(False)
            nextAnimation = pgf.clock() + 100

            StartT = time.time()
            run(pacman)
            EndT = round(time.time() - StartT, 2)

            wr.writerow([EndT, score])


        elif trikey == 1:
            genomes = [Genome() for _ in range(N_POPULATION)]
            f = open('output.csv', 'w', newline='')
            wr = csv.writer(f)
            wr.writerow(["Generation", "Genomes", "Evasion", "Time", "Score"])
            while True:
                n_gen += 1

                for i, genome in enumerate(genomes):
                    StartT = time.time()
                    score = 0
                    dlt = True
                    pgf.hideAll()
                    pgf.screenSize(width, height)
                    point_d = pointSet()
                    dlt = False
                    writeGeneration(n_gen)

                    pgf.setBackgroundImage('Images\Teil_17_Spielfeld.png')
                    pgf.setAutoUpdate(False)

                    point_d = pointSet()
                    pacman = Pacman('pacman', (336, 564), genome=genome)  # 2번째 파라미터는 좌표
                    blinky = Blinky('blinky', (270, 420), 'Images\Teil_17_Blinky_tileset.png')
                    pinky = ghost('pinky', (390, 420), 'Images\Teil_17_pinky_tileset.png')
                    inky = ghost('inky', (360, 276), 'Images\Teil_17_inky_tileset.png')
                    clyde = ghost('clyde', (360, 276), 'Images\Teil_17_clyde_tileset.png')

                    pgf.updateDisplay()
                    Figures = [pacman, blinky, pinky, inky, clyde]
                    pgf.setAutoUpdate(False)
                    nextAnimation = pgf.clock() + 100
                    run(pacman)
                    EndT = round(time.time() - StartT,2)  # 시간 측정 끝

                    genome.fitness = pacman.evasion
                    wr.writerow([n_gen, i, pacman.evasion, EndT, score])  # csv 파일에 현재 유전자 각 컬럼 값 입력

                    if pgf.keyPressed('1'):
                        n_gen = 0
                        break

                if pgf.keyPressed('1'):
                    break

                if best_genomes is not None:  # best_genomes 갱신
                    genomes.extend(best_genomes)

                genomes.sort(key=lambda x: x.fitness, reverse=True)  # 유전자 정렬: 기본 오름차순 정렬 reverse=True는 내림차순으로 변셩,
                # key인자에 함수를 넘겨주어 fitness값을 내림 차순으로 정렬

                print('===== Generaton #%s\tBest Fitness %s =====' % (n_gen, genomes[0].fitness))  # 세대 끝, 최고 적합도 출력
                # print(genomes[0].w1, genomes[0].w2)

                best_genomes = deepcopy(genomes[:N_BEST])

                # crossover
                for i in range(N_CHILDREN):  # child 개의 유전자 생성
                    new_genome = deepcopy(best_genomes[0])
                    a_genome = rnd.choice(best_genomes)
                    b_genome = rnd.choice(best_genomes)
                    # genome에서 만든 neural network의 hidden layer 부분을 최적화하기 위해 유전 알고리즘을 사용함
                    # single crossover로 crossover 지점은 rnd으로 함 randint(a,b) a~b까지 랜덤한 수
                    cut = rnd.randint(0,
                                      new_genome.w1.shape[1])  # shape는 행렬의 행,열 반환 shape[1]은 열. 최고 유전자 수는 항상 input의 갯수를 넘어서는 안됨
                    new_genome.w1[i, :cut] = a_genome.w1[i, :cut]
                    new_genome.w1[i, cut:] = b_genome.w1[i, cut:]

                    cut = rnd.randint(0, new_genome.w2.shape[1])
                    new_genome.w2[i, :cut] = a_genome.w2[i, :cut]
                    new_genome.w2[i, cut:] = b_genome.w2[i, cut:]

                    cut = rnd.randint(0, new_genome.w3.shape[1])
                    new_genome.w3[i, :cut] = a_genome.w3[i, :cut]
                    new_genome.w3[i, cut:] = b_genome.w3[i, cut:]

                    cut = rnd.randint(0, new_genome.w4.shape[1])
                    new_genome.w4[i, :cut] = a_genome.w4[i, :cut]
                    new_genome.w4[i, cut:] = b_genome.w4[i, cut:]

                    best_genomes.append(new_genome)  # crossover

                # mutation 0.4 확률로 mutation 발생시킴
                genomes = []
                for i in range(int(N_POPULATION / (N_BEST + N_CHILDREN))):
                    for bg in best_genomes:
                        new_genome = deepcopy(bg)

                        mean = 20
                        stddev = 10

                        if rnd.uniform(0, 1) < PROB_MUTATION:
                            new_genome.w1 += new_genome.w1 * np.random.normal(mean, stddev,
                                                                              size=(4, 10)) / 100 * np.random.randint(-1, 2,
                                                                                                                      (4, 10))
                        if rnd.uniform(0, 1) < PROB_MUTATION:
                            new_genome.w2 += new_genome.w2 * np.random.normal(mean, stddev,
                                                                              size=(10, 20)) / 100 * np.random.randint(-1, 2,
                                                                                                                       (10, 20))
                        if rnd.uniform(0, 1) < PROB_MUTATION:
                            new_genome.w3 += new_genome.w3 * np.random.normal(mean, stddev,
                                                                              size=(20, 10)) / 100 * np.random.randint(-1, 2,
                                                                                                                       (20, 10))
                        if rnd.uniform(0, 1) < PROB_MUTATION:
                            new_genome.w4 += new_genome.w4 * np.random.normal(mean, stddev,
                                                                              size=(10, 4)) / 100 * np.random.randint(-1, 2,
                                                                                                                      (10, 4))

                        genomes.append(new_genome)


                if pgf.keyPressed('1'):
                    break