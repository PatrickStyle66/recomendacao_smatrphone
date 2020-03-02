from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from owlready2 import *
import os
onto = get_ontology("recomendacaoCelulares.owl")
onto.load()

query = onto.Thing("a")
description ={"Xiaomi_MI_Mix_2":"O Xiaomi Qin AI Pro é um smartphone Android mediano, ideal para quem não tem muitas exigências mas não abre mão de um bom display touchscreen. As funções oferecidas pelo Xiaomi Qin AI Pro são mais ou menos as mesmas oferecidas em outros dispositivos avançados, começando com a conectividade Wi-fi e GPS. Tem leitor multimídia e bluetooth. Enfatizamos a boa memória interna de 32 GB mas sem a possibilidade de expansão. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA.Tem uma grande tela Touchscreen de 5.05 polegadas com uma resolução de 1440x576 pixels. Câmera de 5 megapixels que permite ao Xiaomi Qin AI Pro tirar fotos de alta qualidade com uma resolução de 2582x1936 pixels. Muito fino, 8.6 milímetros, o que torna o Xiaomi Qin AI Pro realmente bom para o transporte.",
              "iPhone_11":"O Apple iPhone 11 é um dos smartphones iOS mais avançados e completos que existem em circulação. Tem um grande display de 6.1 polegadas com uma resolução de 1792x828 pixel. As funcionalidades oferecidas pelo Apple iPhone 11 são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 512 GB mas sem a possibilidade de expansão.Câmera discreta de 12 megapixel mas que permite ao Apple iPhone 11 tirar fotos de boa qualidade com uma resolução de 4000x3000 pixel e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels.",
              "iPhone_6S":"O Apple iPhone 6S é um smartphone iOS de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma tela Touchscreen de 4.7 polegadas com uma resolução de 1334x750 pixels. Sobre as características deste Apple iPhone 6S na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, videoconferência e bluetooth. Enfatizamos a boa memória interna de 128 GB mas sem a possibilidade de expansão.O Apple iPhone 6S é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Apple iPhone 6S tirar fotos de alta qualidade com uma resolução de 4608x2592 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 7.1 milímetros, o que torna o Apple iPhone 6S realmente interessante.",
              "iPhone_8_Plus":"O Apple iPhone 8 Plus é um dos smartphones iOS mais avançados e completos que existem em circulação. Tem um grande display de 5.5 polegadas com uma resolução de 1920x1080 pixel. As funcionalidades oferecidas pelo Apple iPhone 8 Plus são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 256 GB mas sem a possibilidade de expansão.Câmera discreta de 12 megapixel mas que permite ao Apple iPhone 8 Plus tirar fotos de boa qualidade com uma resolução de 4608x2592 pixel e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. A espessura de 7.5mm torna o Apple iPhone 8 Plus um dos telefones mais completos e finos.",
              "iPhone_XS_Max":"O Apple iPhone XS Max é um dos smartphones iOS mais avançados e completos que existem em circulação. Tem um grande display de 6.5 polegadas com uma resolução de 2688x1242 pixel. As funcionalidades oferecidas pelo Apple iPhone XS Max são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 512 GB mas sem a possibilidade de expansão.Câmera discreta de 12 megapixel mas que permite ao Apple iPhone XS Max tirar fotos de boa qualidade com uma resolução de 4608x2592 pixel e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. A espessura de 7.7mm torna o Apple iPhone XS Max um dos telefones mais completos e finos.",
              "ZenFone_Max_Shot":"O Asus ZenFone Max Shot é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma enorme tela Touchscreen de 6.26 polegadas com uma resolução de 2280x1080 pixel. Sobre as características deste Asus ZenFone Max Shot na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, rádio, videoconferência e bluetooth. Enfatizamos a boa memória interna de 32 GB com a possibilidade de expansão.O Asus ZenFone Max Shot é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Asus ZenFone Max Shot tirar fotos de alta qualidade com uma resolução de 4000x3000 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels. Muito fino, 8.5 milímetros, o que torna o Asus ZenFone Max Shot realmente interessante.",
              "ZenFone_Zoom":"O Asus ZenFone Zoom é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma grande tela Touchscreen de 5.5 polegadas com uma boa resolução de 1920x1080 pixels. Sobre as características deste Asus ZenFone Zoom na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, videoconferência e bluetooth. Enfatizamos a boa memória interna de 128 GB com a possibilidade de expansão.O Asus ZenFone Zoom é um produto com poucos concorrentes em termos de multimídia graças à câmera de 13 megapixels que permite ao Asus ZenFone Zoom tirar fotos fantásticas com uma resolução de 4128x3096 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels.",
              "ZenFone_Zoom_S":"O Asus ZenFone Zoom S é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma grande tela Touchscreen de 5.5 polegadas com uma boa resolução de 1920x1080 pixels. Sobre as características deste Asus ZenFone Zoom S na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, rádio, videoconferência e bluetooth. Enfatizamos a boa memória interna de 32 GB com a possibilidade de expansão.O Asus ZenFone Zoom S é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Asus ZenFone Zoom S tirar fotos de alta qualidade com uma resolução de 4608x2592 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 8 milímetros, o que torna o Asus ZenFone Zoom S realmente interessante.",
              "Huawei_P_smart":"O Huawei P smart 2019 é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma enorme tela Touchscreen de 6.21 polegadas com uma resolução de 2340x1080 pixel. Sobre as características deste Huawei P smart 2019 na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, rádio, videoconferência e bluetooth. Enfatizamos a boa memória interna de 64 GB com a possibilidade de expansão.O Huawei P smart 2019 é um produto com poucos concorrentes em termos de multimídia graças à câmera de 13 megapixels que permite ao Huawei P smart 2019 tirar fotos fantásticas com uma resolução de 4163x3122 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels. Muito fino, 8 milímetros, o que torna o Huawei P smart 2019 realmente interessante.",
              "Huawei_P30_Pro":"O Huawei P30 Pro é um smartphone Android com características inovadoras que o tornam uma excelente opção para qualquer tipo de utilização, representando um dos melhores dispositivos móveis já feitos. A tela de 6.47 polegadas coloca esse Huawei no topo de sua categoria. A resolução também é alta: 2340x1080 pixel. As funcionalidades oferecidas pelo Huawei P30 Pro são muitas e todas top de linha. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS presente no aparelho. Tem também leitor multimídia, videoconferência, e bluetooth. Enfatizamos a excelente memória interna de 256 GB com a possibilidade de expansão.A excelência deste Huawei P30 Pro é completada por uma câmera de 40 megapixels que permite tirar fotos fantásticas com uma resolução de 7303x5477 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. A espessura de 8.4 milímetros é realmente ótima e torna o Huawei P30 Pro ainda mais espetacular.",
              "Lg_G2_Mini_Lite":"O LG G2 mini LTE é um smartphone Android simples, mas com funcionalidades completas, mas ainda oferece poucas funcionalidades para lazer e diversão. As funcionalidades oferecidas pelo LG G2 mini LTE são mais ou menos as presentes em todos os dispositivos mais avançados, começando com a conectividade Wi-fi e o GPS. Dispõe além de mp3 player, radio, video conferência e bluetooth. Enfatizamos a 8 GB com a possibilidade de expansão. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA.Tem uma grande tela Touchscreen de 4.7 polegadas com uma resolução de 960x540 pixels. O LG G2 mini LTE é um produto com poucos concorrentes em termos de multimídia graças à câmera de 8 megapixels que permite ao LG G2 mini LTE tirar fotos fantásticas com uma resolução de 3264x2448 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels. Muito fino, 9.8 milímetros, o que torna o LG G2 mini LTE realmente bom para o transporte.",
              "Lg_K7":"O LG K7 é um smartphone Android simples, mas com funcionalidades completas, mas ainda oferece poucas funcionalidades para lazer e diversão. As funcionalidades oferecidas pelo LG K7 são mais ou menos as presentes em todos os dispositivos mais avançados, começando com a conectividade Wi-fi e o GPS. Dispõe além de mp3 player, video conferência e bluetooth. Enfatizamos a 8 GB com a possibilidade de expansão. Excelente a transferência de dados e navegação web através do suporte HSDPA e HSUPA.Tem uma enorme tela Touchscreen de 5 polegadas com uma resolução de 854x480 pixel que não é das mais elevadas. Ótima a câmera de 5 megapixels que permite ao LG K7 tirar fotos de alta qualidade com uma resolução de 2592x1944 pixels e gravar vídeos. Muito fino, 8.9 milímetros, o que torna o LG K7 realmente bom para o transporte.",
              "Motorola_EX128":"O Motorola EX128 possui uma tela sensível ao toque de 3,2 polegadas, câmera de 3,2 megapixels, estéreo Bluetooth, reprodutor de música, rádio estéreo FM e slot para cartão de memória microSD.",
              "Motorola_E4":"O Motorola Moto E4 é um smartphone Android mediano, ideal para quem não tem muitas exigências mas não abre mão de um bom display touchscreen. As funções oferecidas pelo Motorola Moto E4 são mais ou menos as mesmas oferecidas em outros dispositivos avançados, começando com a conectividade Wi-fi e GPS. Tem leitor multimídia, videoconferência e bluetooth. Enfatizamos a boa memória interna de 16 GB com a possibilidade de expansão. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA.Tem uma grande tela Touchscreen de 5 polegadas com uma resolução de 1280x720 pixels. Ótima a câmera de 8 megapixels que permite ao Motorola Moto E4 tirar fotos fantásticas com uma resolução de 3266x2449 pixels e gravar vídeos com uma resolução de 1280x720 pixel. Muito fino, 8.9 milímetros, o que torna o Motorola Moto E4 realmente bom para o transporte.",
              "Motorola_G7_Plus":"O Motorola Moto G7 Plus é um smartphone Android avançado e abrangente em todos os pontos de vista com algumas características excelentes. Tem uma grande tela de 6.24 polegadas com uma resolução de 2270x1080 pixels. As funcionalidades oferecidas pelo Motorola Moto G7 Plus são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 64 GB com a possibilidade de expansão.O Motorola Moto G7 Plus é um produto com poucos concorrentes em termos de multimídia graças à câmera de 16 megapixels que permite ao Motorola Moto G7 Plus tirar fotos fantásticas com uma resolução de 4619x3464 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 8.3 milímetros, o que torna o Motorola Moto G7 Plus realmente interessante.",
              "Palm_Phone":"O Palm Phone é um smartphone Android completo, que não tem muito a invejar aos mais avançados dispositivos. A tela Touchscreen é de 3.3 polegadas com uma resolução de 1280x720 pixels. Quanto às funções, no Palm Phone realmente não falta nada. Começando pelo conectividade Wi-fi e GPS. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA. Enfatizamos a boa memória interna de 32 GB mas sem a possibilidade de expansão.Este Palm Phone é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Palm Phone tirar fotos fantásticas com uma resolução de 4000x3000 pixels e gravar vídeos com uma resolução de 1280x720 pixel. Muito fino, 7.4 milímetros, o que torna o Palm Phone realmente interessante.",
              "Galaxy_A30s":"Samsung Galaxy A30s é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma enorme tela Touchscreen de 6.4 polegadas com uma resolução de 1560x720 pixel que não é das mais elevadas. Sobre as características deste Samsung Galaxy A30s na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, rádio, videoconferência, TV e bluetooth. Enfatizamos a boa memória interna de 64 GB com a possibilidade de expansão.O Samsung Galaxy A30s é um produto com poucos concorrentes em termos de multimídia graças à câmera de 25 megapixels que permite ao Samsung Galaxy A30s tirar fotos fantásticas com uma resolução de 5774x4330 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels. Muito fino, 7.7 milímetros, o que torna o Samsung Galaxy A30s realmente interessante.",
              "Galaxy_Note_9":"O Samsung Galaxy Note 9 é um dos smartphones Android mais avançados e completos que existem em circulação. Tem um grande display de 6.4 polegadas e uma resolução de 2960x1440 pixels que é uma das mais altas atualmente em circulação. As funcionalidades oferecidas pelo Samsung Galaxy Note 9 são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 128 GB com a possibilidade de expansão.Câmera discreta de 12 megapixel mas que permite ao Samsung Galaxy Note 9 tirar fotos de boa qualidade com uma resolução de 4290x2800 pixel e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels.",
              "Galaxy_S10_Plus":"O Samsung Galaxy S10 Plus é um smartphone Android com características inovadoras que o tornam uma excelente opção para qualquer tipo de utilização, representando um dos melhores dispositivos móveis já feitos. A tela de 6.4 polegadas coloca esse Samsung no topo de sua categoria. Além disso a resolução é das mais altas atualmente em circulação: 3040x1440 pixel. As funcionalidades oferecidas pelo Samsung Galaxy S10 Plus são muitas e todas top de linha. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS presente no aparelho. Tem também leitor multimídia, videoconferência, e bluetooth. Enfatizamos a excelente memória interna de 128 GB com a possibilidade de expansão.Câmera de 12 megapixel. A espessura de apenas 7.8 milímetros torna o Samsung Galaxy S10 Plus um dos telefones mais finos que existem.",
              "Galaxy_S7":"O Samsung Galaxy S7 é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma grande tela Touchscreen de 5.1 polegadas com uma boa resolução de 2560x1440 pixels. Sobre as características deste Samsung Galaxy S7 na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, videoconferência e bluetooth. Enfatizamos a boa memória interna de 32 GB com a possibilidade de expansão.O Samsung Galaxy S7 é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Samsung Galaxy S7 tirar fotos de alta qualidade com uma resolução de 4290x2800 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 7.9 milímetros, o que torna o Samsung Galaxy S7 realmente interessante.",
              "Multilaser_E_Lite":"O Multilaser E Lite é um smartphone Android simples, mas com funcionalidades completas, mas ainda oferece poucas funcionalidades para lazer e diversão. As funcionalidades oferecidas pelo Multilaser E Lite são mais ou menos as presentes em todos os dispositivos mais avançados, começando com a conectividade Wi-fi e o GPS. Dispõe além de mp3 player, video conferência e bluetooth. Enfatizamos a boa 16 GB com a possibilidade de expansão. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA.Tem uma ampla tela Touchscreen de 4 polegadas com uma resolução de 800x480 pixels . Ótima a câmera de 5 megapixels que permite ao Multilaser E Lite tirar fotos de alta qualidade com uma resolução de 2582x1936 pixels. Muito fino, 9.4 milímetros, o que torna o Multilaser E Lite realmente bom para o transporte.",
              "Lg_Q_Note_Plus":"O LG Q Note Plus é um smartphone Android completo, que não tem muito a invejar aos mais avançados dispositivos. Surpreendente é sua tela Touchscreen de 6.2 polegadas, que coloca esse LG no topo de sua categoria. A resolução também é alta: 2160x1080 pixel. Quanto às funções, no LG Q Note Plus realmente não falta nada. Começando pelo conectividade Wi-fi e GPS. A transferência de dados e navegação web sao fornecidas pela rede UMTS, mas não suporta tecnologias mais recentes, tais como HSDPA. Enfatizamos a boa memória interna de 64 GB com a possibilidade de expansão.Este LG Q Note Plus é um produto com poucos concorrentes em termos de multimídia graças à câmera de 16 megapixels que permite ao LG Q Note Plus tirar fotos fantásticas com uma resolução de 4619x3464 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels. Muito fino, 8.1 milímetros, o que torna o LG Q Note Plus realmente interessante.",
              "Redmi_8":"O Redmi 8 é um smartphone Android de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma enorme tela Touchscreen de 6.22 polegadas com uma resolução de 1520x720 pixel que não é das mais elevadas. Sobre as características deste Redmi 8 na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, rádio, videoconferência e bluetooth. Enfatizamos a boa memória interna de 32 GB com a possibilidade de expansão.O Redmi 8 é um produto com poucos concorrentes em termos de multimídia graças à câmera de 12 megapixels que permite ao Redmi 8 tirar fotos de alta qualidade com uma resolução de 4000x3000 pixels e gravar vídeos em alta definição (Full HD) com uma resolução de 1920x1080 pixels.",
              "Motorola_One_Hyper":"O Motorola One Hyper é, sem dúvida, um dos smartphones Android mais avançados e abrangentes disponíveis no mercado, graças ao seu rico equipamento e recursos multimídia avançados. Tem um grande display de 6.5 polegadas com uma resolução de 2340x1080 pixel. As funcionalidades oferecidas pelo Motorola One Hyper são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 128 GB com a possibilidade de expansão.O Motorola One Hyper é um produto com poucos concorrentes em termos de multimídia graças à câmera de 64 megapixels que permite ao Motorola One Hyper tirar fotos fantásticas com uma resolução de 9238x6928 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels.",
              "Xiaomi_MI_A3":"O Xiaomi Mi A3 é um celular Touchscreen de bom nível, ótimo para fotos, que pode satisfazer até o mais exigente dos usuários. Tem uma enorme tela Touchscreen de 6.08 polegadas com uma resolução de 1560x720 pixel que não é das mais elevadas. Sobre as características deste Xiaomi Mi A3 na verdade não falta nada. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS. Tem também leitor multimídia, videoconferência e bluetooth. Enfatizamos a boa memória interna de 64 GB com a possibilidade de expansão.O Xiaomi Mi A3 é um produto com poucos concorrentes em termos de multimídia graças à câmera de 48 megapixels que permite ao Xiaomi Mi A3 tirar fotos fantásticas com uma resolução de 8000x6000 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 8.5 milímetros, o que torna o Xiaomi Mi A3 realmente interessante.",
              "Galaxy_Note_10_Lite":"O Samsung Galaxy Note 10 Lite é um smartphone Android avançado e abrangente em todos os pontos de vista com algumas características excelentes. Tem uma grande tela de 6.7 polegadas com uma resolução de 2400x1080 pixels. As funcionalidades oferecidas pelo Samsung Galaxy Note 10 Lite são muitas e inovadoras. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet. Enfatizamos a excelente memória interna de 128 GB com a possibilidade de expansão.Respeitável a câmera de 12 megapixels que permite ao Samsung Galaxy Note 10 Lite tirar fotos com uma resolução de 4000x3000 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. Muito fino, 8.7 milímetros, o que torna o Samsung Galaxy Note 10 Lite realmente interessante.",
              "Xiaomi_MI_9":"O Xiaomi Mi 9 é um smartphone Android com características inovadoras que o tornam uma excelente opção para qualquer tipo de utilização, representando um dos melhores dispositivos móveis já feitos. A tela de 6.39 polegadas coloca esse Xiaomi no topo de sua categoria. A resolução também é alta: 2340x1080 pixel. As funcionalidades oferecidas pelo Xiaomi Mi 9 são muitas e todas top de linha. Começando pelo LTE 4G que permite a transferência de dados e excelente navegação na internet, além de conectividade Wi-fi e GPS presente no aparelho. Tem também leitor multimídia, videoconferência, e bluetooth. Enfatizamos a excelente memória interna de 64 GB mas sem a possibilidade de expansão.A excelência deste Xiaomi Mi 9 é completada por uma câmera de 48 megapixels que permite tirar fotos fantásticas com uma resolução de 8000x6000 pixels e gravar vídeos em 4K a espantosa resolução de 3840x2160 pixels. A espessura de apenas 7.6 milímetros torna o Xiaomi Mi 9 um dos telefones mais finos que existem.",
              }

