from fastapi import FastAPI
from questions import Questoes

# Criar objeto da classe FastAPI
app = FastAPI(title="Questões", varion="0.1.0") # <- título e versão do app

lista_questoes = Questoes()
questoes = lista_questoes.LISTA

@app.get("/questoes/{materia}")
def get_questao_por_materia(materia: str):
	"""
	Retorna a pergunta e resposta da matéria especificada.

	Args:
	materia: a matéria para a qual você deseja obter a pergunta e resposta.

	Return:
	Json File: json file com pergunta e resposta da matéria especificada.
	"""
	
	for questao in questoes:
		if questao["matéria"] == materia:
			return {"pergunta": questao["pergunta"]}
			
	return {"message": "Matéria não encontrada"}