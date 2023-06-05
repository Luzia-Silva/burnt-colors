# BurntColors

![Alt Text](https://media.giphy.com/media/pQmWjYrz39YAg/giphy.gif)

Ao decorrer do desenvolvimento do projeto BurntColors, enfrentamos dificuldades para estabelecer uma análise de dados de imagens com diferentes colorações em graus de queimaduras I e II, que apresentam uma coloração vermelha, enquanto as queimaduras de grau III ultrapassam todas as camadas da pele.

Para lidar com esse desafio, criamos um algoritmo utilizando a biblioteca OpenCV para processar a imagem com o grau de queimadura e mapear a cor vermelha. Em seguida, o algoritmo busca a quantidade de pixels na cor vermelha e realiza a conversão para porcentagem.

Esses dados são salvos em uma planilha no Google Sheets como base para outras análises. Todos esses dados são coletados para que seja possível calcular a média, o maior e o menor valor encontrados.

Com base nesses resultados, estabelecemos a seguinte lógica: 
    1. Se o valor gerado pela análise da cor vermelha for maior que o menor valor encontrado até o momento, então a queimadura é classificada como Grau I.
    2. Se o valor gerado pela análise da cor vermelha for menor ou igual ao maior valor encontrado até o momento, então a queimadura é classificada como Grau II.
    3. Se um valor não foi encontrado durante a análise, o algoritmo precisa ser executado novamente para que o dado seja inserido e a análise seja feita corretamente.
    4. Se nenhuma das condições acima for atendida, isso significa que o algoritmo não pode realizar análises de queimaduras de Grau III.
Essas regras são para definir um sistema para classificar queimaduras em Grau I e Grau II com base na análise da cor vermelha. Se nenhuma das condições for atendida ou se a queimadura for de Grau III, o algoritmo não será capaz de fazer a análise. 

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
- [Numpy](https://numpy.org/) - versão 1.24.3
- [Google-api-python-client](https://developers.google.com/sheets/api/guides/libraries?hl=pt-br#python) - versão 3.10.6


<br>
 <h3 align="center">
      <p>Copyright © 2023 Girludev Company</p>
    
 </h3>