class questionScreen():
    def radioEventS0(self):
        radSelected = self.radValues.get()

        if radSelected == 1:
            self.query.Android = [onto.true]
        elif radSelected == 2:
            self.query.iOS = [onto.true]
    def radioEventTela(self):
        radSelected = self.radValues1.get()

        if radSelected == 1:
            self.query.TelaHD = [onto.true]
        elif radSelected == 2:
            self.query.TelaHD = [onto.false]
    def radioEventCam(self):
        radSelected = self.radValues2.get()

        if radSelected == 1:
            self.query.CameraFrontal = [onto.true]
        elif radSelected == 2:
            self.query.CameraFrontal = [onto.false]
    def radioEventChip(self):
        radSelected = self.radValues3.get()

        if radSelected == 1:
            self.query.Dualchip = [onto.true]
        elif radSelected == 2:
            self.query.Dualchip = [onto.false]
    def radioEventLeitor(self):
        radSelected = self.radValues4.get()

        if radSelected == 1:
            self.query.LeitorBiometrico = [onto.true]
        elif radSelected == 2:
            self.query.LeitorBiometrico = [onto.false]
    def radioEventFace(self):
        radSelected = self.radValues5.get()

        if radSelected == 1:
            self.query.ReconhecimentoFacial = [onto.true]
        elif radSelected == 2:
            self.query.ReconhecimentoFacial = [onto.false]
    def radioEventAgua(self):
        radSelected = self.radValues6.get()

        if radSelected == 1:
            self.query.ResistenciaAgua = [onto.true]
        elif radSelected == 2:
            self.query.ResistenciaAgua = [onto.false]
    def radioEventUsb(self):
        radSelected = self.radValues7.get()

        if radSelected == 1:
            self.query.UsbTipoC = [onto.true]
        elif radSelected == 2:
            self.query.UsbTipoC = [onto.false]
    def radioEvent4k(self):
        radSelected = self.radValues8.get()

        if radSelected == 1:
            self.query.Video4K = [onto.true]
        elif radSelected == 2:
            self.query.Video4K = [onto.false]
    def radioEventWifi(self):
        radSelected = self.radValues9.get()

        if radSelected == 1:
            self.query.WiFi = [onto.true]
        elif radSelected == 2:
            self.query.WiFi = [onto.false]
    def radioEventValor(self):
        radSelected = self.radValues10.get()

        if radSelected == 1:
            self.query.ValorMenorQueMil = [onto.true]
        elif radSelected == 2:
            self.query.ValorEntreMilEDoisMil = [onto.true]
        elif radSelected == 3:
            self.query.ValorMaiorQueDoisMil = [onto.true]
    def __init__(self,root,query):
        self.root = root
        self.root.title('Recomendador de Smartphones')
        self.query = query
        Label(text="Sistema Android ou iOS?").grid(row = 1, column = 1,pady = 10)
        self.radValues = IntVar()
        rad1 = ttk.Radiobutton(text = 'Android',value = 1,variable = self.radValues,command = self.radioEventS0)
        rad1.grid(row = 2, column = 1, columnspan=3,sticky = W)
        rad2 = ttk.Radiobutton(text = 'iOS',value = 2,variable = self.radValues,command = self.radioEventS0)
        rad2.grid(row=2, column=2, columnspan=3, sticky=W)
        Label(text ="Tem o Display HD?").grid(row = 3, column = 1,pady = 10)
        self.radValues1 = IntVar()
        rad3 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues1, command=self.radioEventTela)
        rad3.grid(row=4, column=1, columnspan=3, sticky=W)
        rad4 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues1, command=self.radioEventTela)
        rad4.grid(row=4, column=2, columnspan=3, sticky=W)
        self.radValues2 = IntVar()
        Label(text = "Tem Câmera Frontal?").grid(row = 5,column = 1,pady = 10)
        rad5 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues2, command=self.radioEventCam)
        rad5.grid(row=6, column=1, columnspan=3, sticky=W)
        rad6 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues2, command=self.radioEventCam)
        rad6.grid(row=6, column=2, columnspan=3, sticky=W)
        Label(text = "Tem Dual Chip?").grid(row = 7,column = 1, pady = 10)
        self.radValues3 = IntVar()
        rad7 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues3, command=self.radioEventChip)
        rad7.grid(row=8, column=1, columnspan=3, sticky=W)
        rad8 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues3, command=self.radioEventChip)
        rad8.grid(row=8, column=2, columnspan=3, sticky=W)
        Label(text = "Tem Leitor Biométrico?").grid(row = 9,column = 1,pady = 10)
        self.radValues4 = IntVar()
        rad9 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues4, command=self.radioEventLeitor)
        rad9.grid(row=10, column=1, columnspan=3, sticky=W)
        rad10 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues4, command=self.radioEventLeitor)
        rad10.grid(row=10, column=2, columnspan=3, sticky=W)
        Label(text="Tem Reconhecimento Facial?").grid(row=11, column=1, pady=10)
        self.radValues5 = IntVar()
        rad11 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues5, command=self.radioEventFace)
        rad11.grid(row=12, column=1, columnspan=3, sticky=W)
        rad12 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues5, command=self.radioEventFace)
        rad12.grid(row=12, column=2, columnspan=3, sticky=W)
        Label(text="Tem resistência a água?").grid(row = 13,column = 1, pady = 10)
        self.radValues6 = IntVar()
        rad13 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues6, command=self.radioEventAgua)
        rad13.grid(row=14, column=1, columnspan=3, sticky=W)
        rad14 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues6, command=self.radioEventAgua)
        rad14.grid(row=14, column=2, columnspan=3, sticky=W)
        Label(text ="Tem Entrada USB Tipo C?").grid(row = 15,column = 1, pady = 10)
        self.radValues7 = IntVar()
        rad15 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues7, command=self.radioEventUsb)
        rad15.grid(row=16, column=1, columnspan=3, sticky=W)
        rad16 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues7, command=self.radioEventUsb)
        rad16.grid(row=16, column=2, columnspan=3, sticky=W)
        Label(text = "Suporta Vídeo em 4K?").grid(row = 17,column = 1,pady = 10)
        self.radValues8 = IntVar()
        rad17 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues8, command=self.radioEvent4k)
        rad17.grid(row=18, column=1, columnspan=3, sticky=W)
        rad18 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues8, command=self.radioEvent4k)
        rad18.grid(row=18, column=2, columnspan=3, sticky=W)
        Label(text = "Tem conexão Wifi?").grid(row= 19,column = 1, pady = 10)
        self.radValues9 = IntVar()
        rad19 = ttk.Radiobutton(text='Sim', value=1, variable=self.radValues9, command=self.radioEventWifi)
        rad19.grid(row=20, column=1, columnspan=3, sticky=W)
        rad20 = ttk.Radiobutton(text='Não', value=2, variable=self.radValues9, command=self.radioEventWifi)
        rad20.grid(row=20, column=2, columnspan=3, sticky=W)
        Label(text = "Qual a média de Preço?").grid(row = 21,column = 1,pady = 10)
        self.radValues10 = IntVar()
        rad21 = ttk.Radiobutton(text='Menor que R$1000', value=1, variable=self.radValues10, command=self.radioEventValor)
        rad21.grid(row=22, column=1, columnspan=1, sticky=W)
        rad22 = ttk.Radiobutton(text='Entre R$1000 e R$2000', value=2, variable=self.radValues10, command=self.radioEventValor)
        rad22.grid(row=22, column=2, columnspan=1, sticky=W)
        rad23 = ttk.Radiobutton(text='Maior que R$2000', value=3, variable=self.radValues10,command=self.radioEventValor)
        rad23.grid(row=22, column=3, columnspan=1, sticky=W)
        ttk.Button(text ="Enviar",command =self.root.destroy).grid(row =24,column = 1)

