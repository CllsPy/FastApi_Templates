from fastapi import FastAPI

# Criar instância FastAPI
app = FastAPI()

@app.get("/") # <- usamos get para obter informações
def questionAnswer():
	"""
	Retorna os dados
	que pedimos
	"""
	return {"Quanto é 1+1?": "2"}