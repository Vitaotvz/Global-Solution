# Função para adicionar uma denúncia
def adicionar_denuncia(usuarios, denuncias, localizacoes, tipos_incidente, status_denuncia):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    descricao = input("Descreva a denúncia: ")
    rua = input("Digite o nome da rua: ")
    numero = float(input("Digite o numero do local: "))
    tipo_incidente = input("Digite o tipo de incidente: ")
    status = "Pendente"  # Novas denúncias começam com status pendente

    id_usuario = len(usuarios) + 1
    id_denuncia = len(denuncias) + 1
    id_local = len(localizacoes) + 1

    usuarios.append({"ID_Usuário": id_usuario, "Nome": nome, "Email": email})
    localizacoes.append({"ID_Local": id_local, "rua": rua, "numero": numero})
    tipos_incidente.append({"ID_Tipo_Incidente": id_denuncia, "Nome_Tipo": tipo_incidente})
    denuncias.append({
        "ID_Denúncia": id_denuncia,
        "ID_Usuário": id_usuario,
        "ID_Local": id_local,
        "ID_Tipo_Incidente": id_denuncia,
        "ID_Status": 1,  # 1 representa "Pendente"
        "Descrição": descricao,
        "Data_Hora": "2023-12-01 12:00:00"  # Simulando uma data e hora
    })
    status_denuncia.append({"ID_Status": 1, "Descrição_Status": "Pendente"})
    
    print("Denúncia registrada com sucesso!")

# Função para exibir todas as denúncias
def exibir_denuncias(denuncias, usuarios, localizacoes, tipos_incidente, status_denuncia):
    for denuncia in denuncias:
        usuario = next(user for user in usuarios if user["ID_Usuário"] == denuncia["ID_Usuário"])
        localizacao = next(loc for loc in localizacoes if loc["ID_Local"] == denuncia["ID_Local"])
        tipo_incidente = next(tipo for tipo in tipos_incidente if tipo["ID_Tipo_Incidente"] == denuncia["ID_Tipo_Incidente"])
        status = next(stat for stat in status_denuncia if stat["ID_Status"] == denuncia["ID_Status"])

        print(f"\nDenúncia #{denuncia['ID_Denúncia']}")
        print(f"Usuário: {usuario['Nome']} ({usuario['Email']})")
        print(f"Localização: rua {localizacao['rua']}, numero {localizacao['numero']}")
        print(f"Tipo de Incidente: {tipo_incidente['Nome_Tipo']}")
        print(f"Descrição: {denuncia['Descrição']}")
        print(f"Status: {status['Descrição_Status']}")
        print(f"Data e Hora: {denuncia['Data_Hora']}")

# Função principal
def main():
    usuarios = []
    denuncias = []
    localizacoes = []
    tipos_incidente = []
    status_denuncia = []

    while True:
        print("\n=== Menu ===")
        print("1. Fazer uma Denúncia")
        print("2. Exibir Denúncias")
        print("3. Sair")

        escolha = input("Escolha a opção (1/2/3): ")

        if escolha == "1":
            adicionar_denuncia(usuarios, denuncias, localizacoes, tipos_incidente, status_denuncia)
        elif escolha == "2":
            exibir_denuncias(denuncias, usuarios, localizacoes, tipos_incidente, status_denuncia)
        elif escolha == "3":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
