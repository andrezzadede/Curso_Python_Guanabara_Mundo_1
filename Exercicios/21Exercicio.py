#Faça um programa que abra o reproduza o audio de um arquivo MP3

import pygame
pygame.mixer.init()

pygame.mixer.music.load('yours.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()