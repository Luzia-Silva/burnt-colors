# BurntColors

![Alt Text](https://media.giphy.com/media/pQmWjYrz39YAg/giphy.gif)

Ao decorrer do desenvolvimento do projeto BurntColors, enfrentamos dificuldades para estabelecer uma análise de dados de imagens com diferentes colorações em graus de queimaduras I e II, que apresentam uma coloração vermelha, enquanto as queimaduras de grau III ultrapassam todas as camadas da pele.

Para lidar com esse desafio, criamos um algoritmo utilizando a biblioteca OpenCV para processar a imagem com o grau de queimadura e mapear a cor vermelha. Em seguida, o algoritmo busca a quantidade de pixels na cor vermelha e realiza a conversão para porcentagem.

Esses dados são salvos em uma planilha no Google Sheets como base para outras análises. Todos esses dados são coletados para que seja possível calcular a média, o maior e o menor valor encontrados.

Com base nesses resultados, estabelecemos a seguinte lógica: valores menores do que o menor valor encontrado são classificados como "Grau I de queimadura", enquanto valores maiores do que o valor encontrado são classificados como "Grau II de queimadura". No entanto, é importante ressaltar que esse trabalho não busca uma análise exata dos graus de queimaduras, mas sim o processamento de uma pequena quantidade de dados que pode permitir que o algoritmo gere análises inteligentes.

Esse projeto openSource para que as comunidade possam implementar melhorias e trazer inovações e até mesmo a conexão com banco de dados que suportam uma quantidade mais robusta de dados.

</br>

# Inicialização

Instale as dependências disponibilizadas no requirements.txt dentro do seu ambiente virtual, então siga todos os passos abaixo:

Windows:

```
  python -m venv venv
  source venv/Scripts/activate
  pip install -r requirements.txt
  python3 main.py

```

Linux:

```
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python3 main.py

```

# Depêndencias

- [Opencv-python](https://opencv.org/) - versão 4.7.0.72
- [Matplotlib](https://matplotlib.org/) - versão 3.7.1
- [Numpy](https://numpy.org/) - versão 1.24.3
- [Google-api-python-client](https://developers.google.com/sheets/api/guides/libraries?hl=pt-br#python) - vers3.10.6


# Resultados 

<br>
 <h3 align="center">
      <p>Copyright © 2023 Girludev Company</p>
    
 </h3>




