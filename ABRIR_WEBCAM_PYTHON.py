"""
PROJETO PARA APRENDER A LIGAR WEBCAM USANDO O PYTHON
"""

"""
Criado: 18/02/22
Autor: Gregory Wells
Objetivo: aprender novas aplicações do python e lógicas que poderao ser usadas em projetos mais robustos.
"""


import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #criei uma variável para receber o objeto de captura de tela e passa a
#webcam 0 (default ou a padrão do notebook) como a webcam que será utilizada.

while True:
    conexao, frame = video.read()   #aqui irá ler a conexão e o frame à frame enquanto o loop estiver rodando
    cv2.imshow('Video', frame)  #aqui mostrará os frames
    if cv2.waitKey(1) == ord('f'):   #aqui eu criei um botão que irá forçar a finalização da gravação com a webcam
        break   #ela terá o delayde 1s, ou seja, a cada segundo o programa irá esperar o botão para finalizar a aplicação.

video.release() #este comando serve para 'liberar' a câmera após o término do uso.
cv2.destroyAllWindows() #aqui serve para limpar a memória ao final da gravação para não desperdiçar espaço atoa