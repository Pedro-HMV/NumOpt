# NumOpt
Resolução de um problema de otimização numérica de uma função com duas variáveis.
## Arquivos
Este repositório contém:
- O [relatório](https://github.com/Pedro-HMV/NumOpt/blob/master/Teste%20otimiza%C3%A7%C3%A3o%20num%C3%A9rica.html) descrevendo o problema e todos os passos da solução matemática (favor baixar e abrir com um navegador, formato _html_);
	- Caso tenha problemas ao visualizar o arquivo _html_, o relatório também está disponível [em _pdf_ ](https://github.com/Pedro-HMV/NumOpt/blob/master/Otimiza%C3%A7%C3%A3o%20Num%C3%A9rica.pdf), porém os links presentes no documento não funcionarão;
- O [código Python](https://github.com/Pedro-HMV/NumOpt/blob/master/main.py) implementado para realizar os cálculos de uma etapa da resolução (ver relatório para mais informações);
- A [lista de dependências](https://github.com/Pedro-HMV/NumOpt/blob/master/requirements.txt) que devem ser instaladas para executar o código (instruções abaixo).
## Executando o código
<details>
<summary>Clique para exibir/esconder um resumo dos comandos</summary>
<br/>

- **Windows:**
```
python3 -m venv NumOpt

NumOpt\Scripts\activate.bat

cd NumOpt

git clone git@github.com:Pedro-HMV/NumOpt.git

pip install -r requirements.txt

python3 main.py
```
	
- **Linux/MacOS:**		
``` 
python3 -m venv NumOpt

source NumOpt/bin/activate

cd NumOpt

git clone git@github.com:Pedro-HMV/NumOpt.git

pip install -r requirements.txt

python3 main.py
```
	
</details>

<hr>

### Mais detalhes:
1. **Versão do Python:** o programa foi desenvolvido com a versão **3.8.10** 
2. **Ambiente virtual:** é recomendado criar um ambiente virtual para instalar as dependências ([saiba mais](https://docs.python.org/pt-br/3/tutorial/venv.html#creating-virtual-environments))
3. **Instalar dependências:**
- Clonar repositório: `git clone git@github.com:Pedro-HMV/NumOpt.git`
- Ativar ambiente virtual (se ainda não estiver ativado)
- Instalar as dependências a partir do arquivo _requirements.txt_: `pip install -r requirements.txt`
4. **Executar o script:** com as dependências instaladas e o ambiente virtual ativo, o script contido em _main.py_ pode ser executado via IDE (como [PyCharm](https://www.jetbrains.com/pt-br/pycharm/), [VSCode](https://code.visualstudio.com), entre outros) ou via linha de comando: `python3 main.py`
