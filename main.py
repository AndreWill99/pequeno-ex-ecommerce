class Produto:
  def __init__(self, id, nome, preco):
      self.id = id
      self.nome = nome
      self.preco = preco

# Classe Carrinho de Compras para gerenciar os itens no carrinho
class CarrinhoDeCompras:
  def __init__(self):
      self.itens = []

  def adicionar_item(self, produto, quantidade):
      self.itens.append({"produto": produto, "quantidade": quantidade})

  def calcular_total(self):
      total = 0
      for item in self.itens:
          total += item["produto"].preco * item["quantidade"]
      return total

# Classe Cliente para representar os clientes que fazem compras
class Cliente:
  def __init__(self, nome, email):
      self.nome = nome
      self.email = email

# Exemplo de uso do sistema de e-commerce
if __name__ == "__main__":
  # Criar alguns produtos
  produto1 = Produto(1, "Camiseta", 20.0)
  produto2 = Produto(2, "Calça Jeans", 50.0)
  produto3 = Produto(3, "Tênis", 80.0)

  # Criar um cliente
  cliente = Cliente("João", "joao@email.com")

  # Cliente adiciona itens ao carrinho de compras
  carrinho = CarrinhoDeCompras()
  carrinho.adicionar_item(produto1, 2)
  carrinho.adicionar_item(produto2, 1)
  carrinho.adicionar_item(produto3, 1)

  # Calcular o total da compra
  total_compra = carrinho.calcular_total()

  # Exibir informações da compra
  print(f"Cliente: {cliente.nome} ({cliente.email})")
  print("Itens no Carrinho:")
  for item in carrinho.itens:
      print(f"- {item['quantidade']}x {item['produto'].nome}")
  print(f"Total da Compra: R${total_compra}")
  