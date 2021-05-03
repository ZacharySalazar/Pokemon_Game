from Pokemons import *
from Abilities import *
from Images import *
from Trainers import *
from Colors import *
import pygame
pygame.init()
PokemonFont = pygame.font.SysFont('trebuchetms', 45)
win = pygame.display.set_mode([1600, 800])
pygame.display.set_caption('Pokemon Game')


#Create Trainers and assign their pokemon
Player = Trainer("Player1")
Ai = Trainer("AI")
Player.add_pokemon(Geodude)
Ai.add_pokemon(Sandshrew)

#Anchor and current positions of imgs
Player_img_anchor = (150, 500)
Ai_img_anchor = (1200, 10)
PlayerX, PlayerY = (150, 500)
AiX, AiY = (1200, 10)

class GameUI():

    def draw_pokemon():
        """Draws Pokemon Imgs, Names, and Health Bars"""
        win.blit(Player.pokemon_list[0].img, (PlayerX, PlayerY))
        win.blit(Ai.pokemon_list[0].img, (AiX, AiY))
        if PlayerX == Player_img_anchor[0] and PlayerY == Player_img_anchor[1]:
            #Pokemon Name and Level Text
            playerPokemonNameText = PokemonFont.render(Player.current_pokemon.name, False, (0, 0, 0))
            playerPokemonNameLvlText = PokemonFont.render(":L" + str(Player.current_pokemon.lvl), False, (0, 0, 0))
            win.blit(playerPokemonNameText, (1200, 400))
            win.blit(playerPokemonNameLvlText, (1250, 450))
            #Pokemon Health bars
            pygame.draw.rect(win, green, pygame.Rect(1100, 500, 400, 10))


running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    win.fill(white)



    #Draw Pokemon
    GameUI.draw_pokemon()

    #Draw Player Pokemon Abilities
    textsurface = PokemonFont.render('Some Text', False, (0, 0, 0))
    win.blit(textsurface, (100, 100))



    pygame.display.update()

# Done! Time to quit.
pygame.quit()

Rattatata.use_ability(1, Pigey)

