from fastapi import FastAPI, Path

# Criar instância FastAPI
app = FastAPI()

questions = {

	"Matemática": {

		"geometria": "1+1?",
		"aritimética": "1+1?"
	},

	"Física": {

		"geometria": "2+2?",
		"aritimética": "2+2?"
	},
}

@app.get("/") # <- usamos get para obter informações
def questionAnswer():
	"""
	Retorna os dados
	que pedimos
	"""
	return {"Quanto é 1+1?": "2"}


@app.get("/get-question/{disciplina}") # <- usamos get para obter informações
def get_question(disciplina: str = Path(None)):
	return questions[disciplina]
	