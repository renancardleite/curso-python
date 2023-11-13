import json
from datetime import datetime, timedelta, date

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime('%d/%m/%Y')
        return super().default(obj)

class GerenciadorOrçamento:
    def __init__(self):
        self.saldo = 0.0
        self.transações = []
        self.despesas_a_vencer = []

    def adicionar_transação(self, descrição, valor, é_receita, data):
        try:
            data = datetime.strptime(data, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de data inválido. Certifique-se de usar o formato dd/mm/yyyy.")
            return

        self.transações.append({"descrição": descrição, "valor": valor, "é_receita": é_receita, "data": data})
        if é_receita:
            self.saldo += valor
        else:
            self.saldo -= valor

    def adicionar_despesa_a_vencer(self, descrição, valor, data_input):
        try:
            data = datetime.strptime(data_input, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de data inválido. Certifique-se de usar o formato dd/mm/yyyy.")
            return
        
        self.despesas_a_vencer.append({"descrição": descrição, "valor": valor, "data": data})
        print("Despesa a vencer adicionada com sucesso!")

    def mostrar_despesas_a_vencer(self, data):
        print("\nDespesas a Vencer na Data:")
        for despesa in self.despesas_a_vencer:
            if despesa["data"] == data:
                print(f"{despesa['descrição']} - R${despesa['valor']}")

    def calcular_saldo_no_dia_saldo_após_transação(self, data):
        saldo_após_transação = 0.0
        for transação in self.transações:
            if transação["data"] <= data:
                valor = transação["valor"]
                if transação.get("é_receita", False):
                    saldo_após_transação += valor
                else:
                    saldo_após_transação -= valor
        return saldo_após_transação


    
    def mostrar_transações(self):
        saldo_atual = 0.0
        data_atual = None
        saldo_final = 0.0

        print("\nExtrato Bancário:")
        for transação in self.transações:
            data_transação = transação["data"]
            

            tipo_transação = "Receita" if transação.get("é_receita", False) else "Despesa"
            valor_transação = transação["valor"]
            if not transação.get("é_receita", False):
                valor_transação = -valor_transação
            print(f"\nData: {data_transação.strftime('%d/%m/%Y')} {tipo_transação}: {transação['descrição']} - R${valor_transação:.2f}")

            if data_transação != data_atual:
                saldo_atual = self.calcular_saldo_no_dia_saldo_após_transação(data_transação, saldo_atual)
                print(f"\nData: {data_transação.strftime('%d/%m/%Y')} - Saldo: R${saldo_atual:.2f}")
                data_atual = data_transação

        saldo_final = self.calcular_saldo_no_dia_saldo_após_transação(datetime.now().date(), saldo_final)
        print(f"\nSaldo Final: R${saldo_final:.2f}")

    def calcular_saldo_no_dia_saldo_após_transação(self, data, saldo_anterior):
        saldo_após_transação = saldo_anterior
        for transação in self.transações:
            if transação["data"] <= data:
                valor_transação = transação["valor"]
                if not transação.get("é_receita", False):
                    valor_transação =- valor_transação
                saldo_após_transação += valor_transação
        return saldo_após_transação

    def marcar_despesa_como_paga(self, descrição, data):
        for despesa in self.despesas_a_vencer:
            if despesa["descrição"] == descrição and despesa["data"] == data:
                self.despesas_a_vencer.remove(despesa)
                self.transações.append({"descrição": f"Despesa paga: {descrição}", "valor": -despesa["valor"]})
                self.saldo -= despesa["valor"]
                print("Despesa marcada como paga e removida das despesas a vencer.")

    def mostrar_saldo(self):
        print(f"Saldo Atual: R${self.saldo:.2f}")

    def salvar_dados(self, arquivo):
        dados = {
            "saldo": self.saldo,
            "transações": self.transações,
            "despesas_a_vencer": self.despesas_a_vencer
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, cls=DateEncoder)  # Use a classe de codificação personalizada

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self.saldo = dados.get("saldo", 0.0)
                self.transações = dados.get("transações", [])
                self.despesas_a_vencer = dados.get("despesas_a_vencer", [])
        except (FileNotFoundError, json.JSONDecodeError):
            pass

def main():
    arquivo_dados = "dados.json"
    gerenciador_orçamento = GerenciadorOrçamento()
    gerenciador_orçamento.carregar_dados(arquivo_dados)

    while True:
        print("\nGerenciador de Orçamento")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Adicionar Despesa a Vencer")
        print("4. Mostrar Transações")
        print("5. Mostrar Despesas a Vencer Hoje")
        print("6. Mostrar Despesas a Vencer Amanhã")
        print("7. Mostrar Saldo")
        print("8. Baixar Despesa a Vencer")
        print("9. Sair")


        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            descrição = input("Digite a descrição: ")
            valor = float(input("Digite o valor: "))
            data = input("Digite a data (dd/mm/yyyy): ")
            gerenciador_orçamento.adicionar_transação(descrição, valor, é_receita=True, data=data)
            print("Receita adicionada com sucesso!")

        elif escolha == "2":
            descrição = input("Digite a descrição: ")
            valor = float(input("Digite o valor: "))
            data = input("Digite a data (dd/mm/yyyy): ")
            gerenciador_orçamento.adicionar_transação(descrição, valor, é_receita=False, data=data)
            print("Despesa adicionada com sucesso!")

        elif escolha == "3":
            descrição = input("Digite a descrição: ")
            valor = float(input("Digite o valor: "))
            data = input("Digite a data de vencimento (dd/mm/yyyy): ")
            gerenciador_orçamento.adicionar_despesa_a_vencer(descrição, valor, data=data)
            print("Despesa a vencer adicionada com sucesso!")
        
        elif escolha == "4":
            gerenciador_orçamento.mostrar_transações()

        elif escolha == "5":
            hoje = datetime.now().date()
            gerenciador_orçamento.mostrar_despesas_a_vencer(hoje)

        elif escolha == "6":
            amanhã = datetime.now().date() + timedelta(days=1)
            gerenciador_orçamento.mostrar_despesas_a_vencer(amanhã)

        elif escolha == "7":
            gerenciador_orçamento.mostrar_saldo()

        elif escolha == "8":
            data_input = input("Digite a data para listar as despesas a vencer (dd/mm/yyyy): ")
            data = datetime.strptime(data_input, "%d/%m/%Y").date()

            print("\nDespesas a Vencer na Data:")
            index = 1
            for despesa in gerenciador_orçamento.despesas_a_vencer:
                if despesa["data"] == data:
                    print(f"{index}. {despesa['descrição']} - R${despesa['valor']}")
                    index += 1
            if index == 1:
                print("Nenhuma despesa encontrada para essa data.")

            opção = input("\nDigite o número da despesa a ser baixada (ou 0 para voltar): ")
            if opção.isdigit():
                opção = int(opção)
            if 1 <= opção <= index - 1:
                despesa_baixada = gerenciador_orçamento.despesas_a_vencer[opção - 1]
                gerenciador_orçamento.marcar_despesa_como_paga(despesa_baixada["descrição"], despesa_baixada["data"])
                print("Despesa marcada como paga e removida das despesas a vencer.")
            elif opção == 0:
                print("Operação cancelada.")
            else:
                print("Opção inválida.")

        elif escolha == "9":
            print("Encerrando o Gerenciador de Orçamento. Até logo!")
            gerenciador_orçamento.salvar_dados(arquivo_dados)
            break

        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()