root = Tk()
root.geometry('500x725')
rec = questionScreen(root,query)
root.mainloop()
sync_reasoner()
celular = str(rec.query.__class__)
if "FusionClass" in celular:
    celular = celular[celular.rfind("FusionClass") + 12:]
    celular = celular.replace("recomendacaoCelulares.","")
    celular = celular.rstrip(">")
    celular = celular.split(",")
    print("Celulares Recomendados:")
    i = 0
    for x in celular:

        if x[0] == " ":
            x = x[1:]
        name = x
        x =  x.replace("_"," ")
        class photo(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master
                Label(text="Celular recomendado: " + x, font="Impact 25").pack()
                if i != len(celular) - 1:
                    ttk.Button(text="Próximo", command=self.master.destroy).pack(side=RIGHT,fill = X)
                self.pack(fill=BOTH, expand=1)
                load = Image.open(os.path.join('images', name + ".png"))
                render = ImageTk.PhotoImage(load)
                img = Label(self, image=render)
                img.image = render
                img.place(x=0, y=200)
                img.pack(side=LEFT)
                text = Text(master, height=50, width=100)
                text.insert(INSERT, description[name])
                text.config(state="disable")
                text.pack(fill = BOTH,expand = 1)

        root = Tk()
        root.wm_title("Smartphone")
        photo(root)
        root.geometry("727x532")
        root.mainloop()
        i = i+1
elif "celularesdisponiveis" in celular.lower():
    class notFound(Frame):
        def __init__(self,master =None):
                Frame.__init__(self,master)
                self.master = master
                Label(text ="Sem Recomendações Para Esta Especificação",font ="Impact 25").pack()
                self.pack(fill=BOTH, expand=1)
                load = Image.open(os.path.join('images', "prohibited.png"))
                render = ImageTk.PhotoImage(load)
                img = Label(self, image=render)
                img.image = render
                img.place(x=0, y=200)
                img.pack()

    root = Tk()
    root.wm_title("Smartphone")
    notFound(root)
    root.geometry("727x532")
    root.mainloop()
else:
    celular =celular.replace("recomendacaoCelulares.","").strip("")
    class photo(Frame):
        def __init__(self,master =None):
                Frame.__init__(self,master)
                self.master = master
                Label(text ="Celular recomendado: "+celular.replace("_"," "),font ="Impact 25").pack()
                self.pack(fill = BOTH,expand = 1)
                load = Image.open(os.path.join('images',celular +".png"))
                render = ImageTk.PhotoImage(load)
                img = Label(self,image =render)
                img.image = render
                img.place(x=0,y=200)
                img.pack(side =LEFT)
                text = Text(master,height = 50, width = 100)
                text.insert(INSERT,description[celular])
                text.config(state = "disable")
                text.pack()
    root = Tk()
    root.wm_title("Smartphone")
    photo(root)
    root.geometry("727x532")
    root.mainloop()
    print(celular)
