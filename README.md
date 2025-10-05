# RAG Sanitario
Chatbot RAG sanitario que contesta preguntas citando guías clínicas,  lee informes HTML de urgencias,  extrae variables clínicas y rellena un formulario.


## Requisitos
- Docker + Docker Compose

## Levantar todo con Docker
1. `docker compose up -d`
2. Descargar el modelo en Ollama (sólo la primera vez):
`docker exec -it ollama ollama pull mistral:7b-instruct-q4`
