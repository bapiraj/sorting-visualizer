"""
SORTING VISUALIZER
"""

import sys
import time
import pygame
import numpy as np

pygame.init()
pygame.display.set_caption("SORTING VISUALIZER")
WINDOW_SIZE = 1280, 720
STEP = WINDOW_SIZE[0]/WINDOW_SIZE[1]
SCREEN = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (66, 149, 245)
CLOCK = pygame.time.Clock()
FRAMERATE = 30
BACKGROUND_COLOR = WHITE_COLOR
ARRAY_COLOR = BLUE_COLOR
FONT = pygame.font.SysFont("bahnschrift", 20)


class Visualizer:
    def __init__(self):
        self.array = np.arange(0.0, WINDOW_SIZE[0], STEP)
        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.array)

    def display_array(self, msg):
        SCREEN.fill(BACKGROUND_COLOR)
        for i, ele in enumerate(self.array):
            pygame.draw.rect(SCREEN, ARRAY_COLOR, [0, i, ele, 1])
        text = FONT.render(msg, True, BLACK_COLOR)
        SCREEN.blit(text, (1100, 0))
        pygame.display.update()

    def bubble_sort(self):
        size = WINDOW_SIZE[1]
        for i in range(size):
            for j in range(i+1, size):
                event = self.check_input()
                if event == "QUIT":
                    sys.exit()
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]
            self.display_array("BUBBLE SORT")
            CLOCK.tick(30)

    def insertion_sort(self):
        size = WINDOW_SIZE[1]
        for i in range(1, size):
            j = i-1
            key = self.array[i]
            while j > -1 and self.array[j] > key:
                event = self.check_input()
                if event == "QUIT":
                    sys.exit()
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key
            self.display_array("INSERTION SORT")
            CLOCK.tick(30)

    def selection_sort(self):
        size = WINDOW_SIZE[1]
        for i in range(size):
            min_index = i
            for j in range(i+1, size):
                event = self.check_input()
                if event == "QUIT":
                    sys.exit()
                if self.array[min_index] > self.array[j]:
                    min_index = j
            self.array[min_index], self.array[i] = self.array[i], self.array[min_index]
            self.display_array("SELECTION SORT")
            CLOCK.tick(30)

    def partition(self, low, high):
        i = (low-1)
        pivot = self.array[high]
        for j in range(low, high):
            if self.array[j] <= pivot:
                i = i+1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        return i+1

    def quick_sort(self, low, high):
        if len(self.array) == 1:
            return
        event = self.check_input()
        if event == "QUIT":
            sys.exit()
        if low < high: 
            index = self.partition(low, high)
            self.display_array("QUICK SORT")
            self.quick_sort(low, index-1)
            self.display_array("QUICK SORT")
            self.quick_sort(index+1, high)
            self.display_array("QUICK SORT")
            CLOCK.tick(30)

    def merge(self, start, mid, end):
        start2 = mid + 1

        if self.array[mid] <= self.array[start2]:
            return
        while start <= mid and start2 <= end:
            if self.array[start] <= self.array[start2]:
                start += 1
            else:
                value = self.array[start2]
                index = start2
                while index != start:
                    self.array[index] = self.array[index - 1]
                    index -= 1
                self.array[start] = value
                start += 1
                mid += 1
                start2 += 1

    def merge_sort(self, left, right):
        event = self.check_input()
        if event == "QUIT":
            sys.exit()
        if left < right:
            mid = left + (right - left) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.display_array("MERGE SORT")  
            self.merge(left, mid, right)
            self.display_array("MERGE SORT")
            CLOCK.tick(30)

    def heapify(self, size, index):
        event = self.check_input()
        if event == "QUIT":
            sys.exit()
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and self.array[largest] < self.array[left]:
            largest = left
        if right < size and self.array[largest] < self.array[right]:
            largest = right
        if largest != index:
            self.array[index], self.array[largest] = self.array[largest], self.array[index] 
            self.heapify(size, largest)

    def heap_sort(self):
        size = len(self.array)
        for i in range(size//2 - 1, -1, -1):
            self.heapify(size, i)
        for i in range(size-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)
            self.display_array("HEAP SORT")
            CLOCK.tick(30)

    def shell_sort(self):
        size = len(self.array)
        gap = size//2
        while gap > 0:
            for i in range(gap, size):
                event = self.check_input()
                if event == "QUIT":
                    sys.exit()
                temp = self.array[i]
                j = i 
                while  j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap] 
                    j -= gap
                self.array[j] = temp
                self.display_array("SHELL SORT")
                CLOCK.tick(240)
            gap //= 2

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

def run():
    viz = Visualizer()
    viz.bubble_sort()
    time.sleep(2)
    viz.shuffle()
    viz.insertion_sort()
    time.sleep(2)
    viz.shuffle()
    viz.selection_sort()
    time.sleep(2)
    viz.shuffle()
    viz.quick_sort(0, WINDOW_SIZE[1]-1)
    time.sleep(2)
    viz.shuffle()
    viz.merge_sort(0, WINDOW_SIZE[1]-1)
    time.sleep(2)
    viz.shuffle()
    viz.heap_sort()
    time.sleep(2)
    viz.shuffle()
    viz.shell_sort()
    time.sleep(2)
    while True:
        if viz.check_input() == "QUIT":
            pygame.quit()
            sys.exit()
run()
