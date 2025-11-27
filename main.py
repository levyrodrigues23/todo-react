from jogo import Jogo
from cliente import Cliente
from locadora import Locadora

def run_simulation():
    """
    Executa uma simulação de operações de uma locadora de jogos.
    Cria uma locadora, adiciona jogos, cria clientes e simula
    o aluguel de um jogo.
    """
    # Criando a locadora
    minha_locadora = Locadora("Gemini Games")

    # Adicionando jogos ao catálogo
    jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", "Aventura", 5)
    jogo2 = Jogo("Red Dead Redemption 2", "Ação/Aventura", 3)
    jogo3 = Jogo("Stardew Valley", "Simulação", 7)
    
    minha_locadora.adicionar_jogo(jogo1)
    minha_locadora.adicionar_jogo(jogo2)
    minha_locadora.adicionar_jogo(jogo3)
    
    print("\n") # Adiciona espaço para melhor legibilidade
    minha_locadora.listar_catalogo()

    # Criando clientes
    cliente1 = Cliente("Alice")
    cliente2 = Cliente("Bob")

    print(f"\nClientes da locadora: {cliente1} e {cliente2}\n")

    # Simulação de operações
    print("--- Início das Operações de Aluguel ---\n")

    # Alice aluga um jogo
    jogo_zelda = minha_locadora.buscar_jogo("The Legend of Zelda: Breath of the Wild")
    if jogo_zelda:
        cliente1.alugar_jogo(jogo_zelda)
    
    print("\n")
    minha_locadora.listar_catalogo()
    print("\n")
    cliente1.listar_jogos_alugados()

    print("--- Fim das Operações ---\n")

def main():
    run_simulation()

if __name__ == "__main__":
    main()
