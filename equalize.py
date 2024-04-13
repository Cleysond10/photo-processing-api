import base64
import numpy as np
import cv2


def quantil_equalize(base64_string):
    """Function to equalize image"""
    # Decode base64 string to image
    nparr = np.frombuffer(base64.b64decode(base64_string), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert BGR to YCrCb
    img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Equalize Y channel using percentiles
    y_channel = img_converted[:,:,0]
    min_percentile = np.percentile(y_channel, 1)
    max_percentile = np.percentile(y_channel, 99)
    y_channel = np.clip(y_channel, min_percentile, max_percentile)
    y_channel = ((y_channel - min_percentile) / (max_percentile - min_percentile)) * 255
    img_converted[:,:,0] = y_channel.astype(np.uint8)

    # Convert YCrCb back to BGR
    img_output = cv2.cvtColor(img_converted, cv2.COLOR_YCrCb2BGR)

    # Encode BGR image to base64 string
    _, img_encoded = cv2.imencode('.jpg', img_output)
    base64_output = base64.b64encode(img_encoded).decode('utf-8')

    return base64_output


# ==============================================================================

# def quantil_equalize_2(base64_string):
#     """Function to equalize image in YCrCb with percentil of 0,1."""
#     nparr = np.frombuffer(base64.b64decode(base64_string), np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     # Converte BRG para YCrCb com o formato
#     jpgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

#     # Isola a imagem em nível de cinza - GRAY, para melhorar os limiares dela
#     jpGray = jpgYCrCb[:, :, 0]  # Obtem a banda Y da imagem YCrCb

#     # Quantil's Equalize method

#     # Step 1 - Definição dos Percentis [minPercentil,maxPercentil]
#     minPercentil = np.percentile(jpGray, 1)
#     maxPercentil = np.percentile(jpGray, 99)

#     # Step 2 - Truncamentodos dos dados pelos Percentis [minPercentil,maxPercentil]
#     jpgTrunc = jpGray

#     n_linhas = jpgTrunc.shape[0]

#     for i in range(n_linhas):
#         arr = jpgTrunc[i, :]
#         jpgTrunc[i, np.where(arr > maxPercentil)] = maxPercentil
#         jpgTrunc[i, np.where(arr < minPercentil)] = minPercentil

#     # Step 3 - Mapeamento dos dados [minPercentil,maxPercentil] para [0,255]
#     jpgMap = jpgTrunc

#     n2_linhas = jpgMap.shape[0]

#     razao = maxPercentil - minPercentil

#     for i in range(n2_linhas):
#         arr2 = jpgMap[i, :]
#         jpgMap[i, :] = ((arr2 - minPercentil)/razao)*255

#     # Altera o valor da banda Y na imagem YCrCb para converter para a BGR em seguida.
#     jpgYCrCbResult = jpgYCrCb
#     # Obtem a banda Y da imagem YCrCb Resultante
#     jpgYCrCbResult[:, :, 0] = jpgMap
#     jpgResult = cv2.cvtColor(jpgYCrCbResult, cv2.COLOR_YCrCb2BGR)

#     _, img_encoded = cv2.imencode('.jpg', jpgResult)
#     base64_output = base64.b64encode(img_encoded).decode('utf-8')

#     return base64_output
