
from turtle import Turtle, Screen
import os
from PIL import Image

# Configura a tela com imagem ou cor no fundo
def configurar_tela(bg_image="img/fundo.png", bg_color=None):
    screen = Screen()

    if os.path.isfile(bg_image):
        #Obter dimensoes da imagem
        with Image.open(bg_image) as img:
            largura, altura = img.size
        
        #ajustar o tamanho da tela 
        screen.setup(width=largura, height=altura)
        screen.bgpic(bg_image)

    return screen   

# Configura a tartaruga
def configura_tartaruga():
    t = Turtle()
    t.shape("turtle") 
    t.color("white","darkgreen")
    t.speed(1)

    return t

# Movimenta a tartaruga para frente
def mov_frente():
    global movendo_frente
    movendo_frente = True

# Para o movimento da tartaruga para frente
def stop_frente():
    global movendo_frente
    movendo_frente = False

# Movimenta a tartaruga para trás
def mov_tras():
    global movendo_tras
    movendo_tras = True

# Para o movimento da tartaruga para trás
def stop_tras():
    global movendo_tras
    movendo_tras = False

# Movimenta a tartaruga para trás
def rot_direita():
    global rotaciona_direita
    rotaciona_direita = True

# Para o movimento da tartaruga para esquerda
def stop_direita():
    global rotaciona_direita
    rotaciona_direita = False

# Movimenta a tartaruga para trás
def rot_esquerda():
    global rotaciona_esquerda
    rotaciona_esquerda = True

# Para o movimento da tartaruga para esquerda
def stop_esquerda():
    global rotaciona_esquerda
    rotaciona_esquerda = False

# Fecha a aplicação
def fechar_aplicacao():
    global screen
    screen.bye()

# Função principal
def main():
    global movendo_frente, movendo_tras, rotaciona_direita, rotaciona_esquerda
    screen = configurar_tela()
    t = configura_tartaruga()

    movendo_frente = False
    movendo_tras = False
    rotaciona_direita = False
    rotaciona_esquerda = False

    limite_x_max = screen.window_width() / 2 - 20
    limite_x_min = -limite_x_max
    limite_y_max = screen.window_height() / 2 - 20
    limite_y_min = -limite_y_max

   

    # Associa o movimento da tartaruga às teclas correspondentes
    screen.onkeypress(mov_frente, "w")  # Tecla "w" para frente
    screen.onkey(stop_frente, "w")  # Solta a tecla "w"
    
    screen.onkeypress(mov_tras, "s")  # Tecla "s" para trás
    screen.onkey(stop_tras, "s")  # Solta a tecla "s"
    
    screen.onkeypress(rot_direita, "d")  # Tecla "d" para direita
    screen.onkey(stop_direita, "d")  # Solta a tecla "d"
    
    screen.onkeypress(rot_esquerda, "a")  # Tecla "a" para esquerda
    screen.onkey(stop_esquerda, "a")  # Solta a tecla a"
    
    screen.onkey(fechar_aplicacao, 'q') #fechar aplicativo
    
    # Habilita o tratamento de eventos de teclado
    screen.listen()

    # Loop principal
    while True:
        
        if t.xcor() >= limite_x_max or t.xcor() <= limite_x_min or t.ycor() >= limite_y_max or t.ycor() <= limite_y_min:
            t.goto(0,0)
            
        else:     
            if movendo_frente:
                t.forward(10)
            if movendo_tras:
                t.backward(10)
            if rotaciona_direita:
                t.right(10)
            if rotaciona_esquerda:
                t.left(10)

        # Atualiza a tela
        screen.update()

if __name__ == "__main__":
    main()
