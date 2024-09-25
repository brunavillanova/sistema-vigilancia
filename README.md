Documentação do Sistema de Vigilância com YOLOv8
Descrição

Este projeto utiliza o modelo YOLOv8 para detectar pessoas em um vídeo. O sistema processa os frames do vídeo em tempo real, exibindo caixas delimitadoras ao redor das detecções e mostrando a taxa de quadros por segundo (FPS).
Requisitos

    Python 3.7 ou superior
    Bibliotecas necessárias:
        opencv-python
        ultralytics

Instalação

    Clone o repositório:

    bash

git clone https://github.com/brunavillanova/sistema-vigilancia.git
cd sistema-vigilancia

Instale as dependências:

bash

    pip install opencv-python ultralytics

    Baixe o modelo YOLOv8: Certifique-se de que o arquivo yolov8n.pt (modelo nano) está na pasta classificadores.

    Prepare seu vídeo: Coloque o arquivo de vídeo desejado na pasta videos e certifique-se de que o caminho no código está correto.

Uso

    Execute o script:

    bash

    python sistema_de_vigilancia.py

    Visualização: O sistema abrirá uma janela exibindo o vídeo processado, com detecções de pessoas e a taxa de FPS atual. Para sair do vídeo, pressione a tecla "q".

Estrutura do Código
Principais componentes:

    Importação de bibliotecas: O código começa importando as bibliotecas necessárias: YOLO do pacote ultralytics e cv2 para manipulação de vídeo.

    Carregamento do modelo: O modelo YOLOv8 é carregado a partir do arquivo .pt.

    Captura de vídeo: O vídeo é aberto usando a função cv.VideoCapture.

    Processamento de frames: Um loop é iniciado para ler e processar cada frame do vídeo. Para cada frame:
        O tamanho do frame é reduzido para otimizar a detecção.
        O modelo realiza a detecção de pessoas.
        As caixas delimitadoras são desenhadas em torno das detecções.
        O FPS é calculado e exibido.

Exibição de resultados:

Os frames processados são exibidos em uma janela até que a tecla "q" seja pressionada ou até que o vídeo termine.
Contribuição

Se você deseja contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas.
Licença

Este projeto está sob a licença MIT.
