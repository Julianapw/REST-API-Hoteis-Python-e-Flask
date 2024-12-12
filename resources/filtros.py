def normalize_path_params(cidade=None, estrela_min=0, estrela_max=5, diaria_min=0, diaria_max=10000, limit=50, offset=0, **dados):
    if cidade:
        return{
            "estrela_min":estrela_min,
            "estrela_max":estrela_max,
            "diaria_min":diaria_min,
            "diaria_max":diaria_max,
            "cidade":cidade,
            "limit":limit,
            "offset":offset
        }
    return{
        "estrela_min":estrela_min,
            "estrela_max":estrela_max,
            "diaria_min":diaria_min,
            "diaria_max":diaria_max,
            "cidade":cidade,
            "limit":limit,
            "offset":offset}

consulta_sem_cidade = "SELECT * FROM hoteis WHERE (estrela>=? and estrela<=?) and (diaria>=? ? and diaria<=?) LIMIT ? OFFSET ?"
consulta_com_cidade = "SELECT * FROM hoteis WHERE (estrela>=? and estrela<=?) and (diaria>=? ? and diaria<=?) and cidade=? LIMIT ? OFFSET ?"