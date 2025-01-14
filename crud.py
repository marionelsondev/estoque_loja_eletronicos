from sqlalchemy.orm import sessionmaker
from models import Product, Sale, StockQuantityError, db
from datetime import datetime

Session = sessionmaker(bind=db)
session = Session()

def register_product():
    name = input("Digite o nome do produto: ").upper()
    price = float(input("Digite o preço do produto: "))
    stock_quantity = int(input("Digite a quantidade em estoque do produto: "))
    product = Product(name, price, stock_quantity)
    session.add(product)
    session.commit()
    print("Produto cadastrado com sucesso!")

def list_stock():
    products = session.query(Product).all()
    print(86*"-")
    print(f"{"CÓDIGO":^5} | {"NOME":^40} | R$:{"PREÇO":^10} | {"QUANTIDADE EM ESTOQUE":^10}")
    print(86*"-")
    for product in products:
        print(f"{product.id:<6} | {product.name:<40} | {product.price:<10.2f} | {product.stock_quantity:<10}")

def update_product():
    search_name = input("Digite o nome do produto que deseja atualizar: ").upper()
    product = session.query(Product).filter(Product.name==search_name).first()
    product.name = input("Digite um novo nome para o produto: ").upper()
    product.price = float(input("Digite um novo preço para o produto: "))
    product.stock_quantity = int(input("Digite a nova quantidade em estoque do produto: "))
    session.add(product)
    session.commit()
    print("INFORMAÇÕES ATUALIZADAS DO PRODUTO")
    print(23*"-")
    print(f"CÓDIGO: {product.id}")
    print(f"NOME: {product.name}")
    print(f"PREÇO: {product.price}")
    print(f"QUANTIDADE EM ESTOQUE: {product.stock_quantity}")
    
def delete_product():
    search_name = input("Digite o nome do produto que deseja deletar: ").upper()
    product = session.query(Product).filter(Product.name==search_name).first()
    session.delete(product)
    session.commit()

def sell():
    customer = input("Digite o nome do cliente: ").upper()
    list_stock()
    product_id = input("Digite o código do produto que deseja vender: ")
    product = session.query(Product).filter(Product.id==product_id).first()
    sale_date = datetime.now()
    while True:
        try:
            quantity_sold = int(input(f"Digite a quantidade que deseja vender do produto [{product.name}]: "))

            if quantity_sold <= 0:
                raise ValueError("A quantidade vendida deve ser maior que zero.")
            
            if quantity_sold > product.stock_quantity:
                raise StockQuantityError(quantity_sold, product.stock_quantity)
            
            quantity_sold = quantity_sold
            break
        except (ValueError, StockQuantityError) as e:
            print(e)
    total = quantity_sold * product.price
    product.stock_quantity = product.stock_quantity - quantity_sold
    sale = Sale(customer, sale_date, quantity_sold, total, product.id)
    session.add(sale, product)
    session.commit()


def list_sales():
    pass

def system_actions(option):
    if option == 1:
        register_product()
    elif option == 2:
        update_product()
    elif option == 3:
        delete_product()
    elif option == 4:
        list_stock()
    elif option == 5:
        sell()
