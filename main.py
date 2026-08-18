# main.py

def calcular_media():
    print("--- Calculadora de Média Escolar ---")
    
    try:
        # Recebe os dados do usuário
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        # Realiza o cálculo
        media = (nota1 + nota2) / 2
        print(f"\nMédia final: {media:.2f}")
        
        # Verifica a situação do aluno
        if media >= 6.0:
            print("Status: Aprovado!")
        else:
            print("Status: Reprovado.")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos usando ponto (ex: 7.5).")

if __name__ == "__main__":
    calcular_media()
