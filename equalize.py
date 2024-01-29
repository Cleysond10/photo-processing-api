import os
import numpy as np
import cv2


def quantil_equalize(path):
    """Function to equalize image in YCrCb with percentil of 0,1."""
    filename = os.path.basename(path).split('.')[0]

    # Read image no formato BGR do OpenCV
    jpgColor = cv2.imread(path)

    # Salva a imagem original
    cv2.imwrite(f'{filename}_Original.JPG', jpgColor)

    # Converte BRG para YCrCb com o formato
    jpgYCrCb = cv2.cvtColor(jpgColor, cv2.COLOR_BGR2YCrCb)

    # Isola a imagem em nível de cinza - GRAY, para melhorar os limiares dela
    jpGray = jpgYCrCb[:, :, 0]  # Obtem a banda Y da imagem YCrCb

    # Quantil's Equalize method

    # Step 1 - Definição dos Percentis [minPercentil,maxPercentil]
    minPercentil = np.percentile(jpGray, 1)
    maxPercentil = np.percentile(jpGray, 99)

    # Step 2 - Truncamentodos dos dados pelos Percentis [minPercentil,maxPercentil]
    jpgTrunc = jpGray

    n_linhas = jpgTrunc.shape[0]

    for i in range(n_linhas):
        arr = jpgTrunc[i, :]
        jpgTrunc[i, np.where(arr > maxPercentil)] = maxPercentil
        jpgTrunc[i, np.where(arr < minPercentil)] = minPercentil

    # Step 3 - Mapeamento dos dados [minPercentil,maxPercentil] para [0,255]
    jpgMap = jpgTrunc

    n2_linhas = jpgMap.shape[0]

    razao = maxPercentil - minPercentil

    for i in range(n2_linhas):
        arr2 = jpgMap[i, :]
        jpgMap[i, :] = ((arr2 - minPercentil)/razao)*255

    # Altera o valor da banda Y na imagem YCrCb para converter para a BGR em seguida.
    jpgYCrCbResult = jpgYCrCb
    # Obtem a banda Y da imagem YCrCb Resultante
    jpgYCrCbResult[:, :, 0] = jpgMap
    jpgResult = cv2.cvtColor(jpgYCrCbResult, cv2.COLOR_YCrCb2BGR)

    # Salva a imagem final
    cv2.imwrite(f'{filename}_quantil_equaliz.JPG', jpgResult)
