from conexao import db

def executar():
    print("\nIniciando testes")

#Teste 1: Ranges;
    print("\nExecutando Busca por Intervalo:")
    query_range = {"ano_publicacao": {"$gte": 2000, "$lte": 2010}}
    
#Comando Explain do MongoDB;
    comando_range = {
        "explain": {
            "find": "livros",
            "filter": query_range
        },
        "verbosity": "executionStats"
    }
    
    resultado_range = db.command(comando_range)
    stats_range = resultado_range['executionStats']
    
    print(f"Tempo de execução: {stats_range['executionTimeMillis']} ms")
    print(f"Documentos examinados: {stats_range['totalDocsExamined']}")
    print(f"Documentos retornados: {stats_range['nReturned']}")


#Teste 2: Expressões Regulares
    print("\nExecutando Busca por Regex:")
    query_regex = {"titulo": {"$regex": "^O Mistério"}} 
    
    comando_regex = {
        "explain": {
            "find": "livros",
            "filter": query_regex
        },
        "verbosity": "executionStats"
    }
    
    resultado_regex = db.command(comando_regex)
    stats_regex = resultado_regex['executionStats']
    
    print(f"Tempo de execução: {stats_regex['executionTimeMillis']} ms")
    print(f"Documentos examinados: {stats_regex['totalDocsExamined']}")


#Teste 3: Busca Textual
    print("\nExecutando Busca Textual:")
    query_texto = {"$text": {"$search": "aventura história"}}
    
    comando_texto = {
        "explain": {
            "find": "livros",
            "filter": query_texto
        },
        "verbosity": "executionStats"
    }
    
    resultado_texto = db.command(comando_texto)
    stats_texto = resultado_texto['executionStats']
    
    print(f"Tempo de execução: {stats_texto['executionTimeMillis']} ms")
    print(f"Documentos examinados: {stats_texto['totalDocsExamined']}")
