# Faça um programa que reproduza um aúdio MP3
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
pygame.init()
pygame.mixer.music.load(open(file='C:/Users/Eder/.vscode/Python/Exercícios/Curso_em_Vídeo/Ex021.mp3'))
pygame.mixer.music.play()
print('QUANDO BATE AQUELA SAUDADE')
print()
print("""\033[1;35m      Tantantatantatnatntantantantantanntatatantantantantantantatantttumtumttutatumtutmtutdumdudmdumdudmdudum\n
      dudmdudmudmdumdmudmdumdudmdumudumdmdumdumudmdmumdutautmsumdudumdumdudmudmdutautaotataotataotatoat\n
      aotataotaoatoatotaotaotaotatoaotataotatoatoataotaotaotaoattoataotaotaotaotaotaotaotaatotaotao\n
      taotaotaotaotaotatoaotattoa\n
      é vc que tem os olhos tao gigantes\n
      e a boca tão gostosa\n
      eu não vou aguentar.\n
      Senta aqui do lado\n
      e tira logo a roupa\n
      esquece oq n importa\n
      nem vamos conversar.\n
      Olha bem mulher\n
      eu vou te ser sincero\n
      quero te ver de branco\n
      quero te ver no altar.\n
      Não tem medo não\n
      eu sei vai dar errado\n
      a gente fica longe\n
      e volta a namorar depois.\n
      Olha bem mulher\n
      eu vou te ser sincero\n
      eu to com uma vontade danada de te entregar todos os beijos que eu não te dei\n
      e eu to com uma saudade danada de ir dormir bem cansado e de acordar do teu lado pra te dizer que eu te amo\n
      que eu te amo demais\n
      lalallaisalsdaialailaialçaialailaialaialialaialaialai\n
      Olha bem mulher\n
      eu vou te ser sincero\n
      quero te ver de branco\n
      quero te ver no altar\n
      Não tem medo não\n
      a gente fica longe\n
      a gente até se esconde\n
      e volta a namorar depois\n
      É vc que tem\n
      os olhos tão gigantes\n
      e a boca tão gostosa\n
      eu não vou aguentar\n
      Olha bem mulher\n
      eu vou te ser sincero\n
      eu to com uma vontade danada de te entregar todos os beijos que eu n te dei\n
      e eu to com uma saudade apertada de ir dormir bem cansado e de acordar do teu lado pra te dizer\n
      que eu te amo\n
      que eu te amo demais\n
      lalailaialialailaialaialailaialaialailaialai\n
      laialaialialaialaialailaaialaialialaialaialialaiaailka\n
      EU TO COM UMA VONTADE DANADA DE TE ENTREGAR TODOS OS BEIJOS QUE EU N TE DEI\n
      E EU TO COM UMA SAUDADE APERTADA DE IR DORMIR BEM CANSADO\n
      E DE ACORDAR DO TEU LADO PRA TE DIZER\n
      QUE EU TE AMO\n
      QUE EU TE AMO DEMAIS\n
      LALAIALAILAIALAIALIALAIALAIALIALAIALAILAIALAILAIALAIALAILAIALAIALAIALAILAIALA\n
      LAIALAIALAILAIALAIAALAIALAIAAIALAIALAIALIALAIAAIALIA\n
      TUNTUNTUNDANDTUNDANTUNDANTUN.\033[m""")
input()
pygame.event.wait()
resp = str(input('Caso queira encerrar, digite STOP: ')).strip().upper()[0]
if resp in 'S':
    pygame.mixer.music.stop()