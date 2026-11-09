import pygame
from common.colors import White
from common.constrants import width, height

_front = None

def get_front(size=300:
    global front
        if_front is None or _font.get_height() != size:
    _font = pygame.font.SysFont("calibri",size)
return_font

def draw_score(scren,score, font=None):
    """ Renderiza 'Pontos:X' no canto superior direto."""
    f = fontor get_font()
    text = f.render(f"Pontos:{score}", True, White)
    screen.blit(text, width - 130,10))

def draw_paused(screen, font=None):
    """renderiza 'PAUSADO' no centro da tela."""
    f= font or get_font()
    msg=frender("PAUSADO", True, White)
    rect = msg.get_rect(center=(width // 2,height //2)) screen.blit(msg, rect)

def draw_start_msg(screen, font=None):
    """Renderiza mensagem de início centralizada."""
    f= font or get.font()
    msg= frender("Pressione qualquer tecla para iniciar", True, White)
    rect = msg.get_rect(center=(width // 2,180))
    screen.blit(msg,rect)